
import socket

class Network():
     # connection controller to client, it require the ip of the server to be init
    def __init__(self,ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        
   #     self.send("1")
        
        
# funcion que recibe la informacion de las posiciones de los objetos desde el sefvidor
    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
        
# funcion que envia informacion al servidor
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
         
    def run_network(self):        
        run=True
        while run:
            self.send("1,1")
        