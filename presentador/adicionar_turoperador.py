from vistas.editar_turoperador_ui import EditarTuroperador

class PresentadorAdicionarTuroperador:

    def __init__(self, hotel, presentadorPrincipal):
        self.__hotel = hotel
        self.__vista = EditarTuroperador(self)
        self.__presentadorPrincipal = presentadorPrincipal

    def iniciar(self):
        self.__vista.iniciar()

    def adicionarTuroperador(self, nombre, codigo, nacionalidad):
        self.__hotel.adicionarTuroperador(nacionalidad, nombre, codigo)
        self.__presentadorPrincipal.actualizarAcciones()

