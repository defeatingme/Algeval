# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'batch_result_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Result(object):
    def setupUi(self, Result):
        if not Result.objectName():
            Result.setObjectName(u"Result")
        Result.resize(800, 800)
        Result.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.label_ak = QLabel(Result)
        self.label_ak.setObjectName(u"label_ak")
        self.label_ak.setGeometry(QRect(10, 10, 781, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        self.label_ak.setFont(font)
        self.label_ak.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_ak.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_result = QFrame(Result)
        self.frame_result.setObjectName(u"frame_result")
        self.frame_result.setGeometry(QRect(385, 50, 401, 641))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        self.frame_result.setFont(font1)
        self.frame_result.setStyleSheet(u"border: 1px solid rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border-radius: 2px")
        self.frame_result.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_result.setFrameShadow(QFrame.Shadow.Raised)
        self.label_result = QLabel(self.frame_result)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(0, 0, 401, 30))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.label_result.setFont(font2)
        self.label_result.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_sol_grade = QLabel(self.frame_result)
        self.label_sol_grade.setObjectName(u"label_sol_grade")
        self.label_sol_grade.setGeometry(QRect(0, 510, 121, 50))
        self.label_sol_grade.setFont(font2)
        self.label_sol_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_sol_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_fa_grade = QLabel(self.frame_result)
        self.label_fa_grade.setObjectName(u"label_fa_grade")
        self.label_fa_grade.setGeometry(QRect(120, 510, 120, 50))
        self.label_fa_grade.setFont(font2)
        self.label_fa_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_fa_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_overall_grade = QLabel(self.frame_result)
        self.label_overall_grade.setObjectName(u"label_overall_grade")
        self.label_overall_grade.setGeometry(QRect(240, 510, 161, 50))
        self.label_overall_grade.setFont(font2)
        self.label_overall_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_overall_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.web_result = QWebEngineView(self.frame_result)
        self.web_result.setObjectName(u"web_result")
        self.web_result.setGeometry(QRect(0, 30, 401, 450))
        self.web_result.setFont(font1)
        self.web_result.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"")
        self.label_prob_grade = QLabel(self.frame_result)
        self.label_prob_grade.setObjectName(u"label_prob_grade")
        self.label_prob_grade.setGeometry(QRect(0, 480, 401, 30))
        self.label_prob_grade.setFont(font2)
        self.label_prob_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);\n"
"")
        self.label_fa_grade_2 = QLabel(self.frame_result)
        self.label_fa_grade_2.setObjectName(u"label_fa_grade_2")
        self.label_fa_grade_2.setGeometry(QRect(120, 590, 120, 50))
        self.label_fa_grade_2.setFont(font2)
        self.label_fa_grade_2.setStyleSheet(u"color: rgba(224, 224, 224, 32);\n"
"background-color: rgba(48, 48, 48, 32);\n"
"border: 1px solid rgba(208, 172, 220, 32);\n"
"")
        self.label_fa_grade_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_sol_grade_2 = QLabel(self.frame_result)
        self.label_sol_grade_2.setObjectName(u"label_sol_grade_2")
        self.label_sol_grade_2.setGeometry(QRect(0, 590, 121, 50))
        self.label_sol_grade_2.setFont(font2)
        self.label_sol_grade_2.setStyleSheet(u"color: rgba(224, 224, 224, 32);\n"
"background-color: rgba(48, 48, 48, 32);\n"
"border: 1px solid rgba(208, 172, 220, 32);\n"
"")
        self.label_sol_grade_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_overall_grade_2 = QLabel(self.frame_result)
        self.label_overall_grade_2.setObjectName(u"label_overall_grade_2")
        self.label_overall_grade_2.setGeometry(QRect(240, 590, 161, 50))
        self.label_overall_grade_2.setFont(font2)
        self.label_overall_grade_2.setStyleSheet(u"color: rgba(224, 224, 224, 32);\n"
"background-color: rgba(48, 48, 48, 32);\n"
"border: 1px solid rgba(208, 172, 220, 32);\n"
"")
        self.label_overall_grade_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_prob_grade_2 = QLabel(self.frame_result)
        self.label_prob_grade_2.setObjectName(u"label_prob_grade_2")
        self.label_prob_grade_2.setGeometry(QRect(0, 560, 401, 30))
        self.label_prob_grade_2.setFont(font2)
        self.label_prob_grade_2.setStyleSheet(u"color: rgba(224, 224, 224, 32);\n"
"background-color: rgba(48, 48, 48, 32);\n"
"border: 1px solid rgba(208, 172, 220, 32);\n"
"")
        self.web_latex = QWebEngineView(Result)
        self.web_latex.setObjectName(u"web_latex")
        self.web_latex.setGeometry(QRect(15, 330, 361, 361))
        self.web_latex.setFont(font1)
        self.web_latex.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"border: 1px solid rgb(208, 172, 220)")
        self.push_next = QPushButton(Result)
        self.push_next.setObjectName(u"push_next")
        self.push_next.setGeometry(QRect(200, 710, 181, 25))
        self.push_next.setFont(font1)
        self.push_next.setStyleSheet(u"QPushButton {\n"
"background-color: #333;\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: rgb(64, 64, 64);\n"
"color:  rgb(192, 192, 192);\n"
"border: 1px solid rgb(192, 192, 192);\n"
"border-radius: 4px\n"
"}\n"
"")
        self.push_next.setCheckable(False)
        self.push_prev = QPushButton(Result)
        self.push_prev.setObjectName(u"push_prev")
        self.push_prev.setGeometry(QRect(10, 710, 180, 25))
        self.push_prev.setFont(font1)
        self.push_prev.setStyleSheet(u"QPushButton {\n"
"background-color: #333;\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: rgb(64, 64, 64);\n"
"color:  rgb(192, 192, 192);\n"
"border: 1px solid rgb(192, 192, 192);\n"
"border-radius: 4px\n"
"}\n"
"")
        self.push_prev.setCheckable(False)
        self.push_save = QPushButton(Result)
        self.push_save.setObjectName(u"push_save")
        self.push_save.setGeometry(QRect(400, 740, 360, 31))
        self.push_save.setFont(font1)
        self.push_save.setStyleSheet(u"QPushButton {\n"
"background-color: #333;\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 4px\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: rgb(64, 64, 64);\n"
"color:  rgb(192, 192, 192);\n"
"border: 1px solid rgb(192, 192, 192);\n"
"border-radius: 4px\n"
"}\n"
"")
        self.push_save.setCheckable(False)
        self.label_student_name = QLabel(Result)
        self.label_student_name.setObjectName(u"label_student_name")
        self.label_student_name.setGeometry(QRect(401, 705, 80, 21))
        self.label_student_name.setFont(font)
        self.label_student_name.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None;\n"
"border: None")
        self.label_student_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.edit_student_name = QLineEdit(Result)
        self.edit_student_name.setObjectName(u"edit_student_name")
        self.edit_student_name.setGeometry(QRect(450, 700, 271, 30))
        self.edit_student_name.setFont(font1)
        self.edit_student_name.setStyleSheet(u"padding: 2px; \n"
"border-radius: 2px; \n"
"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(224, 224, 224)")
        self.push_cancel = QPushButton(Result)
        self.push_cancel.setObjectName(u"push_cancel")
        self.push_cancel.setGeometry(QRect(10, 760, 121, 25))
        self.push_cancel.setFont(font1)
        self.push_cancel.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(152, 152, 160);\n"
"    border-bottom: 2px solid rgb(88, 88, 96);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(128, 128, 128);\n"
"    border: 1px solid rgb(128, 128, 128);\n"
"    }\n"
"    QPushButton:hover {\n"
"    color:  rgb(224, 224, 224);\n"
"    border: 1px solid rgb(175, 192, 220);\n"
"    }\n"
"    QPushButton:pressed {\n"
"    background-color:  rgb(208, 172, 220);\n"
"    color: rgb(224, 224, 224);\n"
"    border: 1px solid rgb(224, 224, 224);\n"
"    font-weight: bold;\n"
"    }")
        self.push_cancel.setCheckable(False)
        self.label_page = QLabel(Result)
        self.label_page.setObjectName(u"label_page")
        self.label_page.setGeometry(QRect(10, 50, 91, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(True)
        font3.setUnderline(False)
        self.label_page.setFont(font3)
        self.label_page.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px")
        self.label_page.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_image = QLabel(Result)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(105, 50, 271, 271))
        self.label_image.setFont(font1)
        self.label_image.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"color: rgb(224, 224, 224);\n"
"border-radius: 2px")
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Result)

        QMetaObject.connectSlotsByName(Result)
    # setupUi

    def retranslateUi(self, Result):
        Result.setWindowTitle(QCoreApplication.translate("Result", u"Form", None))
        self.label_ak.setText(QCoreApplication.translate("Result", u"Batch processing results", None))
        self.label_result.setText(QCoreApplication.translate("Result", u"Step-by-step checking result:", None))
        self.label_sol_grade.setText(QCoreApplication.translate("Result", u"Solution:", None))
        self.label_fa_grade.setText(QCoreApplication.translate("Result", u"Final Answer:", None))
        self.label_overall_grade.setText(QCoreApplication.translate("Result", u"Overall:", None))
        self.label_prob_grade.setText(QCoreApplication.translate("Result", u"Grade for problem 1:", None))
        self.label_fa_grade_2.setText(QCoreApplication.translate("Result", u"Final Answer:", None))
        self.label_sol_grade_2.setText(QCoreApplication.translate("Result", u"Solution:", None))
        self.label_overall_grade_2.setText(QCoreApplication.translate("Result", u"Overall:", None))
        self.label_prob_grade_2.setText(QCoreApplication.translate("Result", u"Grade for problem 2:", None))
        self.push_next.setText(QCoreApplication.translate("Result", u"Next", None))
        self.push_prev.setText(QCoreApplication.translate("Result", u"Previous", None))
        self.push_save.setText(QCoreApplication.translate("Result", u"Record checked solutions", None))
        self.label_student_name.setText(QCoreApplication.translate("Result", u"Name:", None))
        self.edit_student_name.setText("")
        self.edit_student_name.setPlaceholderText(QCoreApplication.translate("Result", u"May auto-fill after scan if none", None))
        self.push_cancel.setText(QCoreApplication.translate("Result", u"Cancel", None))
        self.label_page.setText(QCoreApplication.translate("Result", u"Page 0 of 0", None))
        self.label_image.setText(QCoreApplication.translate("Result", u"Source file preview\n"
"270x270", None))
    # retranslateUi

