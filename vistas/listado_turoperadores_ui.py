from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic

class ListadoTuroperadores(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador

        QWidget.__init__(self)
        uic.loadUi('vistas/ui/listado_turoperadores.ui', self)

        self.cerrar.clicked.connect(self.close)
        self.eliminar.clicked.connect(self.eliminarTuroperador)
        self.actualizar.clicked.connect(self.actualizarTuroperador)

        self.listado.currentCellChanged.connect(self.cambiaCelda)

    def iniciar(self):
        self.show()

    def cambiaCelda(self, filaActual):
        self.eliminar.setEnabled(filaActual != -1)
        self.actualizar.setEnabled(filaActual != -1)

    def eliminarTuroperador(self):
        fila = self.listado.currentRow()
        if (fila != -1):
            res = QMessageBox.question(self, '¿Eliminar turoperador?', 'Está seguro que desea eliminar el turoperador seleccionado? Note que si elimina el turoperador también se eliminan todas sus reservaciones. Esta acción no se puede deshacer.', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if (res == QMessageBox.Yes):
                self.__presentador.eliminarTuroperador(self.listado.item(fila, 1).text())

    def actualizarTuroperador(self):
        fila = self.listado.currentRow()
        if (fila != -1):
            self.__presentador.mostrarActualizarTuroperador(fila)

    def rellenarCelda(self, fila, columna, texto):
        self.listado.setItem(fila, columna, QTableWidgetItem(texto))

