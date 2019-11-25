from client.bots.node import node
import math
from server.servidor import jugadores
import constantesCompartidas as cc

RADIUS_PLYS_AROUND = 10
distance = lambda node1,node2: math.sqrt((node1.coord[0]-node2.coord[0])**2 + (node1.coord[1]-node2.coord[1])**2)
def num_jug_alred(actual, equipoContrario):
        for player in equipoContrario:
            dist = distance(actual,player)
            if dist<=RADIUS_PLYS_AROUND:
                actual.increase_n_around()

class ai():
    #Esta "Inteligencia" es probabilistica, no memoriza
    
    def __init__(self):
        pass
            
    def buscar(self, usuario, jugadores):
        for i in jugadores:
            if i.get_usuario()==usuario:
                return i
        return None
        
    def get_min(self, jugadores, balon):
        m = node((0,0),"")
        m.w = 100000000
        for i in jugadores:
            if i.w<m.w and balon.get_usuario()!=i.username:
                m = i
        return m
    
    def get_direction_to_ball(self, jug, bal):
        bX = bal.get_coordenadas()[0]
        bY = bal.get_coordenadas()[1]
        jX = jug.coord[0]
        jY = jug.coord[1]
        coord = (jug.coord[0],jug.coord[1])
        
        if jX<bX:
            coord = (coord[0]+cc.VELOCIDAD_JUGADOR,coord[1])
        else:
            coord = (coord[0]-cc.VELOCIDAD_JUGADOR,coord[1])
        
        if jY<bY:
            coord = (coord[0],coord[1]-cc.VELOCIDAD_JUGADOR)
        else:
            coord = (coord[0],coord[1]+cc.VELOCIDAD_JUGADOR)
        
        return coord
         
    def calcular(self, juagdores, balon):
        #Devuelve, ejemplo: [["test1",(100,153)],["test3",(400,352)]] indicando el nombre y coordenadas del jugador a actualizar
        nodes = []
        equipoA = []
        equipoB = []
        dir1 = []
        dir2 = []
        
        for actual in juagdores:
            n = node(actual.get_coordenadas(),actual.get_usuario(),actual.get_equipo())
            nodes.append(n)
            n.set_dist_to_ball(distance(n,balon)) #Paso 1, calcular distancias al balon. Equivalente Capa 1
            if actual.get_equipo()=="A":
                equipoA.append(n)
            else:
                equipoB.append(n)
        
        for actual in nodes:
            num_jug_alred(actual, equipoB if actual.get_equipo()=="A" else equipoA) #Paso 2, calcular numero de jugadores alrededor de cada uno segun radio definido
            
        aux = self.buscar(balon.get_usuario(),jugadores)
        
        if aux: #Si hay un jugador que tiene el balon, hay que ver si no es cliente y llevarlo al arco
            pass
        else: #Nadie tiene el balon
            #Calculo para que se mueva tanto 1 jugador de A como 1 de B
            for actual in nodes:
                actual.calculate_weight() #Empieza paso 3, multiplico jugadores alrededor contrarios * distancia al balon
            jugA = self.get_min(equipoA,balon)
            jugB = self.get_min(equipoB,balon)
            
            dir1 = [jugA.username,self.get_direction_to_ball(jugA)]
            dir2 = [jugB.username,self.get_direction_to_ball(jugB)]
            
        return [dir1,dir2]
            
