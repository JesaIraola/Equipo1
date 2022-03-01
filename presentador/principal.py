import sys
from datetime import datetime, timedelta
from PyQt5.QtWidgets import QApplication

from modelo.hotel import Hotel
from vistas.ventana_ui import Ventana

from presentador.adicionar_cliente import PresentadorAdicionarCliente
from presentador.listado_clientes import PresentadorListadoClientes
from presentador.adicionar_habitacion import PresentadorAdicionarHabitacion
from presentador.listado_habitaciones import PresentadorListadoHabitaciones
from presentador.adicionar_turoperador import PresentadorAdicionarTuroperador
from presentador.listado_turoperadores import PresentadorListadoTuroperadores
from presentador.adicionar_reservacion_recepcion import PresentadorAdicionarReservacionRecepcion
from presentador.adicionar_reservacion_turoperador import PresentadorAdicionarReservacionTuroperador
from presentador.listado_reservaciones import PresentadorListadoReservaciones
from presentador.porciento_mensual import PresentadorPorcientoMensual
from presentador.maximo_clientes import PresentadorMaximoClientes
from presentador.maximo_sexo import PresentadorMaximoSexo
from presentador.reservaciones_turoperador import PresentadorReservacionesTuroperador

class PresentadorPrincipal:
    def __init__(self):
        self.__hotel = Hotel()

    @property
    def clientes(self):
        return self.__hotel.clientes

    @property
    def habitaciones(self):
        return self.__hotel.habitaciones

    @property
    def turoperadores(self):
        return self.__hotel.turoperadores

    @property
    def reservaciones(self):
        return self.__hotel.reservaciones

    def iniciar(self):
        app = QApplication(sys.argv)
        self.__vista = Ventana(self)
        self.__vista.iniciar()
        app.exec()

    def actualizarAcciones(self):
        self.__vista.actualizarAcciones()

    # clientes
    def mostrarAdicionarCliente(self):
        presentador = PresentadorAdicionarCliente(self.__hotel, self)
        presentador.iniciar()

    def mostrarListadoClientes(self):
        presentador = PresentadorListadoClientes(self.__hotel, self)
        presentador.iniciar()

    # habitaciones
    def mostrarAdicionarHabitacion(self):
        presentador = PresentadorAdicionarHabitacion(self.__hotel)
        presentador.iniciar()

    def mostrarListadoHabitaciones(self):
        presentador = PresentadorListadoHabitaciones(self.__hotel)
        presentador.iniciar()

    # turoperadores
    def mostrarAdicionarTuroperador(self):
        presentador = PresentadorAdicionarTuroperador(self.__hotel, self)
        presentador.iniciar()

    def mostrarListadoTuroperadores(self):
        presentador = PresentadorListadoTuroperadores(self.__hotel, self)
        presentador.iniciar()

    # reservaciones 
    def mostrarListadoReservaciones(self):
        presentador = PresentadorListadoReservaciones(self.__hotel, self)
        presentador.iniciar()

    # reservaciones reception
    def mostrarAdicionarReservacionRecepcion(self):
        presentador = PresentadorAdicionarReservacionRecepcion(self.__hotel, self)
        presentador.iniciar()

    # reservaciones turoperador
    def mostrarAdicionarReservacionTuroperador(self):
        presentador = PresentadorAdicionarReservacionTuroperador(self.__hotel, self)
        presentador.iniciar()

    # consultas auxiliares
    def mostrarPorcientoMensual(self):
        presentador = PresentadorPorcientoMensual(self.__hotel)
        presentador.iniciar()

    def mostrarMaximoClientes(self):
        presentador = PresentadorMaximoClientes(self.__hotel)
        presentador.iniciar()

    def mostrarMaximoSexo(self):
        presentador = PresentadorMaximoSexo(self.__hotel)
        presentador.iniciar()

    def mostrarReservacionesTuroperador(self):
        presentador = PresentadorReservacionesTuroperador(self.__hotel)
        presentador.iniciar()
