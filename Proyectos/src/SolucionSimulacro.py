from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QApplication, QComboBox


class Ejercicio1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Saludo")
        self.layout = QVBoxLayout()

        self.name_imput = QLineEdit()
        self.name_imput.setPlaceholderText("Ingresa tu nombre")
        self.layout.addWidget(self.name_imput)

        self.button = QPushButton("Saludar")
        self.button.clicked.connect(self.change_label)
        self.layout.addWidget(self.button)

        self.label = QLabel("")
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    def change_label(self):
        name = self.name_imput.text()
        self.label.setText(f"Hola, {name}")

class Ejercicio2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selector de color")
        self.layout = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItems(["Rojo", "Verde", "Azul"])
        self.combo.currentTextChanged.connect(self.change_color)
        self.layout.addWidget(self.combo)
        self.setLayout(self.layout)

    def change_color(self, color):
        colors = {"Rojo" : "red", "Verde": "green", "Azul" : "blue"}
        self.setStyleSheet(f"background-color: {colors.get(color, 'white')};")



if __name__ == "__main__":
    app = QApplication([])
    ventana = Ejercicio2()
    ventana.show()
    app.exec()


#--------------------------------------------------------------------------------------------

class Coche:
    def __init__(self):
        self.en_marcha = False
    def arrancar(self):
        self.en_marcha = True

    def detener(self):
        self.en_marcha = False

    def estado(self):
        return 'En marcha' if self.en_marcha else 'Detenido'

def test_coche():
    coche = Coche()
    assert coche.estado() == "Detenido"
    coche.arrancar()
    assert coche.estado() == "En marcha"
    coche.detener()
    assert coche.estado() == "Detenido"


#--------------------------------------------------------------------------------------------
import pandas as pd
import altair as alt
import datapane as dp

if __name__ == "__main__":
    fichero_csv = "prueba.csv"
    ventas = pd.read_csv(fichero_csv)

    bar_chat = alt.Chart(ventas).mark_bar().encode(
        x="Producto:N",
        y="Unidades:Q"
    ).properties(
        title="Ventas por producto"
    )

    line_chart = alt.Chart(ventas).mark_line().encode(
        x="Mes:N",
        y="Unidades:Q"
    ).properties(
        title="Ventas por Mes"
    )

    report = dp.Report(
        bar_chat,
        line_chart
    )

    report.save("informe_ejercicio6.html")