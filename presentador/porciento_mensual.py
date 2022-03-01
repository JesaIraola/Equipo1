from vistas.porciento_mensual_ui import PorcientoMensual

class PresentadorPorcientoMensual:
    def __init__(self, hotel):
        self.__hotel = hotel
        self.__vista = PorcientoMensual(self)
        self.__nacionalidades = []

    def iniciar(self):
        self.__vista.iniciar()

    def insertarNacionalidades(self):
        self.__nacionalidades = []
        self.__vista.nacionalidades.clear()
        
        for clie in self.__hotel.clientes:
            try:
                index = self.__nacionalidades.index(clie.nacionalidad)
            except:
                self.__nacionalidades.append(clie.nacionalidad)
                self.__vista.nacionalidades.insertItem(len(self.__nacionalidades), clie.nacionalidad)

    def calcularPorciento(self, indice):
        return self.__hotel.porcientoMensual(self.__nacionalidades[indice])

