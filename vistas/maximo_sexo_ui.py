from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

class MaximoSexo(QWidget):

    def __init__(self, presentador):
        self.__presentador = presentador
        
        QWidget.__init__(self)
        uic.loadUi('vistas/ui/maximo_sexo.ui', self)

        self.calcular.clicked.connect(self.ejecutar)
        self.cerrar.clicked.connect(self.close)

    def iniciar(self):
        self.__presentador.insertarNacionalidades()
        self.show()

    def ejecutar(self):
        try:
            mensaje = self.__presentador.calcularMaximoSexo(self.nacionalidades.currentIndex())
            QMessageBox.information(self, 'Máximo de sexo', mensaje, QMessageBox.Ok, QMessageBox.Ok)
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)


