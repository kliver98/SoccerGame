from client.model import balon, campo, aplicacion
from client.model.jugador import Jugador


class Partido():
    
    #Atributos
    """Atributo que referencia a un balon"""
    __balon = None
    """Atributo que referencia a un campo"""
    __campo = None
    """Atributo que referencia a una lista de jugadores"""
    __jugadores = None
    """Atributo string que tiene el nombre del jugador del cliente, el unico jugador que puede controlar"""
    __usuario_de_jugador = None
    
    def __init__(self, usuario_de_jugador, numero_campo):
        """Constructor que inicializa el balon, el campo y la lista de jugadores. Recibe el nombre de usuario que controla el cliente, 
        numero (entero positivo) de la imagen del campo a cargar"""
        self.__usuario_de_jugador = usuario_de_jugador
        self.__balon = balon.Balon()
        self.__campo = campo.Campo(numero_campo)
        self.__jugadores = []
        
    def agregar_jugador(self, usuario, equipo):
        """Metodo para agregar un jugador a la lista de jugadores"""
        self.__jugadores.append(Jugador(usuario,equipo))
    
    def esta_jugador_dentro_campo(self, coordenadas_campo, coordenadas_jugador):
        """Metodo que verifica si un jugador esta dentro de las coordenadas del campo.
        Recibe coordenadas_campo y coordenadas_jugador que son un arreglo conteniendo informacion respectiva de las coordenas [x,y]"""
        return self.__campo.esta_jugador_dentro_campo(coordenadas_campo, coordenadas_jugador)
    
    def mover_jugador(self, izquierda, derecha, arriba, abajo):
        jugador = self.get_jugador(self.__usuario_de_jugador)
        jugador.mover(izquierda, derecha, arriba, abajo)
    
    def get_datos_jugadores(self):
        """Metodo que retorna arreglo de seis datos de la informacion de los usuarios, separados por aplicacion.SEPARADOR
        nombre de usuario, equipo, coordenada en x, coordenada en y, ruta de la imagen, entero para rotar la imagen"""
        datos = []
        for i in self.__jugadores:
            aux = i.get_datos()
            aux2 = i.configurar_imagen()
            regex = aplicacion.SEPARADOR
            datos.append(f"{aux[0]}{regex}{aux[1]}{regex}{aux[2]}{regex}{aux[3]}{regex}{aux2[0]}{regex}{aux2[1]}")
        return datos
    
    def get_jugador(self, usuario):
        """Metodo que retorna un objeto jugador que su nombre de usuario es igual a obtenido por parametro"""
        for i in self.__jugadores:
            if i.get_usuario()==usuario:
                return i
        return None
    
    def set_datos_jugadores(self, datos):
        """Metodo que actualiza las coordenadas de los jugadores que se obtienen por parametro, 
        es un arreglo y cada uno tiene get_datos() de clase jugador"""
        for i in datos:
            if i.get_usuario()==self.__usuario_de_jugador:
                continue
            aux = i.split(aplicacion.SEPARADOR) #Recordar, son 4. Usuario, equipo, coordenada en x y coordenada en y
            jugador = self.get_jugador(aux[0])
            jugador.set_coordenadas(aux[2],aux[3])
            
    def set_datos_balon(self, x, y,usuario):
        """Metodo que mueve las coordenadas de la imagen del balon, retorna string de ruta generada de la imagen del balon y 
        angulo de imagen para rotar. Separa estos dos datos por aplicacion.SEPARADOR"""
        mover = self.__balon.actualizar_datos(x, y, usuario)
        return f"{mover[0]}{aplicacion.SEPARADOR}{mover[1]}"
            
    def get_posicion_balon(self):
        """Metodo que retorna un string con la posicion (x,y) del balon separado por: aplicacion.SEPARADOR"""
        coord = self.__balon.get_coordenadas()
        return f"{coord[0]}{aplicacion.SEPARADOR}{coord[1]}"
    
    def get_ruta_imagen_campo(self):
        """Metodo que retorna un string con la ruta de imagen del campo"""
        return self.__campo.get_ruta_imagen()
    
    def get_usuario_de_jugador(self):
        return self.__usuario_de_jugador
            