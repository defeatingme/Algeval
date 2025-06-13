# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asm_dialog_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Confirmation(object):
    def setupUi(self, Confirmation):
        if not Confirmation.objectName():
            Confirmation.setObjectName(u"Confirmation")
        Confirmation.resize(720, 540)
        Confirmation.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.push_forbid = QPushButton(Confirmation)
        self.push_forbid.setObjectName(u"push_forbid")
        self.push_forbid.setGeometry(QRect(200, 490, 151, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        self.push_forbid.setFont(font)
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
        self.push_allow = QPushButton(Confirmation)
        self.push_allow.setObjectName(u"push_allow")
        self.push_allow.setGeometry(QRect(370, 490, 151, 30))
        self.push_allow.setFont(font)
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
        self.label_prob_num = QLabel(Confirmation)
        self.label_prob_num.setObjectName(u"label_prob_num")
        self.label_prob_num.setGeometry(QRect(10, 10, 701, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setUnderline(False)
        self.label_prob_num.setFont(font1)
        self.label_prob_num.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_prob_num.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.web_ak_latex = QWebEngineView(Confirmation)
        self.web_ak_latex.setObjectName(u"web_ak_latex")
        self.web_ak_latex.setGeometry(QRect(15, 80, 341, 351))
        self.web_ak_latex.setFont(font)
        self.web_ak_latex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_ak_latex = QLabel(Confirmation)
        self.label_ak_latex.setObjectName(u"label_ak_latex")
        self.label_ak_latex.setGeometry(QRect(15, 50, 341, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setUnderline(False)
        self.label_ak_latex.setFont(font2)
        self.label_ak_latex.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_ak_latex.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_has_latex = QLabel(Confirmation)
        self.label_has_latex.setObjectName(u"label_has_latex")
        self.label_has_latex.setGeometry(QRect(365, 50, 341, 31))
        self.label_has_latex.setFont(font2)
        self.label_has_latex.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(224, 224, 224);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_has_latex.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.web_has_latex = QWebEngineView(Confirmation)
        self.web_has_latex.setObjectName(u"web_has_latex")
        self.web_has_latex.setGeometry(QRect(365, 80, 341, 351))
        self.web_has_latex.setFont(font)
        self.web_has_latex.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"border: 1px solid rgb(208, 172, 220);\n"
"")
        self.label_question = QLabel(Confirmation)
        self.label_question.setObjectName(u"label_question")
        self.label_question.setGeometry(QRect(10, 440, 701, 41))
        self.label_question.setFont(font2)
        self.label_question.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px;\n"
"color: rgb(224, 224 224)")
        self.label_question.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.push_cancel = QPushButton(Confirmation)
        self.push_cancel.setObjectName(u"push_cancel")
        self.push_cancel.setGeometry(QRect(10, 500, 151, 25))
        self.push_cancel.setFont(font)
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
        self.push_forbid.raise_()
        self.push_allow.raise_()
        self.label_prob_num.raise_()
        self.web_ak_latex.raise_()
        self.web_has_latex.raise_()
        self.label_has_latex.raise_()
        self.label_ak_latex.raise_()
        self.label_question.raise_()
        self.push_cancel.raise_()

        self.retranslateUi(Confirmation)

        QMetaObject.connectSlotsByName(Confirmation)
    # setupUi

    def retranslateUi(self, Confirmation):
        Confirmation.setWindowTitle(QCoreApplication.translate("Confirmation", u"Dialog", None))
        self.push_forbid.setText(QCoreApplication.translate("Confirmation", u"No, forbid it", None))
        self.push_allow.setText(QCoreApplication.translate("Confirmation", u"Yes, allow it", None))
        self.label_prob_num.setText(QCoreApplication.translate("Confirmation", u"Problem #: Alternative solution method used different from answer key", None))
        self.label_ak_latex.setText(QCoreApplication.translate("Confirmation", u"Answer key:", None))
        self.label_has_latex.setText(QCoreApplication.translate("Confirmation", u"Compared solution:", None))
        self.label_question.setText(QCoreApplication.translate("Confirmation", u"            The solution has an Alternative Method used correctly. Do you want to allow it?(Y/N)", None))
        self.push_cancel.setText(QCoreApplication.translate("Confirmation", u"Cancel checking", None))
    # retranslateUi

