'''
Crea una interfaz que cumpla los siguientes requisitos:
• Crear una ventana principal con un botón que muestre un mensaje cuando sea presionado.
• Crear un menú con al menos tres opciones (por ejemplo: "Nuevo", "Abrir" y "Guardar").
• Crear un menú contextual que permita mostrar un mensaje al hacer clic derecho en la
ventana.
• Añadir una barra de herramientas con un ícono para mostrar un mensaje.
• Utilizar cuadros de mensaje (QMessageBox) para mostrar información al usuario.
'''

import sys

from PySide6.QtGui import QAction, QKeySequence, Qt, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QPushButton, QMessageBox, QMenuBar, \
    QMenu, QToolBar
from pyexpat.errors import messages


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio con PySide6")
        self.setGeometry(100, 100, 600, 400)

        ## Crear el Widget/Layout principal
        central_Widget = QWidget()
        self.setCentralWidget(central_Widget)
        layout = QVBoxLayout()
        central_Widget.setLayout(layout)

        ## Boton principal
        self.button = QPushButton("Presioname")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.show_message)

        ## Menu principal
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)

        ## Crear el menu visible
        file_menu = QMenu("Archivo",self)
        menu_bar.addMenu(file_menu)

        ## Crear las opciones del menu y sus atajos
        new_action = QAction("Nuevo", self)
        new_action.setShortcut(QKeySequence("Ctrl+N"))
        open_action = QAction("Abrir", self)
        open_action.setShortcut(QKeySequence("Ctrl+O"))
        save_action = QAction("Guardar", self)
        save_action.setShortcut(QKeySequence("Ctrl+S"))

        new_action.triggered.connect(lambda: self.show_info("Nuevo seleccionado"))
        open_action.triggered.connect(lambda: self.show_info("Abrir seleccionado"))
        save_action.triggered.connect(lambda: self.show_info("Guardar seleccionado"))

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        ## Menu contextual
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        ## Barra de herramientas
        toolbar = QToolBar("Barra de herramientas",self)
        self.addToolBar(toolbar)
        toolbar_action = QAction(QIcon.fromTheme("help-browser"),"Mostrar mensaje",self)
        toolbar_action.setShortcut(QKeySequence("Ctrl+M"))
        toolbar_action.triggered.connect(lambda: self.show_info("Mensaje desde la barra de herramientas"))
        toolbar.addAction(toolbar_action)


    def show_message(self):
        QMessageBox.information(self, "Mensaje", "¡Boton presionado!")

    def show_info(self, messages):
        QMessageBox.information(self,"Mensaje", messages)

    def show_context_menu(self, position):
        context_menu = QMenu()
        context_action = QAction("Accion contextual", self)
        context_action.setShortcut(QKeySequence("Ctrl+X"))
        context_action.triggered.connect(lambda: self.show_info("Accion contextual seleccionada"))
        context_menu.addAction(context_action)
        context_menu.exec(self.mapToGlobal(position))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()