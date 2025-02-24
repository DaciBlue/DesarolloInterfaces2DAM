# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SemaforoInterfaz.ui'
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
        MainWindow.resize(334, 473)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblRojo = QLabel(self.centralwidget)
        self.lblRojo.setObjectName(u"lblRojo")
        self.lblRojo.setGeometry(QRect(120, 50, 81, 51))
        self.lblRojo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblAmarillo = QLabel(self.centralwidget)
        self.lblAmarillo.setObjectName(u"lblAmarillo")
        self.lblAmarillo.setGeometry(QRect(120, 130, 81, 51))
        self.lblAmarillo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblVerde = QLabel(self.centralwidget)
        self.lblVerde.setObjectName(u"lblVerde")
        self.lblVerde.setGeometry(QRect(120, 210, 81, 51))
        self.lblVerde.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnCambiar = QPushButton(self.centralwidget)
        self.btnCambiar.setObjectName(u"btnCambiar")
        self.btnCambiar.setGeometry(QRect(120, 320, 91, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 334, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Semaforo", None))
        self.btnCambiar.setText(QCoreApplication.translate("MainWindow", u"Cambiar", None))
    # retranslateUi

