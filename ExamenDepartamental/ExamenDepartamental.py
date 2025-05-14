import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/ederg/PycharmProjects/PythonProject1/ExamenDepartamental/VistaExamen.ui", self)
        self.btnCalcular.clicked.connect(self.calcular)
        
        # Configurar el área para la gráfica
        self.figure = Figure(figsize=(6, 4))
        self.canvas = FigureCanvas(self.figure)
        self.grafica_layout = QVBoxLayout()
        self.grafica_layout.addWidget(self.canvas)
        self.frame_grafica.setLayout(self.grafica_layout)
        
    def calcular(self):
        try:
            # Leer el archivo txt
            with open("C:/Users/ederg/PycharmProjects/PythonProject1/ExamenDepartamental/datos.txt", "r") as archivo:
                base = float(archivo.readline().strip())
                altura = float(archivo.readline().strip())
                python = archivo.readline().strip()
            
            # Calcular área
            area = base * altura
            self.lblArea.setText(f"Área del rectángulo: {area}")
            
            # Invertir palabra python sin h
            python_sin_h = python.replace("h", "")
            python_invertido = python_sin_h[::-1]
            self.lblPython.setText(f"Python invertido: {python_invertido}")
            
            # Crear gráfica de barras
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            datos = [base, altura, area]
            etiquetas = ['Base', 'Altura', 'Área']
            colores = ['#4B8BBE', '#306998', '#FFE873']
            
            ax.bar(etiquetas, datos, color=colores)
            ax.set_title('Medidas del Rectángulo')
            ax.set_ylabel('Valores')
            ax.grid(True, alpha=0.3)
            
            # Actualizar la gráfica
            self.figure.tight_layout()
            self.canvas.draw()
            
        except Exception as e:
            self.lblArea.setText(f"Error: {str(e)}")
            self.lblPython.setText("Error al procesar los datos")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
