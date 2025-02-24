'''
Crear un QPushButton que cambie su tamaño dependiendo de la longitud del texto que tenga.
Utiliza el decorador @Property para gestionar la propiedad text y un slot que se ejecute cuando
cambie el texto.
Pasos:
1. Crea un CustomButton que herede de QPushButton.
2. Implementa una propiedad text que emita una señal cuando cambie el texto.
3. Conecta la señal textoCambiado a un slot que cambie el tamaño del botón de acuerdo con la
longitud del texto.
4. Asegúrate de que el tamaño del botón cambie de forma dinámica al modificar el texto.
'''
from PySide6.QtCore import Signal, Slot, Property, Qt
from PySide6.QtWidgets import QPushButton, QSizePolicy, QWidget, QVBoxLayout, QLabel, QLineEdit, QApplication, \
    QMessageBox


class CustomButton(QPushButton):
    # Señal personalizada, emite texto cuando cambia el contenido del botón
    textoSenal = Signal(str)

    def __init__(self, text=""):
        super().__init__(text)
        self.texto_escrito = text  # Guardamos el texto inicial en un atributo propio

        # Conectar la señal personalizada para ajustar el tamaño del botón
        self.textoSenal.connect(self.actualizar_tam)

        # El botón no debería cambiar su tamaño de forma automática (lo manejamos nosotros)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    # Propiedad personalizada para el texto: la usamos para gestionar cambios
    @Property(str)
    def texto(self):
        return self.texto_escrito

    # Si el texto cambia, actualiza el estado del botón y emite la señal
    @texto.setter
    def texto(self, value):
        if self.texto_escrito != value:  # Solo actualizamos si el texto es diferente
            self.texto_escrito = value
            self.setText(value)  # Cambia el texto visible en el botón
            self.textoSenal.emit(value)  # Notificamos que el texto ha cambiado

    # Este slot se encarga de ajustar el tamaño del botón según la longitud del texto
    @Slot(str)
    def actualizar_tam(self, tam):
        ancho = len(tam) * 10  # Cada carácter añade 10 píxeles de ancho
        self.setMinimumWidth(ancho)  # Ajustamos el ancho mínimo del botón


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Boton personalizado")  # Título de la ventana
        self.setGeometry(100, 100, 300, 300)  # Posición y tamaño inicial de la ventana

        # Creamos un layout vertical para organizar los widgets
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Una etiqueta arriba para dar instrucciones al usuario
        self.label = QLabel("Ingresa un texto: ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar texto en la etiqueta
        self.layout.addWidget(self.label)

        # QLineEdit para que el usuario escriba algo
        self.textoEscrito = QLineEdit()
        self.textoEscrito.setPlaceholderText("Escribe un texto para cambiar el tamaño del boton")
        self.textoEscrito.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar texto del input
        self.layout.addWidget(self.textoEscrito)

        # Nuestro botón personalizado, que cambiará dinámicamente su tamaño
        self.btnEscribir = CustomButton("")
        self.layout.addWidget(self.btnEscribir)
        # Centrar el botón en el layout
        self.layout.setAlignment(self.btnEscribir, Qt.AlignmentFlag.AlignCenter)

        # Cuando presionemos el botón, se ejecuta una función para mostrar un mensaje
        self.btnEscribir.clicked.connect(self.texto_boton)

        # Botón para borrar el contenido del input (por comodidad)
        self.btnBorrar = QPushButton("Borrar")
        self.layout.addWidget(self.btnBorrar)
        # Conectar el botón de borrar para limpiar lo que escribió el usuario
        self.btnBorrar.clicked.connect(lambda: self.textoEscrito.setText(""))

        # Hacer que el texto del input actualice el texto del botón personalizado al instante
        self.textoEscrito.textChanged.connect(lambda text: setattr(self.btnEscribir, 'texto', text))

    # Al apretar el botón, muestra un mensaje con el texto actual
    def texto_boton(self):
        texto = self.btnEscribir.texto  # Obtenemos el texto actual del botón
        self.mensaje = QMessageBox()  # Crear cuadro de mensaje
        self.mensaje.setWindowTitle("Boton personalizado")  # Título del cuadro
        self.mensaje.setIcon(QMessageBox.Information)  # Icono informativo
        self.mensaje.setText(f"El texto introducido en el botón es:\n {texto}")  # Mensaje principal
        self.mensaje.setStandardButtons(QMessageBox.Close)  # Botón para cerrar
        self.mensaje.exec()  # Mostrar el cuadro de diálogo


if __name__ == "__main__":
    app = QApplication()  # Crear la aplicación principal
    window = Ventana()  # Creamos nuestra ventana personalizada
    window.show()  # Mostrar la ventana en pantalla
    app.exec()  # Ejecutar el loop de la aplicación




