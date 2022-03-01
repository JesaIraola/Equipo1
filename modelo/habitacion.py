tipoHabitacion={'SIMPLE':1,'DOBLE':2,'TRIPLE':3,'SUITE':4}
estiloHabitacion={'ANTIGUA':1, 'MODERNA':2, 'NATURAL':3}

class Habitacion:
    def __init__(self, numero, tipo, tiene_internet, estilo):
        self.actualizar(numero, tipo, tiene_internet, estilo)

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        if not isinstance(value, int):
            raise TypeError('Número de habitación [' + str(value) + '] incorrecto: use un valor numérico entero')
        self.__numero=value

    @property
    def tipo (self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        if value == None or not value:
            raise NameError('El tipo de habitación es requerido')
        elif tipoHabitacion.get(value)==None:
            raise TypeError('Tipo de Habitación [' + value + '] es incorrecto: use SIMPLE, DOBLE, TRIPLE o SUITE.')
        self.__tipo=value

    @property
    def tiene_internet (self):
        return self.__tiene_internet

    @tiene_internet.setter
    def tiene_internet(self, value):
        if not isinstance(value, bool):
            raise TypeError('El uso de internet es incorrecto: use un valor lógico')
        self.__tiene_internet=value

    @property
    def estilo (self):
        return self.__estilo

    @estilo.setter
    def estilo(self, value):
        if value == None or not value:
            raise NameError('El estilo de habitación es requerido')
        elif estiloHabitacion.get(value)==None:
            raise TypeError('Estilo de Habitación [' + value + '] es incorrecto: use ANTIGUA, MODERNA o NATURAL.')
        self.__estilo=value

    def costo(self):
        costos={'SIMPLE':15,'DOBLE':25,'TRIPLE':40,'SUITE':60}
        costo=costos.get(self.__tipo)
        if self.__tiene_internet:
            costo += 20

        return costo

    def actualizar(self, numero, tipo, tiene_internet, estilo):
        self.numero = numero
        self.tipo = tipo
        self.tiene_internet = tiene_internet
        self.estilo = estilo
