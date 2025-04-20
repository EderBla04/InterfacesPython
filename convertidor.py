import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi



class ConvertidorTemperatura(QMainWindow):

    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), "convertidor.ui")  # Asegurar la ruta
        loadUi(ruta_ui, self)  # Cargar la interfaz

        # Llenar los combobox con las unidades de temperatura
        unidades = ["Celsius", "Fahrenheit", "Kelvin"]
        self.combo_entrada.addItems(unidades)
        self.combo_salida.addItems(unidades)

        # Conectar el botón de convertir
        self.boton_convertir.clicked.connect(self.convertir_temperatura)

    def convertir_temperatura(self):
        try:
            valor = float(self.campo_temperatura.text())
            unidad_origen = self.combo_entrada.currentText()
            unidad_destino = self.combo_salida.currentText()

            # Si las unidades son iguales no hay conversión
            if unidad_origen == unidad_destino:
                resultado = valor
            else:
                resultado = self.realizar_conversion(valor, unidad_origen, unidad_destino)

            self.label_resultado.setText(f"{resultado:.2f} {unidad_destino}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Introduce un valor numérico")

    def realizar_conversion(self, valor, unidad_origen, unidad_destino):
        if unidad_origen == "Celsius":
            if unidad_destino == "Fahrenheit":
                return (valor * 9/5) + 32
            elif unidad_destino == "Kelvin":
                return valor + 273.15

        elif unidad_origen == "Fahrenheit":
            if unidad_destino == "Celsius":
                return (valor - 32) * 5/9
            elif unidad_destino == "Kelvin":
                return (valor - 32) * 5/9 + 273.15

        elif unidad_origen == "Kelvin":
            if unidad_destino == "Celsius":
                return valor - 273.15
            elif unidad_destino == "Fahrenheit":
                return (valor - 273.15) * 9/5 + 32

        return valor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ConvertidorTemperatura()
    ventana.show()
    sys.exit(app.exec())
