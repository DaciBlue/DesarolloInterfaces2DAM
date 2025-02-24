import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from src.Clase2Interfaz import Ui_MainWindow

class Clase2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnIncrementa.clicked.connect(lambda : self.increm_decrem(1))
        self.ui.btnDecrementa.clicked.connect(lambda : self.increm_decrem(-1))
        self.ui.btnReset.clicked.connect(lambda: self.reset())
        self.ui.btnSuma.clicked.connect(lambda: self.sumar())
        self.ui.btnResta.clicked.connect(lambda: self.restar())
        self.ui.btnCambiar.clicked.connect(lambda: self.cambiarTitulo())

    def increm_decrem(self, numero):
        try:
            #Se crea un contador que recoge lo que hay en el numero mostrado arriba
            contador = int(self.ui.lblContador.text())

            #Le decimos que se actualize la interfaz del lbl contador
            self.ui.lblContador.setText(str(contador + numero))

            #Añadimos color .setStyleSheet
            if contador + numero > 0:
                self.ui.lblContador.setStyleSheet("background-color: green")
            elif contador + numero == 0:
                self.ui.lblContador.setStyleSheet("background-color: purple")
            else:
                self.ui.lblContador.setStyleSheet("background-color: red")

        except ValueError:
            print("Numero invalido")

    def sumar(self):
        try:

            #Guardo las cosas en variables nuevas para cambiar un poco
            numero = int(self.ui.lineEdit.text())
            contador2 = int(self.ui.lblContador.text())

            resultado = contador2 + numero

            self.ui.lblContador.setText(str(resultado))

            if resultado > 0:
                self.ui.lblContador.setStyleSheet("background-color: green")
            elif resultado == 0:
                self.ui.lblContador.setStyleSheet("background-color: purple")
            else:
                self.ui.lblContador.setStyleSheet("background-color: red")

        except ValueError:
            print("Numero introducido en la casilla no es valido, usa numeros")

    def restar(self):
        try:
            numero = int(self.ui.lineEdit.text())
            contador2 = int(self.ui.lblContador.text())

            resultado = contador2 - numero

            self.ui.lblContador.setText(str(resultado))

            if resultado > 0:
                self.ui.lblContador.setStyleSheet("background-color: green")
            elif resultado == 0:
                self.ui.lblContador.setStyleSheet("background-color: purple")
            else:
                self.ui.lblContador.setStyleSheet("background-color: red")

        except ValueError:
            print("Numero introducido en la casilla no es valido, usa numeros")

    def reset(self):
        '''Esta funcion la creo para que directamente al darle al boton del reset
          haga ambas cosas a la vez: poner un 0 y el color de fondo morado'''
        try:
            self.ui.lblContador.setText("0")
            self.ui.lblContador.setStyleSheet("background-color: purple")
        except ValueError:
            print("Numero invalido")


    def cambiarTitulo(self):
        titulo = self.ui.pteTitulo.toPlainText()
        self.setWindowTitle(titulo)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Clase2()
    window.show()
    sys.exit(app.exec())