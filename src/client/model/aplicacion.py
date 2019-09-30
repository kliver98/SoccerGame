from client.model import partido
"""Constante global, no ligada a la clase, para identificar donde estan los recursos para usar en el juego"""
LOCACION_RESOURCES = "../../resources/"
"""Constante global, no ligada a la clase, para concatenar datos y despues tambien poder separarlos (split). 
El separador sera tanto para modelo, vista y/o controlador"""
SEPARADOR = "-"
"""Constante global, no ligada a la clase, que representa el nombre de la aplicacion"""
NOMBRE_APLICACION = "Soccer Game"

class Aplicacion():
    
    #Atributos
    """Atributo que referencia a un partido"""
    __partido = None
    
    def __init__(self):
        """Constructor vacio que solo inicializa el objeto aplicacion"""
        pass
    
    def iniciar_partido(self, usuario_de_jugador, numero_campo = 3):
        """Metodo que crea un nuevo partido. Recibe el nombre de usuario del cliente (el unico que se puede controlar), 
        numero de la imagen del campo a cargar, por defecto es el campo 3"""
        self.__partido = partido.Partido(usuario_de_jugador , numero_campo)
        
    def agregar_jugador(self, usuario, equipo):
        """Metodo que agrega un jugador al partido actual que se este jugando"""
        self.__partido.agregar_jugador(usuario, equipo)
        
    def get_datos_jugadores(self):
        """Metodo que retorna arreglo de seis datos de la informacion de los usuarios, separados por aplicacion.SEPARADOR
        nombre de usuario, equipo, coordenada en x, coordenada en y, ruta de la imagen, entero para rotar la imagen"""
        return self.__partido.get_datos_jugadores()
    
    def set_datos_jugadores(self, datos):
        """Metodo que actualiza las coordenadas de los jugadores que se obtienen por parametro, 
        datos es un arreglo y cada uno tiene get_datos() de clase jugador pero es un string separado por ,
        Ejemplo: arr = ['jugador1,False,100,200' , 'jugador2,False,150,180' , 'jugador3,True,400,50' , 'jugador4,True,350,149']"""
        self.__partido.set_datos_jugadores(datos)
        
    def set_posicion_balon(self, x, y):
        """Metodo que mueve las coordenadas de la imagen del balon, retorna tupla de ruta generada de la imagen del balon y angulo de imagen para rotar"""
        return self.__partido.set_posicion_partido(x,y)
    
    def get_posicion_balon(self):
        """Metodo que retorna un string con la posicion (x,y) del balon separado por: aplicacion.SEPARADOR"""
        return self.__partido.get_posicion_balon()
    
    def get_ruta_imagen_campo(self):
        """Metodo que retorna un string con la ruta de la imagen del campo a cargar"""
        return self.__partido.get_ruta_imagen_campo()