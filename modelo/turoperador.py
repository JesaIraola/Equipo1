class Turoperador:
    def __init__(self, nacionalidad, nombre, codigo):
        self.actualizar(nacionalidad, nombre, codigo)

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self,value):
        if value == None or not value:
            raise NameError('La nacionalidad es requerida')
        self.__nacionalidad=value.upper()

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value):
        if value == None or not value:
            raise NameError('El nombre del turoperador es requerido')
        self.__nombre=value

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,value):
        if value == None or not value:
            raise NameError('El código es requerido')
        self.__codigo=value.upper()

    def actualizar(self, nacionalidad, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.nacionalidad = nacionalidad


