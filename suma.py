import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi

# Credenciales correctas

USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "1234"

class VentanaLogin(QMainWindow):

    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), "suma.ui")  # Asegurar la ruta
        loadUi(ruta_ui, self)  # Cargar la interfaz

        # Conectar el botón a la función de login
        self.boton_suma.clicked.connect(self.suma)

    def suma(self):

        try:
            num1 = float(self.numero1.text())
            num2 = float(self.numero2.text())
            resultado = num1 + num2
            QMessageBox.information(self, "Resultado", f"El resultado es: {resultado}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese números válidos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaLogin()
    ventana.show()
    sys.exit(app.exec())