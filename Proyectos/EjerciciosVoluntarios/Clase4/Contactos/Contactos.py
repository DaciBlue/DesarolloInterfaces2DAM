'''
Crea una aplicación que permita gestionar contactos. Debe incluir:
• Un botón que, al presionarse, agregue un contacto ficticio a una lista y muestre un mensaje
confirmando la acción.
• Un menú con las opciones "Añadir contacto", "Ver contactos" y "Eliminar contacto", cada
una mostrando un mensaje informativo.
'''

import sys

from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Contactos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contactos")
        self.setGeometry(100, 100, 400, 600)

        ## Crear la base
        base_Widget = QWidget()
        self.setCentralWidget(base_Widget)
        layout = QVBoxLayout()
        base_Widget.setLayout(layout)

        ## QLine para nombre del contacto
        self.qlineNombre = QLineEdit()
        self.qlineNombre.setPlaceholderText("Introduzca nombre del contacto")
        layout.addWidget(self.qlineNombre)

        ## Boton Ficticio
        self.btn = QPushButton("Añadir contacto")
        layout.addWidget(self.btn)
        self.btn.clicked.connect(lambda: self.agregar_contacto())

        ## Una lista para los contactos
        self.lista_contactos = QListWidget()
        layout.addWidget(self.lista_contactos)
        self.lista_contactos.setStyleSheet(
            "font-size: 18px; bold: True;")
        self.lista_contactos.hide()

        ## La base del menu
        menu = QMenuBar()
        self.setMenuBar(menu)

        ## Hacer el menu visible
        pestania = QMenu("Opciones")
        menu.addMenu(pestania)

        ## Añadir cosas a la pestaña Opciones
        # Dar nombres
        action_agregar = QAction("Añadir contacto", self)
        action_ver = QAction("Ver contactos", self)
        action_eliminar = QAction("Eliminar contacto", self)

        # Agregarlas a la pestaña
        pestania.addAction(action_agregar)
        pestania.addAction(action_ver)
        pestania.addAction(action_eliminar)

        # Mensajes al pulsar las opciones
        action_agregar.triggered.connect(lambda: self.agregar_contacto())
        action_ver.triggered.connect(lambda: self.ver_lista())
        action_eliminar.triggered.connect(lambda: self.eliminar_contacto())



    def agregar_contacto_ficticio(self):
        QMessageBox.information(self,"Mensaje","Usuario ficticio agregado")

    def agregar_contacto(self):
        contacto = self.qlineNombre.text()
        self.lista_contactos.addItem(contacto)
        QMessageBox.information(self,"Mensaje",f"Usuario '{contacto}' agregado")
        self.qlineNombre.clear()

    def eliminar_contacto(self):
        QMessageBox.information(self,"Mensaje","Contacto eliminado")

    def ver_lista(self):
        self.lista_contactos.show()
        QMessageBox.information(self,"Mensaje","Lista de contactos")


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Contactos()
    window.show()
    app.exec()