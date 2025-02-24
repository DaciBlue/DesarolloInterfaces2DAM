# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalculaDescuentoInterfaz.ui'
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
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(423, 438)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tePrecio = QTextEdit(self.centralwidget)
        self.tePrecio.setObjectName(u"tePrecio")
        self.tePrecio.setGeometry(QRect(240, 70, 104, 41))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.tePrecio.setFont(font)
        self.tePrecio.setStyleSheet(u"background-color: rgb(115, 132, 118);")
        self.tePrecio.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhNoTextHandles)
        self.tePrecio.setMidLineWidth(0)
        self.lblTxtPrecio = QLabel(self.centralwidget)
        self.lblTxtPrecio.setObjectName(u"lblTxtPrecio")
        self.lblTxtPrecio.setGeometry(QRect(40, 70, 131, 31))
        self.lblTxtPrecio.setFont(font)
        self.lblTxtDescuento = QLabel(self.centralwidget)
        self.lblTxtDescuento.setObjectName(u"lblTxtDescuento")
        self.lblTxtDescuento.setGeometry(QRect(30, 120, 161, 41))
        self.lblTxtDescuento.setFont(font)
        self.teDescuento = QTextEdit(self.centralwidget)
        self.teDescuento.setObjectName(u"teDescuento")
        self.teDescuento.setGeometry(QRect(240, 120, 104, 41))
        self.teDescuento.setFont(font)
        self.teDescuento.setStyleSheet(u"background-color: rgb(115, 132, 118);")
        self.teDescuento.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhNoTextHandles)
        self.teDescuento.setMidLineWidth(0)
        self.pbCalcular = QPushButton(self.centralwidget)
        self.pbCalcular.setObjectName(u"pbCalcular")
        self.pbCalcular.setGeometry(QRect(130, 200, 131, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pbCalcular.setFont(font1)
        self.pbCalcular.setStyleSheet(u"background-color: rgb(83, 88, 107);")
        self.lblTxtFinal = QLabel(self.centralwidget)
        self.lblTxtFinal.setObjectName(u"lblTxtFinal")
        self.lblTxtFinal.setGeometry(QRect(40, 290, 161, 41))
        self.lblTxtFinal.setFont(font)
        self.lblFinal = QLabel(self.centralwidget)
        self.lblFinal.setObjectName(u"lblFinal")
        self.lblFinal.setGeometry(QRect(230, 290, 141, 41))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.lblFinal.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 423, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CalculaDescuento", None))
        self.tePrecio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"precio", None))
        self.lblTxtPrecio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ff5500;\">Introduzca precio</span></p></body></html>", None))
        self.lblTxtDescuento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ff5500;\">Introduzca descuento</span></p></body></html>", None))
        self.teDescuento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descuento %", None))
        self.pbCalcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.lblTxtFinal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ff5500;\">Precio con descuento</span></p></body></html>", None))
        self.lblFinal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#00aa00;\"><br/></span></p></body></html>", None))
    # retranslateUi

