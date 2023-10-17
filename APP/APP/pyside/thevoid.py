# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thevoid.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_theVoid(object):
    def setupUi(self, theVoid):
        if not theVoid.objectName():
            theVoid.setObjectName(u"theVoid")
        theVoid.resize(1319, 871)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(theVoid.sizePolicy().hasHeightForWidth())
        theVoid.setSizePolicy(sizePolicy)
        theVoid.setMinimumSize(QSize(800, 600))
        theVoid.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(theVoid)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.section1 = QFrame(self.frame)
        self.section1.setObjectName(u"section1")
        sizePolicy.setHeightForWidth(self.section1.sizePolicy().hasHeightForWidth())
        self.section1.setSizePolicy(sizePolicy)
        self.section1.setFrameShape(QFrame.StyledPanel)
        self.section1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.section1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.controlAndInfo = QFrame(self.section1)
        self.controlAndInfo.setObjectName(u"controlAndInfo")
        sizePolicy.setHeightForWidth(self.controlAndInfo.sizePolicy().hasHeightForWidth())
        self.controlAndInfo.setSizePolicy(sizePolicy)
        self.controlAndInfo.setStyleSheet(u"")
        self.controlAndInfo.setFrameShape(QFrame.StyledPanel)
        self.controlAndInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.controlAndInfo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.aboutAndConnection = QFrame(self.controlAndInfo)
        self.aboutAndConnection.setObjectName(u"aboutAndConnection")
        sizePolicy.setHeightForWidth(self.aboutAndConnection.sizePolicy().hasHeightForWidth())
        self.aboutAndConnection.setSizePolicy(sizePolicy)
        self.aboutAndConnection.setStyleSheet(u"")
        self.aboutAndConnection.setFrameShape(QFrame.StyledPanel)
        self.aboutAndConnection.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.aboutAndConnection)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logoAndId = QFrame(self.aboutAndConnection)
        self.logoAndId.setObjectName(u"logoAndId")
        self.logoAndId.setFrameShape(QFrame.StyledPanel)
        self.logoAndId.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.logoAndId)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.logo = QLabel(self.logoAndId)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u"image: url(:/logo/logo.svg);")

        self.verticalLayout_3.addWidget(self.logo)

        self.teamNo = QLabel(self.logoAndId)
        self.teamNo.setObjectName(u"teamNo")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro Medium"])
        font1.setPointSize(14)
        self.teamNo.setFont(font1)
        self.teamNo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.teamNo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.teamNo)

        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.logoAndId)

        self.connectMenu = QFrame(self.aboutAndConnection)
        self.connectMenu.setObjectName(u"connectMenu")
        sizePolicy.setHeightForWidth(self.connectMenu.sizePolicy().hasHeightForWidth())
        self.connectMenu.setSizePolicy(sizePolicy)
        self.connectMenu.setFrameShape(QFrame.StyledPanel)
        self.connectMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.connectMenu)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.infoConnect = QFrame(self.connectMenu)
        self.infoConnect.setObjectName(u"infoConnect")
        sizePolicy.setHeightForWidth(self.infoConnect.sizePolicy().hasHeightForWidth())
        self.infoConnect.setSizePolicy(sizePolicy)
        self.infoConnect.setFrameShape(QFrame.StyledPanel)
        self.infoConnect.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.infoConnect)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.infoTitle = QLabel(self.infoConnect)
        self.infoTitle.setObjectName(u"infoTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.infoTitle.sizePolicy().hasHeightForWidth())
        self.infoTitle.setSizePolicy(sizePolicy1)
        self.infoTitle.setFont(font1)
        self.infoTitle.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.infoTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.infoTitle)

        self.connectButton = QPushButton(self.infoConnect)
        self.connectButton.setObjectName(u"connectButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy2)
        self.connectButton.setFont(font1)
        self.connectButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.connectButton.setStyleSheet(u"QPushButton {\n"
"\n"
"color: #ffffff;\n"
"background-color:#252525;\n"
"border-radius: 5px;\n"
"border: 1px solid #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid #ffffff;\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.connectButton)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout_5.addWidget(self.infoConnect)

        self.ipPortBaudRate = QFrame(self.connectMenu)
        self.ipPortBaudRate.setObjectName(u"ipPortBaudRate")
        self.ipPortBaudRate.setFrameShape(QFrame.StyledPanel)
        self.ipPortBaudRate.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ipPortBaudRate)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ipArea = QFrame(self.ipPortBaudRate)
        self.ipArea.setObjectName(u"ipArea")
        self.ipArea.setFrameShape(QFrame.StyledPanel)
        self.ipArea.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ipArea)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ipTitle = QLabel(self.ipArea)
        self.ipTitle.setObjectName(u"ipTitle")
        self.ipTitle.setFont(font1)
        self.ipTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.ipTitle)

        self.ipInput = QLineEdit(self.ipArea)
        self.ipInput.setObjectName(u"ipInput")
        self.ipInput.setFont(font1)
        self.ipInput.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 37, 37);\n"
"border: 0;")

        self.horizontalLayout_4.addWidget(self.ipInput)


        self.verticalLayout_6.addWidget(self.ipArea)

        self.portArea = QFrame(self.ipPortBaudRate)
        self.portArea.setObjectName(u"portArea")
        self.portArea.setFrameShape(QFrame.StyledPanel)
        self.portArea.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.portArea)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.portTitle = QLabel(self.portArea)
        self.portTitle.setObjectName(u"portTitle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.portTitle.sizePolicy().hasHeightForWidth())
        self.portTitle.setSizePolicy(sizePolicy3)
        self.portTitle.setFont(font1)
        self.portTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.portTitle)

        self.portDataList = QComboBox(self.portArea)
        self.portDataList.addItem("")
        self.portDataList.addItem("")
        self.portDataList.addItem("")
        self.portDataList.setObjectName(u"portDataList")
        self.portDataList.setFont(font1)
        self.portDataList.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 37, 37);\n"
"border: 0;")

        self.horizontalLayout_5.addWidget(self.portDataList)


        self.verticalLayout_6.addWidget(self.portArea)

        self.baudrateArea = QFrame(self.ipPortBaudRate)
        self.baudrateArea.setObjectName(u"baudrateArea")
        self.baudrateArea.setFrameShape(QFrame.StyledPanel)
        self.baudrateArea.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.baudrateArea)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.baudrateTitle = QLabel(self.baudrateArea)
        self.baudrateTitle.setObjectName(u"baudrateTitle")
        sizePolicy3.setHeightForWidth(self.baudrateTitle.sizePolicy().hasHeightForWidth())
        self.baudrateTitle.setSizePolicy(sizePolicy3)
        self.baudrateTitle.setFont(font1)
        self.baudrateTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.baudrateTitle)

        self.baudrateDataList = QComboBox(self.baudrateArea)
        self.baudrateDataList.setObjectName(u"baudrateDataList")
        self.baudrateDataList.setFont(font1)
        self.baudrateDataList.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 37, 37);\n"
"border: 0;")

        self.horizontalLayout_6.addWidget(self.baudrateDataList)


        self.verticalLayout_6.addWidget(self.baudrateArea)


        self.verticalLayout_5.addWidget(self.ipPortBaudRate)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 3)

        self.horizontalLayout_2.addWidget(self.connectMenu)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.aboutAndConnection)

        self.timeAndFile = QFrame(self.controlAndInfo)
        self.timeAndFile.setObjectName(u"timeAndFile")
        sizePolicy.setHeightForWidth(self.timeAndFile.sizePolicy().hasHeightForWidth())
        self.timeAndFile.setSizePolicy(sizePolicy)
        self.timeAndFile.setFrameShape(QFrame.StyledPanel)
        self.timeAndFile.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.timeAndFile)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.timeFrame = QFrame(self.timeAndFile)
        self.timeFrame.setObjectName(u"timeFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.timeFrame.sizePolicy().hasHeightForWidth())
        self.timeFrame.setSizePolicy(sizePolicy4)
        self.timeFrame.setFrameShape(QFrame.StyledPanel)
        self.timeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.timeFrame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.liveTimeFrame = QFrame(self.timeFrame)
        self.liveTimeFrame.setObjectName(u"liveTimeFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.liveTimeFrame.sizePolicy().hasHeightForWidth())
        self.liveTimeFrame.setSizePolicy(sizePolicy5)
        font2 = QFont()
        font2.setFamilies([u"Ubuntu Mono"])
        font2.setPointSize(16)
        self.liveTimeFrame.setFont(font2)
        self.liveTimeFrame.setFrameShape(QFrame.StyledPanel)
        self.liveTimeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.liveTimeFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 0, -1, 0)
        self.liveTimeName = QLabel(self.liveTimeFrame)
        self.liveTimeName.setObjectName(u"liveTimeName")
        sizePolicy3.setHeightForWidth(self.liveTimeName.sizePolicy().hasHeightForWidth())
        self.liveTimeName.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro Medium"])
        font3.setPointSize(16)
        self.liveTimeName.setFont(font3)
        self.liveTimeName.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.liveTimeName)

        self.liveTimeValue = QLabel(self.liveTimeFrame)
        self.liveTimeValue.setObjectName(u"liveTimeValue")
        self.liveTimeValue.setFont(font3)
        self.liveTimeValue.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.liveTimeValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.liveTimeValue)


        self.verticalLayout_7.addWidget(self.liveTimeFrame)

        self.startTimeFrame = QFrame(self.timeFrame)
        self.startTimeFrame.setObjectName(u"startTimeFrame")
        self.startTimeFrame.setFont(font2)
        self.startTimeFrame.setFrameShape(QFrame.StyledPanel)
        self.startTimeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.startTimeFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.startTimeName = QLabel(self.startTimeFrame)
        self.startTimeName.setObjectName(u"startTimeName")
        sizePolicy3.setHeightForWidth(self.startTimeName.sizePolicy().hasHeightForWidth())
        self.startTimeName.setSizePolicy(sizePolicy3)
        self.startTimeName.setFont(font3)
        self.startTimeName.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.startTimeName)

        self.startTimeValue = QLabel(self.startTimeFrame)
        self.startTimeValue.setObjectName(u"startTimeValue")
        self.startTimeValue.setFont(font3)
        self.startTimeValue.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.startTimeValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.startTimeValue)


        self.verticalLayout_7.addWidget(self.startTimeFrame)

        self.disconnectTimeFrame = QFrame(self.timeFrame)
        self.disconnectTimeFrame.setObjectName(u"disconnectTimeFrame")
        self.disconnectTimeFrame.setFrameShape(QFrame.StyledPanel)
        self.disconnectTimeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.disconnectTimeFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.disconnectTime = QLabel(self.disconnectTimeFrame)
        self.disconnectTime.setObjectName(u"disconnectTime")
        sizePolicy3.setHeightForWidth(self.disconnectTime.sizePolicy().hasHeightForWidth())
        self.disconnectTime.setSizePolicy(sizePolicy3)
        self.disconnectTime.setFont(font1)
        self.disconnectTime.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.disconnectTime)

        self.disconnectTimeValue = QLabel(self.disconnectTimeFrame)
        self.disconnectTimeValue.setObjectName(u"disconnectTimeValue")
        self.disconnectTimeValue.setFont(font3)
        self.disconnectTimeValue.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.disconnectTimeValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.disconnectTimeValue)


        self.verticalLayout_7.addWidget(self.disconnectTimeFrame)

        self.downTimeFrame = QFrame(self.timeFrame)
        self.downTimeFrame.setObjectName(u"downTimeFrame")
        self.downTimeFrame.setFrameShape(QFrame.StyledPanel)
        self.downTimeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.downTimeFrame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.downTimeName = QLabel(self.downTimeFrame)
        self.downTimeName.setObjectName(u"downTimeName")
        sizePolicy3.setHeightForWidth(self.downTimeName.sizePolicy().hasHeightForWidth())
        self.downTimeName.setSizePolicy(sizePolicy3)
        self.downTimeName.setFont(font3)
        self.downTimeName.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.downTimeName)

        self.downTimeValue = QLabel(self.downTimeFrame)
        self.downTimeValue.setObjectName(u"downTimeValue")
        self.downTimeValue.setFont(font1)
        self.downTimeValue.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.downTimeValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.downTimeValue)


        self.verticalLayout_7.addWidget(self.downTimeFrame)

        self.totalTimeFrame = QFrame(self.timeFrame)
        self.totalTimeFrame.setObjectName(u"totalTimeFrame")
        self.totalTimeFrame.setFrameShape(QFrame.StyledPanel)
        self.totalTimeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.totalTimeFrame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.totalTimeName = QLabel(self.totalTimeFrame)
        self.totalTimeName.setObjectName(u"totalTimeName")
        sizePolicy3.setHeightForWidth(self.totalTimeName.sizePolicy().hasHeightForWidth())
        self.totalTimeName.setSizePolicy(sizePolicy3)
        self.totalTimeName.setFont(font3)
        self.totalTimeName.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.totalTimeName)

        self.totalTimeValue = QLabel(self.totalTimeFrame)
        self.totalTimeValue.setObjectName(u"totalTimeValue")
        self.totalTimeValue.setFont(font3)
        self.totalTimeValue.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.totalTimeValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.totalTimeValue)


        self.verticalLayout_7.addWidget(self.totalTimeFrame)


        self.horizontalLayout_7.addWidget(self.timeFrame)

        self.fileSendFrame = QFrame(self.timeAndFile)
        self.fileSendFrame.setObjectName(u"fileSendFrame")
        sizePolicy.setHeightForWidth(self.fileSendFrame.sizePolicy().hasHeightForWidth())
        self.fileSendFrame.setSizePolicy(sizePolicy)
        self.fileSendFrame.setFrameShape(QFrame.StyledPanel)
        self.fileSendFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.fileSendFrame)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.fileFrame = QFrame(self.fileSendFrame)
        self.fileFrame.setObjectName(u"fileFrame")
        sizePolicy.setHeightForWidth(self.fileFrame.sizePolicy().hasHeightForWidth())
        self.fileFrame.setSizePolicy(sizePolicy)
        self.fileFrame.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(37, 37, 37);")
        self.fileFrame.setFrameShape(QFrame.StyledPanel)
        self.fileFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.fileFrame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fileInput = QLabel(self.fileFrame)
        self.fileInput.setObjectName(u"fileInput")
        sizePolicy3.setHeightForWidth(self.fileInput.sizePolicy().hasHeightForWidth())
        self.fileInput.setSizePolicy(sizePolicy3)
        self.fileInput.setFont(font1)
        self.fileInput.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.fileInput)


        self.verticalLayout_8.addWidget(self.fileFrame)

        self.chooseButton = QPushButton(self.fileSendFrame)
        self.chooseButton.setObjectName(u"chooseButton")
        sizePolicy.setHeightForWidth(self.chooseButton.sizePolicy().hasHeightForWidth())
        self.chooseButton.setSizePolicy(sizePolicy)
        self.chooseButton.setFont(font1)
        self.chooseButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.chooseButton.setStyleSheet(u"QPushButton {\n"
"\n"
"color: #ffffff;\n"
"background-color:#252525;\n"
"border-radius: 5px;\n"
"border: 1px solid #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid #ffffff;\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.chooseButton)

        self.sendButton = QPushButton(self.fileSendFrame)
        self.sendButton.setObjectName(u"sendButton")
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setFont(font1)
        self.sendButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendButton.setStyleSheet(u"QPushButton {\n"
"\n"
"color: #ffffff;\n"
"background-color:#252525;\n"
"border-radius: 5px;\n"
"border: 1px solid #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid #ffffff;\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.sendButton)


        self.horizontalLayout_7.addWidget(self.fileSendFrame)


        self.verticalLayout_2.addWidget(self.timeAndFile)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 3)

        self.verticalLayout.addWidget(self.controlAndInfo)

        self.buttons = QFrame(self.section1)
        self.buttons.setObjectName(u"buttons")
        sizePolicy.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.buttons)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 5, 0, 5)
        self.startButton = QPushButton(self.buttons)
        self.startButton.setObjectName(u"startButton")
        sizePolicy2.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy2)
        self.startButton.setFont(font1)
        self.startButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.startButton.setStyleSheet(u"QPushButton {\n"
"\n"
"color: #ffffff;\n"
"background-color:#252525;\n"
"border-radius: 5px;\n"
"border: 1px solid #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid #ffffff;\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.verticalLayout_9.addWidget(self.startButton)

        self.otherButtonSet = QFrame(self.buttons)
        self.otherButtonSet.setObjectName(u"otherButtonSet")
        sizePolicy4.setHeightForWidth(self.otherButtonSet.sizePolicy().hasHeightForWidth())
        self.otherButtonSet.setSizePolicy(sizePolicy4)
        self.otherButtonSet.setFrameShape(QFrame.StyledPanel)
        self.otherButtonSet.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.otherButtonSet)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.buzzerButton = QPushButton(self.otherButtonSet)
        self.buzzerButton.setObjectName(u"buzzerButton")
        sizePolicy2.setHeightForWidth(self.buzzerButton.sizePolicy().hasHeightForWidth())
        self.buzzerButton.setSizePolicy(sizePolicy2)
        self.buzzerButton.setFont(font1)
        self.buzzerButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.buzzerButton.setStyleSheet(u"QPushButton {\n"
"\n"
"color: #ffffff;\n"
"background-color:#252525;\n"
"border-radius: 5px;\n"
"border: 1px solid #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid #ffffff;\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.buzzerButton, 0, 0, 1, 1)

        self.gpsButton = QPushButton(self.otherButtonSet)
        self.gpsButton.setObjectName(u"gpsButton")
        sizePolicy2.setHeightForWidth(self.gpsButton.sizePolicy().hasHeightForWidth())
        self.gpsButton.setSizePolicy(sizePolicy2)
        self.gpsButton.setFont(font1)
        self.gpsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.gpsButton.setStyleSheet(u"QPushButton {\n"
"\n"
"color: #ffffff;\n"
"background-color:#252525;\n"
"border-radius: 5px;\n"
"border: 1px solid #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid #ffffff;\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.gpsButton, 0, 1, 1, 1)

        self.cameraButton = QPushButton(self.otherButtonSet)
        self.cameraButton.setObjectName(u"cameraButton")
        sizePolicy2.setHeightForWidth(self.cameraButton.sizePolicy().hasHeightForWidth())
        self.cameraButton.setSizePolicy(sizePolicy2)
        self.cameraButton.setFont(font1)
        self.cameraButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cameraButton.setStyleSheet(u"QPushButton {\n"
"\n"
"color: #ffffff;\n"
"background-color:#252525;\n"
"border-radius: 5px;\n"
"border: 1px solid #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid #ffffff;\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.cameraButton, 0, 2, 1, 1)

        self.gyroButton = QPushButton(self.otherButtonSet)
        self.gyroButton.setObjectName(u"gyroButton")
        sizePolicy2.setHeightForWidth(self.gyroButton.sizePolicy().hasHeightForWidth())
        self.gyroButton.setSizePolicy(sizePolicy2)
        self.gyroButton.setFont(font1)
        self.gyroButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.gyroButton.setStyleSheet(u"QPushButton {\n"
"\n"
"color: #ffffff;\n"
"background-color:#252525;\n"
"border-radius: 5px;\n"
"border: 1px solid #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid #ffffff;\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.gyroButton, 1, 0, 1, 1)

        self.disconnectButton = QPushButton(self.otherButtonSet)
        self.disconnectButton.setObjectName(u"disconnectButton")
        sizePolicy2.setHeightForWidth(self.disconnectButton.sizePolicy().hasHeightForWidth())
        self.disconnectButton.setSizePolicy(sizePolicy2)
        self.disconnectButton.setFont(font1)
        self.disconnectButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.disconnectButton.setStyleSheet(u"QPushButton {\n"
"\n"
"color: #ffffff;\n"
"background-color:#252525;\n"
"border-radius: 5px;\n"
"border: 1px solid #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid #ffffff;\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.disconnectButton, 1, 1, 1, 1)

        self.preasureButton = QPushButton(self.otherButtonSet)
        self.preasureButton.setObjectName(u"preasureButton")
        sizePolicy2.setHeightForWidth(self.preasureButton.sizePolicy().hasHeightForWidth())
        self.preasureButton.setSizePolicy(sizePolicy2)
        self.preasureButton.setFont(font1)
        self.preasureButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.preasureButton.setStyleSheet(u"QPushButton {\n"
"\n"
"color: #ffffff;\n"
"background-color:#252525;\n"
"border-radius: 5px;\n"
"border: 1px solid #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid #ffffff;\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.preasureButton, 1, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.otherButtonSet)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 2)

        self.verticalLayout.addWidget(self.buttons)

        self.terminalArea = QFrame(self.section1)
        self.terminalArea.setObjectName(u"terminalArea")
        sizePolicy.setHeightForWidth(self.terminalArea.sizePolicy().hasHeightForWidth())
        self.terminalArea.setSizePolicy(sizePolicy)
        self.terminalArea.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;")
        self.terminalArea.setFrameShape(QFrame.StyledPanel)
        self.terminalArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.terminalArea)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.terminalTitle = QLabel(self.terminalArea)
        self.terminalTitle.setObjectName(u"terminalTitle")
        font4 = QFont()
        font4.setFamilies([u"Source Code Pro Medium"])
        font4.setPointSize(11)
        self.terminalTitle.setFont(font4)
        self.terminalTitle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.terminalTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.terminalTitle)

        self.terminalScreen = QTextBrowser(self.terminalArea)
        self.terminalScreen.setObjectName(u"terminalScreen")
        font5 = QFont()
        font5.setFamilies([u"Terminal"])
        font5.setPointSize(15)
        self.terminalScreen.setFont(font5)
        self.terminalScreen.setStyleSheet(u"background-color:#000;\n"
"\n"
"border: 1px solid #454545;\n"
"border-radius: 7px;")
        self.terminalScreen.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.terminalScreen.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_10.addWidget(self.terminalScreen)

        self.terminalCommandArea = QFrame(self.terminalArea)
        self.terminalCommandArea.setObjectName(u"terminalCommandArea")
        self.terminalCommandArea.setStyleSheet(u"background-color: #000;\n"
"padding: 3px;\n"
"padding-left: 7px;\n"
"color: rgb(255, 255, 255);\n"
"margin-bottom: 3px;\n"
"\n"
"border: 1px solid #454545;\n"
"border-radius: 7px;")
        self.terminalCommandArea.setFrameShape(QFrame.StyledPanel)
        self.terminalCommandArea.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.terminalCommandArea)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.terminalCommandInput = QLineEdit(self.terminalCommandArea)
        self.terminalCommandInput.setObjectName(u"terminalCommandInput")
        font6 = QFont()
        font6.setFamilies([u"Source Code Pro Medium"])
        self.terminalCommandInput.setFont(font6)
        self.terminalCommandInput.setStyleSheet(u"\n"
"padding: 3px;\n"
"padding-left: 7px;\n"
"color: rgb(255, 255, 255);\n"
"margin-bottom: 3px;\n"
"\n"
"border: 0px solid #454545;\n"
"border-radius: 7px;")
        self.terminalCommandInput.setPlaceholderText(u"command")

        self.horizontalLayout_13.addWidget(self.terminalCommandInput)

        self.sendButtonCommand = QPushButton(self.terminalCommandArea)
        self.sendButtonCommand.setObjectName(u"sendButtonCommand")
        self.sendButtonCommand.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendButtonCommand.setStyleSheet(u"image: url(:/icon/sendIcon.svg);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: 0px;\n"
"color: rgba(255, 255, 255, 0);")
        icon = QIcon()
        icon.addFile(u":/icon/sendIcon.svg", QSize(), QIcon.Normal, QIcon.On)
        self.sendButtonCommand.setIcon(icon)
        self.sendButtonCommand.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(self.sendButtonCommand)


        self.verticalLayout_10.addWidget(self.terminalCommandArea)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 10)

        self.verticalLayout.addWidget(self.terminalArea)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 4)

        self.horizontalLayout.addWidget(self.section1)

        self.section2 = QFrame(self.frame)
        self.section2.setObjectName(u"section2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.section2.sizePolicy().hasHeightForWidth())
        self.section2.setSizePolicy(sizePolicy6)
        self.section2.setFrameShape(QFrame.StyledPanel)
        self.section2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.section2)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cameraArea = QFrame(self.section2)
        self.cameraArea.setObjectName(u"cameraArea")
        self.cameraArea.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;")
        self.cameraArea.setFrameShape(QFrame.StyledPanel)
        self.cameraArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.cameraArea)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.cameraTitle = QLabel(self.cameraArea)
        self.cameraTitle.setObjectName(u"cameraTitle")
        sizePolicy.setHeightForWidth(self.cameraTitle.sizePolicy().hasHeightForWidth())
        self.cameraTitle.setSizePolicy(sizePolicy)
        self.cameraTitle.setFont(font3)
        self.cameraTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.cameraTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.cameraTitle)

        self.camera = QWidget(self.cameraArea)
        self.camera.setObjectName(u"camera")
        self.camera.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;")

        self.verticalLayout_12.addWidget(self.camera)

        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 5)

        self.verticalLayout_4.addWidget(self.cameraArea)

        self.humidityArea = QFrame(self.section2)
        self.humidityArea.setObjectName(u"humidityArea")
        sizePolicy2.setHeightForWidth(self.humidityArea.sizePolicy().hasHeightForWidth())
        self.humidityArea.setSizePolicy(sizePolicy2)
        self.humidityArea.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;")
        self.humidityArea.setFrameShape(QFrame.StyledPanel)
        self.humidityArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.humidityArea)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.humidityTitle = QLabel(self.humidityArea)
        self.humidityTitle.setObjectName(u"humidityTitle")
        sizePolicy.setHeightForWidth(self.humidityTitle.sizePolicy().hasHeightForWidth())
        self.humidityTitle.setSizePolicy(sizePolicy)
        self.humidityTitle.setFont(font3)
        self.humidityTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.humidityTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.humidityTitle)

        self.humidity = QWidget(self.humidityArea)
        self.humidity.setObjectName(u"humidity")
        self.humidity.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;")

        self.verticalLayout_13.addWidget(self.humidity)

        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 5)

        self.verticalLayout_4.addWidget(self.humidityArea)

        self.preasureArea = QFrame(self.section2)
        self.preasureArea.setObjectName(u"preasureArea")
        sizePolicy2.setHeightForWidth(self.preasureArea.sizePolicy().hasHeightForWidth())
        self.preasureArea.setSizePolicy(sizePolicy2)
        font7 = QFont()
        font7.setPointSize(11)
        self.preasureArea.setFont(font7)
        self.preasureArea.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;")
        self.preasureArea.setFrameShape(QFrame.StyledPanel)
        self.preasureArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.preasureArea)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.preasureTitle = QLabel(self.preasureArea)
        self.preasureTitle.setObjectName(u"preasureTitle")
        sizePolicy.setHeightForWidth(self.preasureTitle.sizePolicy().hasHeightForWidth())
        self.preasureTitle.setSizePolicy(sizePolicy)
        self.preasureTitle.setFont(font3)
        self.preasureTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.preasureTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.preasureTitle)

        self.preasure = QWidget(self.preasureArea)
        self.preasure.setObjectName(u"preasure")
        self.preasure.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;")

        self.verticalLayout_14.addWidget(self.preasure)

        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 5)

        self.verticalLayout_4.addWidget(self.preasureArea)


        self.horizontalLayout.addWidget(self.section2)

        self.section3 = QFrame(self.frame)
        self.section3.setObjectName(u"section3")
        sizePolicy6.setHeightForWidth(self.section3.sizePolicy().hasHeightForWidth())
        self.section3.setSizePolicy(sizePolicy6)
        font8 = QFont()
        font8.setFamilies([u"Source Code Pro Medium"])
        font8.setPointSize(10)
        self.section3.setFont(font8)
        self.section3.setStyleSheet(u"")
        self.section3.setFrameShape(QFrame.StyledPanel)
        self.section3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.section3)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gpsArea = QFrame(self.section3)
        self.gpsArea.setObjectName(u"gpsArea")
        self.gpsArea.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;")
        self.gpsArea.setFrameShape(QFrame.StyledPanel)
        self.gpsArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.gpsArea)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.gpsTitle = QLabel(self.gpsArea)
        self.gpsTitle.setObjectName(u"gpsTitle")
        sizePolicy.setHeightForWidth(self.gpsTitle.sizePolicy().hasHeightForWidth())
        self.gpsTitle.setSizePolicy(sizePolicy)
        self.gpsTitle.setFont(font3)
        self.gpsTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.gpsTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.gpsTitle)

        self.gps = QWidget(self.gpsArea)
        self.gps.setObjectName(u"gps")
        self.gps.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;")

        self.verticalLayout_17.addWidget(self.gps)

        self.verticalLayout_17.setStretch(0, 1)
        self.verticalLayout_17.setStretch(1, 5)

        self.verticalLayout_11.addWidget(self.gpsArea)

        self.temperatureArea = QFrame(self.section3)
        self.temperatureArea.setObjectName(u"temperatureArea")
        sizePolicy2.setHeightForWidth(self.temperatureArea.sizePolicy().hasHeightForWidth())
        self.temperatureArea.setSizePolicy(sizePolicy2)
        self.temperatureArea.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;")
        self.temperatureArea.setFrameShape(QFrame.StyledPanel)
        self.temperatureArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.temperatureArea)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.temperatureTitle = QLabel(self.temperatureArea)
        self.temperatureTitle.setObjectName(u"temperatureTitle")
        sizePolicy.setHeightForWidth(self.temperatureTitle.sizePolicy().hasHeightForWidth())
        self.temperatureTitle.setSizePolicy(sizePolicy)
        self.temperatureTitle.setFont(font3)
        self.temperatureTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.temperatureTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.temperatureTitle)

        self.temperature = QWidget(self.temperatureArea)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;")

        self.verticalLayout_16.addWidget(self.temperature)

        self.verticalLayout_16.setStretch(0, 1)
        self.verticalLayout_16.setStretch(1, 5)

        self.verticalLayout_11.addWidget(self.temperatureArea)

        self.accelerometerArea = QFrame(self.section3)
        self.accelerometerArea.setObjectName(u"accelerometerArea")
        sizePolicy4.setHeightForWidth(self.accelerometerArea.sizePolicy().hasHeightForWidth())
        self.accelerometerArea.setSizePolicy(sizePolicy4)
        self.accelerometerArea.setFont(font7)
        self.accelerometerArea.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;")
        self.accelerometerArea.setFrameShape(QFrame.StyledPanel)
        self.accelerometerArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.accelerometerArea)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.accelerometerTitle = QLabel(self.accelerometerArea)
        self.accelerometerTitle.setObjectName(u"accelerometerTitle")
        sizePolicy.setHeightForWidth(self.accelerometerTitle.sizePolicy().hasHeightForWidth())
        self.accelerometerTitle.setSizePolicy(sizePolicy)
        self.accelerometerTitle.setFont(font3)
        self.accelerometerTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.accelerometerTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.accelerometerTitle)

        self.accelerometer = QWidget(self.accelerometerArea)
        self.accelerometer.setObjectName(u"accelerometer")
        self.accelerometer.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;")

        self.verticalLayout_15.addWidget(self.accelerometer)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 5)

        self.verticalLayout_11.addWidget(self.accelerometerArea)


        self.horizontalLayout.addWidget(self.section3)

        self.section4 = QFrame(self.frame)
        self.section4.setObjectName(u"section4")
        sizePolicy6.setHeightForWidth(self.section4.sizePolicy().hasHeightForWidth())
        self.section4.setSizePolicy(sizePolicy6)
        self.section4.setStyleSheet(u"")
        self.section4.setFrameShape(QFrame.StyledPanel)
        self.section4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.section4)
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.errorArea = QFrame(self.section4)
        self.errorArea.setObjectName(u"errorArea")
        self.errorArea.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;")
        self.errorArea.setFrameShape(QFrame.StyledPanel)
        self.errorArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.errorArea)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, 5, 10, 10)
        self.errorTitle = QLabel(self.errorArea)
        self.errorTitle.setObjectName(u"errorTitle")
        sizePolicy.setHeightForWidth(self.errorTitle.sizePolicy().hasHeightForWidth())
        self.errorTitle.setSizePolicy(sizePolicy)
        self.errorTitle.setFont(font3)
        self.errorTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.errorTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.errorTitle)

        self.errorSet = QFrame(self.errorArea)
        self.errorSet.setObjectName(u"errorSet")
        self.errorSet.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;")
        self.horizontalLayout_18 = QHBoxLayout(self.errorSet)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.error1 = QLabel(self.errorSet)
        self.error1.setObjectName(u"error1")
        sizePolicy.setHeightForWidth(self.error1.sizePolicy().hasHeightForWidth())
        self.error1.setSizePolicy(sizePolicy)
        self.error1.setFont(font3)
        self.error1.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 3px;\n"
"color: rgb(255, 255, 255);")
        self.error1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.error1)

        self.error2 = QLabel(self.errorSet)
        self.error2.setObjectName(u"error2")
        sizePolicy.setHeightForWidth(self.error2.sizePolicy().hasHeightForWidth())
        self.error2.setSizePolicy(sizePolicy)
        self.error2.setFont(font3)
        self.error2.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 3px;\n"
"color: rgb(255, 255, 255);")
        self.error2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.error2)

        self.error3 = QLabel(self.errorSet)
        self.error3.setObjectName(u"error3")
        sizePolicy.setHeightForWidth(self.error3.sizePolicy().hasHeightForWidth())
        self.error3.setSizePolicy(sizePolicy)
        self.error3.setFont(font3)
        self.error3.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 3px;\n"
"color: rgb(255, 255, 255);")
        self.error3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.error3)

        self.error4 = QLabel(self.errorSet)
        self.error4.setObjectName(u"error4")
        sizePolicy.setHeightForWidth(self.error4.sizePolicy().hasHeightForWidth())
        self.error4.setSizePolicy(sizePolicy)
        self.error4.setFont(font3)
        self.error4.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 3px;\n"
"color: rgb(255, 255, 255);")
        self.error4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.error4)

        self.error5 = QLabel(self.errorSet)
        self.error5.setObjectName(u"error5")
        sizePolicy.setHeightForWidth(self.error5.sizePolicy().hasHeightForWidth())
        self.error5.setSizePolicy(sizePolicy)
        self.error5.setFont(font3)
        self.error5.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 3px;\n"
"color: rgb(255, 255, 255);")
        self.error5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.error5)


        self.verticalLayout_19.addWidget(self.errorSet)

        self.verticalLayout_19.setStretch(0, 1)
        self.verticalLayout_19.setStretch(1, 5)

        self.verticalLayout_24.addWidget(self.errorArea)

        self.gyroArea = QFrame(self.section4)
        self.gyroArea.setObjectName(u"gyroArea")
        self.gyroArea.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;")
        self.gyroArea.setFrameShape(QFrame.StyledPanel)
        self.gyroArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.gyroArea)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 5, 5, 5)
        self.gyroTitle = QLabel(self.gyroArea)
        self.gyroTitle.setObjectName(u"gyroTitle")
        sizePolicy.setHeightForWidth(self.gyroTitle.sizePolicy().hasHeightForWidth())
        self.gyroTitle.setSizePolicy(sizePolicy)
        self.gyroTitle.setFont(font3)
        self.gyroTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.gyroTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.gyroTitle)

        self.gyro = QOpenGLWidget(self.gyroArea)
        self.gyro.setObjectName(u"gyro")
        sizePolicy2.setHeightForWidth(self.gyro.sizePolicy().hasHeightForWidth())
        self.gyro.setSizePolicy(sizePolicy2)

        self.verticalLayout_20.addWidget(self.gyro)

        self.xArea = QHBoxLayout()
        self.xArea.setObjectName(u"xArea")
        self.xArea.setContentsMargins(10, -1, 10, -1)
        self.xTitle = QLabel(self.gyroArea)
        self.xTitle.setObjectName(u"xTitle")
        sizePolicy3.setHeightForWidth(self.xTitle.sizePolicy().hasHeightForWidth())
        self.xTitle.setSizePolicy(sizePolicy3)
        self.xTitle.setFont(font3)
        self.xTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")

        self.xArea.addWidget(self.xTitle)

        self.xValue = QLabel(self.gyroArea)
        self.xValue.setObjectName(u"xValue")
        self.xValue.setFont(font3)
        self.xValue.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.xValue.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.xArea.addWidget(self.xValue)


        self.verticalLayout_20.addLayout(self.xArea)

        self.yArea = QHBoxLayout()
        self.yArea.setObjectName(u"yArea")
        self.yArea.setContentsMargins(10, -1, 10, -1)
        self.yTitle = QLabel(self.gyroArea)
        self.yTitle.setObjectName(u"yTitle")
        sizePolicy3.setHeightForWidth(self.yTitle.sizePolicy().hasHeightForWidth())
        self.yTitle.setSizePolicy(sizePolicy3)
        self.yTitle.setFont(font1)
        self.yTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")

        self.yArea.addWidget(self.yTitle)

        self.yValue = QLabel(self.gyroArea)
        self.yValue.setObjectName(u"yValue")
        self.yValue.setFont(font3)
        self.yValue.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.yValue.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.yArea.addWidget(self.yValue)


        self.verticalLayout_20.addLayout(self.yArea)

        self.zArea = QHBoxLayout()
        self.zArea.setObjectName(u"zArea")
        self.zArea.setContentsMargins(10, -1, 10, -1)
        self.zTitle = QLabel(self.gyroArea)
        self.zTitle.setObjectName(u"zTitle")
        sizePolicy3.setHeightForWidth(self.zTitle.sizePolicy().hasHeightForWidth())
        self.zTitle.setSizePolicy(sizePolicy3)
        self.zTitle.setFont(font3)
        self.zTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")

        self.zArea.addWidget(self.zTitle)

        self.zValue = QLabel(self.gyroArea)
        self.zValue.setObjectName(u"zValue")
        self.zValue.setFont(font3)
        self.zValue.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.zValue.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.zArea.addWidget(self.zValue)


        self.verticalLayout_20.addLayout(self.zArea)

        self.verticalLayout_20.setStretch(0, 1)
        self.verticalLayout_20.setStretch(1, 7)
        self.verticalLayout_20.setStretch(2, 1)
        self.verticalLayout_20.setStretch(3, 1)
        self.verticalLayout_20.setStretch(4, 1)

        self.verticalLayout_24.addWidget(self.gyroArea)

        self.speedArea = QFrame(self.section4)
        self.speedArea.setObjectName(u"speedArea")
        self.speedArea.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 1px solid #fff;\n"
"border-radius: 7px;")
        self.speedArea.setFrameShape(QFrame.StyledPanel)
        self.speedArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.speedArea)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.speedTitle = QLabel(self.speedArea)
        self.speedTitle.setObjectName(u"speedTitle")
        sizePolicy.setHeightForWidth(self.speedTitle.sizePolicy().hasHeightForWidth())
        self.speedTitle.setSizePolicy(sizePolicy)
        self.speedTitle.setFont(font3)
        self.speedTitle.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);")
        self.speedTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.speedTitle)

        self.speed = QWidget(self.speedArea)
        self.speed.setObjectName(u"speed")
        self.speed.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"border: 0px solid #fff;\n"
"border-radius: 7px;")

        self.verticalLayout_23.addWidget(self.speed)

        self.verticalLayout_23.setStretch(0, 1)
        self.verticalLayout_23.setStretch(1, 5)

        self.verticalLayout_24.addWidget(self.speedArea)

        self.verticalLayout_24.setStretch(0, 1)
        self.verticalLayout_24.setStretch(1, 5)
        self.verticalLayout_24.setStretch(2, 3)

        self.horizontalLayout.addWidget(self.section4)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        theVoid.setCentralWidget(self.centralwidget)

        self.retranslateUi(theVoid)

        QMetaObject.connectSlotsByName(theVoid)
    # setupUi

    def retranslateUi(self, theVoid):
        theVoid.setWindowTitle(QCoreApplication.translate("theVoid", u"the.void", None))
        self.logo.setText("")
        self.teamNo.setText(QCoreApplication.translate("theVoid", u"TEAM NO", None))
        self.infoTitle.setText(QCoreApplication.translate("theVoid", u"INFO", None))
        self.connectButton.setText(QCoreApplication.translate("theVoid", u"CONNECT", None))
        self.ipTitle.setText(QCoreApplication.translate("theVoid", u"IP:", None))
        self.portTitle.setText(QCoreApplication.translate("theVoid", u"PORT:", None))
        self.portDataList.setItemText(0, QCoreApplication.translate("theVoid", u"123", None))
        self.portDataList.setItemText(1, QCoreApplication.translate("theVoid", u"456", None))
        self.portDataList.setItemText(2, QCoreApplication.translate("theVoid", u"789", None))

        self.baudrateTitle.setText(QCoreApplication.translate("theVoid", u"BAUDRATE:", None))
        self.liveTimeName.setText(QCoreApplication.translate("theVoid", u"TIME", None))
        self.liveTimeValue.setText(QCoreApplication.translate("theVoid", u"12:00", None))
        self.startTimeName.setText(QCoreApplication.translate("theVoid", u"START", None))
        self.startTimeValue.setText(QCoreApplication.translate("theVoid", u"12:00", None))
        self.disconnectTime.setText(QCoreApplication.translate("theVoid", u"DISCONNECT", None))
        self.disconnectTimeValue.setText(QCoreApplication.translate("theVoid", u"12:00", None))
        self.downTimeName.setText(QCoreApplication.translate("theVoid", u"DOWN", None))
#if QT_CONFIG(tooltip)
        self.downTimeValue.setToolTip(QCoreApplication.translate("theVoid", u"<html><head/><body><p>12:00</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.downTimeValue.setText(QCoreApplication.translate("theVoid", u"12:00", None))
        self.totalTimeName.setText(QCoreApplication.translate("theVoid", u"ALL", None))
        self.totalTimeValue.setText(QCoreApplication.translate("theVoid", u"12:00", None))
        self.fileInput.setText(QCoreApplication.translate("theVoid", u"name.mp4", None))
        self.chooseButton.setText(QCoreApplication.translate("theVoid", u"CHOOSE", None))
        self.sendButton.setText(QCoreApplication.translate("theVoid", u"SEND", None))
        self.startButton.setText(QCoreApplication.translate("theVoid", u"START", None))
        self.buzzerButton.setText(QCoreApplication.translate("theVoid", u"BUZZER", None))
        self.gpsButton.setText(QCoreApplication.translate("theVoid", u"GPS", None))
        self.cameraButton.setText(QCoreApplication.translate("theVoid", u"CAMERA", None))
        self.gyroButton.setText(QCoreApplication.translate("theVoid", u"GYRO", None))
        self.disconnectButton.setText(QCoreApplication.translate("theVoid", u"DISCONNECT", None))
        self.preasureButton.setText(QCoreApplication.translate("theVoid", u"PREASURE", None))
        self.terminalTitle.setText(QCoreApplication.translate("theVoid", u"TERMINAL", None))
        self.terminalScreen.setHtml(QCoreApplication.translate("theVoid", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Terminal'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#f3ff00;\">connecting...</span></p></body></html>", None))
        self.terminalScreen.setSearchPaths([])
        self.terminalCommandInput.setText("")
        self.sendButtonCommand.setText("")
        self.cameraTitle.setText(QCoreApplication.translate("theVoid", u"CAMERA", None))
        self.humidityTitle.setText(QCoreApplication.translate("theVoid", u"HUMIDITY", None))
        self.preasureTitle.setText(QCoreApplication.translate("theVoid", u"PREASURE", None))
        self.gpsTitle.setText(QCoreApplication.translate("theVoid", u"GPS", None))
        self.temperatureTitle.setText(QCoreApplication.translate("theVoid", u"TEMPERATURE", None))
        self.accelerometerTitle.setText(QCoreApplication.translate("theVoid", u"ACCELEROMETER", None))
        self.errorTitle.setText(QCoreApplication.translate("theVoid", u"ERROR", None))
        self.error1.setText(QCoreApplication.translate("theVoid", u"1", None))
        self.error2.setText(QCoreApplication.translate("theVoid", u"2", None))
        self.error3.setText(QCoreApplication.translate("theVoid", u"3", None))
        self.error4.setText(QCoreApplication.translate("theVoid", u"4", None))
        self.error5.setText(QCoreApplication.translate("theVoid", u"5", None))
        self.gyroTitle.setText(QCoreApplication.translate("theVoid", u"GYRO", None))
        self.xTitle.setText(QCoreApplication.translate("theVoid", u"X:", None))
        self.xValue.setText(QCoreApplication.translate("theVoid", u"123", None))
        self.yTitle.setText(QCoreApplication.translate("theVoid", u"Y:", None))
        self.yValue.setText(QCoreApplication.translate("theVoid", u"456", None))
        self.zTitle.setText(QCoreApplication.translate("theVoid", u"Z:", None))
        self.zValue.setText(QCoreApplication.translate("theVoid", u"789", None))
        self.speedTitle.setText(QCoreApplication.translate("theVoid", u"SPEED", None))
    # retranslateUi

