'''
El archivo CSV (inventario.csv) contiene la información
1. Carga de Datos:
• La aplicación debe cargar los datos desde el archivo inventario.csv utilizando la
librería pandas.
• Cada producto tiene una categoría, cantidad disponible, precio unitario y fecha de
entrada al inventario.
2. Generación de Gráficos:
• Gráfico de barras: Muestra el total de unidades disponibles por categoría (por
ejemplo, cuántas unidades de "Electrónica", "Muebles" y "Ropa" hay en inventario).
• Gráfico de líneas: Muestra la evolución de unidades disponibles a lo largo del tiempo
para cada categoría (basado en la fecha de entrada de los productos).
3. Informe HTML Interactivo: La aplicación debe generar un informe HTML que contenga:
• Un título que indique la categoría seleccionada por el usuario.
• Un gráfico de barras con el total de unidades disponibles por categoría.
• Un gráfico de líneas mostrando la evolución del inventario por categoría.
• Una tabla con los productos de la categoría seleccionada, mostrando la cantidad
disponible, el precio unitario y la fecha de entrada.
4. Interfaz Gráfica:
• Selector de Categoría: Un combo box que permita seleccionar la categoría de
productos para analizar (por ejemplo, "Electrónica", "Muebles" o "Ropa").
• Botón de Generación de Informe: Un botón que actualice el informe HTML con los
gráficos y datos de la categoría seleccionada.
• Vista Web: Mostrar el informe generado dentro de la misma aplicación, utilizando un
componente de vista web que cargue el archivo HTML generado.
5. Generación Asíncrona:
• La generación del informe debe ser asíncrona para que la interfaz no se congele
mientras se procesan los datos y se generan los gráficos.
6. Guardar y Cargar el Informe:
• El informe debe guardarse como un archivo HTML en una ruta accesible.
• El archivo debe cargarse en la vista web sin que el usuario tenga que abrir el archivo
manualmente.
'''
import sys
import pandas as pd
import altair as alt
import datapane as dp
import os

from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QComboBox, QApplication, QVBoxLayout, QWidget

fichero_csv = "inventario.csv"
df = pd.read_csv(fichero_csv)

def generar_informe(categoria):
    datos_categoria = df[df['Categoria'] == categoria]

    grafico_barras = alt.Chart(datos_categoria).mark_bar().encode(
        x='Categoria:N', y='Unidades Disponibles:Q', color='Categoria:N'
    ).properties(title = f"Total de unidades disponibles por categoria en {categoria}")

    grafico_lineas = alt.Chart(datos_categoria).mark_line().encode(
        x='Fecha de Entrada:T', y='Unidades Disponibles:Q', color='Categoria:N'
    ).properties(title = f"Evolucion de unidades disponibles en {categoria}")

    titulo = dp.HTML('<h1>Informe</h1>')
    reporte = dp.Report(
        titulo,
        dp.Plot(grafico_barras),
        dp.Plot(grafico_lineas)
    )
    ruta_reporte = os.path.abspath("informe_inventario.html")
    reporte.save(ruta_reporte)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Informe de inventario")

        self.selector_categoria = QComboBox()
        self.selector_categoria.addItems(df['Categoria'].unique())
        self.selector_categoria.currentTextChanged.connect(self.actualizar_reporte)

        self.vista_web = QWebEngineView()

        layout = QVBoxLayout()
        layout.addWidget(self.selector_categoria)
        layout.addWidget(self.vista_web)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def actualizar_reporte(self):
        categoria_seleccionada = self.selector_categoria.currentText()
        generar_informe(categoria_seleccionada)
        ruta_reporte = "informe_inventario.html"
        if os.path.exists(ruta_reporte):
            with open(ruta_reporte,'r', encoding='utf-8') as file:
                html_leer = file.read()
                self.vista_web.setHtml(html_leer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())