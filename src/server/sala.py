from server import balon
import _thread



class Sala:
    ''' atributos de una sala del servidor para representar un partido'''
    __balon=balon.Balon()
    __jugador1=None
    __jugador2=None
    __timer =None
    
    
    def __init__(self):
        pass