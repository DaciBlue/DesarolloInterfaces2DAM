# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clase2Interfaz.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 586)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblContador = QLabel(self.centralwidget)
        self.lblContador.setObjectName(u"lblContador")
        self.lblContador.setGeometry(QRect(240, 70, 281, 41))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(14)
        font.setBold(True)
        self.lblContador.setFont(font)
        self.lblContador.setTextFormat(Qt.TextFormat.AutoText)
        self.lblContador.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnDecrementa = QPushButton(self.centralwidget)
        self.btnDecrementa.setObjectName(u"btnDecrementa")
        self.btnDecrementa.setGeometry(QRect(330, 160, 111, 51))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.btnDecrementa.setFont(font1)
        self.btnReset = QPushButton(self.centralwidget)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setGeometry(QRect(540, 160, 111, 51))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.btnReset.setFont(font2)
        self.btnIncrementa = QPushButton(self.centralwidget)
        self.btnIncrementa.setObjectName(u"btnIncrementa")
        self.btnIncrementa.setGeometry(QRect(120, 160, 111, 51))
        self.btnIncrementa.setFont(font1)
        self.btnSuma = QPushButton(self.centralwidget)
        self.btnSuma.setObjectName(u"btnSuma")
        self.btnSuma.setGeometry(QRect(210, 310, 141, 51))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.btnSuma.setFont(font3)
        self.btnResta = QPushButton(self.centralwidget)
        self.btnResta.setObjectName(u"btnResta")
        self.btnResta.setGeometry(QRect(420, 310, 141, 51))
        font4 = QFont()
        font4.setFamilies([u"Comic Sans MS"])
        font4.setBold(True)
        self.btnResta.setFont(font4)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 240, 211, 51))
        self.lineEdit.setFont(font2)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pteTitulo = QPlainTextEdit(self.centralwidget)
        self.pteTitulo.setObjectName(u"pteTitulo")
        self.pteTitulo.setGeometry(QRect(300, 460, 351, 51))
        font5 = QFont()
        font5.setFamilies([u"Comic Sans MS"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.pteTitulo.setFont(font5)
        self.pteTitulo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pteTitulo.setFrameShape(QFrame.Shape.WinPanel)
        self.pteTitulo.setFrameShadow(QFrame.Shadow.Sunken)
        self.pteTitulo.setLineWidth(4)
        self.pteTitulo.setReadOnly(False)
        self.btnCambiar = QPushButton(self.centralwidget)
        self.btnCambiar.setObjectName(u"btnCambiar")
        self.btnCambiar.setGeometry(QRect(660, 460, 111, 51))
        self.btnCambiar.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 805, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblContador.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnDecrementa.setText(QCoreApplication.translate("MainWindow", u"Decrementa 1", None))
        self.btnReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btnIncrementa.setText(QCoreApplication.translate("MainWindow", u"Incrementa 1", None))
        self.btnSuma.setText(QCoreApplication.translate("MainWindow", u"Suma N\u00ba Introducido", None))
        self.btnResta.setText(QCoreApplication.translate("MainWindow", u"Resta N\u00ba Introducido", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce numero", None))
        self.pteTitulo.setPlainText("")
        self.pteTitulo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introduce aqui tu titulo y presiona cambiar", None))
        self.btnCambiar.setText(QCoreApplication.translate("MainWindow", u"Cambiar", None))
    # retranslateUi

