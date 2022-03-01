from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic

class ListadoHabitaciones(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador

        QWidget.__init__(self)
        uic.loadUi('vistas/ui/listado_habitaciones.ui', self)

        self.cerrar.clicked.connect(self.close)
        self.eliminar.clicked.connect(self.eliminarHabitacion)
        self.actualizar.clicked.connect(self.actualizarHabitacion)

        self.listado.currentCellChanged.connect(self.cambiaCelda)

    def iniciar(self):
        self.show()

    def cambiaCelda(self, filaActual):
        self.eliminar.setEnabled(filaActual != -1)
        self.actualizar.setEnabled(filaActual != -1)

    def eliminarHabitacion(self):
        fila = self.listado.currentRow()
        if (fila != -1):
            res = QMessageBox.question(self, '¿Eliminar habitación?', 'Está seguro que desea eliminar la habitación seleccionado? Note que si elimina la habitación también se eliminan todas sus reservaciones. Esta acción no se puede deshacer.', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if (res == QMessageBox.Yes):
                self.__presentador.eliminarHabitacion(int(self.listado.item(fila, 0).text()))

    def actualizarHabitacion(self):
        fila = self.listado.currentRow()
        if (fila != -1):
            self.__presentador.mostrarActualizarHabitacion(fila)

    def rellenarCelda(self, fila, columna, texto):
        self.listado.setItem(fila, columna, QTableWidgetItem(texto))

    def rellenarFilas(self):
        self.limpiarListado()

        for hab in self.__habitaciones:
            i = self.listado.rowCount()

            self.listado.insertRow(i)

            self.listado.setItem(i, 0, QTableWidgetItem(str(hab.numero)))
            self.listado.setItem(i, 1, QTableWidgetItem(hab.tipo))
            self.listado.setItem(i, 2, QTableWidgetItem(hab.estilo))

            if (hab.tiene_internet):
                tieneInternet = 'Si'
            else:
                tieneInternet = 'No'

            self.listado.setItem(i, 3, QTableWidgetItem(tieneInternet))
            self.listado.setItem(i, 4, QTableWidgetItem(str(hab.costo())))

        self.listado.resizeColumnsToContents()
        self.listado.setCurrentCell(-1, -1)

