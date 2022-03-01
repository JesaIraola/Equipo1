from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

class ReservacionesTuroperador(QWidget):

    def __init__(self, presentador):
        self.__presentador = presentador
        
        QWidget.__init__(self)
        uic.loadUi('vistas/ui/reservaciones_turoperador.ui', self)

        self.calcular.clicked.connect(self.ejecutar)
        self.cerrar.clicked.connect(self.close)

    def iniciar(self):
        self.__presentador.insertarTuroperadores()
        self.show()

    def ejecutar(self):
        try:
            self.__presentador.calcularReservacionesTuroperador(self.turoperadores.currentIndex())
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)

    def limpiarListado(self):
        while self.clientes.rowCount() > 0:
            self.clientes.removeRow(0)
        
    def rellenarCelda(self, fila, columna, texto):
        self.clientes.setItem(fila, columna, QTableWidgetItem(texto))


