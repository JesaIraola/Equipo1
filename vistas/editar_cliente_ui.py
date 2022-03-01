from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

SEXOS = ['M', 'F']

class EditarCliente(QWidget):

    cuandoGuarde = pyqtSignal()

    def __init__(self, presentador, indice = -1):
        self.__presentador = presentador
        self.__indice = indice

        QWidget.__init__(self)
        uic.loadUi('vistas/ui/editar_cliente.ui', self)

        if (indice == -1):
            self.adicionar.clicked.connect(self.adicionarCliente)
            self.adicionar.setText('Adicionar')
        else:
            self.adicionar.clicked.connect(self.actualizarCliente)
            self.adicionar.setText('Actualizar')

        self.cancelar.clicked.connect(self.close)
        self.iniciarValores('', '', 18, '', '', False)

    def iniciar(self):
        self.show()

    def iniciarValores(self, nombre, numero, edad, sexo, nacionalidad, visitaPrevia):
        self.nombre.setText(nombre)
        self.numero.setText(numero)
        self.edad.setValue(edad)

        try:
            index = SEXOS.index(sexo)
        except:
            index = -1

        self.sexo.setCurrentIndex(index)

        self.nacionalidad.setText(nacionalidad)
        self.visitaPrevia.setChecked(visitaPrevia)

    def adicionarCliente(self):
        sexo = self.__obtenerSexo()

        try:
            self.__presentador.adicionarCliente(self.numero.text(), self.nombre.text(), self.edad.value(), sexo, self.nacionalidad.text(), self.visitaPrevia.isChecked())

            QMessageBox.information(self, 'Información', 'El cliente se ha adicionado correctamente.', QMessageBox.Ok, QMessageBox.Ok)
            self.cuandoGuarde.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)

    def actualizarCliente(self):
        sexo = self.__obtenerSexo()

        try:
            self.__presentador.actualizarCliente(self.numero.text(), self.nombre.text(), self.edad.value(), sexo, self.nacionalidad.text(), self.visitaPrevia.isChecked(), self.__indice)

            QMessageBox.information(self, 'Información', 'El cliente se ha actualizado correctamente.', QMessageBox.Ok, QMessageBox.Ok)
            self.cuandoGuarde.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)

    def __obtenerSexo(self):
        if self.sexo.currentIndex() == -1:
            sexo = ''
        else:
            try:
                sexo = SEXOS[self.sexo.currentIndex()]
            except:
                sexo = ''

        return sexo
