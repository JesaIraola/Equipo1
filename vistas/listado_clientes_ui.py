from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt5 import uic

class ListadoClientes(QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador

        QWidget.__init__(self)
        uic.loadUi('vistas/ui/listado_clientes.ui', self)

        self.cerrar.clicked.connect(self.close)
        self.eliminar.clicked.connect(self.eliminarCliente)
        self.actualizar.clicked.connect(self.actualizarCliente)
        
        self.listado.currentCellChanged.connect(self.cambiaCelda)
        self.listado.horizontalHeaderItem(1).setToolTip('Número de identificación')

    def iniciar(self):
        self.show()

    def cambiaCelda(self, filaActual):
        self.eliminar.setEnabled(filaActual != -1)
        self.actualizar.setEnabled(filaActual != -1)

    def eliminarCliente(self):
        fila = self.listado.currentRow()
        if (fila != -1):
            res = QMessageBox.question(self, '¿Eliminar cliente?', 'Está seguro que desea eliminar el cliente seleccionado? Note que si elimina el cliente también se eliminan todas sus reservaciones. Esta acción no se puede deshacer.', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if (res == QMessageBox.Yes):
                self.__presentador.eliminarCliente(self.listado.item(fila, 1).text())

    def actualizarCliente(self):
        fila = self.listado.currentRow()
        if (fila != -1):
            self.__presentador.mostrarActualizarCliente(fila)

    def rellenarCelda(self, fila, columna, texto):
        self.listado.setItem(fila, columna, QTableWidgetItem(texto))

