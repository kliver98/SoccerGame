from server import balon
from server import estadisticas
import _thread



class Sala:
    '''maximo de jugadores por equipo'''
    MAX_JUGADORES_TEAM=3
    ''' atributos de una sala del servidor para representar un partido'''
    __balon=None
    '''map de jugadores Key=username,[team,..otros atributos]'''
    __jugadores=None
    __timer =None
    __estadisticas=None
    
    
    
    '''duracion de un tiempo en el partido, expresado en segundos'''
    DURACION_TIEMPO=60
    
    def __init__(self):
        self.__balon=balon.Balon()
        self.__estadisticas=estadisticas.Estadisticas()
        self.__jugadores={}