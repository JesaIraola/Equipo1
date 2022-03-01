from modelo.habitacion import Habitacion
from modelo.turoperador import Turoperador
from modelo.reservacion import Reservacion
from modelo.cliente import Cliente
from datetime import datetime, timedelta

HORA_ENTRADA='14:00'
HORA_SALIDA='09:00'

class Hotel:
    def __init__(self):
        self.__habitaciones=[]
        self.__turoperadores=[]
        self.__reservaciones=[]
        self.__clientes=[]

    @property
    def habitaciones(self):
        return self.__habitaciones

    @property
    def turoperadores(self):
        return self.__turoperadores

    @property
    def reservaciones(self):
        return self.__reservaciones

    @property
    def clientes(self):
        return self.__clientes

    def adicionarHabitacion(self, numero, tipo, tiene_internet, estilo):
        if self.obtenerHabitacionXNumero(numero) != None:
            raise IndexError('La habitación con número ' + str(numero) + ' ya está previamente registrada en el hotel')
        else:
            hab=Habitacion(numero, tipo, tiene_internet, estilo)
            self.__habitaciones.append(hab)

    def adicionarTuroperador(self, nacionalidad, nombre, codigo):
        if self.obtenerTuroperadoresXCodigo(codigo) != None:
            raise IndexError('El turoperador con código ' + str(codigo) + ' ya está previamente registrado en el hotel')
        elif len([tur for tur in self.__turoperadores if tur.nombre == nombre]) > 0:
            raise IndexError('El turoperador con nombre ' + str(nombre) + ' ya está previamente registrado en el hotel')
        else:
            turoperador = Turoperador(nacionalidad, nombre, codigo)
            self.__turoperadores.append(turoperador)

    def adicionarCliente(self, numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa):
        if self.obtenerClienteXNumero(numero_identificacion) != None:
            raise IndexError('El cliente con número de identificación ' + str(numero_identificacion) + ' ya está previamente registrado en el hotel')
        else:
            cliente = Cliente(numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa)
            self.__clientes.append(cliente)

    def adicionarReservacion(self, numero_identificacion_cliente, codigo, numero_habitacion, fecha_entrada, cantidad_dias, tipo_pago, codigo_turoperador, es_tour):
        if self.obtenerReservacionesXCodigo(codigo) != None:
            raise IndexError('La reservación con código ' + str(codigo) + ' ya está previamente registrada en el hotel')

        if numero_habitacion == None or not numero_habitacion:
            raise IndexError('El número de la habitación es requerido')

        hab = self.obtenerHabitacionXNumero(numero_habitacion)
        if hab == None:
            raise IndexError('La habitación con número ' + str(numero_habitacion) + ' no existe en el hotel')
        elif not self.__tieneCapacidad(hab, fecha_entrada, cantidad_dias):
            raise TypeError('El hotel no tiene capacidad en la habitación ' + str(numero_habitacion) + ' en la fecha solicitada')

        if numero_identificacion_cliente == None or not numero_identificacion_cliente:
            raise IndexError('El número de identificación del cliente es requerido')

        clie = self.obtenerClienteXNumero(numero_identificacion_cliente)
        if clie == None:
            raise IndexError('El cliente con número de identificación ' + str(numero_identificacion_cliente) + ' no está asociado al hotel')

        if codigo_turoperador == None:
            turoperador = None
        else:
            turoperador = self.obtenerTuroperadoresXCodigo(codigo_turoperador)
            if turoperador == None:
                raise IndexError('El turoperador con código ' + str(codigo_turoperador) + ' no está asociado al hotel')

        res = Reservacion(clie, codigo, hab, fecha_entrada, cantidad_dias, tipo_pago, turoperador, es_tour)
        self.__reservaciones.append(res)

    def actualizarHabitacion(self, numero, tipo, tiene_internet, estilo, indice):
        if len(self.__habitaciones) == 0 or indice >= len(self.__habitaciones):
            raise IndexError('La habitación a actualizar tiene que existir en el hotel')
        elif len([i for i in range(len(self.__habitaciones)) if self.__habitaciones[i].numero == numero and indice != i]) > 0:
            raise IndexError('La habitación con número ' + str(numero) + ' ya está previamente registrada en el hotel')
        else:
            self.__habitaciones[indice].actualizar(numero, tipo, tiene_internet, estilo)

    def actualizarTuroperador(self, nacionalidad, nombre, codigo, indice):
        if len(self.__turoperadores) == 0 or indice >= len(self.__turoperadores):
            raise IndexError('El turoperador a actualizar tiene que existir en el hotel')
        elif len([i for i in range(len(self.__turoperadores)) if self.__turoperadores[i].codigo == codigo.upper() and indice != i]) > 0:
            raise IndexError('El turoperador con código ' + str(codigo) + ' ya está previamente registrado en el hotel')
        elif len([i for i in range(len(self.__turoperadores)) if self.__turoperadores[i].nombre == nombre and indice != i]) > 0:
            raise IndexError('El turoperador con nombre ' + str(nombre) + ' ya está previamente registrado en el hotel')
        else:
            self.__turoperadores[indice].actualizar(nacionalidad, nombre, codigo)

    def actualizarCliente(self, numero_identificacion, nombre, edad, sexo, nacionalidad,visita_previa, indice):
        if len(self.__clientes) == 0 or indice >= len(self.__clientes):
            raise IndexError('El cliente a actualizar tiene que existir en el hotel')
        elif len([i for i in range(len(self.__clientes)) if self.__clientes[i].numero_identificacion == numero_identificacion.upper() and indice != i]) > 0:
            raise IndexError('El cliente con número de identificación ' + str(numero_identificacion) + ' ya está previamente registrado en el hotel')
        else:
            self.__clientes[indice].actualizar(numero_identificacion, nombre, edad, sexo, nacionalidad, visita_previa)

    def actualizarReservacion(self, numero_identificacion_cliente, codigo, numero_habitacion, fecha_entrada, cantidad_dias, tipo_pago, codigo_turoperador, es_tour, indice):
        if len(self.__reservaciones) == 0 or indice >= len(self.__reservaciones):
            raise IndexError('La reservación a actualizar tiene que existir en el hotel')
        elif len([i for i in range(len(self.__reservaciones)) if self.__reservaciones[i].codigo == codigo.upper() and indice != i]) > 0:
            raise IndexError('La reservación con código ' + str(codigo) + ' ya está previamente registrada en el hotel')
        else:
            hab = self.obtenerHabitacionXNumero(numero_habitacion)
            if hab == None:
               raise IndexError('La habitación con número ' + str(numero_habitacion) + ' no existe en el hotel')
            elif not self.__tieneCapacidad(hab, fecha_entrada, cantidad_dias, indice):
                raise TypeError('El hotel no tiene capacidad en la habitación ' + str(numero_habitacion) + ' en la fecha solicitada')

            clie = self.obtenerClienteXNumero(numero_identificacion_cliente)
            if clie == None:
                raise TypeError('El cliente con número de identificación ' + str(numero_identificacion_cliente) + ' no está asociado al hotel')

            if codigo_turoperador == None:
                turoperador = None
            else:
                turoperador = self.obtenerTuroperadoresXCodigo(codigo_turoperador)
                if turoperador == None:
                    raise TypeError('El turoperador con código ' + str(codigo_turoperador) + ' no está asociado al hotel')

        self.__reservaciones[indice].actualizar(clie, codigo, hab, fecha_entrada, cantidad_dias, tipo_pago, turoperador, es_tour)

    def eliminarReservacion(self, codigo):
        self.__reservaciones = [res for res in self.__reservaciones if res.codigo != codigo.upper()]
        return self.__reservaciones

    def eliminarHabitacion(self, numero):
        reservacionesExistentes = [self.__reservaciones[i].codigo for i in range(len(self.__reservaciones)) if self.__reservaciones[i].habitacion.numero == numero]
        for codigo in reservacionesExistentes:
            self.eliminarReservacion(codigo)

        self.__habitaciones = [hab for hab in self.__habitaciones if hab.numero != numero]
        return self.__habitaciones

    def eliminarTuroperador(self, codigo):
        reservacionesExistentes = [self.__reservaciones[i].codigo for i in range(len(self.__reservaciones)) if self.__reservaciones[i].turoperador != None and self.__reservaciones[i].turoperador.codigo == codigo.upper()]
        for cod in reservacionesExistentes:
            self.eliminarReservacion(cod)

        self.__turoperadores = [tur for tur in self.__turoperadores if tur.codigo != codigo.upper()]
        return self.__turoperadores

    def eliminarCliente(self, numero_identificacion):
        reservacionesExistentes = [self.__reservaciones[i].codigo for i in range(len(self.__reservaciones)) if self.__reservaciones[i].cliente != None and self.__reservaciones[i].cliente.numero_identificacion == numero_identificacion.upper()]
        for codigo in reservacionesExistentes:
            self.eliminarReservacion(codigo)

        self.__clientes = [clie for clie in self.__clientes if clie.numero_identificacion != numero_identificacion.upper()]
        return self.__clientes

    def costoReservacion(self, codigo):
        reservaciones = [res for res in self.__reservaciones if res.codigo == codigo.upper()]
        if len(reservaciones) == 0:
            raise IndexError('No existe reservación con el código: ' + str(codigo))

        return reservaciones[0].costo()

    def porcientoMensual(self, nacionalidad):
        if len(self.__reservaciones) == 0:
            return  0

        hoy = datetime.now()
        reservaciones = [res for res in self.__reservaciones if res.turoperador == None and res.cliente.nacionalidad == nacionalidad and res.fecha.month == hoy.month and res.fecha.year == hoy.year]
        return len(reservaciones) * 100 / len(self.__reservaciones)

    def maxClientes(self, nacionalidad):
        hoy = datetime.now()
        max = None
        maxMes = None
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        reservaciones = [res for res in self.__reservaciones if res.fecha_entrada.year == hoy.year - 1 and res.cliente.nacionalidad == nacionalidad]
        for mes in range(12):
            clientes = []
            for res in reservaciones:
                if res.fecha_entrada.month == mes + 1:
                    clientes.append(res.cliente.numero_identificacion)
            if max == None or len(clientes) > max:
                max = len(clientes)
                maxMes = meses[mes]

        if max == 0:
            return 'No existen reservaciones de clientes de la nacionalidad ' +str(nacionalidad) + ' en el año anterior'
        else:
            return 'El mes con más clientes de la nacionalidad ' + str(nacionalidad) + ' en el año anterior es: ' + str(maxMes)

    def maxSexo(self, nacionalidad):
        hoy = datetime.now()
        max = None
        maxSexo = None
        sexos = [{'nombre': 'Femenino', 'sigla': 'F'}, {'nombre': 'Masculino', 'sigla': 'M'}]
        reservaciones = [res for res in self.__reservaciones if res.fecha_entrada.year == hoy.year and res.cliente.nacionalidad == nacionalidad]
        for sexo in sexos:
            reservacionesXSexo = [res for res in reservaciones if res.cliente.sexo ==sexo['sigla']]

            if max == None or len(reservacionesXSexo) > max:
                max = len(reservacionesXSexo)
                maxSexo = sexo['nombre']

        if max == 0:
            return 'No existen reservaciones de clientes de la nacionalidad ' +str(nacionalidad) + ' en el año actual'
        else:
            return 'El sexo con más clientes de la nacionalidad ' + str(nacionalidad) + ' en el presente año es: ' + str(maxSexo)

    def reservacionesXTuroperador(self, codigo):
        reservaciones = [res for res in self.__reservaciones if res.turoperador != None and res.turoperador.codigo == codigo.upper()]
        clientes = []
        for res in reservaciones:
            clientes.append({'nombre': res.cliente.nombre, 'fecha_entrada': res.fecha_entrada})

        for i in range(len(clientes) - 1):
            for j in range(i + 1, len(clientes)):
                if clientes[i]['fecha_entrada'] > clientes[j]['fecha_entrada']:
                    c = clientes[i]
                    clientes[i] = clientes[j]
                    clientes[j] = c

        return clientes

    def obtenerClienteXNumero(self, numero_identificacion):
        clientes = [clie for clie in self.__clientes if clie.numero_identificacion == numero_identificacion.upper()]
        if len(clientes) > 0:
            return clientes[0]
        else:
            return None

    def obtenerHabitacionXNumero(self, numero):
        habitaciones = [hab for hab in self.__habitaciones if hab.numero == numero]
        if len(habitaciones) > 0:
            return habitaciones[0]
        else:
            return None

    def obtenerTuroperadoresXCodigo(self, codigo):
        turoperadores = [tur for tur in self.__turoperadores if tur.codigo == codigo.upper()]
        if len(turoperadores) > 0:
            return turoperadores[0]
        else:
            return None

    def obtenerReservacionesXCodigo(self, codigo):
        reservaciones = [res for res in self.__reservaciones if res.codigo == codigo.upper()]
        if len(reservaciones) > 0:
            return reservaciones[0]
        else:
            return None

    def __tieneCapacidad(self, habitacion, fecha_entrada, cantidad_dias, ignorar_indice = -1):
        if not isinstance(habitacion, Habitacion):
            raise TypeError('La habitación a reservar tiene que ser una instancia de la clase Habitacion')
        elif not isinstance(fecha_entrada, datetime):
            raise TypeError('La fecha de entrada tiene que ser una instancia de la clase datetime')

        capacidad = True
        entrada = datetime.strptime(str(fecha_entrada.day) + '-' + str(fecha_entrada.month) + '-' + str(fecha_entrada.year) + ' ' + HORA_ENTRADA, '%d-%m-%Y %H:%M')

        fecha_salida = fecha_entrada + timedelta(days=cantidad_dias)
        salida = datetime.strptime(str(fecha_salida.day) + '-' + str(fecha_salida.month) + '-' + str(fecha_salida.year) + ' ' + HORA_SALIDA, '%d-%m-%Y %H:%M')

        i=0
        while capacidad and i < len(self.__reservaciones):
            if (ignorar_indice == -1 or i != ignorar_indice) and habitacion.numero == self.__reservaciones[i].habitacion.numero:
                comienzo = datetime.strptime(str(self.__reservaciones[i].fecha_entrada.day) + '-' + str(self.__reservaciones[i].fecha_entrada.month) + '-' + str(self.__reservaciones[i].fecha_entrada.year) + ' ' + HORA_ENTRADA, '%d-%m-%Y %H:%M')

                fecha_salida = self.__reservaciones[i].fecha_entrada + timedelta(days = self.__reservaciones[i].cantidad_dias)
                final = datetime.strptime(str(fecha_salida.day) + '-' + str(fecha_salida.month) + '-' + str(fecha_salida.year) + ' ' + HORA_ENTRADA, '%d-%m-%Y %H:%M')

                if comienzo <= entrada <= final or comienzo <= salida <= final:
                    capacidad = False

            i = i + 1

        return capacidad



