from PyQt5.QtWidgets import QWidget, QMessageBox, QComboBox
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from datetime import datetime

TIPOS_PAGO = ['EFECTIVO', 'TARJETA MAGNETICA']

class EditarReservacionRecepcion(QWidget):

    cuandoGuarde = pyqtSignal()

    def __init__(self, presentador, indice = -1):
        self.__presentador = presentador
        self.__indice = indice

        QWidget.__init__(self)
        self.loadUi()

        if (indice == -1):
            self.adicionar.clicked.connect(self.adicionarReservacion)
            self.adicionar.setText('Adicionar')
        else:
            self.adicionar.clicked.connect(self.actualizarReservacion)
            self.adicionar.setText('Actualizar')

        self.cancelar.clicked.connect(self.close)
        self.adicionarCliente.clicked.connect(self.__presentador.mostrarAdicionarCliente)
        self.adicionarHabitacion.clicked.connect(self.__presentador.mostrarAdicionarHabitacion)

    @property
    def clienteActual(self):
        return self.__obtenerCliente()

    @property
    def habitacionActual(self):
        return self.__obtenerHabitacion()

    @property
    def tipoPagoActual(self):
        return self.__obtenerTipoPago()

    @property
    def presentador(self):
        return self.__presentador

    @property
    def indice(self):
        return self.__indice

    def loadUi(self):
        uic.loadUi('vistas/ui/editar_reservacion_recepcion.ui', self)

    def iniciar(self):
        self.iniciarValores('', '', -1, '', datetime.now(), 1)
        self.show()

    def iniciarValores(self, numero_identificacion_cliente, numero_habitacion, tipo_pago, codigo, fecha_entrada, cantidad_dias):
        self.codigo.setText(codigo)
        self.cantidadDias.setValue(cantidad_dias)
        self.fechaEntrada.setDate(fecha_entrada)

        try:
            index = TIPOS_PAGO.index(tipo_pago)
        except:
            index = -1

        self.tipoPago.setCurrentIndex(index)

        self.__presentador.insertarClientes(numero_identificacion_cliente)
        self.__presentador.insertarHabitaciones(numero_habitacion)

    def adicionarReservacion(self):
        numero_identificacion_cliente = self.__obtenerCliente()
        numero_habitacion = self.__obtenerHabitacion()
        tipo_pago = self.__obtenerTipoPago()

        try:
            qtDate = self.fechaEntrada.date()
            fecha_entrada = datetime.strptime(str(qtDate.day()) + '-' + str(qtDate.month()) + '-' + str(qtDate.year()), '%d-%m-%Y')
            self.__presentador.adicionarReservacion(numero_identificacion_cliente, numero_habitacion, tipo_pago, self.codigo.text(), fecha_entrada, int(self.cantidadDias.text()), None, False)

            QMessageBox.information(self, 'Información', 'La reservacion se ha adicionado correctamente.', QMessageBox.Ok, QMessageBox.Ok)
            self.cuandoGuarde.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)

    def actualizarReservacion(self):
        numero_identificacion_cliente = self.__obtenerCliente()
        numero_habitacion = self.__obtenerHabitacion()
        tipo_pago = self.__obtenerTipoPago()

        try:
            qtDate = self.fechaEntrada.date()
            fecha_entrada = datetime.strptime(str(qtDate.day()) + '-' + str(qtDate.month()) + '-' + str(qtDate.year()), '%d-%m-%Y')
            self.__presentador.actualizarReservacion(numero_identificacion_cliente, numero_habitacion, tipo_pago, self.codigo.text(), fecha_entrada, int(self.cantidadDias.text()), None, False, self.__indice)

            QMessageBox.information(self, 'Información', 'El reservacion se ha actualizado correctamente.', QMessageBox.Ok, QMessageBox.Ok)
            self.cuandoGuarde.emit()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e), QMessageBox.Ok, QMessageBox.Ok)

    def __obtenerCliente(self):
        if self.cliente.currentIndex() == -1:
            cliente = ''
        else:
            try:
                cliente = self.__presentador.obtenerCliente(self.cliente.currentIndex())
            except:
                cliente = ''

        return cliente

    def __obtenerHabitacion(self):
        if self.habitacion.currentIndex() == -1:
            habitacion = ''
        else:
            try:
                habitacion = self.presentador.obtenerHabitacion(self.habitacion.currentIndex())                
            except:
                habitacion = ''

        return habitacion

    def __obtenerTipoPago(self):
        if self.tipoPago.currentIndex() == -1:
            tipoPago = ''
        else:
            try:
                tipoPago = TIPOS_PAGO[self.tipoPago.currentIndex()]
            except:
                tipoPago = ''

        return tipoPago





