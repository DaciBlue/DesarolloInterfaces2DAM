'''
Crea una aplicación que permita agregar tareas a una lista. El usuario puede escribir una tarea en un
cuadro de texto y agregarla a un área de texto más grande que muestra todas las tareas acumuladas
'''
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLineEdit, QTextEdit, QWidget, QPushButton
from PySide6.QtCore import  Qt


class Tareas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tareas")
        self.setGeometry(100, 100, 300, 400)
        self.show()

        ##Principal
        self.principal = QVBoxLayout()
        self.setLayout(self.principal)

        ##Entrada de texto
        self.tarea = QLineEdit()
        self.tarea.setStyleSheet("font-size: 18px")
        self.tarea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tarea.setPlaceholderText("Ingresa tu tarea")
        self.principal.addWidget(self.tarea)

        ##Boton
        self.boton = QPushButton("Agregar")
        self.boton.setStyleSheet("font-size: 14px")
        self.principal.addWidget(self.boton)
        self.boton.clicked.connect(self.agregar_tarea)

        #Acumulacion de tareas
        self.lista = QTextEdit()
        self.lista.setReadOnly(True)
        self.lista.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lista.setPlaceholderText("Aqui estaran sus tareas pendientes")
        self.lista.setStyleSheet("font-size: 18px")
        self.principal.addWidget(self.lista)

        ##Boton reset
        self.reset = QPushButton("Reset")
        self.reset.setStyleSheet("font-size: 14px")
        self.principal.addWidget(self.reset)
        self.reset.clicked.connect(self.reseterar)

        ##Sumatorio
        self.contador = 1

    def agregar_tarea(self):
        texto = self.tarea.text()
        ##Agregar el texto a la lista sumando 1 numero delante
        self.lista.append(f"{self.contador}. {texto}")
        self.contador += 1
        self.tarea.clear()

    def reseterar(self):
        self.lista.clear()
        self.contador = 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tareas()
    window.show()
    app.exec()