'''
Tu desafío es crear un componente personalizado en Qt que represente un indicador de
progreso circular. Este indicador debe ser visualmente atractivo y mostrar el progreso en
porcentaje. Deberás implementar tanto la creación del componente visual como la lógica
detrás del progreso. ¡Demuestra tus habilidades en la creación de nuevos componentes!
Pautas de solución
>> Utiliza una clase heredada de `QWidget` para crear el componente.
>> Diseña la interfaz visual que representará el indicador circular.
>> Implementa la lógica para actualizar el progreso en porcentaje.
>> Utiliza señales y ranuras para gestionar la comunicación entre la interfaz y la lógica.
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, pyqtSignal

class BarraProgresoCircular(QWidget):
    progresoCambiado = pyqtSignal(int)  # Señal que emite el nuevo valor del progreso

    def __init__(self, padre=None, color_base=QColor(220, 220, 220),
                 color_progreso=QColor(0, 150, 255), color_texto=Qt.black, grosor=10):
        super().__init__(padre)
        self.progreso = 0  # Inicializa el progreso en 0
        self.color_base = color_base
        self.color_progreso = color_progreso
        self.color_texto = color_texto
        self.grosor = grosor
        self.setMinimumSize(100, 100)

    def establecerProgreso(self, valor):
        """
        Establece el progreso asegurándose de que esté en el rango de 0 a 100
        Luego actualiza la interfaz y emite la señal con el nuevo valor
        """
        self.progreso = max(0, min(valor, 100))
        self.update()  # Llama a paintEvent para redibujar el widgett
        self.progresoCambiado.emit(self.progreso)  # emite la señal con el nuevo valor

    def paintEvent(self, evento):
        """
        Evento de dibujo que renderiza el indicador de progreso circular.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # los bordes de los graaficos

        ancho, alto = self.width(), self.height()
        tamano = min(ancho, alto) - self.grosor
        rectangulo = int(self.grosor / 2), int(self.grosor / 2), int(tamano), int(tamano)  # Define el aarea de dibujo

        # Cambiar el color del progreso a verde si es 100%
        if self.progreso == 100:
            self.color_progreso = QColor(0, 255, 0)  # Verde
        else:
            self.color_progreso = QColor(0, 0, 255)  # azull

        # Dibuja el circul de fondo
        pen = QPen(self.color_base, self.grosor)  # Define el color y grosor de la lnea
        painter.setPen(pen)  # Aplica la pluma al QPainte
        painter.drawEllipse(*rectangulo)  # Dibuja un ciirculo de fondo

        # dibuja el arco de progreso
        pen.setColor(self.color_progreso)  # Cambia el color del arco
        painter.setPen(pen)
        angulo_barra = int(360 * self.progreso / 100 * 16)  # Convierte el progreso en grados para PyQt
        painter.drawArc(*rectangulo, -90 * 16, -angulo_barra)  # Dibuja el arco representando el progreso

        # dbuja el texto del porcentaje en el centro
        painter.setPen(self.color_texto)  # Establece el color del texto
        fuente = QFont("Arial", 16, QFont.Bold)  # Tamaño 16 y negrita
        painter.setFont(fuente)
        painter.drawText(self.rect(), Qt.AlignCenter, f"{self.progreso}%")  # Dibuja el porcentaje en el centro

        painter.end()


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reto 2")
        self.setGeometry(100, 100, 250, 300)

        widget_central = QWidget()
        layout = QVBoxLayout(widget_central)
        self.setCentralWidget(widget_central)

        # Crear la barra de progreso circular
        self.barra_progreso = BarraProgresoCircular(grosor=25)
        layout.addWidget(self.barra_progreso)

        # boton para aumentar el progreso
        self.boton = QPushButton("Aumentar Progreso")
        self.boton.clicked.connect(self.incrementar_progrso)
        layout.addWidget(self.boton)

        self.progreso_actual = 0

        # Boton para disminuir el progreo
        self.boton = QPushButton("Disminuir Progreso")
        self.boton.clicked.connect(self.disminir_progreso)
        layout.addWidget(self.boton)


    def disminir_progreso(self):
        # Disminuye el progreso en 10, sin superar el 0
        self.progreso_actual = max(self.progreso_actual - 10, 0)
        self.barra_progreso.establecerProgreso(self.progreso_actual)

    def incrementar_progrso(self):
        # Aumenta el progreso en 10, sin superar 100
        self.progreso_actual = min(self.progreso_actual + 10, 100)
        self.barra_progreso.establecerProgreso(self.progreso_actual)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
