# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IHMv2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QLabel,
                               QMainWindow, QMenuBar, QProgressBar, QPushButton,
                               QSizePolicy, QStatusBar, QToolButton, QWidget)
import sys, psutil

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1088, 585)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ONOFF = QPushButton(self.centralwidget)
        self.ONOFF.setObjectName(u"ONOFF")
        self.ONOFF.setGeometry(QRect(80, 370, 171, 91))
        self.ONOFF.setAutoFillBackground(False)
        self.ONOFF.setStyleSheet(u"QPushButton {\n"
                                 "color: #333;\n"
                                 "border: 2px solid #555;\n"
                                 "border-radius: 20px;\n"
                                 "border-style: outset;\n"
                                 "background: qradialgradient(\n"
                                 "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                 "radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                 ");\n"
                                 "padding: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "background: qradialgradient(\n"
                                 "cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                 "radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                 ");\n"
                                 "}")
        icon = QIcon()
        iconThemeName = u"OnOff"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.ONOFF.setIcon(icon)
        self.COMPAS = QLCDNumber(self.centralwidget)
        self.COMPAS.setObjectName(u"COMPAS")
        self.COMPAS.setGeometry(QRect(50, 80, 231, 171))
        self.COMPAS.setSmallDecimalPoint(False)
        self.BATTERIE = QProgressBar(self.centralwidget)
        self.BATTERIE.setObjectName(u"BATTERIE")
        self.BATTERIE.setGeometry(QRect(820, 180, 221, 61))
        self.BATTERIE.setAcceptDrops(True)
        self.BATTERIE.setStyleSheet(u"QProgressBar{\n"
                                    "	background-color:rgba(250, 0, 0, 120);\n"
                                    "}\n"
                                    "QProgressBar:chunk{\n"
                                    "	 background-color:rgba(61, 174, 233, 240);\n"
                                    "}")
        self.BATTERIE.setValue(psutil.sensors_battery().percent)
        self.BATTERIE.setMaximum(100)
        self.BATTERIE.setMinimum(0)
        self.BATTERIE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.BATTERIE.setTextVisible(True)
        self.BATTERIE.setOrientation(Qt.Horizontal)
        self.BATTERIE.setTextDirection(QProgressBar.TopToBottom)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 25, 231, 61))
        font = QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(820, 130, 221, 51))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 0, 221, 51))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(430, 360, 161, 81))
        self.toolButton.setArrowType(Qt.LeftArrow)
        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(600, 440, 161, 81))
        self.toolButton_2.setArrowType(Qt.DownArrow)
        self.toolButton_3 = QToolButton(self.centralwidget)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(770, 360, 161, 81))
        self.toolButton_3.setArrowType(Qt.RightArrow)
        self.toolButton_4 = QToolButton(self.centralwidget)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(QRect(600, 280, 161, 81))
        self.toolButton_4.setArrowType(Qt.UpArrow)
        self.CAMERA = QLabel(self.centralwidget)
        self.CAMERA.setObjectName(u"CAMERA")
        self.CAMERA.setGeometry(QRect(390, 60, 351, 181))
        self.CAMERA.setAutoFillBackground(True)
        self.CAMERA.setFrameShape(QFrame.Panel)
        self.CAMERA.setFrameShadow(QFrame.Raised)
        self.CAMERA.setLineWidth(7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1088, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ONOFF.setText(QCoreApplication.translate("MainWindow", u"On   /   OFF", None))
        self.BATTERIE.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Orientarion(\u00b0)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Etat batterie", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Retour cam\u00e9ra", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.CAMERA.setText("")
    # retranslateUi

