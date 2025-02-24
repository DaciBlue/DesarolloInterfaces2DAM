import sys

from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QGridLayout, QPushButton
from PySide6.QtCore import Qt

class Clase3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 300, 400)

        ##Layout Principal

        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

        ##Pantalla

        self.pantalla = QLineEdit()
        self.pantalla.setReadOnly(True)
        self.pantalla.setStyleSheet("font-size: 24px;")
        ## alinear pantalla a la derecha
        self.pantalla.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layout_principal.addWidget(self.pantalla)

        ##Grid de los Botones

        self.grid_layout = QGridLayout()
        self.layout_principal.addLayout(self.grid_layout)
        self.crear_botones()

    def crear_botones(self):
        botones = {
            '7':(0,0), '8':(0,1), '9':(0,2), '/':(0,3),
            '4':(1,0), '5':(1,1), '6':(1,2), '*':(1,3),
            '1':(2,0), '2':(2,1), '3':(2,2), '-':(2,3),
            '0':(3,0), 'C':(3,1), '=':(3,2), '+':(3,3)
        }
        for texto, posicion in botones.items():
            boton = QPushButton(texto)
            boton.setStyleSheet("font-size: 18px;")
            boton.clicked.connect(self.manejar_click)
            self.grid_layout.addWidget(boton, *posicion)

    def manejar_click(self):
        boton = self.sender()
        texto = boton.text()
        if texto == 'C':
            self.pantalla.clear()
        elif texto == '=':
            try:
                resultado = eval(self.pantalla.text())
                self.pantalla.setText(str(resultado))
            except Exception:
                self.pantalla.setText("Error Matemático")
        else:
            self.pantalla.setText(self.pantalla.text() + texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Clase3()
    window.show()
    app.exec()