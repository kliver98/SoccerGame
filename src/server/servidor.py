import socket
import sys
from server import sala

MAX_JUGADORES=30
CONEXIONES_ESPERA=10
jugadores={}
salas={}


'''se piden los parametros para iniciar el servidor'''
server = input("Please insert the ip server, it will be locallhost for defect")
port = 5555
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


while True:
    '''tupla (socket asignado, mensaje de direccion) al aceptar un cliente'''
    net, addr = s.accept() 
    print("Connected to:", addr)#notificacion de cliente conectado, reportando su ip
    
    
    '''TODO:  logica para crear salas, asignar jugadores a una sala'''