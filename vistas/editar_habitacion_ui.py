from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

TIPOS = ['SIMPLE', 'DOBLE', 'TRIPLE', 'SUITE']
ESTILOS = ['ANTIGUA', 'MODERNA', 'NATURAL']

class EditarHabitacion(QWidget):

    cuandoGuarde = pyqtSignal()

    def __init__(self, presentador, indice = -1):
        self.__presentador = presentador
        self.__indice = indice

        QWidget.__init__(self)
        uic.loadUi('vistas/ui/editar_habitacion.ui', self)

        if (indice == -1):
            self.adicionar.clicked.connect(self.adicionarHabitacion)
            self.adicionar.setText('Adicionar')
        else:
            self.adicionar.clicked.connect(self.actualizarHabitacion)
            self.adicionar.setText('Actualizar')

        self.cancelar.clicked.connect(self.close)

        self.iniciarValores(-1, '', '', False)

    def iniciar(self):
        self.show()

    def iniciarValores(self, numero, tipo, estilo, tiene_internet):
        self.numero.setValue(numero)
        self.tieneInternet.setChecked(tiene_internet)

        try:
            index = TIPOS.index(tipo)
        except:
            index = -1

        self.tipo.setCurrentIndex(index)

        try:
            index = ESTILOS.index(estilo)
        except:
            index = -1

        self.estilo.setCurrentIndex(index)

    def adicionarHabitacion(self):
        tipo = self.__obtenerTipo()
        estilo = self.__obtenerEstilo()

        try:
            self.__presentador.adicionarHabitacion(int(self.numero.text()), tipo, estilo, self.tieneInternet.isChecked())

            QMessageBox.information(self, 'Información', 'La habitación se ha adicionado correctamente.', QMessageBox.Ok, QMessageBox.Ok)
            self.cuandoGuarde.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)

    def actualizarHabitacion(self):
        tipo = self.__obtenerTipo()
        estilo = self.__obtenerEstilo()

        try:
            self.__presentador.actualizarHabitacion(int(self.numero.text()), tipo, estilo, self.tieneInternet.isChecked(), self.__indice)

            QMessageBox.information(self, 'Información', 'La habitación se ha actualizado correctamente.', QMessageBox.Ok, QMessageBox.Ok)
            self.cuandoGuarde.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)

    def __obtenerTipo(self):
        if self.tipo.currentIndex() == -1:
            tipo = ''
        else:
            try:
                tipo = TIPOS[self.tipo.currentIndex()]
            except:
                tipo = ''

        return tipo

    def __obtenerEstilo(self):
        if self.estilo.currentIndex() == -1:
            estilo = ''
        else:
            try:
                estilo = ESTILOS[self.estilo.currentIndex()]
            except:
                estilo = ''

        return estilo








