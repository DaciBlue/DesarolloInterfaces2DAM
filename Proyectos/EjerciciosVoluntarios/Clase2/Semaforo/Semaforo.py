import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from EjerciciosVoluntarios.Clase2.Semaforo import SemaforoInterfaz


class Semaforo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = SemaforoInterfaz.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lblRojo.setStyleSheet("background-color: red")
        self.ui.btnCambiar.clicked.connect(self.cambiar)

    def cambiar(self):
        try:
            # Ciclo de colores del semáforo
            if self.ui.lblRojo.styleSheet() == "background-color: red":
                self.ui.lblRojo.setStyleSheet("")
                self.ui.lblAmarillo.setStyleSheet("background-color: yellow")
            elif self.ui.lblAmarillo.styleSheet() == "background-color: yellow":
                self.ui.lblAmarillo.setStyleSheet("")
                self.ui.lblVerde.setStyleSheet("background-color: green")
            elif self.ui.lblVerde.styleSheet() == "background-color: green":
                self.ui.lblVerde.setStyleSheet("")
                self.ui.lblRojo.setStyleSheet("background-color: red")
        except ValueError:
            print("Error al cambiar el color del semáforo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Semaforo()
    window.show()
    sys.exit(app.exec())
