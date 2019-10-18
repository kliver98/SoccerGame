"""Esta es la la clase controladora. Esta se encargara de conectar la logica del modelo con la interfaz"""
"""Importaciones de clases"""
from client.view.PanelJuego import PanelJuego
from client.model import partido
class Controlador():
    __panelJuego = None
    __partido = None
    
    """Metodos establecidos para la conexion entre modelo e interfaz"""
    
    """constructor del controlador, se le pasa por parametro la referencia del partido a empezar"""
    def __init__(self,partido):
        self.__partido = partido
    """inicia la ventana en la cual se jugara el partido, se le pasa por parametro al constructor de la ventana una referencia de este controlador"""
    def iniciarCampoDeJuego(self):
        self.__panelJuego = PanelJuego(self)
    """Metoodo que retorna arreglo de strings que contienen los datos de los jugadores"""
    def get_datos_jugadores(self):
        return self.__partido.get_datos_jugadores()
    """Metodo que retorna un string con las coordenadas x y coordenadas y del balon"""
    def get_posicion_balon(self):
        return self.__partido.get_posicion_balon()
    """Metodo que retorna un string con la ruta de la imagen del balon y el angulo de rotcion del mismo"""
    def get_imagen_balon(self):
        return self.__partido.get_imagen_actual_balon()
    
    """Metodo que le pasa al objeto partido hacia donde fue movido el jugador"""
    def moverJugador(self, izquierda, derecha, arriba, abajo):
        self.__partido.mover_jugador( izquierda, derecha, arriba, abajo)
       
    """Metodo 2"""    
    """Metodo 3"""    
    """Metodo 4"""    
    """Metodo 5"""    
    """Metodo 6"""
    """Metodo 7"""
    """Metodo 8"""
    """Metodo 9"""
    """Metodo 10"""
    """Metodo 11"""
    """Metodo 12"""
    """Metodo 13"""
    """Metodo 14"""
    """Metodo 15"""
    """Metodo 16"""
    """Metodo 17"""
    """Metodo 18"""
    """Metodo 19"""
    """Metodo 20"""
    """Metodo 21"""
    """Metodo 22"""