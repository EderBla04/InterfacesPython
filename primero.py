import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), "primero.ui")  # Cargar la interfaz
        loadUi(ruta_ui, self)

        # Conectar el botón con la función para cambiar el texto
        self.boton.clicked.connect(self.mostrar_hola_mundo)

    def mostrar_hola_mundo(self):
        """ Cambia el texto de la QLabel a 'Hola Mundo' """
        self.label.setText("Hola Mundo")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())