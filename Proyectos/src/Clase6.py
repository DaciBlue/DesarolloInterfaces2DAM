'''
NOTE: Crear un botón personalizado que cambie de color dependiendo del texto que tenga. Además, se
debe incluir un slot que responda a la señal emitida cuando el texto cambie, y realice una acción
como cambiar el tamaño del texto o imprimir un mensaje en la consola.
Pasos:
1. Crea un CustomButton que herede de QPushButton.
2. Implementa una propiedad text que se pueda modificar desde el exterior y emita una señal
textoCambiado cuando el texto cambie.
3. Agrega un métodoo set_color_based_on_text que cambie el color de fondo del botón según el
texto.
4. Crea un slot on_text_changed que se conecte a la señal textoCambiado y cambie el tamaño
del texto cuando esta señal sea emitida.
5. Añade una animación que cambie gradualmente el color del botón utilizando un QTimer.
6. Prueba el funcionamiento, cambiando el texto del botón y viendo cómo cambia el color y el
tamaño del texto
'''
import sys

from PySide6.QtGui import QColor
from PySide6.QtWidgets import QPushButton, QApplication, QGraphicsDropShadowEffect
from PySide6.QtCore import Signal, Property, QTimer, Slot


class CustomButton(QPushButton):
    ## Definimos una señal personalizada que emitira cuando el texto cambie
    texto_cambiado = Signal(str)
    def __init__(self, text = "Texto inicial"):
        super().__init__(text) ## Llamamos al constructor de QPushButton con texto inicial
        self._text = text ## Inicializamos el atributo _text con el texto proporcionado
        self.set_color_based_on_text() ## Llamar a funcion para que actualice el color
        self.set_text_size(12) ## Establezco el tamaño de boton a 12px
        self.add_shado_effect()
        self.texto_cambiado.connect(self.on_text_changed)

    @Property(str) # Defino una propiedad text que devuelve el valor de _text
    def text(self):
        return self._text

    @text.setter
    def text(self, value): ## Si el texto es distinto el anterior
        if self._text != value:
            self._text = value ## actualizo la variable interna
            self.setText(value) ## cambio el texto del boton
            self.texto_cambiado.emit(value) ## emito la señal del textoCambiado para notificar el cambio

    def set_color_based_on_text(self):
        ## Definir un diccionario que a un valor del texto lo mapea a un color
        color_map = {
            "Rojo": "red",
            "Verde": "green",
            "Azul": "blue"
        }

        color = color_map.get(self._text,"gray") ## Si no encuentra el texto, usamos el color gris por defecto
        self.setStyleSheet(f"background-color:{color}")

    def set_text_size(self, size):
        self.setStyleSheet(f"font-size:{size}px") ## Establecemos el tamaño usando CSS

    def add_shado_effect(self):
        ## Crear un efecto de sombra
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20) ## El radio de difuminado
        shadow.setColor(QColor(0, 0, 0, 160)) ## Establecer el color la sombra
        shadow.setOffset(3, 3) ## Desplazamiento de la sombra
        self.setGraphicsEffect(shadow)

    def animate_color_change(self, target_color):
        ## Inicializamos el color actual con el color objetivo
        self.color_actual = QColor(self.palette().button().color())
        self.target_color = QColor(target_color)

        ## Cambio el color de manera gradual
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.step_color_change)
        self.timer.start(1000) ## Este temporizador se ajusta cada 1000ms

    def step_color_change(self):
        step = 10 ## Cambio de color
        current_rgb = self.color_actual.getRgb()[:3]
        target_rgb = self.target_color.getRgb()[:3]

        ## Calcular el nuevo RGB intermedio
        new_rgb = [
            min(255, max(0,current_rgb[i]+ target_rgb[i]))
            for i in range(3)
        ]
        self.color_actual.setRgb(*new_rgb)
        self.setStyleSheet(f"background-color: {self.color_actual.name()};")
        if self.color_actual.getRgb() == target_rgb:
            self.timer.stop()
        self.update()

    @Slot(str)
    def on_text_changed(self, new_text):
        self.set_text_size(16)
        print(f"Texto del boton cambiado a: {new_text}")

if __name__ == "__main__":
    app = QApplication(sys.argv) ## Inicializamos una aplicacion QT
    button = CustomButton("Rojo") ## Creamos un boton con texto inicial a "Rojo"
    button.show() ## Muestro el boton
    button.setText("Verde")
    button.animate_color_change("blue")
    app.exec()

