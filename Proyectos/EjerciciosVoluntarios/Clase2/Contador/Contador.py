import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from EjerciciosVoluntarios.Clase2.Contador import ContadorInterfaz


class Contador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ContadorInterfaz.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnClick.clicked.connect(self.contarclicks)

    def contarclicks(self):
        contarTexto = self.ui.lblContador.text()
        contar = int(contarTexto) if contarTexto else 0
        self.ui.lblContador.setText(str(contar + 1))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Contador()
    window.show()
    sys.exit(app.exec())