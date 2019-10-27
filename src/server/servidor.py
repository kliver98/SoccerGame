import socket
import sys
from server import sala
from server import publicidadController

MAX_JUGADORES=30
CONEXIONES_ESPERA=10
jugadores={}
salas=[]


'''se piden los parametros para iniciar el servidor'''
server = "localhost"#input("Please insert the ip server, it will be localhost for defect")
port = 5558
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

''' se inicia el servidor con los parametros'''
try:
    if server is None:
        server="localhost"
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(CONEXIONES_ESPERA)
print("server was started, waiting for connections")

def verificar_disponible():
    sa=None
    for i in salas:
        if i.esta_disponible():
            return i
    return sa

publicidad=publicidadController.PublicidadController(server)
publicidad.correr()

currentPlayer=0
currentRoom=0
while True:
    '''tupla (socket asignado, mensaje de direccion) al aceptar un cliente'''
    net, addr = s.accept() 
    print("Connected to:", addr)#notificacion de cliente conectado, reportando su ip
    sa=verificar_disponible()
    if not sa:
        sa= sala.Sala(currentRoom)
        salas.append(sa)
        currentRoom+=1
    sa.add_player(net,currentPlayer)
    currentPlayer+=1
    '''TODO:  logica para crear salas, asignar jugadores a una sala'''