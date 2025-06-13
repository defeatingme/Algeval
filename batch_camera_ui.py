# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'batch_camera_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QWidget)

class Ui_Camera(object):
    def setupUi(self, Camera):
        if not Camera.objectName():
            Camera.setObjectName(u"Camera")
        Camera.resize(1200, 800)
        Camera.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255))")
        self.actionExit = QAction(Camera)
        self.actionExit.setObjectName(u"actionExit")
        self.actionStartCamera = QAction(Camera)
        self.actionStartCamera.setObjectName(u"actionStartCamera")
        self.actionStopCamera = QAction(Camera)
        self.actionStopCamera.setObjectName(u"actionStopCamera")
        self.actionSettings = QAction(Camera)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionAbout_Qt = QAction(Camera)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.centralwidget = QWidget(Camera)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 820, 740))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        palette = QPalette()
        gradient = QLinearGradient(1, 1, 1, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(64, 64, 64, 255))
        gradient.setColorAt(1, QColor(48, 48, 48, 255))
        brush = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        gradient1 = QLinearGradient(1, 1, 1, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(64, 64, 64, 255))
        gradient1.setColorAt(1, QColor(48, 48, 48, 255))
        brush1 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        gradient2 = QLinearGradient(1, 1, 1, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(64, 64, 64, 255))
        gradient2.setColorAt(1, QColor(48, 48, 48, 255))
        brush2 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        gradient3 = QLinearGradient(1, 1, 1, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(64, 64, 64, 255))
        gradient3.setColorAt(1, QColor(48, 48, 48, 255))
        brush3 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        gradient4 = QLinearGradient(1, 1, 1, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(64, 64, 64, 255))
        gradient4.setColorAt(1, QColor(48, 48, 48, 255))
        brush4 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        gradient5 = QLinearGradient(1, 1, 1, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(64, 64, 64, 255))
        gradient5.setColorAt(1, QColor(48, 48, 48, 255))
        brush5 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        gradient6 = QLinearGradient(1, 1, 1, 0)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(64, 64, 64, 255))
        gradient6.setColorAt(1, QColor(48, 48, 48, 255))
        brush6 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        gradient7 = QLinearGradient(1, 1, 1, 0)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(64, 64, 64, 255))
        gradient7.setColorAt(1, QColor(48, 48, 48, 255))
        brush7 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        gradient8 = QLinearGradient(1, 1, 1, 0)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(64, 64, 64, 255))
        gradient8.setColorAt(1, QColor(48, 48, 48, 255))
        brush8 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setStyleSheet(u"border: 1px solid rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"")
        self.viewfinderPage = QWidget()
        self.viewfinderPage.setObjectName(u"viewfinderPage")
        self.gridLayout_5 = QGridLayout(self.viewfinderPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.viewfinder = QVideoWidget(self.viewfinderPage)
        self.viewfinder.setObjectName(u"viewfinder")

        self.gridLayout_5.addWidget(self.viewfinder, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.viewfinderPage)
        self.previewPage = QWidget()
        self.previewPage.setObjectName(u"previewPage")
        self.gridLayout_4 = QGridLayout(self.previewPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lastImagePreviewLabel = QLabel(self.previewPage)
        self.lastImagePreviewLabel.setObjectName(u"lastImagePreviewLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lastImagePreviewLabel.sizePolicy().hasHeightForWidth())
        self.lastImagePreviewLabel.setSizePolicy(sizePolicy1)
        self.lastImagePreviewLabel.setFrameShape(QFrame.Shape.Box)

        self.gridLayout_4.addWidget(self.lastImagePreviewLabel, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.previewPage)
        self.push_back = QPushButton(self.centralwidget)
        self.push_back.setObjectName(u"push_back")
        self.push_back.setGeometry(QRect(830, 720, 121, 25))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
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
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(830, 440, 361, 151))
        font1 = QFont()
        font1.setPointSize(11)
        self.frame.setFont(font1)
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 40, 40, 255), stop:1 rgba(56, 56, 56, 255));\n"
"border: 1px solid rgb(175, 192, 220);\n"
"border-radius: 2px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.takeImageButton = QPushButton(self.frame)
        self.takeImageButton.setObjectName(u"takeImageButton")
        self.takeImageButton.setEnabled(False)
        self.takeImageButton.setGeometry(QRect(20, 10, 151, 61))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.takeImageButton.setFont(font2)
        self.takeImageButton.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(160, 160, 160);\n"
"    border-bottom: 2px solid rgb(96, 96, 96);\n"
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
        self.push_retake = QPushButton(self.frame)
        self.push_retake.setObjectName(u"push_retake")
        self.push_retake.setEnabled(False)
        self.push_retake.setGeometry(QRect(20, 80, 151, 25))
        self.push_retake.setFont(font2)
        self.push_retake.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(160, 160, 160);\n"
"    border-bottom: 2px solid rgb(96, 96, 96);\n"
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
        self.push_feed = QPushButton(self.frame)
        self.push_feed.setObjectName(u"push_feed")
        self.push_feed.setEnabled(False)
        self.push_feed.setGeometry(QRect(190, 10, 151, 61))
        self.push_feed.setFont(font2)
        self.push_feed.setStyleSheet(u"QPushButton {\n"
"    color:  rgb(224, 224, 224);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0  rgba(48, 48, 48, 255), stop:1 rgba(64, 64, 64, 255));\n"
"    border: 1px solid rgb(160, 160, 160);\n"
"    border-bottom: 2px solid rgb(96, 96, 96);\n"
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
        self.push_stop = QPushButton(self.frame)
        self.push_stop.setObjectName(u"push_stop")
        self.push_stop.setGeometry(QRect(190, 80, 151, 25))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.push_stop.setFont(font3)
        self.push_stop.setStyleSheet(u"QPushButton {\n"
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
        self.push_stop.setCheckable(False)
        self.push_delete = QPushButton(self.frame)
        self.push_delete.setObjectName(u"push_delete")
        self.push_delete.setGeometry(QRect(20, 110, 151, 25))
        self.push_delete.setFont(font3)
        self.push_delete.setStyleSheet(u"QPushButton {\n"
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
        self.push_delete.setCheckable(False)
        self.push_size = QPushButton(self.frame)
        self.push_size.setObjectName(u"push_size")
        self.push_size.setGeometry(QRect(190, 110, 151, 25))
        self.push_size.setFont(font3)
        self.push_size.setStyleSheet(u"QPushButton {\n"
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
        self.push_size.setCheckable(False)
        self.push_view_ak = QPushButton(self.centralwidget)
        self.push_view_ak.setObjectName(u"push_view_ak")
        self.push_view_ak.setGeometry(QRect(1060, 10, 121, 25))
        self.push_view_ak.setFont(font)
        self.push_view_ak.setStyleSheet(u"QPushButton {\n"
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
        self.push_view_ak.setCheckable(False)
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(830, 40, 361, 361))
        self.label_image.setFont(font)
        self.label_image.setStyleSheet(u"border: 1px solid  rgb(208, 172, 220);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(64, 64, 64, 255), stop:1 rgba(48, 48, 48, 255));\n"
"color: rgb(224, 224, 224);\n"
"border-radius: 2px")
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_counter = QLabel(self.centralwidget)
        self.label_counter.setObjectName(u"label_counter")
        self.label_counter.setGeometry(QRect(830, 410, 201, 21))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(True)
        self.label_counter.setFont(font4)
        self.label_counter.setStyleSheet(u"background-color: None;\n"
"color: rgb(192, 192, 192);\n"
"border: None;\n"
"")
        self.label_counter.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.push_view_info = QPushButton(self.centralwidget)
        self.push_view_info.setObjectName(u"push_view_info")
        self.push_view_info.setGeometry(QRect(960, 720, 201, 25))
        self.push_view_info.setFont(font)
        self.push_view_info.setStyleSheet(u"QPushButton {\n"
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
        self.push_view_info.setCheckable(False)
        self.label_ak_count = QLabel(self.centralwidget)
        self.label_ak_count.setObjectName(u"label_ak_count")
        self.label_ak_count.setGeometry(QRect(830, 0, 211, 41))
        self.label_ak_count.setFont(font4)
        self.label_ak_count.setStyleSheet(u"color: rgb(224, 224, 224);\n"
"background-color: None")
        self.label_ak_count.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.push_view_has = QPushButton(self.centralwidget)
        self.push_view_has.setObjectName(u"push_view_has")
        self.push_view_has.setGeometry(QRect(1040, 410, 151, 25))
        self.push_view_has.setFont(font)
        self.push_view_has.setStyleSheet(u"QPushButton {\n"
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
        self.push_view_has.setCheckable(False)
        self.push_start = QPushButton(self.centralwidget)
        self.push_start.setObjectName(u"push_start")
        self.push_start.setGeometry(QRect(860, 620, 300, 41))
        self.push_start.setFont(font)
        self.push_start.setStyleSheet(u"QPushButton {\n"
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
        self.push_start.setCheckable(False)
        self.label_start = QLabel(self.centralwidget)
        self.label_start.setObjectName(u"label_start")
        self.label_start.setGeometry(QRect(860, 600, 301, 21))
        self.label_start.setFont(font4)
        self.label_start.setStyleSheet(u"background-color: None;\n"
"color: rgb(192, 192, 192);\n"
"border: None;\n"
"")
        self.label_start.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.push_cancel = QPushButton(self.centralwidget)
        self.push_cancel.setObjectName(u"push_cancel")
        self.push_cancel.setGeometry(QRect(1040, 670, 121, 25))
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
        Camera.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Camera)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 21))
        self.menubar.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: #eee")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDevices = QMenu(self.menubar)
        self.menuDevices.setObjectName(u"menuDevices")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Camera.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Camera)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"color: #eee; \n"
"background-color: rgb(64,64,64)")
        Camera.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDevices.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionStartCamera)
        self.menuFile.addAction(self.actionStopCamera)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_Qt)

        self.retranslateUi(Camera)
        self.actionExit.triggered.connect(Camera.close)
        self.takeImageButton.clicked.connect(Camera.takeImage)
        self.actionSettings.triggered.connect(Camera.configureCaptureSettings)
        self.actionStartCamera.triggered.connect(Camera.startCamera)
        self.actionStopCamera.triggered.connect(Camera.stopCamera)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Camera)
    # setupUi

    def retranslateUi(self, Camera):
        Camera.setWindowTitle(QCoreApplication.translate("Camera", u"Camera", None))
        self.actionExit.setText(QCoreApplication.translate("Camera", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("Camera", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionStartCamera.setText(QCoreApplication.translate("Camera", u"Start Camera", None))
        self.actionStopCamera.setText(QCoreApplication.translate("Camera", u"Stop Camera", None))
        self.actionSettings.setText(QCoreApplication.translate("Camera", u"Change Settings", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("Camera", u"About Qt", None))
        self.lastImagePreviewLabel.setText("")
        self.push_back.setText(QCoreApplication.translate("Camera", u"Back", None))
        self.takeImageButton.setText(QCoreApplication.translate("Camera", u"Capture image", None))
        self.push_retake.setText(QCoreApplication.translate("Camera", u"Retake capture", None))
        self.push_feed.setText(QCoreApplication.translate("Camera", u"Activate feed", None))
        self.push_stop.setText(QCoreApplication.translate("Camera", u"Stop", None))
        self.push_delete.setText(QCoreApplication.translate("Camera", u"Delete image", None))
        self.push_size.setText(QCoreApplication.translate("Camera", u"View character sizes", None))
        self.push_view_ak.setText(QCoreApplication.translate("Camera", u"View AK(s)", None))
        self.label_image.setText(QCoreApplication.translate("Camera", u"Source file preview\n"
"360x360", None))
        self.label_counter.setText(QCoreApplication.translate("Camera", u"*No. of images captured: 0", None))
        self.push_view_info.setText(QCoreApplication.translate("Camera", u"View full checking info", None))
        self.label_ak_count.setText(QCoreApplication.translate("Camera", u"\n"
"AK 1: SOL steps = 0, FA weight: 20", None))
        self.push_view_has.setText(QCoreApplication.translate("Camera", u"View solution(s)", None))
        self.push_start.setText(QCoreApplication.translate("Camera", u"Start batch processing", None))
        self.label_start.setText(QCoreApplication.translate("Camera", u"*Start checking solutions from images", None))
        self.push_cancel.setText(QCoreApplication.translate("Camera", u"Cancel", None))
        self.menuFile.setTitle(QCoreApplication.translate("Camera", u"File", None))
        self.menuDevices.setTitle(QCoreApplication.translate("Camera", u"Devices", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Camera", u"Help", None))
    # retranslateUi

