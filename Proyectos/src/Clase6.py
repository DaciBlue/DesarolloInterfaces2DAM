'''
Crear un botón personalizado que cambie de color dependiendo del texto que tenga. Además, se
debe incluir un slot que responda a la señal emitida cuando el texto cambie, y realice una acción
como cambiar el tamaño del texto o imprimir un mensaje en la consola.
Pasos:
1. Crea un CustomButton que herede de QPushButton.
2. Implementa una propiedad text que se pueda modificar desde el exterior y emita una señal
textoCambiado cuando el texto cambie.
3. Agrega un método set_color_based_on_text que cambie el color de fondo del botón según el
texto.
4. Crea un slot on_text_changed que se conecte a la señal textoCambiado y cambie el tamaño
del texto cuando esta señal sea emitida.
5. Añade una animación que cambie gradualmente el color del botón utilizando un QTimer.
6. Prueba el funcionamiento, cambiando el texto del botón y viendo cómo cambia el color y el
tamaño del texto
'''
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal


class CustomButton(QPushButton):
    ## Definimos una señal personalizada que emitira cuando el texto cambie
    texto_cambiado = Signal(str)
    def __init__(self, text = "Texto inicial"):
        super().__init__(text) ## Llamamos al constructor de QPushButton con texto inicial

    @text.setter
    def text(self, value): ## Si el texto es distinto el anterior
        if self._text != value:
            self._text = value ## actualizo la variable interna
            self.setText(value) ## cambio el texto del boton
            self.texto_cambiado.emit(value) ## emito la señal del textoCambiado para notificar el cambio

