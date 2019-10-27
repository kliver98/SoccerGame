import socket

import _thread

class Servidor_UDP:
    server="localhost"
    port=13060
    BUFFER_SIZE=2**16
    
    def __init__(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind((self.server,self.port))
        print("UDP inciiando")
        
    def correr(self):
        print("UDP corriendo")
        _thread.start_new_thread(self.__thread,())
            
   
    def enviar(self,data,address):
        self.sock.sendto(data,address)
        
    def recibir(self):
        data,address= self.sock.recvfrom(self.BUFFER_SIZE)
        return data,address

