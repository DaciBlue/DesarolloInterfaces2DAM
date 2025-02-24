import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from src import Clase2InterfazGrupo1

class Clase2_Grupo1(QMainWindow):
    """
    Constructor de la clase Clase2_Grupo1
    self > instancia propia de la clase
    super().__init__() > llama al constructor de la clase padre
    """
    def __init__(self):
        super().__init__()
        self.ui = Clase2InterfazGrupo1.Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.btnIncrementar.clicked.connect(lambda : self.sumar_restar(1))
        self.ui.btnDecrementar.clicked.connect(lambda : self.sumar_restar(-1))
        self.ui.btnResetear.clicked.connect(lambda: self.ui.lblContador.clear())

    def sumar_restar(self, numero):
        try:
            contador = int(self.ui.lblContador.text())
            resultado = contador + numero
            self.ui.lblContador.setText(str(resultado))
            if resultado > 0:
                self.ui.lblContador.setStyleSheet("background-color: green")
            elif resultado == 0:
                self.ui.lblContador.setStyleSheet("background-color: purple")
            else:
                self.ui.lblContador.setStyleSheet("background-color: red")
        except ValueError:
            print("Numero invalido")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Clase2_Grupo1()
    window.show()
    sys.exit(app.exec())