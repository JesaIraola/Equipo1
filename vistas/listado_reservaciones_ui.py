from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic

class ListadoReservaciones(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador

        QWidget.__init__(self)
        uic.loadUi('vistas/ui/listado_reservaciones.ui', self)

        self.cerrar.clicked.connect(self.close)
        self.eliminar.clicked.connect(self.eliminarReservacion)
        self.actualizar.clicked.connect(self.actualizarReservacion)

        self.listado.currentCellChanged.connect(self.cambiaCelda)
        self.listado.horizontalHeaderItem(2).setToolTip('Habitación')
        self.listado.horizontalHeaderItem(4).setToolTip('Cantidad de días')

    def iniciar(self):
        self.show()

    def cambiaCelda(self, filaActual):
        self.eliminar.setEnabled(filaActual != -1)
        self.actualizar.setEnabled(filaActual != -1)

    def eliminarReservacion(self):
        fila = self.listado.currentRow()
        if (fila != -1):
            res = QMessageBox.question(self, '¿Eliminar reservación?', 'Está seguro que desea eliminar la reservación seleccionada? Esta acción no se puede deshacer.', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if (res == QMessageBox.Yes):
                self.__presentador.eliminarReservacion(self.listado.item(fila, 0).text())

    def actualizarReservacion(self):
        fila = self.listado.currentRow()
        if (fila != -1):
            self.__presentador.mostrarActualizarReservacion(fila)

    def rellenarCelda(self, fila, columna, texto):
        self.listado.setItem(fila, columna, QTableWidgetItem(texto))

