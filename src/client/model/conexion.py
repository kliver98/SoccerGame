import socket

class Conexion():
    
    BUFFER_SIZE=2048
    
    def __init__(self,ip):
        '''inicializa la coneccion con el servidor'''
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip
        self.port = 5558
        self.addr = (self.server, self.port)
        print(self.addr)
        self.info = self.conectar()
        print(f"info: {self.info}")
     
    def  conectar(self):
        '''metodo para conectar el cliente con el servidor'''
        try:
            self.client.connect(self.addr)
            return self.client.recv(self.BUFFER_SIZE).decode()
        except Exception as e:
            print('Error al intentar conectar el cliente con el servidor')
            print(e.trace_call())
            
       
    def getInfo(self):
        '''funcion que retorna la ultima cadena de informacion recibida'''
        return self.info
    
    def enviar(self,datos):
        '''funcion que envia los datos al servidor y retorna la informacion que replica el servidor
        datos: datos a enviar
        return: informacion proveniente del servidor'''
        try:
            self.client.send(str.encode(datos))
            return self.client.recv(self.BUFFER_SIZE).decode()
        except socket.error as e:
            print("Error de conexion al enviar informacion")
            print(e)
        