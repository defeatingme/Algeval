# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rec_dialog_ui.ui'
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
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(720, 480)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.frame_latex = QFrame(Dialog)
        self.frame_latex.setObjectName(u"frame_latex")
        self.frame_latex.setGeometry(QRect(350, 50, 361, 411))
        self.frame_latex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px")
        self.frame_latex.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_latex.setFrameShadow(QFrame.Shadow.Raised)
        self.label_time = QLabel(self.frame_latex)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(10, 390, 351, 21))
        font = QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet(u"background-color: None;\n"
"color: rgb(192, 192, 192);\n"
"border: None;")
        self.label_time.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.web_latex = QWebEngineView(self.frame_latex)
        self.web_latex.setObjectName(u"web_latex")
        self.web_latex.setGeometry(QRect(0, 30, 361, 361))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        self.web_latex.setFont(font1)
        self.web_latex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_latex = QLabel(self.frame_latex)
        self.label_latex.setObjectName(u"label_latex")
        self.label_latex.setGeometry(QRect(0, 0, 225, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setUnderline(False)
        self.label_latex.setFont(font2)
        self.label_latex.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_latex.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_steps = QLabel(self.frame_latex)
        self.label_steps.setObjectName(u"label_steps")
        self.label_steps.setGeometry(QRect(220, 0, 141, 31))
        self.label_steps.setFont(font2)
        self.label_steps.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_steps.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_allow = QPushButton(Dialog)
        self.push_allow.setObjectName(u"push_allow")
        self.push_allow.setGeometry(QRect(20, 390, 151, 25))
        self.push_allow.setFont(font1)
        self.push_allow.setStyleSheet(u"QPushButton {\n"
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
        self.push_allow.setCheckable(False)
        self.push_cancel = QPushButton(Dialog)
        self.push_cancel.setObjectName(u"push_cancel")
        self.push_cancel.setGeometry(QRect(10, 440, 121, 25))
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
        self.label_ak = QLabel(Dialog)
        self.label_ak.setObjectName(u"label_ak")
        self.label_ak.setGeometry(QRect(10, 10, 701, 31))
        self.label_ak.setFont(font2)
        self.label_ak.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_ak.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_asm_note = QLabel(Dialog)
        self.label_asm_note.setObjectName(u"label_asm_note")
        self.label_asm_note.setGeometry(QRect(10, 360, 331, 21))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(True)
        font3.setUnderline(False)
        self.label_asm_note.setFont(font3)
        self.label_asm_note.setStyleSheet(u"background-color: None;\n"
"color: rgb(192, 192, 192);\n"
"border: None;\n"
"")
        self.label_asm_note.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.push_forbid = QPushButton(Dialog)
        self.push_forbid.setObjectName(u"push_forbid")
        self.push_forbid.setGeometry(QRect(180, 390, 151, 25))
        self.push_forbid.setFont(font1)
        self.push_forbid.setStyleSheet(u"QPushButton {\n"
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
        self.push_forbid.setCheckable(False)
        self.frame_asm = QFrame(Dialog)
        self.frame_asm.setObjectName(u"frame_asm")
        self.frame_asm.setGeometry(QRect(10, 50, 331, 301))
        self.frame_asm.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px")
        self.frame_asm.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_asm.setFrameShadow(QFrame.Shadow.Raised)
        self.push_generate = QPushButton(self.frame_asm)
        self.push_generate.setObjectName(u"push_generate")
        self.push_generate.setGeometry(QRect(60, 260, 210, 30))
        self.push_generate.setFont(font1)
        self.push_generate.setStyleSheet(u"QPushButton {\n"
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
        self.push_generate.setCheckable(False)
        self.label_input = QLabel(self.frame_asm)
        self.label_input.setObjectName(u"label_input")
        self.label_input.setGeometry(QRect(0, 0, 331, 31))
        self.label_input.setFont(font2)
        self.label_input.setStyleSheet(u"background-color: None;\n"
"color: rgb(224, 224, 224);\n"
"")
        self.label_input.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.edit_asm = QTextEdit(self.frame_asm)
        self.edit_asm.setObjectName(u"edit_asm")
        self.edit_asm.setGeometry(QRect(10, 40, 311, 211))
        font4 = QFont()
        font4.setPointSize(10)
        self.edit_asm.setFont(font4)
        self.edit_asm.setStyleSheet(u"padding: 2px; \n"
"border-radius: 2px; \n"
"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(32, 32, 32);\n"
"color: #eee")
        self.edit_asm.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.push_view = QPushButton(Dialog)
        self.push_view.setObjectName(u"push_view")
        self.push_view.setGeometry(QRect(140, 440, 121, 25))
        self.push_view.setFont(font1)
        self.push_view.setStyleSheet(u"QPushButton {\n"
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
        self.push_view.setCheckable(False)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_time.setText(QCoreApplication.translate("Dialog", u"Runtime: 0.00s", None))
        self.label_latex.setText(QCoreApplication.translate("Dialog", u"ASM recommendation:", None))
        self.label_steps.setText(QCoreApplication.translate("Dialog", u"No. of steps: ", None))
        self.push_allow.setText(QCoreApplication.translate("Dialog", u"Allow", None))
        self.push_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_ak.setText(QCoreApplication.translate("Dialog", u"Generate and recommend Alternative Solution Method (ASM) for AK", None))
        self.label_asm_note.setText(QCoreApplication.translate("Dialog", u"*Allow or forbid recommended ASM in solution checking?", None))
        self.push_forbid.setText(QCoreApplication.translate("Dialog", u"Forbid", None))
        self.push_generate.setText(QCoreApplication.translate("Dialog", u"Generate", None))
        self.label_input.setText(QCoreApplication.translate("Dialog", u"Input desired ASM recommendation:", None))
        self.edit_asm.setPlaceholderText(QCoreApplication.translate("Dialog", u"Recommend an alternative solution method differing from the answer key I provided...", None))
        self.push_view.setText(QCoreApplication.translate("Dialog", u"View AK", None))
    # retranslateUi

