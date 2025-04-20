import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi

class BotonesVista(QMainWindow):

    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), "botones.ui")  # Asegurar la ruta
        loadUi(ruta_ui, self)

        self.boton_ecender.clicked.connect(self.encender)
        self.boton_apagar.clicked.connect(self.apagar)

    def encender(self):
        print("1")

    def apagar(self):
        print("0")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = BotonesVista()
    ventana.show()
    sys.exit(app.exec())