from vistas.editar_habitacion_ui import EditarHabitacion

class PresentadorAdicionarHabitacion:

    def __init__(self, hotel):
        self.__hotel = hotel
        self.__vista = EditarHabitacion(self)

    def iniciar(self):
        self.__vista.iniciar()

    def adicionarHabitacion(self, numero, tipo, estilo, tiene_internet):
        self.__hotel.adicionarHabitacion(numero, tipo, tiene_internet, estilo)

