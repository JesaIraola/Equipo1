from vistas.editar_reservacion_recepcion_ui import EditarReservacionRecepcion
from vistas.editar_cliente_ui import EditarCliente
from vistas.editar_habitacion_ui import EditarHabitacion

class PresentadorAdicionarReservacionRecepcion:

    def __init__(self, hotel, presentadorPrincipal):
        self.__hotel = hotel
        self.__presentadorPrincipal = presentadorPrincipal

    def iniciar(self):
        self.__vista = EditarReservacionRecepcion(self)
        self.__vista.iniciar()

    def adicionarReservacion(self, numero_identificacion_cliente, numero_habitacion, tipo_pago, codigo, fecha_entrada, cantidad_dias, codigo_turoperador, es_tour):
        self.__hotel.adicionarReservacion(numero_identificacion_cliente, codigo, numero_habitacion, fecha_entrada, cantidad_dias, tipo_pago, codigo_turoperador, es_tour)

    def mostrarAdicionarCliente(self):
        self.__vistaAdicionarCliente = EditarCliente(self)
        self.__vistaAdicionarCliente.cuandoGuarde.connect(self.__clienteAdicionado)
        self.__vistaAdicionarCliente.iniciar()

    def adicionarCliente(self, numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa):
        self.__hotel.adicionarCliente(numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa)
        self.__presentadorPrincipal.actualizarAcciones()

    def insertarClientes(self, numero_identificacion):
        indice = -1

        self.__vista.cliente.clear()

        for i in range(len(self.__hotel.clientes)):
            self.__vista.cliente.insertItem(i, self.__hotel.clientes[i].nombre + " - " + self.__hotel.clientes[i].numero_identificacion)
            if self.__hotel.clientes[i].numero_identificacion == numero_identificacion or indice == -1:
                indice = i

        self.__vista.cliente.setCurrentIndex(indice)

    def obtenerCliente(self, indice):
        return self.__hotel.clientes[indice].numero_identificacion

    def mostrarAdicionarHabitacion(self):
        self.__vistaAdicionarHabitacion = EditarHabitacion(self)
        self.__vistaAdicionarHabitacion.cuandoGuarde.connect(self.__habitacionAdicionada)
        self.__vistaAdicionarHabitacion.iniciar()

    def adicionarHabitacion(self, numero, tipo, estilo, tiene_internet):
        self.__hotel.adicionarHabitacion(numero, tipo, tiene_internet, estilo)

    def insertarHabitaciones(self, numero):
        indice = -1

        self.__vista.habitacion.clear()

        for i in range(len(self.__hotel.habitaciones)):
            self.__vista.habitacion.insertItem(i, str(self.__hotel.habitaciones[i].numero))
            if self.__hotel.habitaciones[i].numero == numero or indice == -1:
                indice = i

        self.__vista.habitacion.setCurrentIndex(indice)

    def obtenerHabitacion(self, indice):
        return self.__hotel.habitaciones[indice].numero

    def __clienteAdicionado(self):
        self.insertarClientes(self.__hotel.clientes[-1].numero_identificacion)

    def __habitacionAdicionada(self):
        self.insertarHabitaciones(self.__hotel.habitaciones[-1].numero)






