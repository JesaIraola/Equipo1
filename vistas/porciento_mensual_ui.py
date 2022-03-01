from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

class PorcientoMensual(QWidget):

    def __init__(self, presentador):
        self.__presentador = presentador
        
        QWidget.__init__(self)
        uic.loadUi('vistas/ui/porciento_mensual.ui', self)

        self.calcular.clicked.connect(self.ejecutar)
        self.cerrar.clicked.connect(self.close)

    def iniciar(self):
        self.__presentador.insertarNacionalidades()
        self.show()

    def ejecutar(self):
        try:
            prom = self.__presentador.calcularPorciento(self.nacionalidades.currentIndex())
            QMessageBox.information(self, 'Promedio de Clientes', 'El porciento mensual de reservaciones hechas en la recepción del hotel por clientes de la nacionalidad es: %' + str(round(prom, 2)) + '.', QMessageBox.Ok, QMessageBox.Ok)
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)


