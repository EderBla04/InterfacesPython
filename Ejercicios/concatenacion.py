import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi
class VentanaLogin(QMainWindow):  # Se mantiene el nombre de la clase

    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), "login.ui")  # Se mantiene la carga del UI
        loadUi(ruta_ui, self)

        # Conectar el botón a la función de concatenación
        self.boton_login.clicked.connect(self.verificar_login)

    def verificar_login(self):  # Se mantiene el nombre de la función

        """ Toma los valores de los campos y realiza la concatenación """
        texto1 = self.campo_usuario.text()  # Antes campo_usuario, ahora texto 1
        texto2 = self.campo_contrasena.text()  # Antes campo_contrasena, ahora texto 2
        resultado = texto1 + " " + texto2  # Concatenación con espacio en medio
        QMessageBox.information(self, "Resultado", f"Concatenado: {resultado}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaLogin()  # Se mantiene el nombre de la clase
    ventana.show()
    sys.exit(app.exec())
