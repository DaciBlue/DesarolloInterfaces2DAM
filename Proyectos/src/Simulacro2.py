'''
1.-
Crea una aplicación en PySide6 que permita al usuario ingresar su edad en un QLineEdit, presionar
un botón y mostrar un mensaje en un QLabel indicando si es mayor o menor de edad.
2.-
Crea una aplicación en PySide6 con un QComboBox que permita al usuario seleccionar un tamaño
de fuente (Pequeño, Mediano, Grande) y cambia el tamaño del texto de un QLabel según la
selección.
3.-
Realiza las pruebas unitarias de los métodos que componen las dos aplicaciones anteriores.
4.-
Crea un ejecutable para cada una de las aplicaciones.
5.-
Crea un archivo CSV con datos de temperaturas medias por ciudad en diferentes meses. Luego,
genera:
- Un gráfico de barras con la temperatura media por ciudad.
- Un gráfico de líneas mostrando la variación de temperatura por mes para cada ciudad.
- Un informe con datapane que incluya los gráficos y la tabla de datos
'''
import sys

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QApplication, QComboBox
from PySide6.QtTest import QTest

class Ejercicio1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejercicio 1')
        self.setGeometry(300, 300, 250, 150)

        self.layout = QVBoxLayout()
        self.su_edad = QLineEdit()
        self.layout.addWidget(self.su_edad)

        self.btnEdad = QPushButton('Edad')
        self.btnEdad.clicked.connect(self.calcula_edad)
        self.layout.addWidget(self.btnEdad)

        self.label = QLabel("")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def calcula_edad(self):
        edad = int(self.su_edad.text())
        if edad >= 18:
            self.label.setText("Es mayor de edad")
        else:
            self.label.setText("Es menor de edad")

class Ejercicio2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejercicio 2')
        self.setGeometry(300, 300, 250, 150)

        self.layout = QVBoxLayout()

        self.comboBox = QComboBox()
        self.comboBox.addItems(["Pequeño", "Mediano", "GRANDE"])
        self.comboBox.currentTextChanged.connect(self.cambia_tamano)
        self.layout.addWidget(self.comboBox)

        self.label = QLabel("Texto cambiante")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def cambia_tamano(self, texto):
        texto = self.comboBox.currentText()
        if texto == "Pequeño":
            self.label.setStyleSheet("font-size: 6pt;")
        elif texto == "Mediano":
            self.label.setStyleSheet("font-size: 12pt;")
        else:
            self.label.setStyleSheet("font-size: 22pt;")

import unittest

class TestEjercicio1(unittest.TestCase):
    def setUp(self):
        """ Configura la aplicación y la ventana antes de cada test """
        self.app = QApplication(sys.argv)
        self.ventana = Ejercicio1()

    def test_ejercicio1(self):
        """ Prueba la funcionalidad de calcula_edad """
        self.ventana.su_edad.setText("18")
        self.ventana.calcula_edad()
        self.assertEqual(self.ventana.label.text(), "Es mayor de edad")

        self.ventana.su_edad.setText("0")
        self.ventana.calcula_edad()
        self.assertEqual(self.ventana.label.text(), "Es menor de edad")

class TestEjercicio2(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.ventana = Ejercicio2()

    def test_ejercicio2(self):
        self.ventana.comboBox.setCurrentText("Pequeño")
        self.ventana.cambia_tamano("Pequeño")
        self.assertEqual(self.ventana.label.styleSheet(), "font-size: 6pt;")

        self.ventana.comboBox.setCurrentText("Mediano")
        self.ventana.cambia_tamano("Mediano")
        self.assertEqual(self.ventana.label.styleSheet(), "font-size: 12pt;")

        self.ventana.comboBox.setCurrentText("GRANDE")
        self.ventana.cambia_tamano("GRANDE")
        self.assertEqual(self.ventana.label.styleSheet(), "font-size: 22pt;")

if __name__ == '__main__':
    unittest.main()

import pandas as pd
import altair as alt
import datapane as dp

if __name__ == '__main__':
    # Leer el archivo CSV
    data = pd.read_csv('simulacro2.csv')
    # Gráfico de barras: temperatura media por ciudad
    bar_chart = alt.Chart(data).mark_bar().encode(
        x='Ciudad',
        y='mean(Enero)',
        color='Ciudad'
    ).properties(title='Temperatura Media por Ciudad en Enero')
    # Gráfico de líneas: variación de temperatura por mes para cada ciudad
    line_chart = alt.Chart(data).transform_fold(
        ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        as_=['Mes', 'MediaTemperatura']
    ).mark_line().encode(
        x='Mes',
        y='MediaTemperatura',
        color='Ciudad'
    ).properties(title='Variación de Temperatura por Mes para Cada Ciudad')
    # Crear el informe en Datapane
    report = dp.Report(
        bar_chart,
        line_chart
    )
    # Publicar el informe
    report.save("Informe de Temperaturas")


if __name__ == "__main__":
    app = QApplication([])
    ventana = Ejercicio1()
    ventana.show()
    app.exec()