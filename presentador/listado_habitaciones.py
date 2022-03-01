from vistas.listado_habitaciones_ui import ListadoHabitaciones
from vistas.editar_habitacion_ui import EditarHabitacion

class PresentadorListadoHabitaciones:
    def __init__(self, hotel):
        self.__hotel = hotel
        self.__vista = ListadoHabitaciones(self)

    def iniciar(self):
        self.__vista.iniciar()
        self.__rellenarFilas()

    def eliminarHabitacion(self, numero):
        self.__hotel.eliminarHabitacion(numero)
        self.__rellenarFilas()

    def mostrarActualizarHabitacion(self, indice):
        self.__vista_editar = EditarHabitacion(self, indice)
        self.__vista_editar.iniciarValores(
            self.__hotel.habitaciones[indice].numero,
            self.__hotel.habitaciones[indice].tipo,
            self.__hotel.habitaciones[indice].estilo,
            self.__hotel.habitaciones[indice].tiene_internet,
        )

        self.__vista_editar.cuandoGuarde.connect(self.__rellenarFilas)
        self.__vista_editar.iniciar()

    def actualizarHabitacion(self, numero, tipo, estilo, tiene_internet, indice):
        self.__hotel.actualizarHabitacion(numero, tipo, tiene_internet, estilo, indice)

    def __rellenarFilas(self):
        self.__limpiarListado()

        for habitacion in self.__hotel.habitaciones:
            i = self.__vista.listado.rowCount()

            self.__vista.listado.insertRow(i)

            self.__vista.rellenarCelda(i, 0, str(habitacion.numero))
            self.__vista.rellenarCelda(i, 1, habitacion.tipo)
            self.__vista.rellenarCelda(i, 2, habitacion.estilo)

            if (habitacion.tiene_internet):
                tieneInternet = 'Si'
            else:
                tieneInternet = 'No'

            self.__vista.rellenarCelda(i, 3, tieneInternet)
            self.__vista.rellenarCelda(i, 4, str(habitacion.costo()))

        self.__vista.listado.resizeColumnsToContents()
        self.__vista.listado.setCurrentCell(-1, -1)

    def __limpiarListado(self):
        while self.__vista.listado.rowCount() > 0:
            self.__vista.listado.removeRow(0)
