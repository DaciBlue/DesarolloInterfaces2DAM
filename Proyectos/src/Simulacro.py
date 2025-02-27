'''
PARTE PRÁCTICA
1) Crea una aplicación en PySide6 que tenga una ventana con los siguientes componentes:
• Un QLineEdit para que el usuario ingrese su nombre.
• Un botón para mostrar un mensaje que salude al usuario con su nombre.
• El mensaje debe aparecer en un QLabel debajo del botón, donde se debe actualizar cada vez
que el usuario presione el botón.
2) Crea una ventana en PySide6 con un QComboBox que permita al usuario elegir un color. Según
el color elegido, cambia el color de fondo de la ventana a ese color y crea un ejecutable de la misma
aplicación.
3) Crea un archivo README.md para una aplicación que permita a los usuarios seleccionar y
eliminar archivos de un directorio. El archivo debe incluir:
• Un título con el nombre de la aplicación.
• Una sección de Descripción que explique cómo funciona la aplicación.
• Una sección de Instalación que explique cómo instalar las dependencias necesarias y
ejecutar la aplicación.
4) Escribe pruebas unitarias utilizando pytest para una clase Coche que tiene los siguientes
métodos:
class Coche:
def arrancar(self):
self.en_marcha = True
def detener(self):
self.en_marcha = False
def estado(self):
return 'En marcha' if self.en_marcha else 'Detenido'
Asegúrate de probar los métodos arrancar(), detener(), y estado() para garantizar su correcto
funcionamiento.
5) Crea un archivo CSV con los siguientes datos de ventas y genera un informe con los siguientes
gráficos: A) Un gráfico de barras que muestre las ventas de cada producto. B) Un gráfico de líneas
que muestre la evolución de las ventas por mes para cada producto. C) Un título que describa el
informe.
ARCHIVO CSV:
Producto,Mes,Unidades Vendidas,Precio Unitario (€)
Producto A,Enero,100,25
Producto B,Enero,50,150
Producto C,Febrero,75,30
Producto D,Febrero,30,200
Producto E,Marzo,200,20
Producto F,Marzo,120,15
'''
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QComboBox


class primero(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Saludo")
        self.setFixedSize(400, 400)

        widget_base = QWidget()
        self.setCentralWidget(widget_base)
        layout = QVBoxLayout()
        widget_base.setLayout(layout)

        self.linea_nombre = QLineEdit()
        self.linea_nombre.setPlaceholderText("Nombre")
        layout.addWidget(self.linea_nombre)

        self.btnSaludar = QPushButton("Saludar")
        layout.addWidget(self.btnSaludar)

        self.lbl_mensaje = QLabel("Mensaje")
        self.lbl_mensaje.setAlignment(Qt.AlignCenter)
        self.lbl_mensaje.setStyleSheet("font-size: 22px; bold: true;")
        layout.addWidget(self.lbl_mensaje)

        self.btnSaludar.clicked.connect(self.saludar)


    def saludar(self):
        texto = self.linea_nombre.text()
        self.lbl_mensaje.setText(f"Saludos {texto}!!")

class cambio_color(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Colores")
        self.setFixedSize(400, 400)

        widget_base = QWidget()
        self.setCentralWidget(widget_base)

        self.layout = QVBoxLayout()
        widget_base.setLayout(self.layout)

        self.combo_color = QComboBox()
        self.combo_color.addItems(["Rojo", "Verde", "Azul"])
        self.combo_color.setStyleSheet("font-size: 22px; font-weight: bold; border-radius: 5px; border-color: black; border-size: 5px; color: black;")
        self.layout.addWidget(self.combo_color)
        self.combo_color.currentIndexChanged.connect(self.ventana_color)

        ##para crear el exe
        ##pyinstaller --onefile --windowed Simulacro.py

    def ventana_color(self):
        texto = self.combo_color.currentText()
        ## cambia la ventana de la aplicacion segun el color
        if texto == "Rojo":
            self.setStyleSheet("QWidget { background-color: rgb(255, 0, 0); }")
        elif texto == "Verde":
            self.setStyleSheet("QWidget { background-color: rgb(0, 255, 0); }")
        elif texto == "Azul":
            self.setStyleSheet("QWidget { background-color: rgb(0, 0, 255); }")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = cambio_color()
    window.show()
    sys.exit(app.exec())