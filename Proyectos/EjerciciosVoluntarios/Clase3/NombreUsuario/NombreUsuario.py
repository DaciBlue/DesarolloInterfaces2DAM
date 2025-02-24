'''
Crea una ventana que permita al usuario ingresar un nombre de usuario y una contraseña. Muestra
un mensaje en la consola cuando el usuario presione el botón de iniciar sesión.
'''
import sys

from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt, QLine

class NombreUsuario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 400)
        self.show()

        ##Principal
        self.principal = QVBoxLayout()
        self.setLayout(self.principal)

        #Pantalla
        self.nombre = QLineEdit()
        self.nombre.setAlignment(Qt.AlignCenter)
        self.nombre.setStyleSheet(
            "font-size: 18px;")
        self.nombre.setPlaceholderText("Ingresa tu nombre de usuario")
        self.principal.addWidget(self.nombre)
        self.password = QLineEdit()
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setStyleSheet("font-size: 18px;")
        self.password.setPlaceholderText("Contraseña")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.principal.addWidget(self.password)

        ##Boton
        self.boton = QPushButton("Iniciar Sesion")
        self.principal.addWidget(self.boton)
        self.boton.clicked.connect(self.recoge_datos)

    def recoge_datos(self):
        textoN = self.nombre.text()
        textoP = self.password.text()

        print("Bienvenido ", textoN + "\nTu contraseña es: ", textoP)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NombreUsuario()
    window.show()
    app.exec()
