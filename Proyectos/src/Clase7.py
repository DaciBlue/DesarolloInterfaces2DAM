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

