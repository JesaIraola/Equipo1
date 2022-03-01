from vistas.reservaciones_turoperador_ui import ReservacionesTuroperador

class PresentadorReservacionesTuroperador:
    def __init__(self, hotel):
        self.__hotel = hotel
        self.__vista = ReservacionesTuroperador(self)
        self.__turoperadores = []

    def iniciar(self):
        self.__vista.iniciar()

    def insertarTuroperadores(self):
        self.__turoperadores = []
        for tur in self.__hotel.turoperadores:
            try:
                index = self.__turoperadores.index(tur.codigo)
            except:
                self.__turoperadores.append(tur.codigo)
                self.__vista.turoperadores.insertItem(len(self.__turoperadores), tur.codigo)

    def calcularReservacionesTuroperador(self, indice):
        clientes = self.__hotel.reservacionesXTuroperador(self.__turoperadores[indice])
        self.__vista.limpiarListado()
        
        for clie in clientes:
            i = self.__vista.clientes.rowCount()
            self.__vista.clientes.insertRow(i)

            self.__vista.rellenarCelda(i, 0, clie['nombre'])
            self.__vista.rellenarCelda(i, 1, clie['fecha_entrada'].strftime("%d-%m-%Y"))

        self.__vista.clientes.resizeColumnsToContents()

