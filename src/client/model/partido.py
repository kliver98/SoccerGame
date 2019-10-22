from client.model import balon, campo, aplicacion
from client.model.jugador import Jugador
from client.model.conexion import Conexion
from _thread import *
from msvcrt import kbhit

MODO_JUEGO_ONLINE = 1
MODO_JUEGO_LOCAL = 2
TIEMPO_CADA_JUEGO = 60
TIEMPO_ANUNCIO = 5
VELOCIDAD_JUGADOR = 5

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
    """Atributo para representar un objeto de la clase Conexion si se esta jugando online"""
    __conexion = None
    
    def __init__(self, usuario_de_jugador, numero_campo,ip):
        """Constructor que inicializa el balon, el campo y la lista de jugadores. Recibe el nombre de usuario que controla el cliente, 
        numero (entero positivo) de la imagen del campo a cargar"""
        self.__usuario_de_jugador = usuario_de_jugador
        self.__balon = balon.Balon()
        self.__campo = campo.Campo(numero_campo)
        self.__jugadores = []
        if ip is not None:
            self.__conexion = Conexion(ip)
            print("Conectado con el servidor")
            try:
                print("try")
                self.__conexion.correr()
               # _thread.start_new_thread(self.__threaded_conexion(self.__conexion))
                print("salio")
            except Exception as e:
                print(e.trace_call())
            
    
        
    def agregar_jugador(self, usuario, equipo):
        """Metodo para agregar un jugador a la lista de jugadores"""
        self.__jugadores.append(Jugador(usuario,equipo))
    
    def iniciar_bots(self, num_jugadores_equipo):
        self.__jugadores.append(Jugador(f"{self.__usuario_de_jugador}","A")) #Jugador del usuario del cliente
        for i in range(1,num_jugadores_equipo*2):
            if i<num_jugadores_equipo:
                equipo = "A"
            else:
                equipo = "B"
            self.agregar_jugador(f"bot#{i}",equipo)
        return len(self.__jugadores)==(num_jugadores_equipo*2)
    
    def set_coordenadas_jugador_cliente(self, coord,soltar_balon, anteriores):
        jugador = self.get_jugador(self.__usuario_de_jugador)
        if anteriores:
            jugador.reset_coordenadas(coord)
            return
        if not self.__conexion and not soltar_balon: #Esta jugando LOCAL
            if self.jugador_cliente_colisionando_balon():
                self.mover_balon(coord[0]*VELOCIDAD_JUGADOR,coord[1]*VELOCIDAD_JUGADOR)
        jugador.set_coordenadas(coord[0]*VELOCIDAD_JUGADOR,coord[1]*VELOCIDAD_JUGADOR)
    
    def esta_jugador_dentro_campo(self, coordenadas_campo):
        """Metodo que verifica si un jugador esta dentro de las coordenadas del campo.
        Recibe coordenadas_campo y coordenadas_jugador que son un arreglo conteniendo informacion respectiva de las coordenas [x,y]"""
        coordenadas_jugador = self.get_jugador(self.__usuario_de_jugador).get_coordenadas()
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
            
    def get_datos_balon(self):
        """Metodo que retorna un string con la posicion (x,y) del balon separado por: aplicacion.SEPARADOR"""
        datos = None
        if not self.__conexion: #Es LOCAL, contra PC
            datos = self.__balon.actualizar_datos(0,0,"",False)
        else: #Debo traer datos de balon dle servidor
            datos = None
        coord = self.__balon.get_coordenadas()
        return f"{datos[0]}{aplicacion.SEPARADOR}{datos[1]}{aplicacion.SEPARADOR}{coord[0]}{aplicacion.SEPARADOR}{coord[1]}"
    
    def mover_balon(self,x,y): #Solo se llama en modo de juego LOCAL
        self.__balon.set_coordenadas(x, y)
    
    def jugador_cliente_colisionando_balon(self): #Dado que es el cliente, se que sera del equipo A y solo sera llamado cuando este jugano local
        cliente = self.get_jugador(self.__usuario_de_jugador)
        coord_c = cliente.get_coordenadas()
        coord_b = self.__balon.get_coordenadas()
        if cliente.get_usuario()==self.__balon.get_usuario():
            return True
        if coord_c[0]+30>coord_b[0] and coord_c[0]+10<coord_b[0]:
            if coord_c[1]+40>coord_b[1] and coord_c[1]+5<coord_b[1]:
                return True
        return False
    
    def get_ruta_imagen_campo(self):
        """Metodo que retorna un string con la ruta de imagen del campo"""
        return self.__campo.get_ruta_imagen()
    
    def get_usuario_de_jugador(self):
        """Metodo que retorna un string con el noombre de usuario del jugador de el cliente actual, solo que el controla el cliente actual"""
        return self.__usuario_de_jugador
    
    def get_tiempos(self):
        return (TIEMPO_CADA_JUEGO,TIEMPO_ANUNCIO)
    
    def get_velocidad_jugador(self):
        return VELOCIDAD_JUGADOR
    
    def get_coordenadas_cliente(self):
        return self.get_jugador(self.__usuario_de_jugador).get_coordenadas()
    
    def alguien_tiene_balon(self):
        if self.__balon.get_usuario():
            if self.__balon.get_usuario()!="":
                return True
        
        return False