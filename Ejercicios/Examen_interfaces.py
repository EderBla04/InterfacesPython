#3, 6 line edits
#
#
import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi

class BotonesVista(QMainWindow):

    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), "ListaOrdenada.ui")  # Asegurar la ruta
        loadUi(ruta_ui, self)

        self.Ordenar.clicked.connect(self.ordenar_lista)

    def ordenar_lista(self):

        try:
            num1 = int(self.entrada_1.text())
            num2 = int(self.entrada_2.text())
            num3 = int(self.entrada_3.text())

            lista = [num1, num2, num3]

            lista.sort()

            self.salida_1.setText(str(lista[0]))
            self.salida_2.setText(str(lista[1]))
            self.salida_3.setText(str(lista[2]))

        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese números válidos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = BotonesVista()
    ventana.show()
    sys.exit(app.exec())