from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

class EditarTuroperador(QWidget):

    cuandoGuarde = pyqtSignal()

    def __init__(self, presentador, indice = -1):
        self.__presentador = presentador
        self.__indice = indice

        QWidget.__init__(self)
        uic.loadUi('vistas/ui/editar_turoperador.ui', self)

        if (indice == -1):
            self.adicionar.clicked.connect(self.adicionarTuroperador)
            self.adicionar.setText('Adicionar')
        else:
            self.adicionar.clicked.connect(self.actualizarTuroperador)
            self.adicionar.setText('Actualizar')

        self.cancelar.clicked.connect(self.close)
        self.iniciarValores('', '', '')

    def iniciar(self):
        self.show()

    def iniciarValores(self, nombre, codigo, nacionalidad):
        self.nombre.setText(nombre)
        self.codigo.setText(codigo)
        self.nacionalidad.setText(nacionalidad)

    def adicionarTuroperador(self):
        try:
            self.__presentador.adicionarTuroperador(self.nombre.text(), self.codigo.text(), self.nacionalidad.text())

            QMessageBox.information(self, 'Información', 'El turoperador se ha adicionado correctamente.', QMessageBox.Ok, QMessageBox.Ok)
            self.cuandoGuarde.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)

    def actualizarTuroperador(self):
        try:
            self.__presentador.actualizarTuroperador(self.nombre.text(), self.codigo.text(), self.nacionalidad.text(), self.__indice)

            QMessageBox.information(self, 'Información', 'El turoperador se ha actualizado correctamente.', QMessageBox.Ok, QMessageBox.Ok)
            self.cuandoGuarde.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)
