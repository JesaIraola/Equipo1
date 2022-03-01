from vistas.listado_turoperadores_ui import ListadoTuroperadores
from vistas.editar_turoperador_ui import EditarTuroperador

class PresentadorListadoTuroperadores:

    def __init__(self, hotel, presentadorPrincipal):
        self.__hotel = hotel
        self.__presentadorPrincipal = presentadorPrincipal
        self.__vista = ListadoTuroperadores(self)

    def iniciar(self):
        self.__vista.iniciar()
        self.__rellenarFilas()

    def eliminarTuroperador(self, codigo):
        self.__hotel.eliminarTuroperador(codigo)
        self.__presentadorPrincipal.actualizarAcciones()
        self.__rellenarFilas()

    def mostrarActualizarTuroperador(self, indice):
        self.__vista_editar = EditarTuroperador(self, indice)
        self.__vista_editar.iniciarValores(
            self.__hotel.turoperadores[indice].nombre,
            self.__hotel.turoperadores[indice].codigo,
            self.__hotel.turoperadores[indice].nacionalidad
        )

        self.__vista_editar.cuandoGuarde.connect(self.__rellenarFilas)
        self.__vista_editar.iniciar()

    def actualizarTuroperador(self, nombre, codigo, nacionalidad, indice):
        self.__hotel.actualizarTuroperador(nacionalidad, nombre, codigo, indice)

    def __rellenarFilas(self):
        self.__limpiarListado()

        for turoperador in self.__hotel.turoperadores:
            i = self.__vista.listado.rowCount()

            self.__vista.listado.insertRow(i)

            self.__vista.rellenarCelda(i, 0, turoperador.nombre)
            self.__vista.rellenarCelda(i, 1, turoperador.codigo)
            self.__vista.rellenarCelda(i, 2, turoperador.nacionalidad)

        self.__vista.listado.resizeColumnsToContents()
        self.__vista.listado.setCurrentCell(-1, -1)

    def __limpiarListado(self):
        while self.__vista.listado.rowCount() > 0:
            self.__vista.listado.removeRow(0)

