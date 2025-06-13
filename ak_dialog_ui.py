# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ak_dialog_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1600, 540)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.frame_latex = QFrame(Dialog)
        self.frame_latex.setObjectName(u"frame_latex")
        self.frame_latex.setGeometry(QRect(10, 60, 781, 421))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        self.frame_latex.setFont(font)
        self.frame_latex.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: rgb(64, 64, 64);\n"
"border-radius: 2px\n"
"")
        self.frame_latex.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_latex.setFrameShadow(QFrame.Shadow.Raised)
        self.web_latex = QWebEngineView(self.frame_latex)
        self.web_latex.setObjectName(u"web_latex")
        self.web_latex.setGeometry(QRect(420, 30, 361, 391))
        self.web_latex.setFont(font)
        self.web_latex.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"border: 1px solid rgb(208, 172, 220)")
        self.label_sol_steps = QLabel(self.frame_latex)
        self.label_sol_steps.setObjectName(u"label_sol_steps")
        self.label_sol_steps.setGeometry(QRect(420, 0, 181, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.label_sol_steps.setFont(font1)
        self.label_sol_steps.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);")
        self.label_sol_steps.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_fa_grade = QLabel(self.frame_latex)
        self.label_fa_grade.setObjectName(u"label_fa_grade")
        self.label_fa_grade.setGeometry(QRect(600, 0, 181, 31))
        self.label_fa_grade.setFont(font1)
        self.label_fa_grade.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);")
        self.label_fa_grade.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_file = QLabel(self.frame_latex)
        self.label_file.setObjectName(u"label_file")
        self.label_file.setGeometry(QRect(0, 0, 420, 420))
        self.label_file.setFont(font)
        self.label_file.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"color: rgb(224, 224, 224);\n"
"border-radius: 2px")
        self.label_file.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.push_back = QPushButton(Dialog)
        self.push_back.setObjectName(u"push_back")
        self.push_back.setGeometry(QRect(550, 490, 241, 25))
        self.push_back.setFont(font)
        self.push_back.setStyleSheet(u"QPushButton {\n"
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
        self.push_back.setCheckable(False)
        self.label_ak = QLabel(Dialog)
        self.label_ak.setObjectName(u"label_ak")
        self.label_ak.setGeometry(QRect(10, 20, 781, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setUnderline(False)
        self.label_ak.setFont(font2)
        self.label_ak.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_ak.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_ak_2 = QLabel(Dialog)
        self.label_ak_2.setObjectName(u"label_ak_2")
        self.label_ak_2.setGeometry(QRect(810, 20, 781, 31))
        self.label_ak_2.setFont(font2)
        self.label_ak_2.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_ak_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_latex_2 = QFrame(Dialog)
        self.frame_latex_2.setObjectName(u"frame_latex_2")
        self.frame_latex_2.setGeometry(QRect(810, 60, 781, 421))
        self.frame_latex_2.setFont(font)
        self.frame_latex_2.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: rgb(64, 64, 64);\n"
"border-radius: 2px\n"
"")
        self.frame_latex_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_latex_2.setFrameShadow(QFrame.Shadow.Raised)
        self.web_latex_2 = QWebEngineView(self.frame_latex_2)
        self.web_latex_2.setObjectName(u"web_latex_2")
        self.web_latex_2.setGeometry(QRect(420, 30, 361, 391))
        self.web_latex_2.setFont(font)
        self.web_latex_2.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"border: 1px solid rgb(208, 172, 220)")
        self.label_sol_steps_2 = QLabel(self.frame_latex_2)
        self.label_sol_steps_2.setObjectName(u"label_sol_steps_2")
        self.label_sol_steps_2.setGeometry(QRect(420, 0, 181, 31))
        self.label_sol_steps_2.setFont(font1)
        self.label_sol_steps_2.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);")
        self.label_sol_steps_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_fa_grade_2 = QLabel(self.frame_latex_2)
        self.label_fa_grade_2.setObjectName(u"label_fa_grade_2")
        self.label_fa_grade_2.setGeometry(QRect(600, 0, 181, 31))
        self.label_fa_grade_2.setFont(font1)
        self.label_fa_grade_2.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: rgb(48, 48, 48);")
        self.label_fa_grade_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_file_2 = QLabel(self.frame_latex_2)
        self.label_file_2.setObjectName(u"label_file_2")
        self.label_file_2.setGeometry(QRect(0, 0, 420, 420))
        self.label_file_2.setFont(font)
        self.label_file_2.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"color: rgb(224, 224, 224);\n"
"border-radius: 2px")
        self.label_file_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_sol_steps.setText(QCoreApplication.translate("Dialog", u"Solution steps:", None))
        self.label_fa_grade.setText(QCoreApplication.translate("Dialog", u"Final answer: 10% weight", None))
        self.label_file.setText(QCoreApplication.translate("Dialog", u"Source file preview\n"
"420x420\n"
"\n"
"No source found", None))
        self.push_back.setText(QCoreApplication.translate("Dialog", u"Close", None))
        self.label_ak.setText(QCoreApplication.translate("Dialog", u"Answer key 1:", None))
        self.label_ak_2.setText(QCoreApplication.translate("Dialog", u"Answer key 2:", None))
        self.label_sol_steps_2.setText(QCoreApplication.translate("Dialog", u"Solution steps:", None))
        self.label_fa_grade_2.setText(QCoreApplication.translate("Dialog", u"Final answer weight:", None))
        self.label_file_2.setText(QCoreApplication.translate("Dialog", u"Source file preview\n"
"420x420\n"
"\n"
"No source found", None))
    # retranslateUi

