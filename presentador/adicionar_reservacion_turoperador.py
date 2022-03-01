from presentador.adicionar_reservacion_recepcion import PresentadorAdicionarReservacionRecepcion

from vistas.editar_reservacion_turoperador_ui import EditarReservacionTuroperador
from vistas.editar_turoperador_ui import EditarTuroperador

class PresentadorAdicionarReservacionTuroperador(PresentadorAdicionarReservacionRecepcion):

    def __init__(self, hotel, presentadorPrincipal):
        PresentadorAdicionarReservacionRecepcion.__init__(self, hotel, presentadorPrincipal)

    def iniciar(self):
        self._PresentadorAdicionarReservacionRecepcion__vista = EditarReservacionTuroperador(self)
        self._PresentadorAdicionarReservacionRecepcion__vista.iniciar()

    def mostrarAdicionarTuroperador(self):
        self.__vistaAdicionarTuroperador = EditarTuroperador(self)
        self.__vistaAdicionarTuroperador.cuandoGuarde.connect(self.__turoperadorAdicionado)
        self.__vistaAdicionarTuroperador.iniciar()

    def adicionarTuroperador(self, nombre, codigo, nacionalidad):
        self._PresentadorAdicionarReservacionRecepcion__hotel.adicionarTuroperador(nacionalidad, nombre, codigo)
        self._PresentadorAdicionarReservacionRecepcion__presentadorPrincipal.actualizarAcciones()

    def insertarTuroperadores(self, codigo):
        indice = -1

        self._PresentadorAdicionarReservacionRecepcion__vista.turoperador.clear()

        for i in range(len(self._PresentadorAdicionarReservacionRecepcion__hotel.turoperadores)):
            self._PresentadorAdicionarReservacionRecepcion__vista.turoperador.insertItem(i, str(self._PresentadorAdicionarReservacionRecepcion__hotel.turoperadores[i].codigo))
            if self._PresentadorAdicionarReservacionRecepcion__hotel.turoperadores[i].codigo == codigo or indice == -1:
                indice = i

        self._PresentadorAdicionarReservacionRecepcion__vista.turoperador.setCurrentIndex(indice)

    def obtenerTuroperador(self, indice):
        return self._PresentadorAdicionarReservacionRecepcion__hotel.turoperadores[indice].codigo

    def __turoperadorAdicionado(self):
        self.insertarTuroperadores(self._PresentadorAdicionarReservacionRecepcion__hotel.turoperadores[-1].codigo)

