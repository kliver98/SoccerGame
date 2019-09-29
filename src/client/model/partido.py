from client.model import balon, campo
from client.model.jugador import Jugador


class Partido():
    
    #Atributos
    """Atributo que referencia a un balon"""
    __balon = None
    """Atributo que referencia a un campo"""
    __campo = None
    """Atributo que referencia a una lista de jugadores"""
    __jugadores = None
    
    def __init__(self):
        """Constructor que inicializa el balon, el campo y la lista de jugadores"""
        self.__balon = balon.Balon()
        self.__campo = campo.Campo()
        self.__jugadores = []
        
    def agregar_jugador(self, usuario, equipo):
        """Metodo para agregar un jugador a la lista de jugadores"""
        self.__jugadores.append(Jugador(usuario,equipo))