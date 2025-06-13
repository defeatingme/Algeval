# CAMERA DEVICE FUNCTION: Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations
"""PySide6 port of the QtMultiMedia camera example from Qt v6.x"""
import os
import time
from pathlib import Path
from datetime import datetime
import textwrap
import cv2

from PySide6.QtMultimedia import (QCamera, QCameraDevice, QImageCapture, QMediaCaptureSession, QMediaDevices)
from PySide6.QtWidgets import QMainWindow, QPushButton, QDialog
from PySide6.QtGui import QAction, QActionGroup, QImage, QPixmap
from PySide6.QtCore import (QDir, QTimer, Qt, Slot, Signal, QObject, QThread)
from imagesettings import ImageSettings
from has_camera_ui import Ui_Camera
from styles import buttonStyle, buttonStyle2, mboxStyle, gradeLabelStyle, gradeLabelStyle2

from sim_ocr import SimulateOCR
from evaluation import Evaluation
from render_latex import MathJaxSOL, MathJaxRes, ClearHTML, LoadHTML
from database import Session, AnswerKey, StudentHAS
from ak_dialog import AK_Dialog
from has_dialog import HAS_Dialog
from asm_dialog import ASM_Dialog
from sizes import Characters
from feeder import Feeder


class OCRWorker(QObject):
    finished = Signal(dict, float)
    error = Signal(str)

    def __init__(self, file):
        super().__init__()
        self.file = file


    def run(self):
        try:
            start_ocr_timer = time.time()
            
            output = SimulateOCR(self.file)  # Run OCR

            ocr_time = time.time() - start_ocr_timer

            if output.full_solutions:
                self.finished.emit(output, ocr_time)  # Emit success signal
            else:
                self.error.emit(output.empty_message)
            
        except Exception as e:
            self.error.emit(str(e))



class GPTEvaluationWorker(QObject):
    finished = Signal()
    error = Signal(str, str)  # message, details
    result_ready = Signal(object)
    
    def __init__(self, evaluation, has_latex):
        super().__init__()
        self.eval = evaluation
        self.has_latex = has_latex
        self.result = None
        self.start_time = 0

        
    @Slot()
    def process(self):
        try:
            self.start_time = time.time()
            result = self.eval.evaluate(self.has_latex)
            
            # If None is returned, it means ASM confirmation is needed
            # The signal will be emitted from the Evaluation class directly
            if result is None:
                # Exit without emitting finished signal - we'll handle this later
                return
                
            # We got a result without ASM intervention needed
            self.result = result
            if self.result.problems:
                self.result_ready.emit(self.result)
            else:
                self.error.emit("No HAS Found", self.result.no_HAS_message or "Unknown error")
                
        except Exception as e:
            self.error.emit("Evaluation Error", str(e))
        finally:
            self.finished.emit()



class ASMResponseWorker(QObject):
    finished = Signal()
    error = Signal(str, str)
    result_ready = Signal(object)

    def __init__(self, evaluation, user_response):
        super().__init__()
        self.eval = evaluation
        self.user_response = user_response

        
    @Slot()
    def process(self):
        # Process the ASM response
        try:
            # Send the user's response to the evaluation
            result = self.eval.handleASM1(self.user_response)
            self.result = result
            if self.result.problems:
                self.result_ready.emit(self.result)
            else:
                self.error.emit("No HAS Found", self.result.no_HAS_message or "Unknown error")
                
        except Exception as e:
            self.error.emit("Evaluation Error", str(e))
        finally:
            self.finished.emit()



class FeedWorker(QObject):
    finished = Signal()
    error = Signal(str)

    def __init__(self, feeder):
        super().__init__()
        self.feeder = feeder


    def run(self):
        try:
            self.feeder.send_command("mode1")

            while True:
                # Read and decode the data
                line = self.feeder.arduino.readline().decode('utf-8').strip()
                
                # Process only IR sensor data
                if line == "Object passed. Stopping motor.":
                    time.sleep(1)
                    self.finished.emit()
                    break
                else:
                    continue
                        
        except Exception as e:
            self.error.emit(str(e))



class HAS_Camera(QMainWindow):
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

        self.eval.ask_asm_signal.connect(self.ASMConfirmation)
        self.eval.asm_response_signal.connect(self.eval.handleASM1)  
        self.eval.evaluation_done_signal.connect(self.DisplayEval)

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
        
        self.feed = Feeder()
        
        self.clearhtml = ClearHTML()
        self.loadhtml = LoadHTML()
        
        
        self._ui.web_latex.setHtml(self.clearhtml)
        self.reset_result()

        self.image_folder = os.path.join(os.getcwd(), "images", "has")
        os.makedirs(self.image_folder, exist_ok=True)  # Ensure the folder exists

        self._ui.actionAbout_Qt.triggered.connect(qApp.aboutQt)  # noqa: F821
        self.finishedImageProcessing.connect(self.OCRProcessing)

        self._ui.push_feed.clicked.connect(self.activate_mode)
        self._ui.push_stop.clicked.connect(self.stop_feed)

        self._ui.push_save.clicked.connect(self.saveToDatabase)
        self._ui.push_view_ak.clicked.connect(self.view_ak_data)
        self._ui.push_view_has.clicked.connect(self.view_has_data)


        self._ui.push_redo.clicked.connect(self.redoFromOCR)
        self._ui.push_recheck.clicked.connect(self.reEvaluate)
        self._ui.push_size.clicked.connect(self.viewSizes)
        self._ui.push_back.clicked.connect(self.backToSession)

        # disable all buttons by default
        self.updateCameraActive(False)
        ###self.readyForCapture(False)
        self.disableButtons()
        self.fetchStats()
        # try to actually initialize camera & mic
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
        self._ui.push_size.setEnabled(True)

    
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
        self.display_image()


    def display_image(self):
        # Display image in QLabel
        pixmap = QPixmap(self.filename)
        self._ui.label_image.setPixmap(pixmap.scaled(350, 300, Qt.AspectRatioMode.KeepAspectRatio))
        self.finishedImageProcessing.emit()


    ################################################################################
    # OCR and AI Threads

    def OCRProcessing(self):
        self._ui.web_latex.setHtml(self.loadhtml)
        self._ui.web_result.setHtml(self.loadhtml)

        print("OCR Processing Started.")

        self.ocr_thread = QThread()
        self.ocr_worker = OCRWorker(self.filename)

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
        self.has_latex = "\n\n\n".join(
            f"{i+1}. {item.problem_setup or '_'}\n" + (item.expressions or 'No solution')
            for i, item in enumerate(output.full_solutions)
        )
        print(self.has_latex)

        html_content = MathJaxSOL(self.has_latex)
        self._ui.web_latex.setHtml(html_content)

        self._ui.label_ocr_time.setText(f"OCR processing runtime:\n{ocr_time: .2f}s")
                
        if output.name and (not self._ui.edit_student_name.text().strip()):
            self._ui.edit_student_name.setText(str(output.name))
        
        self.GPTEvaluation()


    def handleOCRError(self, error_message):
        self._ui.web_latex.setHtml(self.clearhtml)
        self.reset_result()
        
        mboxStyle.warning(self, "OCR Error", error_message)
        
        self._ui.takeImageButton.setEnabled(True)
        self._ui.takeImageButton.setText("Retake capture")
        self._ui.push_redo.setEnabled(True)
        self._ui.push_size.setEnabled(True)

        self._ui.label_ocr_time.setText("OCR processing runtime:\n 0.00s")
        self._ui.label_check_time.setText("Solution checking runtime:\n 0.00s")
        self._ui.label_total_time.setText("Total runtime from capture to\nresult display: 0.00s")


    def cleanUpOCRThread(self):
        # Safely clean up the OCR thread
        if self.ocr_thread.isRunning():
            self.ocr_thread.quit()
            self.ocr_thread.wait()  # Ensure thread exits before deletion


    def GPTEvaluation(self):
        # Start the evaluation process in a separate thread
        try:
            # Disable UI buttons during evaluation
            self.disableButtons()
            
            # Store start time for performance measurement
            self.start_check_timer = time.time()
            
            # Create thread and worker
            self.eval_thread = QThread()
            self.eval_worker = GPTEvaluationWorker(self.eval, self.has_latex)
            
            # Move worker to thread
            self.eval_worker.moveToThread(self.eval_thread)
            
            # Connect signals
            self.eval_thread.started.connect(self.eval_worker.process)
            self.eval_worker.finished.connect(self.eval_thread.quit)
            self.eval_worker.finished.connect(self.eval_worker.deleteLater)
            self.eval_thread.finished.connect(self.eval_thread.deleteLater)
            
            # Connect result handling
            self.eval_worker.result_ready.connect(self.DisplayEval)
            self.eval_worker.error.connect(self.handleEvaluationError)
                        
            # Start the thread
            self.eval_thread.start()
            
        except Exception as e:
            self.reset_result()
            mboxStyle.warning(self, "Checking Error", str(e))
            self.enableButtons()


    def handleEvaluationError(self, error_type, error_message):
        # Handle errors during evaluation
        if error_type == "No HAS Found":
            html_content = MathJaxRes(error_message)
            self._ui.web_result.setHtml(html_content)
        else:
            self.reset_result()
            mboxStyle.warning(self, "Checking Error", error_message)
            
        self.enableButtons()


    def ASMConfirmation(self, problem):
        # Handle ASM confirmation dialog
        # Calculate time elapsed so far
        check_time = time.time() - self.start_check_timer
        self._ui.label_check_time.setText(f"Solution checking runtime:\n{check_time:.2f}s")

        # Find the answer key ID
        answer_key_id = None
        for j, ak_id in enumerate(self.answer_key_ids):
            if problem.problem_number == (j+1):
                answer_key_id = ak_id
                break

        # Create and show the dialog
        dialog = ASM_Dialog(self, problem, answer_key_id, self.has_latex)
        result = dialog.exec()
        
        if result == QDialog.Accepted:
            # Reset the timer for the next phase
            self.start_check_timer = time.time()
            print(f"User response: {dialog.user_response}")
            self.EvaluateASM(dialog.user_response)            
        else:  # User canceled the dialog
            self.reset_result()
            self.enableButtons()


    def EvaluateASM(self, asm_choice):
        # Create a new thread and worker for handling the ASM response
        self.asm_thread = QThread()
        self.asm_worker = ASMResponseWorker(self.eval, asm_choice)

        # Move worker to thread
        self.asm_worker.moveToThread(self.asm_thread)

        # Connect signals
        self.asm_thread.started.connect(self.asm_worker.process)
        self.asm_worker.finished.connect(self.asm_thread.quit)
        self.asm_worker.finished.connect(self.asm_worker.deleteLater)
        self.asm_thread.finished.connect(self.asm_thread.deleteLater)

        self.asm_worker.result_ready.connect(self.DisplayEval)
        self.asm_worker.error.connect(self.handleEvaluationError)

        # Start the thread
        self.asm_thread.start()


    def DisplayEval(self, result):
        self.result = result

        self.reset_result()
        result_display = "\n\n---\n\n".join(
            textwrap.dedent(f"""\
            ### Problem {prob.problem_number}. {prob.problem}\n{prob.result}\n
            Solution = ({prob.sol_calculation[0].correct_steps}/{prob.sol_calculation[0].total_steps}){prob.sol_calculation[0].weight} = {prob.sol_calculation[0].sol_grade}%
            Final Answer = {prob.fa_grade}%
            Overall Score = {prob.overall_grade}%
            """)
            if prob.sol_calculation else
            textwrap.dedent(f"""\
            ### Problem {prob.problem_number}. {prob.problem}\n{prob.result}\n
            Solution = None = 0%
            Final Answer = {prob.fa_grade or 0}%
            Overall Score = {prob.overall_grade or 0}%
            """)

            for prob in self.result.problems
            ) 

        html_content = MathJaxRes(str(result_display))
        self._ui.web_result.setHtml(html_content)
        # First problem
        if len(self.result.problems) > 0:
            prob_1 = self.result.problems[0]
            self._ui.label_prob_grade.setText(f"Grade for Problem {prob_1.problem_number}:")
            if prob_1.sol_calculation:
                self._ui.label_sol_grade.setText(f"Solution:\n({prob_1.sol_calculation[0].correct_steps}/{prob_1.sol_calculation[0].total_steps}){prob_1.sol_calculation[0].weight} = {prob_1.sol_calculation[0].sol_grade}%")
            else:
                self._ui.label_sol_grade.setText(f"Solution:\nNone = 0%")
            self._ui.label_fa_grade.setText(f"Final Answer:\n{prob_1.fa_grade}%")
            self._ui.label_overall_grade.setText(f"Overall:\n{prob_1.overall_grade}%")

        # Second problem (if exists)
        if len(self.result.problems) > 1:
            prob_2 = self.result.problems[1]
            self._ui.label_prob_grade_2.setText(f"Grade for Problem {prob_2.problem_number}:")
            if prob_2.sol_calculation:
                self._ui.label_sol_grade_2.setText(f"Solution:\n({prob_2.sol_calculation[0].correct_steps}/{prob_2.sol_calculation[0].total_steps}){prob_2.sol_calculation[0].weight} = {prob_2.sol_calculation[0].sol_grade}%")
            else:
                self._ui.label_sol_grade_2.setText(f"Solution:\nNone = 0%")
            self._ui.label_fa_grade_2.setText(f"Final Answer:\n{prob_2.fa_grade}%")
            self._ui.label_overall_grade_2.setText(f"Overall:\n{prob_2.overall_grade}%")

            self._ui.label_prob_grade_2.setStyleSheet(gradeLabelStyle)
            self._ui.label_sol_grade_2.setStyleSheet(gradeLabelStyle)
            self._ui.label_fa_grade_2.setStyleSheet(gradeLabelStyle)
            self._ui.label_overall_grade_2.setStyleSheet(gradeLabelStyle)
        
        #self._ui.label_prob_count.setText(f"No. of problems aimed to\nsolve by the solution: {self.result.problems_count_answered_by_HAS}")

        check_time = time.time() - self.start_check_timer
        self._ui.label_check_time.setText(f"Solution checking runtime:\n{check_time: .2f}s")

        total_time = time.time() - self.start_total_timer
        self._ui.label_total_time.setText(f"Total runtime from capture to\nresult display:{total_time: .2f}s")
        
        print("\n Total runtime: ", total_time)

        #Enable Buttons
        self.enableButtons()
        self._ui.push_save.setEnabled(True)


    def redoFromOCR(self):
        self.start_total_timer = time.time()
        self.disableButtons()        
        self.OCRProcessing()


    def reEvaluate(self):
        self.start_total_timer = time.time()
        self.disableButtons()        
        self.GPTEvaluation()


    ################################################################################
    # Feed Configs

    def activate_mode(self):
        self.disableButtons()
        print("activating feeder...")

        self.feed_thread = QThread()
        self.feed_worker = FeedWorker(self.feed)

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
        self.enableButtons()
        self.takeImage()


    def handleFeedError(self, error_message):        
        mboxStyle.warning(self, "Feed Error", error_message)
        self.enableButtons()
        

    def cleanUpFeedThread(self):
        # Safely clean up the OCR thread
        if self.feed_thread.isRunning():
            self.feed_thread.quit()
            self.feed_thread.wait()  # Ensure thread exits before deletion
            

    def stop_feed(self):
        if self.feed.feeding:
            self.feed.send_command("s")


    ################################################################################
    # Save and Close window

    def saveToDatabase(self):
        self._ui.push_save.setEnabled(False)
        has_name = self._ui.edit_student_name.text().strip() or "Anonymous"

        # Validate the file path before reading the file
        if self.filename == None:
            if self.has_file == None:
                mboxStyle.warning(self, "Error", "No file selected. Please upload an answer key file.");
                return
            else:
                pass
        else:
            # Read file
            try:
                with open(self.filename, "rb") as file:
                    self.has_file = file.read()
            except FileNotFoundError:
                mboxStyle.critical(self, "Error", "File not found. Please check the file path.")
                return
            
        prob_result = self.result.problems
        # Modified code to save results for multiple problems
        if len(prob_result) > 1:
            # If we have two problems to save
            session = Session()
            try:
                for i, prob in enumerate(prob_result[:2]):  # Iterate over list properly
                    for j, ak_id in enumerate(self.answer_key_ids):
                        if prob.problem_number == (j+1):
                            answer_key_id = ak_id
                            break

                    # Extract values safely for each problem
                    result = prob.result
                    employed_asm = prob.employed_asm or False
                                
                    if prob.sol_calculation:
                        sol_fraction = f"{prob.sol_calculation[0].correct_steps}/{prob.sol_calculation[0].total_steps}"
                        sol_grade = prob.sol_calculation[0].sol_grade
                    else:
                        sol_fraction = None
                        sol_grade = 0

                    fa_grade = prob.fa_grade or 0
                    overall_grade = prob.overall_grade or 0


                    # Create a new StudentHAS entry for each problem
                    student_has = StudentHAS(
                        session_id=self.session_id,
                        answer_key_id=answer_key_id,
                        has_name=has_name,
                        has_latex=self.has_latex,
                        result=result,
                        sol_fraction=sol_fraction,
                        sol_grade=sol_grade,
                        fa_grade=fa_grade,
                        overall_grade=overall_grade,
                        used_asm=employed_asm,
                        has_file=self.has_file
                    )

                    # Add each entry
                    session.add(student_has)
                
                # Commit all entries at once
                session.commit()

                # Update UI elements
                self.counter = session.query(StudentHAS).filter_by(session_id=self.session_id).count()

                #UI notifs
                self._ui.statusbar.showMessage("Handwritten solution record saved!")
                self._ui.takeImageButton.setText("Capture image")
                self._ui.label_counter.setText(f"No. of solution checked:\n {self.counter}")
                self._ui.label_last_name.setText(f"Last checked from:\n {has_name}")
                self._ui.edit_student_name.setText("")

            except Exception as e:
                # Rollback session if error occurs
                session.rollback()
                mboxStyle.critical(self, "Database Error", f"Error saving StudentHAS: {str(e)}")
                self._ui.push_save.setEnabled(True)
                print(e)
            finally:
                # Close the session
                session.close()
        else:
            for j, ak_id in enumerate(self.answer_key_ids):
                if prob_result[0].problem_number == (j+1):
                    answer_key_id = ak_id
                    break
            
            session = Session()
            try:
                # Extract values safely
                result = prob_result[0].result
                employed_asm = prob_result[0].employed_asm or False
                            
                if prob_result[0].sol_calculation:
                    sol_fraction = f"{prob_result[0].sol_calculation[0].correct_steps}/{prob_result[0].sol_calculation[0].total_steps}"
                    sol_grade = prob_result[0].sol_calculation[0].sol_grade
                else:
                    sol_fraction = None
                    sol_grade = 0

                fa_grade = prob_result[0].fa_grade or 0
                overall_grade = prob_result[0].overall_grade or 0
         
                # Create a new StudentHAS entry
                student_has = StudentHAS(
                    session_id=self.session_id,
                    answer_key_id=answer_key_id,
                    has_name=has_name,
                    has_latex=self.has_latex,
                    result=result,
                    sol_fraction=sol_fraction,
                    sol_grade=sol_grade,
                    fa_grade=fa_grade,
                    overall_grade=overall_grade,
                    used_asm=employed_asm,
                    has_file=self.has_file
                )
                # Add each entry
                session.add(student_has)
                
                # Commit all entries at once
                session.commit()

                self.counter = session.query(StudentHAS).filter_by(session_id=self.session_id).count()

                #UI notifs
                self._ui.statusbar.showMessage("Handwritten solution record saved!")
                self._ui.takeImageButton.setText("Capture image")
                self._ui.label_counter.setText(f"No. of solution checked:\n {self.counter}")
                self._ui.label_last_name.setText(f"Last checked from:\n {has_name}")
                self._ui.edit_student_name.setText("")

            except Exception as e:
                # Rollback session if error occurs
                session.rollback()
                mboxStyle.critical(self, "Database Error", f" Error saving StudentHAS: {str(e)}")
                self._ui.push_save.setEnabled(True)
                print(e)
            finally:
                # Close the session
                session.close()

    
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
            self.feed.close()
            event.accept()


    ################################################################################
    # Miscellaneous

    def view_ak_data(self):
        dialog = AK_Dialog(self.session_id)
        dialog.exec()  # Opens the dialog modally (blocks input to main window)
    

    def view_has_data(self):
        dialog = HAS_Dialog(self.session_id)
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
            answer_keys = session.query(AnswerKey.id, AnswerKey.fa_weight, AnswerKey.steps_count) \
                .filter_by(session_id=self.session_id) \
                .order_by(AnswerKey.created_at.asc()) \
                .limit(2) \
                .all()

            # Extract values or set defaults if fewer than 2 exist
            if len(answer_keys) >= 1:
                self.first_ak_id = answer_keys[0].id
                fa_weight = answer_keys[0].fa_weight
                steps_count = answer_keys[0].steps_count
                self.answer_key_ids.append(self.first_ak_id)

            else:
                self.first_ak_id = "None"
                fa_weight = 0
                steps_count = 0

            if len(answer_keys) >= 2:
                self.second_ak_id = answer_keys[1].id
                fa_weight_2 = answer_keys[1].fa_weight
                steps_count_2 = answer_keys[1].steps_count
                self.answer_key_ids.append(self.second_ak_id)
            else:
                self.second_ak_id = "None"
                fa_weight_2 = 0
                steps_count_2 = 0
                
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
            self._ui.label_last_name.setText(f"Last checked from:\n {self.last_checked_name}")


    def reset_result(self):
        self._ui.web_result.setHtml(self.clearhtml)

        self._ui.label_prob_grade.setText("Grade for problem 1:")
        self._ui.label_sol_grade.setText("Solution:")
        self._ui.label_fa_grade.setText("Final Answer:")
        self._ui.label_overall_grade.setText("Overall:")

        self._ui.label_prob_grade_2.setText("Grade for problem 2:")
        self._ui.label_sol_grade_2.setText("Solution:")
        self._ui.label_fa_grade_2.setText("Final Answer:")
        self._ui.label_overall_grade_2.setText("Overall:")

        self._ui.label_prob_grade_2.setStyleSheet(gradeLabelStyle2)
        self._ui.label_sol_grade_2.setStyleSheet(gradeLabelStyle2)
        self._ui.label_fa_grade_2.setStyleSheet(gradeLabelStyle2)
        self._ui.label_overall_grade_2.setStyleSheet(gradeLabelStyle2)


    def enableButtons(self):
        self._ui.takeImageButton.setEnabled(True)
        self._ui.takeImageButton.setText("Retake capture")
        self._ui.push_redo.setEnabled(True)
        self._ui.push_recheck.setEnabled(True)
        self._ui.push_size.setEnabled(True)

        if self.feed.arduino:
            self._ui.push_feed.setEnabled(True) 
            self._ui.push_stop.setEnabled(True) 


    def disableButtons(self):
        self._ui.takeImageButton.setEnabled(False)
        self._ui.push_redo.setEnabled(False)
        self._ui.push_recheck.setEnabled(False)
        self._ui.push_save.setEnabled(False)

        self._ui.push_feed.setEnabled(False)