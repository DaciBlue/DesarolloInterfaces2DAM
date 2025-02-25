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
import sys
from PySide6.QtCore import Slot, Property
from PySide6.QtWidgets import QCheckBox, QApplication, QMainWindow
from EjerciciosVoluntarios.Clase6.CheckBox.CheckBoxInterfaz import Ui_MainWindow


class CheckBoxApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.checkBox.toggled.connect(self.cambiarTexto)

    # Slot que maneja el cambio de texto del QLabel
    @Slot(bool)
    def cambiarTexto(self, estado):
        if estado:
            self.ui.lblTexto.setText("Activado")
        else:
            self.ui.lblTexto.setText("Desactivado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheckBoxApp()
    window.show()
    sys.exit(app.exec())