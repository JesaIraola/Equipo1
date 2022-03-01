from vistas.listado_reservaciones_ui import ListadoReservaciones
from vistas.editar_reservacion_recepcion_ui import EditarReservacionRecepcion
from vistas.editar_reservacion_turoperador_ui import EditarReservacionTuroperador
from vistas.editar_cliente_ui import EditarCliente
from vistas.editar_habitacion_ui import EditarHabitacion
from vistas.editar_turoperador_ui import EditarTuroperador

class PresentadorListadoReservaciones:

    def __init__(self, hotel, presentadorPrincipal):
        self.__hotel = hotel
        self.__presentadorPrincipal = presentadorPrincipal
        self.__vista = ListadoReservaciones(self)

    def iniciar(self):
        self.__vista.iniciar()
        self.__rellenarFilas()

    def eliminarReservacion(self, codigo):
        self.__hotel.eliminarReservacion(codigo)
        self.__rellenarFilas()

    def mostrarActualizarReservacion(self, indice):

        if self.__hotel.reservaciones[indice].turoperador == None:
            self.__vista_editar = EditarReservacionRecepcion(self, indice)
            self.__vista_editar.iniciar()
            self.__vista_editar.iniciarValores(
                self.__hotel.reservaciones[indice].cliente.numero_identificacion, 
                self.__hotel.reservaciones[indice].habitacion.numero, 
                self.__hotel.reservaciones[indice].tipo_pago, 
                self.__hotel.reservaciones[indice].codigo, 
                self.__hotel.reservaciones[indice].fecha_entrada, 
                self.__hotel.reservaciones[indice].cantidad_dias
            )
        else:
            self.__vista_editar = EditarReservacionTuroperador(self, indice)
            self.__vista_editar.iniciar()
            self.__vista_editar.iniciarValores(
                self.__hotel.reservaciones[indice].cliente.numero_identificacion, 
                self.__hotel.reservaciones[indice].habitacion.numero, 
                self.__hotel.reservaciones[indice].tipo_pago, 
                self.__hotel.reservaciones[indice].codigo, 
                self.__hotel.reservaciones[indice].fecha_entrada, 
                self.__hotel.reservaciones[indice].cantidad_dias,
                self.__hotel.reservaciones[indice].turoperador,
                self.__hotel.reservaciones[indice].es_tour
            )
            
        self.__vista_editar.cuandoGuarde.connect(self.__rellenarFilas)

    def actualizarReservacion(self, numero_identificacion_cliente, numero_habitacion, tipo_pago, codigo, fecha_entrada, cantidad_dias, codigo_turoperador, es_tour, indice):
        self.__hotel.actualizarReservacion(numero_identificacion_cliente, codigo, numero_habitacion, fecha_entrada, cantidad_dias, tipo_pago, codigo_turoperador, es_tour, indice)

    def mostrarAdicionarCliente(self):
        self.__vistaAdicionarCliente = EditarCliente(self)
        self.__vistaAdicionarCliente.cuandoGuarde.connect(self.__clienteAdicionado)
        self.__vistaAdicionarCliente.iniciar()

    def adicionarCliente(self, numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa):
        self.__hotel.adicionarCliente(numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa)
        self.__presentadorPrincipal.actualizarAcciones()

    def insertarClientes(self, numero_identificacion):
        indice = -1

        self.__vista_editar.cliente.clear()

        for i in range(len(self.__hotel.clientes)):
            self.__vista_editar.cliente.insertItem(i, self.__hotel.clientes[i].nombre + " - " + self.__hotel.clientes[i].numero_identificacion)
            if self.__hotel.clientes[i].numero_identificacion == numero_identificacion or indice == -1:
                indice = i

        self.__vista_editar.cliente.setCurrentIndex(indice)

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

        self.__vista_editar.habitacion.clear()

        for i in range(len(self.__hotel.habitaciones)):
            self.__vista_editar.habitacion.insertItem(i, str(self.__hotel.habitaciones[i].numero))
            if self.__hotel.habitaciones[i].numero == numero or indice == -1:
                indice = i

        self.__vista_editar.habitacion.setCurrentIndex(indice)

    def obtenerHabitacion(self, indice):
        return self.__hotel.habitaciones[indice].numero

    def mostrarAdicionarTuroperador(self):
        self.__vistaAdicionarTuroperador = EditarTuroperador(self)
        self.__vistaAdicionarTuroperador.cuandoGuarde.connect(self.__turoperadorAdicionado)
        self.__vistaAdicionarTuroperador.iniciar()

    def adicionarTuroperador(self, nombre, codigo, nacionalidad):
        self.__hotel.adicionarTuroperador(nacionalidad, nombre, codigo)
        self.__presentadorPrincipal.actualizarAcciones()

    def insertarTuroperadores(self, codigo):
        indice = -1

        self.__vista_editar.turoperador.clear()

        for i in range(len(self.__hotel.turoperadores)):
            self.__vista_editar.turoperador.insertItem(i, str(self.__hotel.turoperadores[i].codigo))
            if self.__hotel.turoperadores[i].codigo == codigo or indice == -1:
                indice = i

        self.__vista_editar.turoperador.setCurrentIndex(indice)

    def obtenerTuroperador(self, indice):
        return self._hotel.turoperadores[indice].codigo

    def __rellenarFilas(self):
        self.__limpiarListado()

        for res in self.__hotel.reservaciones:
            i = self.__vista.listado.rowCount()

            self.__vista.listado.insertRow(i)

            self.__vista.rellenarCelda(i, 0, res.codigo)
            self.__vista.rellenarCelda(i, 1, res.cliente.nombre + " - " + str(res.cliente.numero_identificacion))
            self.__vista.rellenarCelda(i, 2, str(res.habitacion.numero))
            self.__vista.rellenarCelda(i, 3, res.fecha_entrada.strftime("%d-%m-%Y"))
            self.__vista.rellenarCelda(i, 4, str(res.cantidad_dias))
            self.__vista.rellenarCelda(i, 5, str(res.tipo_pago))

            if res.turoperador:
                turoperador = res.turoperador.codigo
            else:
                turoperador = ''
            self.__vista.rellenarCelda(i, 6, turoperador)

            if res.es_tour:
                esTour = 'Si'
            else:
                esTour = 'No'
            self.__vista.rellenarCelda(i, 7, esTour)

            self.__vista.rellenarCelda(i, 8, str(res.costo()))

        self.__vista.listado.resizeColumnsToContents()
        self.__vista.listado.setCurrentCell(-1, -1)

    def __limpiarListado(self):
        while self.__vista.listado.rowCount() > 0:
            self.__vista.listado.removeRow(0)

    def __clienteAdicionado(self):
        self.insertarClientes(self.__hotel.clientes[-1].numero_identificacion)

    def __habitacionAdicionada(self):
        self.insertarHabitaciones(self.__hotel.habitaciones[-1].numero)

    def __turoperadorAdicionado(self):
        self.insertarTuroperadores(self._PresentadorAdicionarReservacionRecepcion__hotel.turoperadores[-1].codigo)

