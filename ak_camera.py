# CAMERA DEVICE FUNCTIONS: Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations
import os
import cv2
import copy

import time
from pathlib import Path
from datetime import datetime
from PySide6.QtMultimedia import (QCamera, QCameraDevice, QImageCapture, QMediaCaptureSession, QMediaDevices)
from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtGui import QAction, QActionGroup, QImage, QPixmap
from PySide6.QtCore import (QDir, QTimer, Qt, Slot, Signal, QThread)

from imagesettings import ImageSettings
from ak_camera_ui import Ui_Camera
from styles import buttonStyle, buttonStyle2, mboxStyle
from sim_ocr import SimulateOCR
from render_latex import MathJaxSOL, ClearHTML, LoadHTML
from sizes import Characters


class OCRProcessingThread(QThread):
    ocr_completed = Signal(dict)  # Signal to return OCR result and processing time
    ocr_failed = Signal(str)
    def __init__(self, file):
        super().__init__()
        self.file = file

    def run(self):
        try:
            print("OCR Processing Started.")

            # Perform OCR
            output = SimulateOCR(self.file)
            if output.full_solutions:
                self.ocr_completed.emit(output)  # Emit success signal
            else:
                self.ocr_failed.emit(output.empty_message)

            # Emit the result back to the main thread
            self.ocr_completed.emit(output)

        except Exception as e:
            self.ocr_failed.emit(str(e))  # Send error message


class AK_Camera(QMainWindow):
    finishedImageProcessing = Signal()
    imageProcessed = Signal(str, dict)
        
    def __init__(self, session_window):
        super().__init__()

        self.session_window = session_window
        self.cameraStarted = False #Flag for grading window

        self._video_devices_group = None
        self.m_devices = QMediaDevices()
        self.m_imageCapture = None
        self.m_captureSession = QMediaCaptureSession()
        self.m_camera = None
        self.m_mediaRecorder = None

        self.m_isCapturingImage = False
        self.m_applicationExiting = False
        self.m_doImageCapture = True

        self.viewfinderDone = False
        self.imageSavedDone = False
        self.savedFileName = None

        self._ui = Ui_Camera()
        self._ui.setupUi(self)

        for button in self.findChildren(QPushButton):
            button.setStyleSheet(buttonStyle)
        self._ui.takeImageButton.setStyleSheet(buttonStyle2)
        self._ui.push_save.setStyleSheet(buttonStyle2)

        self.clearhtml = ClearHTML()
        self.loadhtml = LoadHTML()

        self._ui.web_latex.setHtml(self.clearhtml)

        self.image_folder = os.path.join(os.getcwd(), "images", "answerkey")
        os.makedirs(self.image_folder, exist_ok=True)  # Ensure the folder exists

        self._ui.actionAbout_Qt.triggered.connect(qApp.aboutQt)  # noqa: F821
        self.finishedImageProcessing.connect(self.OCRProcessing)
        self._ui.push_save.clicked.connect(self.submitImage)
        self._ui.push_back.clicked.connect(self.backToSession)
        self._ui.push_size.clicked.connect(self.viewSizes)
        self._ui.push_redo.clicked.connect(self.redoOCR)

        # disable all buttons by default
        self.updateCameraActive(False)
        ###self.readyForCapture(False)
        self._ui.takeImageButton.setEnabled(False)
        self._ui.push_redo.setEnabled(False)
        self._ui.push_save.setEnabled(False)
        self._ui.push_size.setEnabled(False)
        
        ## try to actually initialize camera & mic
        self.initialize()


    ################################################################################
    # Initializing Camera

    @Slot()
    def initialize(self):
        # Camera devices
        self._video_devices_group = QActionGroup(self)
        self._video_devices_group.setExclusive(True)
        self.updateCameras()
        self.m_devices.videoInputsChanged.connect(self.updateCameras)
        self._video_devices_group.triggered.connect(self.updateCameraDevice)
        self._ui.exposureCompensation.valueChanged.connect(self.setExposureCompensation)

        self.setCamera(QMediaDevices.defaultVideoInput())
        

    @Slot(QCameraDevice)
    def setCamera(self, cameraDevice):
        self.m_camera = QCamera(cameraDevice)
        self.m_captureSession.setCamera(self.m_camera)

        self.m_camera.activeChanged.connect(self.updateCameraActive)
        self.m_camera.errorOccurred.connect(self.displayCameraError)

        if not self.m_imageCapture:
            self.m_imageCapture = QImageCapture()
            self.m_captureSession.setImageCapture(self.m_imageCapture)
            ###self.m_imageCapture.readyForCaptureChanged.connect(self.readyForCapture)
            self.m_imageCapture.imageCaptured.connect(self.processCapturedImage)
            self.m_imageCapture.imageSaved.connect(self.imageSaved)
            self.m_imageCapture.errorOccurred.connect(self.displayCaptureError)

        self.m_captureSession.setVideoOutput(self._ui.viewfinder)

        self.updateCameraActive(self.m_camera.isActive())
        ###self.readyForCapture(self.m_imageCapture.isReadyForCapture())

        self.m_camera.start()
        self.cameraStarted = True #Notify grading window
        self._ui.takeImageButton.setEnabled(True)


    @Slot()
    def displayCameraError(self):
        if self.m_camera.error() != QCamera.NoError:
            mboxStyle.warning(self, "Camera Error",
                                self.m_camera.errorString())
            self._ui.takeImageButton.setEnabled(False)


    @Slot(QAction)
    def updateCameraDevice(self, action):
        self.setCamera(QCameraDevice(action))


    @Slot(int)
    def setExposureCompensation(self, index):
        self.m_camera.setExposureCompensation(index * 0.5)


    ################################################################################
    # Camera Settings

    @Slot()
    def configureCaptureSettings(self):
        if self.m_doImageCapture:
            self.configureImageSettings()
    
    @Slot()
    def configureImageSettings(self):
        settings_dialog = ImageSettings(self.m_imageCapture)

        if settings_dialog.exec():
            settings_dialog.apply_image_settings()

    ################################################################################
    # Menu Bar Functions

    @Slot()
    def startCamera(self):
        self.m_camera.start()
        self._ui.takeImageButton.setEnabled(True)

    @Slot()
    def stopCamera(self):
        self.m_camera.stop()
        self._ui.takeImageButton.setEnabled(False)

    @Slot()
    def updateCameras(self):
        self._ui.menuDevices.clear()
        available_cameras = QMediaDevices.videoInputs()
        for cameraDevice in available_cameras:
            video_device_action = QAction(cameraDevice.description(),
                                          self._video_devices_group)
            video_device_action.setCheckable(True)
            video_device_action.setData(cameraDevice)
            if cameraDevice == QMediaDevices.defaultVideoInput():
                video_device_action.setChecked(True)

            self._ui.menuDevices.addAction(video_device_action)

    @Slot(bool)
    def updateCameraActive(self, active):
        if active:
            self._ui.actionStartCamera.setEnabled(False)
            self._ui.actionStopCamera.setEnabled(True)
            self._ui.actionSettings.setEnabled(True)
        else:
            self._ui.actionStartCamera.setEnabled(True)
            self._ui.actionStopCamera.setEnabled(False)
            self._ui.actionSettings.setEnabled(False)


    ################################################################################
    # Capture Functions
    def keyPressEvent(self, event):
            if event.isAutoRepeat():
                return
            key = event.key()
            if key == Qt.Key.Key_CameraFocus:
                self.displayViewfinder()
                event.accept()
            elif key == Qt.Key.Key_Camera:
                if self.m_doImageCapture:
                    self.takeImage()
                event.accept()
            else:
                super().keyPressEvent(event)


    @Slot()
    def takeImage(self):
        self._ui.takeImageButton.setEnabled(False)
        self._ui.push_save.setEnabled(False)
        self._ui.push_size.setEnabled(False)

        self.start_total_timer = time.time()
        self.m_isCapturingImage = True 

        # Ensure directory exists before saving
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder, exist_ok=True)

        # Generate dynamic file path
        file_path = os.path.join(self.image_folder, f"{datetime.now().strftime("%Y%m%d%H%M%S")}.jpg")

        # Capture image to specified path
        self.m_imageCapture.captureToFile(QDir.toNativeSeparators(file_path)) 


    @Slot(int, QImageCapture.Error, str)
    def displayCaptureError(self, id, error, errorString):
        mboxStyle.warning(self, "Image Capture Error", errorString)
        self.m_isCapturingImage = False
        self._ui.takeImageButton.setEnabled(True)
    
    
    @Slot(int, QImage)
    def processCapturedImage(self, requestId, img):
        scaled_image = img.scaled(self._ui.viewfinder.size(),
                                  Qt.AspectRatioMode.KeepAspectRatio,
                                  Qt.TransformationMode.SmoothTransformation)

        self._ui.lastImagePreviewLabel.setPixmap(QPixmap.fromImage(scaled_image))

        # Display captured image for 1.5 seconds.
        self.displayCapturedImage()
        QTimer.singleShot(1000, self.displayViewfinder)
       

    @Slot()
    def displayCapturedImage(self):
        self._ui.stackedWidget.setCurrentIndex(1)


    @Slot()
    def displayViewfinder(self):
        self._ui.stackedWidget.setCurrentIndex(0)



    @Slot(int, str)
    def imageSaved(self, id, fileName):
        f = QDir.toNativeSeparators(fileName)
        self._ui.statusbar.showMessage(f"Captured \"{f}\"")

        self.m_isCapturingImage = False
        if self.m_applicationExiting:
            self.close()

        self._ui.web_latex.setHtml(self.loadhtml)

        self.filename = fileName
        self.finishedImageProcessing.emit()
        # Start background threads for processing after image is saved


    ################################################################################
    # OCR and AI Threads

    def OCRProcessing(self):
        self.ocr_thread = OCRProcessingThread(self.filename)
        self.ocr_thread.ocr_completed.connect(self.handleOCRSuccess)
        self.ocr_thread.ocr_failed.connect(self.handleOCRError)
        self.ocr_thread.start()

    @Slot(str, float)
    def handleOCRSuccess(self, output):
        try:
            self.output = copy.deepcopy(output)  # Ensure self.output is independent
            temp_output = copy.deepcopy(output)  # Work with a copy

            # Convert to formatted string
            self.ak_latex = "\n\n\n".join(
                f"{item.problem_setup or '_'}\n" + (item.expressions or 'No solution')
                for item in temp_output.full_solutions
            )
            print(self.ak_latex)

            html_content = MathJaxSOL(self.ak_latex)
            self._ui.web_latex.setHtml(html_content)
            
            runtime = time.time() - self.start_total_timer
            self._ui.label_time.setText(f"Runtime: {runtime: .2f}s")

            self._ui.push_save.setEnabled(True)
            self._ui.push_size.setEnabled(True)

        except Exception as e:
            mboxStyle.warning(self, "OCR Error", str(e))
        
        finally:
            self._ui.takeImageButton.setText("Retake capture")
            self._ui.takeImageButton.setEnabled(True)
            self._ui.push_redo.setEnabled(True)


        
    def handleOCRError(self, error_message):
        self._ui.web_latex.setHtml(self.clearhtml)
        mboxStyle.warning(self, "OCR Error", str(error_message))
        
        self._ui.label_time.setText("Runtime: 0.00s")
        self._ui.takeImageButton.setText("Retake capture")
        self._ui.takeImageButton.setEnabled(True)
        self._ui.push_redo.setEnabled(True)


    def redoOCR(self):
        self._ui.takeImageButton.setEnabled(False)
        self._ui.push_redo.setEnabled(False)
        self._ui.push_save.setEnabled(False)
        self._ui.push_size.setEnabled(False)

        self.OCRProcessing()


    ################################################################################
    # Save and Close window

    def submitImage(self):
        if self.ak_latex and self.filename:
            self.imageProcessed.emit(self.filename, self.output)  # Send filename to MainWindow
            self.stopCamera()
            self.close()  # Close capture window

    def backToSession(self):
        self.stopCamera()
        self.close()
        self.session_window.show()


    def closeEvent(self, event):

        if self.m_isCapturingImage:
            self.setEnabled(False)
            self.m_applicationExiting = True
            event.ignore()
        else:
            event.accept()

    def viewSizes(self):
        if self.filename:
            img = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
            blurred = cv2.GaussianBlur(img, (5, 5), 0)  
            _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            valid_chars = []
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                if w < 16 or h < 16:
                    continue
                char_crop = thresh[y:y + h, x:x + w]
                valid_chars.append((None, char_crop, x, y, w, h))

            if valid_chars:
                self.size_window = Characters(valid_chars, img)
                self.size_window.show()
            else:
                print("No valid characters found!")