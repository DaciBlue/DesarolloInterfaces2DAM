import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication
from EjerciciosVoluntarios.Clase2.CalculaDescuento import CalculaDescuentoInterfaz

class CalculaDescuento(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = CalculaDescuentoInterfaz.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pbCalcular.clicked.connect(self.calcular)


    def calcular(self):
        precio = self.ui.tePrecio.toPlainText()
        descuento = self.ui.teDescuento.toPlainText()

        if not precio or not descuento:
            print("No se ha introducido valores en todos los campos")
            self.ui.tePrecio.clear()
            self.ui.teDescuento.clear()
            return

        precioInt = int(precio)
        descuentoInt = int(descuento)

        if precioInt <= 0 | descuentoInt < 0:
            print("El precio o descuento introducido no valido")
            self.ui.tePrecio.clear()
            self.ui.teDescuento.clear()
            return
        else:
            total = precioInt - (precioInt * descuentoInt / 100)
            self.ui.lblFinal.setText(str(total))
            self.ui.lblFinal.setStyleSheet("text-color: white; background-color: green;")
            self.ui.lblFinal.setAlignment(Qt.AlignCenter)
            self.ui.tePrecio.clear()
            self.ui.teDescuento.clear()


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = CalculaDescuento()
    window.show()
    sys.exit(app.exec())