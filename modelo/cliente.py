tipoSexo={'F':1, 'M':2}

class Cliente:
    def __init__(self, numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa):
        self.actualizar(numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa)

    @property
    def numero_identificacion(self):
        return self.__numero_identificacion

    @numero_identificacion.setter
    def numero_identificacion(self,value):
        if value == None or not value:
            raise NameError('El número de identificación es requerido')
        self.__numero_identificacion=value.upper()

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,value):
        if value == None or not value:
            raise NameError('El nombre del cliente es requerido')
        self.__nombre=value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,value):
        if not isinstance(value, int):
            raise TypeError('Edad [' + str(value) + '] incorrecta: use un valor numérico entero')
        self.__edad=value

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self,value):
        if value == None or not value:
            raise NameError('El sexo del cliente es requerido')
        elif tipoSexo.get(value)==None:
            raise TypeError('Sexo [' + value + '] incorrecto: use F para femenino o M para masculino')
        self.__sexo=value

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self,value):
        if value ==None or not value:
            raise TypeError('La nacionalidad es requerida')
        self.__nacionalidad=value.upper()

    @property
    def visita_previa(self):
        return self.__visita_previa

    @visita_previa.setter
    def visita_previa(self,value):
        if not isinstance(value, bool):
            raise TypeError('La visita previa es incorrecta: use un valor lógico')
        self.__visita_previa=value

    def actualizar(self, numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa):
        self.nombre = nombre
        self.numero_identificacion = numero_identificacion
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad
        self.visita_previa = visita_previa


