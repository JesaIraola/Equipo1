from vistas.editar_cliente_ui import EditarCliente

class PresentadorAdicionarCliente:

    def __init__(self, hotel, presentadorPrincipal):
        self.__hotel = hotel
        self.__vista = EditarCliente(self)
        self.__presentadorPrincipal = presentadorPrincipal

    def iniciar(self):
        self.__vista.iniciar()

    def adicionarCliente(self, numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa):
        self.__hotel.adicionarCliente(numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa)
        self.__presentadorPrincipal.actualizarAcciones()

