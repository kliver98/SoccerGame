from server import balon
from server import estadisticas
from _thread import *
from tools import cronometro
import time
import constantesCompartidas as cc #ESTO COMO ESTAMOS TRABAJANDO LOCAL FUNCIONA, YA SI SE DISTRIBUYE TOCA PONER LOS VALORES DE LAS CONSTANTES EN CADA CLASE
TIEMPO_CADA_JUEGO = cc.TIEMPO_CADA_JUEGO
TIEMPO_ANUNCIO = cc.TIEMPO_ANUNCIO
ALTO_VENTANA = cc.ALTO_VENTANA
ANCHO_VENTANA = cc.ANCHO_VENTANA

class Sala:
    '''maximo de jugadores por equipo'''
    MAX_JUGADORES_TEAM=cc.MAX_JUGADORES_TEAM
    ''' atributos de una sala del servidor para representar un partido'''
    __balon=None
    '''map de jugadores Key=username,[team,..otros atributos]'''
    __jugadores=None
    __timer =None
    __estadisticas=None
    __goles = None
    
    '''duracion total que dura todo un partido'''
    DURACION_TIEMPO = (TIEMPO_CADA_JUEGO*2)+TIEMPO_ANUNCIO
    
    def __init__(self,iden):
        
        self.equipoA={}
        self.equipoB={}
        self.__goles = (0,0)
        self.equipos={'A':self.equipoA,'B':self.equipoB}
        self.equipo_disponible='A'
        self.id=iden
        self.disponible=True
        self.__balon=balon.Balon(( (ANCHO_VENTANA/2)-8 , (ALTO_VENTANA/2)-8 ))
        self.__estadisticas=estadisticas.Estadisticas()
        self.__jugadores={}
        self.posicion_actual=1
        self.crono=cronometro.Cronometro()
        
    def add_player(self,net,playerid):
        self.equipos[self.equipo_disponible][playerid]=None
        start_new_thread(self.__threaded_client,(net,playerid,self.equipo_disponible,self.posicion_actual))
        self.__comprobar_disponibilidad()
        
    def __threaded_client(self,net,playerid,equipo,posicion):
        info_out=f"{posicion};{equipo};{self.id}"
        self.enviar(net,info_out)
        
        while True:
            try:
                info_in=self.leer(net) #Aqui esta informacion de 1 jugador "Nombre-Equipo-Coordenadas-SoltarBalon"
                
                aux = info_in.split(",")
                usuario = aux[0]
                equipo = aux[1]
                soltar_balon = aux[4]=="True"
                coord_u = (float(aux[2].split("(")[1]),float(aux[3].split(")")[0]))
                colisionando = self.jugador_colisionando_balon(usuario,equipo,coord_u,soltar_balon)
                if soltar_balon and usuario==self.__balon.get_usuario():
                    self.mover_balon(ANCHO_VENTANA*0.15, 0, equipo, "")
                if colisionando:
                    coord_ant_balon = self.__balon.get_coordenadas()
                    self.mover_balon(coord_u[0], coord_u[1],equipo,usuario)
                    gol = self.hizo_gol()
                    goles = self.__goles
                    if gol==1: #Gol equipo A
                        self.__goles = (goles[0]+1,goles[1])
                        self.__balon.update_coordenadas(((ANCHO_VENTANA/2)-8,(ALTO_VENTANA/2)-8))
                    elif gol==-1: #Gol equipo B
                        self.__goles = (goles[0],goles[1]+1)
                        self.__balon.update_coordenadas(((ANCHO_VENTANA/2)-8,(ALTO_VENTANA/2)-8))
                    elif gol==0:
                        self.__balon.update_coordenadas(coord_ant_balon)
                coord_balon = self.__balon.get_coordenadas()
                info_out=f"{list(self.equipoA.values())};{list(self.equipoB.values())};{self.crono.get_cuenta()};{coord_balon[0]};{coord_balon[1]};{self.__balon.get_usuario()};{self.__goles[0]};{self.__goles[1]}"
                if not(info_in):
                    print(f"Desconectado: {playerid} -> Sala {self.id}")
                else:
                    self.equipos[equipo][playerid]=info_in
                    self.enviar(net,info_out)
        
            except Exception as e:
                
                print(e.trace_call())
                break
        print("Conexion Perdida")
        net.close()
        
    def enviar(self,net,info):  
        net.sendall(str.encode(info))  
    
    def leer(self,net):    
        info=net.recv(2048).decode()
        if info is not None:
            return info
        else:
            return "Vacio"
        
    def __comprobar_disponibilidad(self):
        lonA=len(self.equipoA)
        lonB=len(self.equipoB)
        if lonA+lonB==self.MAX_JUGADORES_TEAM*2: # indica que la sala esta completa
            self.disponible=False
            self.crono.iniciar(self.DURACION_TIEMPO, self.crono.MODO_CRONOMETRO)
        else:
            if lonA < self.MAX_JUGADORES_TEAM:
                self.equipo_disponible='A'
                lonA +=1
            else:
                self.equipo_disponible='B' 
                self.posicion_actual=lonA+lonB+1
    
    def esta_disponible(self):
        return self.disponible
    
    def esta_balon_dentro_campo(self):
        coordenadas_balon = self.__balon.get_coordenadas()
        campo_x = ANCHO_VENTANA
        campo_y = ALTO_VENTANA
        balon_x = coordenadas_balon[0]
        balon_y = coordenadas_balon[1]
        if balon_x>30 and balon_x+40<campo_x:
            if balon_y>4 and balon_y<campo_y:
                return True
        return False
    
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
        elif not self.esta_balon_dentro_campo():
            return 0
    
    def jugador_colisionando_balon(self,usuario,equipo,coord_u,soltar_balon): #Dado que es el cliente, se que sera del equipo A y solo sera llamado cuando este jugano local
        if soltar_balon:
            return False
        coord_b = self.__balon.get_coordenadas()
        if usuario==self.__balon.get_usuario():
            return True
        if equipo=="A":
            if coord_u[0]+30>coord_b[0] and coord_u[0]+10<coord_b[0]:
                if coord_u[1]+40>coord_b[1] and coord_u[1]+5<coord_b[1]:
                    return True
                return False
        elif equipo=="B":
            if coord_u[0]+5>coord_b[0] and coord_u[0]-17<coord_b[0]:
                if coord_u[1]+40>coord_b[1] and coord_u[1]+5<coord_b[1]:
                    return True
                return False
        return False
    
    def mover_balon(self,x,y,equipo,nuevo_usuario = ""):
        self.__balon.set_usuario(nuevo_usuario)
        if nuevo_usuario=="":
            coord = self.__balon.get_coordenadas()
            if equipo=="A":
                self.__balon.set_coordenadas(coord[0]+ANCHO_VENTANA*0.15,coord[1])
            elif equipo=="B":
                self.__balon.set_coordenadas(coord[0]-ANCHO_VENTANA*0.15, coord[1])
            return
        self.__balon.set_posesion(equipo)
        if equipo=="A":
            self.__balon.set_coordenadas(x+28, y+20)
        elif equipo=="B":
            self.__balon.set_coordenadas(x-15, y+20)
            