from client.model import partido
LOCACION_RESOURCES = "../../resources/"

class Aplicacion():
    
    #Atributos
    """Atributo que referencia a un partido"""
    __partido = None
    
    def __init__(self):
        """Constructor vacio que solo inicializa el objeto aplicacion"""
        pass
    
    def iniciar_partido(self):
        """Metodo que crea un nuevo partido"""
        self.__partido = partido.Partido()
        
    def agregar_jugador(self, usuario, equipo):
        """Metodo que agrega un jugador al partido actual que se este jugando"""
        self.__partido.agregar_jugador(usuario, equipo)