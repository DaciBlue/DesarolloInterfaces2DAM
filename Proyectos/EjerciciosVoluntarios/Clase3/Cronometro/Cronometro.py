'''
Crea una aplicación que implemente un cronómetro. Debe incluir botones para iniciar, pausar y
reiniciar el cronómetro, y mostrar el tiempo transcurrido en formato mm:ss. (QTime)
'''
import sys

from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import QTime, QTimer, Qt


class Cronometro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cronometro")
        self.setGeometry(100, 100, 300, 400)
        self.show()

        ##Principal
        self.principal = QVBoxLayout()
        self.setLayout(self.principal)

        ##Cronometro
        self.crono = QTime(0,0)

        ##Etiquetas tiempo
        '''Se mete el tiempo dentro de etiquetas para mostrarlo
        '''
        self.lblTiempo = QLabel(self.crono.toString("mm:ss"))
        self.lblTiempo.setStyleSheet("font-size: 30px; font-weight: bold;")
        self.lblTiempo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.principal.addWidget(self.lblTiempo)

        ##Actualizar cronometro
        self.actualizaCrono = QTimer()
        self.actualizaCrono.setInterval(1000)
        self.actualizaCrono.timeout.connect(self.actualizarTiempo)

        ##Botones
        ##Iniciar
        self.btnIniciar = QPushButton("Iniciar")
        self.principal.addWidget(self.btnIniciar)
        self.btnIniciar.clicked.connect(self.iniciar)
        ##Pausar
        self.btnPausar = QPushButton("Pausar")
        self.principal.addWidget(self.btnPausar)
        self.btnPausar.clicked.connect(self.pausar)
        ##Reiniciar
        self.btnReiniciar = QPushButton("Reiniciar")
        self.principal.addWidget(self.btnReiniciar)
        self.btnReiniciar.clicked.connect(self.reiniciar)

    def actualizarTiempo(self):
        "Incrementa el tiempo en 1 segundo y actualiza la etiqueta"
        self.crono = self.crono.addSecs(1)
        self.lblTiempo.setText(self.crono.toString("mm:ss"))

    def iniciar(self):
        "Inicia o renauda el cronometro"
        if not self.actualizaCrono.isActive():
            self.actualizaCrono.start()
            self.btnIniciar.setEnabled(False)

    def pausar(self):
        "Pausa o reanuda el cronometro y cambia el texto de las etiquetas"
        if self.actualizaCrono.isActive():
            self.actualizaCrono.stop()
            self.btnPausar.setEnabled(False)
            self.btnIniciar.setText("Renaudar")
            self.btnIniciar.setEnabled(True)

    def reiniciar(self):
        "Reinicia el cronometro"
        self.actualizaCrono.stop()
        self.crono = QTime(0,0)
        self.lblTiempo.setText(self.crono.toString("mm:ss"))
        self.btnIniciar.setText("Iniciar")
        self.btnIniciar.setEnabled(True)
        self.btnPausar.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cronometro()
    window.show()
    app.exec()