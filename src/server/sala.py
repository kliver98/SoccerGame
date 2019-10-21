from server import balon
from server import estadisticas
from _thread import *





class Sala:
    '''maximo de jugadores por equipo'''
    MAX_JUGADORES_TEAM=2
    ''' atributos de una sala del servidor para representar un partido'''
    __balon=None
    '''map de jugadores Key=username,[team,..otros atributos]'''
    __jugadores=None
    __timer =None
    __estadisticas=None
    
    
    
    '''duracion de un tiempo en el partido, expresado en segundos'''
    DURACION_TIEMPO=60
    
    def __init__(self,iden):
        
        self.equipoA=[]
        self.equipoB=[]
        self.equipos={'A':self.equipoA,'B':self.equipoB}
        self.equipo_disponible='A'
        self.id=iden
        self.disponible=True
        self.__balon=balon.Balon()
        self.__estadisticas=estadisticas.Estadisticas()
        self.__jugadores={}
        
        
    def add_player(self,net,playerid):
        self.equipos[self.equipo_disponible].append(playerid)
        start_new_thread(self.__threaded_client,(net,playerid,self.equipo_disponible))
        self.__comprobar_disponibilidad()
        
    def __threaded_client(self,net,playerid,equipo):
        info_out=f"sala:{self.id} equipo: {equipo}"
        self.enviar(net,info_out)
        
        while True:
            try:
                info_in=self.leer(net)
                
                if not(info_in):
                    print(f"Desconectado: {playerid}")
                else:
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
        if len(self.equipoA)+len(self.equipoB)==4:
            self.disponible=False
        else:
            if len(self.equipoA) < self.MAX_JUGADORES_TEAM:
                self.equipo_disponible='A'
            else:
                self.equipo_disponible='B'    
    
    def esta_disponible(self):
        return self.disponible        