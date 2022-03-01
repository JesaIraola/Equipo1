from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QCloseEvent, QResizeEvent
from PyQt5 import uic

class Ventana(QMainWindow):
    def __init__(self, presentador):
        self.__presentador = presentador
        QMainWindow.__init__(self)
        uic.loadUi('vistas/ui/ventana.ui', self)

        self.actionSalir.triggered.connect(self.close)

        #clientes
        self.actionAdicionarCliente.triggered.connect(self.__presentador.mostrarAdicionarCliente)
        self.actionListarClientes.triggered.connect(self.__presentador.mostrarListadoClientes)
        
        #habitaciones
        self.actionAdicionarHabitacion.triggered.connect(self.__presentador.mostrarAdicionarHabitacion)
        self.actionListarHabitaciones.triggered.connect(self.__presentador.mostrarListadoHabitaciones)

        #turoperadores
        self.actionAdicionarTuroperador.triggered.connect(self.__presentador.mostrarAdicionarTuroperador)
        self.actionListarTuroperadores.triggered.connect(self.__presentador.mostrarListadoTuroperadores)

        #reservaciones recepcion
        self.actionRecepcion.triggered.connect(self.__presentador.mostrarAdicionarReservacionRecepcion)

        #reservaciones turoperador
        self.actionTuroperador.triggered.connect(self.__presentador.mostrarAdicionarReservacionTuroperador)

        #reservaciones 
        self.actionListarReservaciones.triggered.connect(self.__presentador.mostrarListadoReservaciones)

        #consultas
        self.actionPorcientoMensual.triggered.connect(self.__presentador.mostrarPorcientoMensual)
        self.actionMaximoClientes.triggered.connect(self.__presentador.mostrarMaximoClientes)
        self.actionMaximoSexo.triggered.connect(self.__presentador.mostrarMaximoSexo)
        self.actionReservacionTuroperador.triggered.connect(self.__presentador.mostrarReservacionesTuroperador)

    def iniciar(self):
        self.actualizarAcciones()
        self.show()

    def closeEvent(self, a0: QCloseEvent):
        QMainWindow.closeEvent(self, a0)

    def resizeEvent(self, a0: QResizeEvent):
        fondo = QPixmap('vistas/imgs/fondo.jpg')
        fondo = fondo.scaled(self.size(), Qt.KeepAspectRatioByExpanding)

        paleta = self.palette()
        paleta.setBrush(QPalette.Background, QBrush(fondo))

        self.setPalette(paleta)

    def actualizarAcciones(self):
        existenClientes = len(self.__presentador.clientes) > 0
        existenTuroperadores = len(self.__presentador.turoperadores) > 0

        self.actionPorcientoMensual.setEnabled(existenClientes)
        self.actionMaximoClientes.setEnabled(existenClientes)
        self.actionMaximoSexo.setEnabled(existenClientes)
        self.actionReservacionTuroperador.setEnabled(existenClientes and existenTuroperadores)
        self.actionTuroperador.setEnabled(existenTuroperadores)
