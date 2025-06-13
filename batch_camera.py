# CAMERA DEVICE FUNCTION: Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations
"""PySide6 port of the QtMultiMedia camera example from Qt v6.x"""
import os
import time
from pathlib import Path
from datetime import datetime
import cv2

from PySide6.QtMultimedia import (QCamera, QCameraDevice, QImageCapture, QMediaCaptureSession, QMediaDevices)
from PySide6.QtWidgets import QMainWindow, QMessageBox, QPushButton
from PySide6.QtGui import QAction, QActionGroup, QImage, QPixmap
from PySide6.QtCore import (QDir, QTimer, Qt, Slot, Signal, QObject, QThread)
from imagesettings import ImageSettings
from batch_camera_ui import Ui_Camera
from styles import buttonStyle, buttonStyle2, mboxStyle

from sim_ocr_batch import SimulateOCR
from eval_batch import Evaluation
from database import Session, AnswerKey
from ak_dialog import AK_Dialog
from sizes import Characters
from feeder import Feeder


class OCRWorker(QObject):
    finished = Signal(list, float)
    error = Signal(str)

    def __init__(self, folder):
        super().__init__()
        self.folder = folder


    def run(self):
        try:
            start_ocr_timer = time.time()
            
            output = SimulateOCR(self.folder)  # Run OCR
            print(type(output))
            ocr_time = time.time() - start_ocr_timer
            self.finished.emit(output, ocr_time)  # Send the result back
            
        except Exception as e:
            self.error.emit(str(e))



class GPTWorker(QObject):
    finished = Signal(list, float)  # Emit result and check time
    error = Signal(str)

    def __init__(self, evaluator, output):
        super().__init__()
        self.evaluator = evaluator  # Reference to eval object
        self.output = output  # The OCR results


    def run(self):
        try:
            start_check_timer = time.time()

            result = self.evaluator.evaluate(self.output)
            check_time = time.time() - start_check_timer

            self.finished.emit(result, check_time)  # Send result back
            
        except Exception as e:
            self.error.emit(str(e))  # Send error message



class FeedWorker(QObject):
    finished = Signal()
    error = Signal(str)

    def __init__(self, main, feeder):
        super().__init__()
        self.main = main
        self.feeder = feeder
        self.count = 0


    def run(self):
        try:
            self.feeder.send_command("mode2")
            while True:                
                # Process only IR sensor data
                line = self.feeder.arduino.readline().decode('utf-8').strip()
                
                # Process only IR sensor data
                if line == "capture":
                    self.main.takeImage()
                    self.count += 1
                    
                if self.count == 10:
                    self.finished.emit()
                    break
                
                time.sleep(0.1)  # Small delay to avoid overwhelming the serial port
        
        except Exception as e:
            self.error.emit(str(e))



class Batch_Camera(QMainWindow):
    finishedImageProcessing = Signal()
        
    def __init__(self, session_window, session_id):
        super().__init__()

        self.session_window = session_window
        self.session_id = session_id

        # Attribute from AnswerKey table 
        self.first_ak_id = None
        self.second_ak_id = None
        self.answer_key_ids = []

        # Attribute for StudentHAS table
        self.eval = Evaluation(self.session_id)
        self.result = None
        self.has_file = None

        self.last_checked_name = None
        self.counter = 0

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
        self._ui.push_feed.setStyleSheet(buttonStyle2)
        self._ui.push_start.setStyleSheet(buttonStyle2)

        self.feed = Feeder()

        self.image_folder = os.path.join(os.getcwd(), "images", "batch", str(self.session_id))
        os.makedirs(self.image_folder, exist_ok=True)  # Ensure the folder exists

        self._ui.actionAbout_Qt.triggered.connect(qApp.aboutQt)  # noqa: F821

        self._ui.push_feed.clicked.connect(self.activate_mode)
        self._ui.push_stop.clicked.connect(self.stop_feed)

        self._ui.push_retake.clicked.connect(self.retakeCapture)
        self._ui.push_start.clicked.connect(self.Confirmation)
        self._ui.push_size.clicked.connect(self.viewSizes)
        self._ui.push_view_ak.clicked.connect(self.viewAnswerKey)

        self._ui.push_cancel.clicked.connect(self.cancel_processing)
        self._ui.push_back.clicked.connect(self.backToSession)

        # disable all buttons by default
        self.updateCameraActive(False)
        ###self.readyForCapture(False)
        self.disableButtons()
        self.fetchStats()
        # try to actually initialize camera & mic
        self.initialize()
        
        folder_exists = self.check_folder()
        if folder_exists:
            self._ui.push_start.setEnabled(True)
        self._ui.label_counter.setText(f"No. of images captured: {self.counter}")


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
        self.setCamera(QMediaDevices.defaultVideoInput())

        self.feed_present()


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
        self._ui.takeImageButton.setEnabled(True)
        self.displayViewfinder()


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


    def feed_present(self):
        if self.feed.arduino:
            self._ui.push_feed.setEnabled(True)
        else:
            self._ui.push_feed.setEnabled(False)
            self._ui.push_stop.setEnabled(False)


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
        self.disableButtons()
        self.start_total_timer = time.time()

        self.m_isCapturingImage = True

        # Ensure directory exists before saving
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder, exist_ok=True)

        # Generate dynamic file path
        filename = os.path.join(self.image_folder, f"{datetime.now().strftime("%Y%m%d%H%M%S")}.jpg")

        # Capture image to specified path
        self.m_imageCapture.captureToFile(QDir.toNativeSeparators(filename)) 


    @Slot(int, QImageCapture.Error, str)
    def displayCaptureError(self, id, error, errorString):
        mboxStyle.warning(self, "Image Capture Error", errorString)
        self.m_isCapturingImage = False
        
        self._ui.takeImageButton.setEnabled(True)
        self._ui.push_retake.setEnabled(True)

    
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
    
        self.filename = fileName
        self.check_folder()
        self._ui.label_counter.setText(f"No. of images captured: {self.counter}")

        self.display_image()


    def display_image(self):
        # Display image in QLabel
        pixmap = QPixmap(self.filename)
        self._ui.label_image.setPixmap(pixmap.scaled(360, 360, Qt.AspectRatioMode.KeepAspectRatio))
        
        self.enableButtons()
        
        
    def retakeCapture(self):
        os.remove(self.filename)
        self.takeImage()
        

    ################################################################################
    # OCR and AI Threads

    def Confirmation(self):
        # Ask ASM permission before processing
        if not self.asm_choice:
            response = mboxStyle.question(
                self,
                "AK 1: Alternative Method confirmation",
                "Do you want to allow Alternative Solution Methods (ASM) in the checking process for Answer Key 1?",
            )
            # Send the user’s response back to the worker thread
            if response == QMessageBox.Yes:
                print("User allowed ASM.")
                self.asm_choice = "Allow ASM for HAS"
            elif response == QMessageBox.No:
                self.asm_choice = "Forbid ASM for HAS"
            else:
                return
                
            session = Session()
            try:
                answer_key = session.get(AnswerKey, self.first_ak_id)
                answer_key.asm_choice = self.asm_choice
                session.commit()
                        
            except Exception as e:
                session.rollback()
                mboxStyle.critical(self, "Database Error", f"Failed to save answer key: {e}")
                print(e)
            finally:
                session.close()
        
        if self.second_ak_id:    
            if not self.asm_choice_2:
                response = mboxStyle.question(
                    self,
                    "AK 2: Alternative Method confirmation",
                    "Do you want to allow Alternative Solution Methods (ASM) in the checking process for Answer Key 2?",
                )
                # Send the user’s response back to the worker thread
                if response == QMessageBox.Yes:
                    print("User allowed ASM.")
                    self.asm_choice_2 = "Allow ASM for HAS"
                elif response == QMessageBox.No:
                    self.asm_choice_2 = "Forbid ASM for HAS"
                else:
                    return
                
                session = Session()
                try:
                    answer_key = session.get(AnswerKey, self.second_ak_id)
                    answer_key.asm_choice = self.asm_choice_2
                    session.commit()
                            
                except Exception as e:
                    session.rollback()
                    mboxStyle.critical(self, "Database Error", f"Failed to save answer key: {e}")
                    print(e)
                finally:
                    session.close()
        start_batch = mboxStyle.question(
            self,
            "Proceed with Batch Processing",
            "Do you want start processing?\nThis may take long depending on no. of images.",
        )
        # Send the user’s response back to the worker thread
        if start_batch == QMessageBox.Yes:
            self.startBatchProcessing()
        else:
            return
            

    def startBatchProcessing(self):
        self.start_total_timer = time.time()
        self.disableButtons()
        self._ui.push_cancel.setEnabled(True)

        self._ui.label_start.setText("*Processing started. This may take a few minutes... ")
        print("OCR Processing Started.")

        self.ocr_thread = QThread()
        self.ocr_worker = OCRWorker(self.image_folder)

        self.ocr_worker.moveToThread(self.ocr_thread)

        # Connect signals
        self.ocr_thread.started.connect(self.ocr_worker.run)
        self.ocr_worker.finished.connect(self.handleOCRSuccess)
        self.ocr_worker.error.connect(self.handleOCRError)

        # Ensure proper cleanup
        self.ocr_worker.finished.connect(self.cleanUpOCRThread)
        self.ocr_worker.error.connect(self.cleanUpOCRThread)

        # Start the OCR thread
        self.ocr_thread.start()


    def handleOCRSuccess(self, output, ocr_time):
        self.output = output
        print(self.output)
        print(f"OCR processing runtime:\n{ocr_time: .2f}s")
        print("hellow")

        self.GPTEvaluation()


    def handleOCRError(self, error_message):
        mboxStyle.warning(self, "OCR Error", error_message)        
        self._ui.takeImageButton.setEnabled(True)
        self._ui.takeImageButton.setText("Retake capture")
        self._ui.push_size.setEnabled(True)


    def cleanUpOCRThread(self):
        # Safely clean up the OCR thread
        if self.ocr_thread.isRunning():
            self.ocr_thread.quit()
            self.ocr_thread.wait()  # Ensure thread exits before deletion


    def GPTEvaluation(self):
        try:
            self.gpt_thread = QThread()
            self.gpt_worker = GPTWorker(self.eval, self.output)

            self.gpt_worker.moveToThread(self.gpt_thread)

            # Connect signals
            self.gpt_thread.started.connect(self.gpt_worker.run)
            self.gpt_worker.finished.connect(self.handleGPTSuccess)
            self.gpt_worker.error.connect(self.handleGPTError)

            # Ensure proper cleanup
            self.gpt_worker.finished.connect(self.cleanUpGPTThread)
            self.gpt_worker.error.connect(self.cleanUpGPTThread)

            # Start the GPT evaluation thread
            self.gpt_thread.start()

        except Exception as e:
            mboxStyle.warning(self, "Checking Error", str(e))
            self.enableButtons()


    def handleGPTSuccess(self, result, check_time):
        print(f"\nGPT evaluation completed in {check_time:.2f} seconds")
        total_time = time.time() - self.start_total_timer

        self.result = result
        print("GPT Evaluation Result:", self.result)
        print(f"\nBatch processing completed in {total_time:.2f} seconds")

        self.viewResults()


    def handleGPTError(self, error_message):
        mboxStyle.warning(self, "GPT Evaluation Error", error_message)
        self.enableButtons()  # Re-enable UI buttons


    def cleanUpGPTThread(self):
        if self.gpt_thread.isRunning():
            self.gpt_thread.quit()
            self.gpt_thread.wait()
            self.gpt_thread.deleteLater()
            self.gpt_worker.deleteLater()


    ################################################################################
    # Feed Configs

    def activate_mode(self):
        self.disableButtons()
        print("activating feeder...")

        self.feed_thread = QThread()
        self.feed_worker = FeedWorker(self, self.feed)

        self.feed_worker.moveToThread(self.feed_thread)

        # Connect signals
        self.feed_thread.started.connect(self.feed_worker.run)
        self.feed_worker.finished.connect(self.handleFeedSuccess)
        self.feed_worker.error.connect(self.handleFeedError)

        # Ensure proper cleanup
        self.feed_worker.finished.connect(self.cleanUpFeedThread)
        self.feed_worker.error.connect(self.cleanUpFeedThread)

        # Start the OCR thread
        self.feed_thread.start()


    def handleFeedSuccess(self):
        if self.feed.feeding:
            self.feed.send_command("s")


    def handleFeedError(self, error_message):        
        mboxStyle.warning(self, "OCR Error", error_message)
        self.enableButtons()
    
    
    def cleanUpFeedThread(self):
        # Safely clean up thread
        if self.feed_thread.isRunning():
            self.feed_thread.quit()
            self.feed_thread.wait()  # Ensure thread exits before deletion


    def stop_feed(self):
        if self.feed.feeding:
            self.feed.send_command("s")


    ################################################################################
    # Save and Close window

    def viewResults(self):
        self.stopCamera()

        from batch_result import Batch_Result

        self.result_window = Batch_Result(self, self.session_id, self.output, self.result)
        self.result_window.show()
        self.close()


    def cancel_processing(self):
        if self.ocr_thread:
            self.ocr_worker.stop()
            self.cleanUpOCRThread()
        if self.gpt_thread:
            self.gpt_worker.stop()
            self.cleanUpGPTThread()
        
        self.enableButtons()
        self._ui.label_start.setText("*Start checking solutions from images")

    
    def backToSession(self):
        self.stopCamera()
        self.close()
        self.session_window.show()


    def closeEvent(self, event):
        if self.feed.feeding:
            self.feed.send_command("s")

        if self.m_isCapturingImage:
            self.setEnabled(False)
            self.m_applicationExiting = True
            event.ignore()
        else:
            self.feed.close()
            event.accept()


    ################################################################################
    # Miscellaneous

    def viewAnswerKey(self):
        dialog = AK_Dialog(self.session_id)
        dialog.exec()  # Opens the dialog modally (blocks input to main window)
    

    def viewSizes(self):
        if self.filename:
            img = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
            blurred = cv2.GaussianBlur(img, (5, 5), 0)  
            _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            valid_chars = []
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                if w < 16 and h < 16:
                    continue
                char_crop = thresh[y:y + h, x:x + w]
                valid_chars.append((None, char_crop, x, y, w, h))

            if valid_chars:
                self.size_window = Characters(valid_chars, img)
                self.size_window.show()
            else:
                print("No valid characters found!")
        else:
            mboxStyle.warning(self, "Image Error", "No captured image file saved.")


    def fetchStats(self):
        session = Session()
        try:
            # Fetch the first two answer_key records associated with the session_id
            answer_keys = session.query(AnswerKey.id, 
                                        AnswerKey.fa_weight, 
                                        AnswerKey.steps_count, 
                                        AnswerKey.asm_choice) \
                .filter_by(session_id=self.session_id) \
                .order_by(AnswerKey.created_at.asc()) \
                .limit(2) \
                .all()

            # Extract values or set defaults if fewer than 2 exist
            if len(answer_keys) >= 1:
                self.first_ak_id = answer_keys[0].id
                fa_weight = answer_keys[0].fa_weight
                steps_count = answer_keys[0].steps_count
                self.asm_choice = answer_keys[0].asm_choice
                self.answer_key_ids.append(self.first_ak_id)

            else:
                self.first_ak_id = None
                fa_weight = 0
                steps_count = 0
                self.asm_choice = None

            if len(answer_keys) >= 2:
                self.second_ak_id = answer_keys[1].id
                fa_weight_2 = answer_keys[1].fa_weight
                steps_count_2 = answer_keys[1].steps_count
                self.asm_choice_2 = answer_keys[1].asm_choice
                
                self.answer_key_ids.append(self.second_ak_id)
            else:
                self.second_ak_id = None
                fa_weight_2 = 0
                steps_count_2 = 0
                self.asm_choice_2 = None
                
            # Update UI labels
            if len(answer_keys) == 1:
                self._ui.label_ak_count.setText(
                    f"AK 1: SOL steps = {steps_count}, FA weight: {fa_weight}%"
                )
            elif len(answer_keys) == 2:
                self._ui.label_ak_count.setText(
                    f"AK 1: SOL steps = {steps_count}, FA weight: {fa_weight}%\n"
                    f"AK 2: SOL steps = {steps_count_2}, FA weight: {fa_weight_2}%"
                )
            else:
                self._ui.label_ak_count.setText("No answer keys found.")

        except Exception as e:
            mboxStyle.critical(self, "Database Error", f"Error fetching AK data: {str(e)}")
            print(f"Error fetching AK data: {e}")

        finally:
            session.close()
            self._ui.label_counter.setText(f"No. of solutions checked:\n {self.counter}")


    def check_folder(self):
        # Check if the folder exists
        if not os.path.isdir(self.image_folder):
            print(f"The folder '{self.image_folder}' does not exist.")
            return False
        
        # List all files in the folder
        files_in_folder = os.listdir(self.image_folder)
        
        # Define common image extensions
        image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"}
        
        # Check if there are any image files in the folder
        image_files = [f for f in files_in_folder if os.path.splitext(f)[1].lower() in image_extensions]
        
        if not image_files:
            print(f"The folder '{self.image_folder}' exists, but contains no image files.")
            return False
        
        # If there are image files
        print(f"The folder '{self.image_folder}' contains image files: {image_files}")
        self.counter = len(image_files)
        return True


    def enableButtons(self):
        self._ui.takeImageButton.setEnabled(True)
        self._ui.takeImageButton.setText("Capture as\nanother solution")
        self._ui.push_retake.setEnabled(True)
        self._ui.push_size.setEnabled(True)
        self._ui.push_start.setEnabled(True)

        if self.feed.arduino:
            self._ui.push_feed.setEnabled(True) 
            self._ui.push_stop.setEnabled(True) 


    def disableButtons(self):
        self._ui.takeImageButton.setEnabled(False)
        self._ui.push_retake.setEnabled(False)
        self._ui.push_size.setEnabled(False)
        self._ui.push_start.setEnabled(False)

        self._ui.push_feed.setEnabled(False) 
