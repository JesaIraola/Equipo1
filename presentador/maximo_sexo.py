from vistas.maximo_sexo_ui import MaximoSexo

class PresentadorMaximoSexo:
    def __init__(self, hotel):
        self.__hotel = hotel
        self.__vista = MaximoSexo(self)

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

    def calcularMaximoSexo(self, indice):
        return self.__hotel.maxSexo(self.__nacionalidades[indice])


