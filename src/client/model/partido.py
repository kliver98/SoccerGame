from client.model import balon, campo, aplicacion
from client.model.jugador import Jugador
from client.model.conexion import Conexion
from client.model import udp_capturador
from _thread import *
from msvcrt import kbhit
import random
import constantesCompartidas as cc #ESTO COMO ESTAMOS TRABAJANDO LOCAL FUNCIONA, YA SI SE DISTRIBUYE TOCA PONER LOS VALORES DE LAS CONSTANTES EN CADA CLASE


MODO_JUEGO_ONLINE = 1
MODO_JUEGO_LOCAL = 2
TIEMPO_CADA_JUEGO = cc.TIEMPO_CADA_JUEGO
TIEMPO_ANUNCIO = cc.TIEMPO_ANUNCIO
VELOCIDAD_JUGADOR = cc.VELOCIDAD_JUGADOR
ALTO_VENTANA = cc.ALTO_VENTANA
ANCHO_VENTANA = cc.ANCHO_VENTANA
MAX_JUGADORES_TEAM = cc.MAX_JUGADORES_TEAM

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
    __goles_equipos = None
    """Atributo para representar un objeto de la clase Conexion si se esta jugando online"""
    __conexion = None
    __datos_servidor = None
    __udp=None
    
    def __init__(self, usuario_de_jugador, numero_campo,ip):
        """Constructor que inicializa el balon, el campo y la lista de jugadores. Recibe el nombre de usuario que controla el cliente, 
        numero (entero positivo) de la imagen del campo a cargar"""
        self.__usuario_de_jugador = usuario_de_jugador
        self.__balon = balon.Balon()
        self.__balon.update_coordenadas(((ANCHO_VENTANA/2)-8,(ALTO_VENTANA/2)-8))
        self.__campo = campo.Campo(numero_campo)
        self.__jugadores = []
        self.partido_listo = False
        self.__goles_equipos = (0,0)
        if ip is not None:
            self.__conexion = Conexion(ip,self)
            self.__udp=udp_capturador.CapturadorUDP()
            print("Conectado con el servidor")
            try:
                print("try")
                self.__conexion.correr()
                self.__udp.correr()
               # _thread.start_new_thread(self.__threaded_conexion(self.__conexion))
               
                print("salio")
            except Exception as e:
                print(e.trace_call())
            
    def agregar_jugador(self, usuario, equipo, coordenadas):
        """Metodo para agregar un jugador a la lista de jugadores"""
        self.__jugadores.append(Jugador(usuario,equipo, coordenadas))
    
    def iniciar_bots(self): #Ya se que selecciono modo Local
        self.__jugadores.append(Jugador(f"{self.__usuario_de_jugador}","A",(ANCHO_VENTANA,ALTO_VENTANA,-1))) #Jugador del usuario del cliente
        for i in range(1,MAX_JUGADORES_TEAM*2):
            if i<MAX_JUGADORES_TEAM:
                equipo = "A"
            else:
                equipo = "B"
            self.agregar_jugador(f"bot#{i}",equipo, (ANCHO_VENTANA,ALTO_VENTANA,-1))
        return len(self.__jugadores)==(MAX_JUGADORES_TEAM*2)
    
    def iniciar_jugadores(self):
        self.__jugadores = []
        A = self.__datos_servidor[0].split("['")[1].split("']")[0].split("', '")
        B = self.__datos_servidor[1].split("['")[1].split("']")[0].split("', '")
        coord = (float(self.__datos_servidor[3]),float(self.__datos_servidor[4]))
        self.__balon.update_coordenadas(coord)
        self.__balon.set_usuario(self.__datos_servidor[5])
        for i in A:
            coord = i.split("(")[1].split(")")[0].split(", ")
            x = int(coord[0])
            y = int(coord[1])
            aux = i.split(",")
            user = aux[0]
            equipo = aux[1]
            self.agregar_jugador(user, equipo, (x,y)) #Suponiendo que en la 0 esta nombre user, en la 1 equipo y en la 2 coordenadas
        for i in B:
            coord = i.split("(")[1].split(")")[0].split(", ")
            x = int(coord[0])
            y = int(coord[1])
            aux = i.split(",")
            user = aux[0]
            equipo = aux[1]
            self.agregar_jugador(user, equipo, (x,y)) #Suponiendo que en la 0 esta nombre user, en la 1 equipo y en la 2 coordenadas
    
    def set_coordenadas_jugador_cliente(self, coord,soltar_balon, anteriores):
        jugador = self.get_jugador(self.__usuario_de_jugador)
        if anteriores:
            jugador.reset_coordenadas(coord)
            return
        coor_ant_b = self.__balon.get_coordenadas()
        if not self.__conexion and not soltar_balon: #Esta jugando LOCAL
            if self.jugador_colisionando_balon(self.get_jugador(self.__usuario_de_jugador)):
                self.mover_balon(coord[0]*VELOCIDAD_JUGADOR,coord[1]*VELOCIDAD_JUGADOR,jugador.get_usuario())
        elif not self.__conexion and soltar_balon and self.__balon.get_usuario()==self.__usuario_de_jugador:
            self.mover_balon(ANCHO_VENTANA*0.15, 0, "")
        coord_anteriores = jugador.get_coordenadas()
        jugador.set_coordenadas(coord[0]*VELOCIDAD_JUGADOR,coord[1]*VELOCIDAD_JUGADOR)
        if not self.esta_jugador_dentro_campo((ANCHO_VENTANA,ALTO_VENTANA),jugador):
            self.__balon.update_coordenadas(coor_ant_b)
            jugador.reset_coordenadas(coord_anteriores)
            return
        if not self.__conexion: #Regreso balon si no esta dentr del campo
            if not self.esta_balon_dentro_campo((ANCHO_VENTANA,ALTO_VENTANA), self.__balon.get_coordenadas()):
                gol = self.hizo_gol() #1 hizo gol equipo A, -1 equipo B y 0 nadie
                goles = self.get_goles()
                if gol==0:
                    self.__balon.update_coordenadas(coor_ant_b)
                    return
                elif gol==1:
                    self.__goles_equipos = (goles[0]+1,goles[1])
                elif gol==-1:
                    self.__goles_equipos = (goles[0],goles[1]+1)
                self.__balon.update_coordenadas(((ANCHO_VENTANA/2)-8,(ALTO_VENTANA/2)-8))
        if self.__conexion: #Esta jugando online
            info_a = self.__conexion.get_info_out().split(",")
            n_info = f"{info_a[0]},{info_a[1]},{jugador.get_coordenadas()},{soltar_balon}"
            self.__conexion.set_info_out(n_info)
            
    def hizo_gol(self): #retorna -1 si hizo gol en la porteria izquierda, 1 gol en la de la derecha y 0 no hizo gol
        coord_b = self.__balon.get_coordenadas()
        coord_a0 = (ANCHO_VENTANA*0.038, ALTO_VENTANA*0.425)
        coord_a1 = (ANCHO_VENTANA*0.038, ALTO_VENTANA*0.575)
        coord_b0 = (ANCHO_VENTANA*0.962, ALTO_VENTANA*0.425)
        coord_b1 = (ANCHO_VENTANA*0.962, ALTO_VENTANA*0.575)
        if coord_b[0]<=coord_a0[0] and coord_b[1]>=coord_a0[1] and coord_b[1]<=coord_a1[1]:
            return -1
        elif coord_b[0]>=coord_b0[0] and coord_b[1]>=coord_b0[1] and coord_b[1]<=coord_b1[1]:
            return 1
        else:
            return 0
    
    def esta_jugador_dentro_campo(self, coordenadas_campo,jugador):
        """Metodo que verifica si un jugador esta dentro de las coordenadas del campo.
        Recibe coordenadas_campo y coordenadas_jugador que son un arreglo conteniendo informacion respectiva de las coordenas [x,y]"""
        return self.__campo.esta_jugador_dentro_campo(coordenadas_campo, jugador.get_coordenadas(),jugador.get_equipo())
    
    def esta_balon_dentro_campo(self,coordenadas_campo, coordenadas_balon):
        return self.__campo.esta_balon_dentro_campo(coordenadas_campo, coordenadas_balon)
    
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
        coord = None
        if not self.__conexion: #Es LOCAL, contra PC
            datos = self.__balon.actualizar_datos(0,0,"",False)
            coord = self.__balon.get_coordenadas()
        else:
            coord = self.__balon.get_coordenadas()
            datos = balon.Balon().actualizar_datos(coord[0],coord[1],self.__balon.get_usuario())
        return f"{datos[0]}{aplicacion.SEPARADOR}{datos[1]}{aplicacion.SEPARADOR}{coord[0]}{aplicacion.SEPARADOR}{coord[1]}"
    
    def mover_balon(self,x,y,nuevo_usuario = ""): #Solo se llama en modo de juego LOCAL
        self.__balon.set_coordenadas(x, y)
        self.__balon.set_usuario(nuevo_usuario)
            
    
    def jugador_colisionando_balon(self,jugador): #Dado que es el cliente, se que sera del equipo A y solo sera llamado cuando este jugano local
        coord_c = jugador.get_coordenadas()
        coord_b = self.__balon.get_coordenadas()
        if jugador.get_usuario()==self.__balon.get_usuario():
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
        jugador = self.get_jugador(self.__usuario_de_jugador)
        if not jugador:
            return (random.randint(100,ANCHO_VENTANA-100),random.randint(100,ALTO_VENTANA-100))
        coord = jugador.get_coordenadas()
        #if not jugador.get_coordenadas():
        #    coord = (random.randint(100,ANCHO_VENTANA-100),random.randint(100,ALTO_VENTANA-100))
        return coord    
        
    
    def alguien_tiene_balon(self):
        if self.__balon.get_usuario():
            if self.__balon.get_usuario()!="":
                return True
        return False
    
    def set_patido_listo(self, estado):
        self.partido_listo = estado
        
    def set_datos_servidor(self, datos):
        self.__datos_servidor = datos.split(";")
    
    def esta_partido_listo(self):
        """Metodo que retornar boolean confirmando si ya se puede mostrar pantalla para iniciar el partido"""
        return self.partido_listo
    
    def get_tiempo_juego_Online(self):
        tiempo = int(self.__datos_servidor[2])
        return tiempo
    
    def get_goles(self):
        if not self.__conexion:
            return self.__goles_equipos
        elif self.__conexion:
            return (float(self.__datos_servidor[6]),float(self.__datos_servidor[7]))