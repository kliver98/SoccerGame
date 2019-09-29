from server import balon
from server import estadisticas
import _thread



class Sala:
    ''' atributos de una sala del servidor para representar un partido'''
    __balon=None
    __jugador1=None
    __jugador2=None
    __timer =None
    __estadisticas=None
    
    '''duracion de un tiempo en el partido, expresado en segundos'''
    DURACION_TIEMPO=60
    
    def __init__(self):
        self.__balon=balon.Balon()
        self.__estadisticas=estadisticas.Estadisticas()