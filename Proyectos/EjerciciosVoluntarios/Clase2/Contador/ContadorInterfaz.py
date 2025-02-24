# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ContadorInterfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(463, 420)
        MainWindow.setStyleSheet(u"background-color: rgb(65, 79, 74);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnClick = QPushButton(self.centralwidget)
        self.btnClick.setObjectName(u"btnClick")
        self.btnClick.setGeometry(QRect(140, 210, 161, 81))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.btnClick.setFont(font)
        self.btnClick.setStyleSheet(u"background-color: rgb(85, 0, 0);")
        self.lblContador = QLabel(self.centralwidget)
        self.lblContador.setObjectName(u"lblContador")
        self.lblContador.setGeometry(QRect(160, 110, 131, 71))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lblContador.setFont(font1)
        self.lblContador.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.lblContador.setTextFormat(Qt.TextFormat.RichText)
        self.lblContador.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblTotal = QLabel(self.centralwidget)
        self.lblTotal.setObjectName(u"lblTotal")
        self.lblTotal.setGeometry(QRect(120, 30, 201, 51))
        self.lblTotal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 463, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Contador", None))
        self.btnClick.setText(QCoreApplication.translate("MainWindow", u"Clickeame", None))
        self.lblContador.setText("")
        self.lblTotal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ff5500;\">Total de clicks</span></p></body></html>", None))
    # retranslateUi

