from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from datetime import datetime
from vistas.editar_reservacion_recepcion_ui import EditarReservacionRecepcion
from vistas.editar_turoperador_ui import EditarTuroperador

class EditarReservacionTuroperador(EditarReservacionRecepcion):

    def __init__(self, presentador, indice = -1):
        EditarReservacionRecepcion.__init__(self, presentador, indice)

    def loadUi(self):
        uic.loadUi('vistas/ui/editar_reservacion_turoperador.ui', self)

    def iniciar(self):
        self.adicionarTuroperador.clicked.connect(self.presentador.mostrarAdicionarTuroperador)
        self.iniciarValores('', '', -1, '', datetime.now(), 1, '', False)
        self.show()

    def iniciarValores(self, numero_identificacion_cliente, numero_habitacion, tipo_pago, codigo, fecha_entrada, cantidad_dias, codigo_turoperador = '', es_tour = False):
        EditarReservacionRecepcion.iniciarValores(self, numero_identificacion_cliente, numero_habitacion, tipo_pago, codigo, fecha_entrada, cantidad_dias)
        self.presentador.insertarTuroperadores(codigo_turoperador)
        self.esTour.setChecked(es_tour)

    def adicionarReservacion(self):
        numero_identificacion_cliente = self.clienteActual
        numero_habitacion = self.habitacionActual
        codigo_turoperador = self.__obtenerTuroperador()
        tipo_pago = self.tipoPagoActual

        try:
            qtDate = self.fechaEntrada.date()
            fecha_entrada = datetime.strptime(str(qtDate.day()) + '-' + str(qtDate.month()) + '-' + str(qtDate.year()), '%d-%m-%Y')
            self.presentador.adicionarReservacion(numero_identificacion_cliente, numero_habitacion, tipo_pago, self.codigo.text(), fecha_entrada, int(self.cantidadDias.text()), codigo_turoperador, self.esTour.isChecked())

            QMessageBox.information(self, 'Información', 'La reservacion se ha adicionado correctamente.', QMessageBox.Ok, QMessageBox.Ok)
            self.cuandoGuarde.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)

    def actualizarReservacion(self):
        numero_identificacion_cliente = self.clienteActual
        numero_habitacion = self.habitacionActual
        codigo_turoperador = self.__obtenerTuroperador()
        tipo_pago = self.tipoPagoActual

        try:
            qtDate = self.fechaEntrada.date()
            fecha_entrada = datetime.strptime(str(qtDate.day()) + '-' + str(qtDate.month()) + '-' + str(qtDate.year()), '%d-%m-%Y')
            self.presentador.actualizarReservacion(numero_identificacion_cliente, numero_habitacion, tipo_pago, self.codigo.text(), fecha_entrada, int(self.cantidadDias.text()), codigo_turoperador, self.esTour.isChecked(), self.indice)

            QMessageBox.information(self, 'Información', 'El reservacion se ha actualizado correctamente.', QMessageBox.Ok, QMessageBox.Ok)
            self.cuandoGuarde.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)

    def __obtenerTuroperador(self):
        if self.turoperador.currentIndex() == -1:
            turoperador = ''
        else:
            try:
                turoperador = self.presentador.obtenerTuroperador(self.turoperador.currentIndex())
            except:
                turoperador = ''

        return turoperador





