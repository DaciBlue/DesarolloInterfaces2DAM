'''
Cargar datos desde un archivo CSV: El archivo CSV (prueba.csv) contiene los siguientes
campos:
• Mes: El mes de la venta.
• Nombre: Nombre del vendedor.
• Importe (€): Importe de la venta.
• Unidades: Número de unidades vendidas.
Generación de gráficos:
• Gráfico de barras que muestre las ventas por vendedor (importe en euros).
• Gráfico de sectores (pie chart) que muestre la distribución de las unidades vendidas por
vendedor.
Informe:
• Crear un informe en formato HTML que contenga:
• Un título con el nombre del mes.
• El total de unidades vendidas en ese mes.
• Una tabla con los detalles de las ventas.
• Los dos gráficos generados (gráfico de barras y gráfico de sectores).
Interfaz gráfica:
• Una ventana que permita seleccionar el mes de interés mediante un combo box
(desplegable).
• Un botón que permita regenerar el informe.
• Un componente de vista web (QWebEngineView) que muestre el informe generado.
Generación asíncrona del informe:
• Cuando se seleccione un mes, la aplicación debe generar el informe y mostrarlo en la vista
web sin bloquear la interfaz de usuario.
Guardar y cargar el informe:
• El informe debe guardarse en un archivo HTML en una ruta absoluta.
• El archivo debe cargarse en la vista web una vez generado.
'''

import pandas as pd
import altair as alt
import datapane as dp
import os

from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QComboBox, QApplication, QVBoxLayout, QWidget

fichero_csv = "prueba.csv"
try:
    df = pd.read_csv(fichero_csv)
except FileNotFoundError:
    raise SystemExit(f"Error: El archivo '{fichero_csv}' no se encuentra.")
except pd.errors.EmptyDataError:
    raise SystemExit(f"Error: El archivo '{fichero_csv}' está vacío.")
except Exception as e:
    raise SystemExit(f"Error al leer el archivo CSV: {e}")


def generar_informe(mes):
    datos_mes = df[df['Mes'] == mes]

    ## Grafico barras
    grafico_barras = alt.Chart(datos_mes).mark_bar().encode(
        x='Nombre:N', y='Importe:Q', color='Nombre:N'
    ).properties(title = f"Ventas por Vendedor en {mes}")

    ## Grafico de sectores
    datos_agg = datos_mes.groupby("Nombre")["Unidades"].sum().reset_index()
    grafico_sectores = alt.Chart(datos_agg).mark_arc().encode(
        theta= 'Unidades:Q',  color = 'Nombre:N'
    ).properties(title = f"Distribucion de unidades vendidas en {mes}")

    titulo = dp.HTML('<h1>Informe</h1>')

    reporte = dp.Report(
        titulo,
        dp.Plot(grafico_barras),
        dp.Plot(grafico_sectores)
    )

    ruta_reporte = os.path.abspath("informe_ventas2.html")
    reporte.save(ruta_reporte)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Informe de ventas")

        self.selector_mes = QComboBox()
        self.selector_mes.addItems(df['Mes'].unique())
        self.selector_mes.currentTextChanged.connect(self.actualizar_reporte)

        self.vista_web = QWebEngineView()

        layout = QVBoxLayout()
        layout.addWidget(self.selector_mes)
        layout.addWidget(self.vista_web)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)



    def actualizar_reporte(self):
        mes_seleccionado = self.selector_mes.currentText()
        generar_informe(mes_seleccionado)
        ruta_reporte = os.path.abspath("informe_ventas2.html")
        if os.path.exists(ruta_reporte):
            with open(ruta_reporte, 'r', encoding='utf-8') as file:
                html_content = file.read()
                self.vista_web.setHtml(html_content)

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()