# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'has_dialog_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Table(object):
    def setupUi(self, Table):
        if not Table.objectName():
            Table.setObjectName(u"Table")
        Table.resize(1080, 720)
        Table.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.frame_has = QFrame(Table)
        self.frame_has.setObjectName(u"frame_has")
        self.frame_has.setGeometry(QRect(10, 50, 1061, 605))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        self.frame_has.setFont(font)
        self.frame_has.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px")
        self.frame_has.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_has.setFrameShadow(QFrame.Shadow.Raised)
        self.table_checked = QTableWidget(self.frame_has)
        self.table_checked.setObjectName(u"table_checked")
        self.table_checked.setGeometry(QRect(0, 0, 1061, 540))
        self.table_checked.setFont(font)
        self.table_checked.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"border-radius: 2px")
        self.label_note = QLabel(self.frame_has)
        self.label_note.setObjectName(u"label_note")
        self.label_note.setGeometry(QRect(10, 540, 820, 21))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setUnderline(False)
        self.label_note.setFont(font1)
        self.label_note.setStyleSheet(u"background-color: None;\n"
"color: rgb(208, 172, 220);\n"
"border: None;")
        self.label_note.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.frame_buttons = QFrame(self.frame_has)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setGeometry(QRect(0, 560, 1061, 45))
        self.frame_buttons.setFont(font)
        self.frame_buttons.setStyleSheet(u"background-color: rgb(48, 48, 48)")
        self.frame_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.push_reload = QPushButton(self.frame_buttons)
        self.push_reload.setObjectName(u"push_reload")
        self.push_reload.setGeometry(QRect(910, 10, 121, 25))
        self.push_reload.setFont(font)
        self.push_reload.setStyleSheet(u"QPushButton {\n"
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
        self.push_reload.setCheckable(False)
        self.push_delete_has = QPushButton(self.frame_buttons)
        self.push_delete_has.setObjectName(u"push_delete_has")
        self.push_delete_has.setGeometry(QRect(20, 10, 121, 25))
        self.push_delete_has.setFont(font)
        self.push_delete_has.setStyleSheet(u"QPushButton {\n"
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
        self.push_delete_has.setCheckable(False)
        self.label_has = QLabel(Table)
        self.label_has.setObjectName(u"label_has")
        self.label_has.setGeometry(QRect(10, 10, 1061, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.label_has.setFont(font2)
        self.label_has.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(208, 172, 220);\n"
"border: 1px solid rgb(208, 172, 220);\n"
"padding: 4px")
        self.label_has.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.push_back = QPushButton(Table)
        self.push_back.setObjectName(u"push_back")
        self.push_back.setGeometry(QRect(10, 670, 121, 25))
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

        self.retranslateUi(Table)

        QMetaObject.connectSlotsByName(Table)
    # setupUi

    def retranslateUi(self, Table):
        Table.setWindowTitle(QCoreApplication.translate("Table", u"Form", None))
        self.label_note.setText(QCoreApplication.translate("Table", u"*Last saved session:", None))
        self.push_reload.setText(QCoreApplication.translate("Table", u"Reload table", None))
        self.push_delete_has.setText(QCoreApplication.translate("Table", u"Delete record", None))
        self.label_has.setText(QCoreApplication.translate("Table", u"Full recorded solutions table", None))
        self.push_back.setText(QCoreApplication.translate("Table", u"Back", None))
    # retranslateUi

