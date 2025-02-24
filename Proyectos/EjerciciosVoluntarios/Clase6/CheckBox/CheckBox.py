'''
Crear una interfaz con un QCheckBox que, cuando se marque o desmarque, cambie el texto de un
QLabel. Utiliza el decorador @Slot para conectar la señal del QCheckBox al slot que modificará el
texto del QLabel.
Pasos:
1. Crea un archivo de interfaz con Qt Designer que tenga un QCheckBox y un QLabel.
2. En el archivo Python, conecta la señal toggled del QCheckBox a un slot que cambie el texto
del QLabel dependiendo de si el QCheckBox está marcado o no.
3. Cuando el QCheckBox esté marcado, cambia el texto del QLabel a "Activado", y cuando no
lo esté, cambia el texto a "Desactivado".
'''
from PySide6.QtCore import Slot, Property
from PySide6.QtWidgets import QCheckBox
from EjerciciosVoluntarios.Clase6.CheckBox.CheckBoxInterfaz import Ui_MainWindow


class CheckBox(QCheckBox):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.checkBox.toggled.connect(self.cambiarTexto)

    @Property(str)
    def texto(self):
