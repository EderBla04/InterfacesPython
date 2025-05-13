import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QTimer
from PyQt6.uic import loadUi

class Temporizador(QMainWindow):

    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), "temporizador.ui")  # Cargar la interfaz
        loadUi(ruta_ui, self)

        # Configurar el temporizador
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.tiempo_restante = 0  # Inicializa el tiempo

        # Conectar el botón para iniciar el temporizador
        self.boton_iniciar.clicked.connect(self.iniciar_temporizador)

    def iniciar_temporizador(self):
        """ Inicia la cuenta regresiva """
        try:
            self.tiempo_restante = int(self.campo_segundos.text())  # Obtener segundos
            if self.tiempo_restante <= 0:
                raise ValueError  # Evitar valores negativos o cero
            self.label_tiempo.setText(f"Tiempo restante: {self.tiempo_restante} s")
            self.timer.start(1000)  # Actualizar cada 1000ms (1 segundo)
            self.campo_segundos.setEnabled(False)  # Deshabilitar la entrada mientras corre
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese un número entero mayor a 0.")

    def actualizar_tiempo(self):

        """ Resta un segundo y actualiza la etiqueta """
        self.tiempo_restante -= 1
        self.label_tiempo.setText(f"Tiempo restante: {self.tiempo_restante} s")
        if self.tiempo_restante <= 0:
            self.timer.stop()
            self.campo_segundos.setEnabled(True)  # Rehabilitar la entrada
            QMessageBox.information(self, "¡Tiempo terminado!", "El tiempo ha finalizado.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Temporizador()
    ventana.show()
    sys.exit(app.exec())