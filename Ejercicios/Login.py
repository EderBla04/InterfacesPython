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
        ruta_ui = os.path.join(os.path.dirname(__file__), "login.ui")  # Asegurar la ruta
        loadUi(ruta_ui, self)  # Cargar la interfaz

        # Conectar el botón a la función de login
        self.boton_login.clicked.connect(self.verificar_login)

    def verificar_login(self):
        usuario = self.campo_usuario.text()
        contrasena = self.campo_contrasena.text()

        if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
            QMessageBox.information(self, "Acceso permitido", "¡Entraste!")
        else:
            QMessageBox.warning(self, "Te equivocaste", "Usuario o "
                                               "contraseña incorrectos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaLogin()
    ventana.show()
    sys.exit(app.exec())