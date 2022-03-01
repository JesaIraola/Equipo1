from vistas.listado_clientes_ui import ListadoClientes
from vistas.editar_cliente_ui import EditarCliente

class PresentadorListadoClientes:

    def __init__(self, hotel, presentadorPrincipal):
        self.__hotel = hotel
        self.__presentadorPrincipal = presentadorPrincipal
        self.__vista = ListadoClientes(self)

    def iniciar(self):
        self.__vista.iniciar()
        self.__rellenarFilas()

    def eliminarCliente(self, numero_identificacion):
        self.__hotel.eliminarCliente(numero_identificacion)
        self.__presentadorPrincipal.actualizarAcciones()
        self.__rellenarFilas()

    def mostrarActualizarCliente(self, indice):
        self.__vista_editar = EditarCliente(self, indice)
        self.__vista_editar.iniciarValores(
            self.__hotel.clientes[indice].nombre,
            self.__hotel.clientes[indice].numero_identificacion,
            self.__hotel.clientes[indice].edad,
            self.__hotel.clientes[indice].sexo,
            self.__hotel.clientes[indice].nacionalidad,
            self.__hotel.clientes[indice].visita_previa
        )

        self.__vista_editar.cuandoGuarde.connect(self.__rellenarFilas)
        self.__vista_editar.iniciar()

    def actualizarCliente(self, numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa, indice):
        self.__hotel.actualizarCliente(numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa, indice)

    def __rellenarFilas(self):
        self.__limpiarListado()

        for cliente in self.__hotel.clientes:
            i = self.__vista.listado.rowCount()

            self.__vista.listado.insertRow(i)

            self.__vista.rellenarCelda(i, 0, cliente.nombre)
            self.__vista.rellenarCelda(i, 1, cliente.numero_identificacion)
            self.__vista.rellenarCelda(i, 2, str(cliente.edad))
            self.__vista.rellenarCelda(i, 3, cliente.sexo)
            self.__vista.rellenarCelda(i, 4, cliente.nacionalidad)

            if (cliente.visita_previa):
                visitaPrevia = 'Si'
            else:
                visitaPrevia = 'No'

            self.__vista.rellenarCelda(i, 5, visitaPrevia)

        self.__vista.listado.resizeColumnsToContents()
        self.__vista.listado.setCurrentCell(-1, -1)

    def __limpiarListado(self):
        while self.__vista.listado.rowCount() > 0:
            self.__vista.listado.removeRow(0)

