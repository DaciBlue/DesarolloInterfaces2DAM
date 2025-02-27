import os
import sys
import pytest
from PySide6.QtWidgets import QApplication

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Simulacro import Coche


# Asegúrate de importar tu clase correcta

@pytest.fixture(scope="session")
def app_instance():
    """Crear una instancia de QApplication solo una vez para todos los tests"""
    app = QApplication([])  # Creamos la instancia de QApplication
    yield app  # Proporciona la aplicación para los tests
    app.quit()  # Cierra la aplicación después de los tests


@pytest.fixture
def window(app_instance):
    """Crear una instancia de TaskManager para cada test"""
    window = Coche()
    return window

def test_arrancar(window):
    window.arrancar()
    assert window.estado() == 'En marcha'

def test_detener(window):
    window.arrancar()  # Primero arrancamos el coche
    window.detener()
    assert window.estado() == 'Detenido'

def test_estado_inicial(window):
    assert window.estado() == 'Detenido'