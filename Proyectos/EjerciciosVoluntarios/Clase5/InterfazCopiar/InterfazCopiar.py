'''
Realiza una interfaz que cumpla los siguientes requisitos a partir del Designer de la librería
PySide6:
• Un menú de aplicación en la barra superior con dos menús: Archivo (con opciones para
Abrir y Salir) y Ayuda (con una opción para Acerca de).
• Un menú contextual que se activa con clic derecho sobre un área de texto. Este menú debe
contener las opciones Copiar, Pegar y Limpiar.
• Un área de texto en donde el usuario pueda escribir, y un botón que cuando se presione,
tome el texto del área de texto y lo muestre en un label.
• Al presionar el botón Cambiar texto, debe mostrar un mensaje de confirmación al usuario

• Barra de herramientas con más acciones: Añadir más botones a la barra de herramientas, como
"Limpiar", que borre el texto en el QLineEdit, y "Mostrar mensaje", que muestre un mensaje
emergente con un texto personalizado
• Ventana de diálogo: Crear una ventana de diálogo que se muestre al hacer clic en una opción del
menú "Ayuda". Esta ventana debe contener texto sobre el funcionamiento de la aplicación y debe
tener un botón de "Cerrar".
'''
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QMenu, QMessageBox
from EjerciciosVoluntarios.Clase5.InterfazCopiar.InterfazCopiarUI import Ui_MainWindow
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCambiar.clicked.connect(self.cambiarTexto)

        self.ui.plainTextEdit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.plainTextEdit.customContextMenuRequested.connect(self.menuContextual)

        self.ui.actionLimpiar.triggered.connect(self.limpiar)
        self.ui.actionMostrar_mensaje.triggered.connect(self.mensaje)
        self.ui.actionAcerca_de.triggered.connect(self.info)


    def cambiarTexto(self):
        texto = self.ui.plainTextEdit.toPlainText()
        self.ui.lblTexto.setText(texto)

    def menuContextual(self, pos):
        menu_contextual = QMenu(self)

        copiar_action = menu_contextual.addAction("Copiar")
        pegar_action = menu_contextual.addAction("Pegar")
        limpiar_action = menu_contextual.addAction("Limpiar")

        copiar_action.triggered.connect(self.copiar)
        pegar_action.triggered.connect(self.pegar)
        limpiar_action.triggered.connect(self.limpiar)

        menu_contextual.exec(self.ui.plainTextEdit.mapToGlobal(pos))

    def copiar(self):
        self.ui.plainTextEdit.copy()

    def pegar(self):
        self.ui.plainTextEdit.paste()

    def limpiar(self):
        self.ui.plainTextEdit.clear()

    def mensaje(self):
        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Mensaje")
        self.mensaje.setText("Este es un mensaje de prueba")
        self.mensaje.setStandardButtons(QMessageBox.Ok)
        self.mensaje.exec()

    def info(self):
        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Acerca de")
        self.mensaje.setText("Esta aplicacion es un ejemplo de un menu contextual"+
                             "\nTiene opciones al hacer click derecho como: Copiar, Pegar, Limpiar"+
                             "\nY una barra de herramientas con mas opciones")
        self.mensaje.setStandardButtons(QMessageBox.Close)
        self.mensaje.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())