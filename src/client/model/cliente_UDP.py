import socket


class ClienteUDP():
    server="localhost"
    port=13060
    BUFFER_SIZE=2**16
    
    def __init__(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.address=(self.server,self.port)
        
        
    def enviar(self,data):
        self.sock.sendto(data,self.address)
        
    def recibir(self):
        data,address=self.sock.recvfrom(self.BUFFER_SIZE)
        return data,address
    
    def close(self):
        self.sock.close()