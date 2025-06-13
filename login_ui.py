# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(760, 540)
        Login.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        Login.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.push_enter = QPushButton(Login)
        self.push_enter.setObjectName(u"push_enter")
        self.push_enter.setGeometry(QRect(530, 490, 211, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(False)
        self.push_enter.setFont(font)
        self.push_enter.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.push_enter.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"    border: 1px solid rgb(208, 172, 220);\n"
"    border-bottom: 2px solid rgb(121, 100, 128);\n"
"    border-radius: 4px\n"
"    }\n"
"    QPushButton:disabled {\n"
"    background-color: rgb(48, 48, 48);\n"
"    color:  rgb(160, 160, 160);\n"
"    border: 1px solid rgb(192, 192, 192);\n"
"    border-radius: 4px\n"
"    }")
        self.push_enter.setCheckable(False)
        self.label_wc = QLabel(Login)
        self.label_wc.setObjectName(u"label_wc")
        self.label_wc.setGeometry(QRect(0, 90, 271, 21))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setKerning(False)
        self.label_wc.setFont(font1)
        self.label_wc.setStyleSheet(u"background-color: rgb(208, 172, 220);\n"
"\n"
"color: rgb(32, 32, 32);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_wc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_name = QLabel(Login)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(0, 110, 761, 61))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(32)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.label_name.setFont(font2)
        self.label_name.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"padding: 8px")
        self.label_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_desc = QLabel(Login)
        self.label_desc.setObjectName(u"label_desc")
        self.label_desc.setGeometry(QRect(0, 170, 761, 41))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.label_desc.setFont(font3)
        self.label_desc.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None\n"
"")
        self.label_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_name = QLineEdit(Login)
        self.edit_name.setObjectName(u"edit_name")
        self.edit_name.setGeometry(QRect(20, 320, 721, 35))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        self.edit_name.setFont(font4)
        self.edit_name.setStyleSheet(u"padding: 8px; \n"
"border-radius: 2px; \n"
"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(32, 32, 32);\n"
"color: #eee")
        self.label_input_name = QLabel(Login)
        self.label_input_name.setObjectName(u"label_input_name")
        self.label_input_name.setGeometry(QRect(20, 300, 361, 20))
        self.label_input_name.setFont(font)
        self.label_input_name.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None\n"
"")
        self.label_input_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.edit_email = QLineEdit(Login)
        self.edit_email.setObjectName(u"edit_email")
        self.edit_email.setGeometry(QRect(20, 380, 721, 35))
        self.edit_email.setFont(font4)
        self.edit_email.setStyleSheet(u"padding: 8px; \n"
"border-radius: 2px; \n"
"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(32, 32, 32);\n"
"color: #eee")
        self.label_input_email = QLabel(Login)
        self.label_input_email.setObjectName(u"label_input_email")
        self.label_input_email.setGeometry(QRect(20, 360, 361, 20))
        self.label_input_email.setFont(font)
        self.label_input_email.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None\n"
"")
        self.label_input_email.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.edit_dept = QLineEdit(Login)
        self.edit_dept.setObjectName(u"edit_dept")
        self.edit_dept.setGeometry(QRect(20, 440, 721, 35))
        self.edit_dept.setFont(font4)
        self.edit_dept.setStyleSheet(u"padding: 8px; \n"
"border-radius: 2px; \n"
"border: 1px solid rgb(208, 172, 220);\n"
"background-color: rgb(32, 32, 32);\n"
"color: #eee")
        self.label_input_dept = QLabel(Login)
        self.label_input_dept.setObjectName(u"label_input_dept")
        self.label_input_dept.setGeometry(QRect(20, 420, 361, 20))
        self.label_input_dept.setFont(font)
        self.label_input_dept.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None\n"
"")
        self.label_input_dept.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_icon = QLabel(Login)
        self.label_icon.setObjectName(u"label_icon")
        self.label_icon.setGeometry(QRect(630, 10, 80, 80))
        self.label_icon.setStyleSheet(u"border: None;\n"
"background-color: None")

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.push_enter.setText(QCoreApplication.translate("Login", u"Start program", None))
        self.label_wc.setText(QCoreApplication.translate("Login", u"Welcome to", None))
        self.label_name.setText(QCoreApplication.translate("Login", u"A  L  G  E  V  A  L", None))
        self.label_desc.setText(QCoreApplication.translate("Login", u"A Step-by-step Handwritten Algebraic Solution Checker\n"
"using GPT-4o.", None))
        self.edit_name.setText("")
        self.edit_name.setPlaceholderText(QCoreApplication.translate("Login", u"Anonymous by default", None))
        self.label_input_name.setText(QCoreApplication.translate("Login", u"Enter your name:", None))
        self.edit_email.setText("")
        self.edit_email.setPlaceholderText(QCoreApplication.translate("Login", u"Optional", None))
        self.label_input_email.setText(QCoreApplication.translate("Login", u"Email:", None))
        self.edit_dept.setText("")
        self.edit_dept.setPlaceholderText(QCoreApplication.translate("Login", u"Optional", None))
        self.label_input_dept.setText(QCoreApplication.translate("Login", u"Department:", None))
        self.label_icon.setText("")
    # retranslateUi

