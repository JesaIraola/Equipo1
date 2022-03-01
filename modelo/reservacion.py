from modelo.cliente import Cliente
from modelo.habitacion import Habitacion
from modelo.turoperador import Turoperador
from datetime import datetime

tipoPago={'TARJETA MAGNETICA':1, 'EFECTIVO':2}

class Reservacion:
    def __init__(self, cliente, codigo, habitacion, fecha_entrada, cantidad_dias, tipo_pago, turoperador, es_tour):
        self.actualizar(cliente, codigo, habitacion, fecha_entrada, cantidad_dias, tipo_pago, turoperador, es_tour)
        self.fecha = datetime.now()

    @property
    def cliente (self):
        return self.__cliente

    @cliente.setter
    def cliente(self, value):
        if not isinstance(value, Cliente):
            raise TypeError('El cliente tiene que ser una instancia de la clase Cliente')
        self.__cliente=value

    @property
    def codigo (self):
        return self.__codigo

    @codigo.setter
    def codigo(self, value):
        if value==None or not value:
            raise TypeError('El codigo de la reservación es requerido')
        self.__codigo=value.upper()

    @property
    def habitacion (self):
        return self.__habitacion

    @habitacion.setter
    def habitacion(self, value):
        if not isinstance(value, Habitacion):
            raise TypeError('La habitación tiene que ser una instancia de la clase Habitación')
        self.__habitacion=value

    @property
    def fecha_entrada (self):
        return self.__fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, value):
        if not isinstance(value, datetime):
            raise TypeError('La fecha tiene que ser una instancia de la clase datetime')
        self.__fecha_entrada=value

    @property
    def cantidad_dias (self):
        return self.__cantidad_dias

    @cantidad_dias.setter
    def cantidad_dias(self, value):
        if not isinstance(value, int):
            raise TypeError('La cantidad de días [' + str(value) + '] es incorrecta: use un valor numérico entero')
        self.__cantidad_dias=value

    @property
    def tipo_pago (self):
        return self.__tipo_pago

    @tipo_pago.setter
    def tipo_pago(self, value):
        if value == None or not value:
            raise NameError('El tipo de pago es requerido')
        elif tipoPago.get(value)==None:
            raise TypeError('El tipo de pago ' + value + ' es incorrecto: use TARJETA MAGNETICA o EFECTIVO')
        self.__tipo_pago=value

    @property
    def turoperador (self):
        return self.__turoperador

    @turoperador.setter
    def turoperador(self, value):
        if not value == None and not isinstance(value, Turoperador):
            raise TypeError('El turoperador tiene que ser una instancia de la clase Turoperador')
        self.__turoperador=value

    @property
    def es_tour (self):
        return self.__es_tour

    @es_tour.setter
    def es_tour(self, value):
        if not isinstance(value, bool):
            raise TypeError('El es_tour es incorrecto: use un valor lógico')
        elif value and self.__turoperador==None:
            raise  TypeError('Solo las reservaciones con turoperadores aceptan tour')
        self.__es_tour=value

    def costo(self):
        costo = self.habitacion.costo()

        if self.turoperador != None:
            costo = costo + 15
            if self.es_tour:
                costo = costo - 3

        if self.tipo_pago == 'TARJETA MAGNETICA':
            costo = costo - costo * 5 / 100

        return costo

    def actualizar(self, cliente, codigo, habitacion, fecha_entrada, cantidad_dias, tipo_pago, turoperador, es_tour):
        self.cliente=cliente
        self.habitacion=habitacion
        self.turoperador=turoperador
        self.es_tour=es_tour
        self.tipo_pago=tipo_pago
        self.codigo=codigo
        self.fecha_entrada=fecha_entrada
        self.cantidad_dias=cantidad_dias
