import socket
import _thread
from client.model import partido

class Conexion():
    
    BUFFER_SIZE=2048
    
    def __init__(self,ip,partido):
        '''inicializa la coneccion con el servidor'''
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip
        self.port = 5558
        self.addr = (self.server, self.port)
        print(self.addr)
        self.partido=partido
        self.info = self.conectar()
        print(f"info: {self.info}")
        params=self.info.split(';')
        self.posicion_entrada=params[0]
        self.equipo=params[1]
        self.nombre=self.partido.get_usuario_de_jugador()
        
        
        self.__iniciar_huesped(self.posicion_entrada,self.nombre,self.equipo)
        self.coor=self.partido.get_coordenadas_cliente()
        self.info_out=f"({self.nombre},{self.equipo},{self.coor}"
     
    def __iniciar_huesped(self,posicion,nombre,equipo):
        coordenadas=self.partido.coordenadas_defecto(posicion)
        self.partido.agregar_jugador(nombre,equipo,coordenadas)
    
    
    def  conectar(self):
        '''metodo para conectar el cliente con el servidor'''
        try:
            self.client.connect(self.addr)
            return self.client.recv(self.BUFFER_SIZE).decode()
        except Exception as e:
            print('Error al intentar conectar el cliente con el servidor')
            print(e.trace_call())
    
    def correr(self):
        _thread.start_new_thread(self.__threaded_conexion,())   
      
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
            self.close()
    
    def __threaded_conexion(self):
        print("entro")
        while True:
            try:
                self.info=   self.enviar(self.info_out)
                print(f"entrada = {self.info}")
            except Exception as e:
                print(e.trace_call())        
                self.close()
    
    def set_info_out(self,info):
        self.info_out=info
                    
    def close(self):
        self.client.close()
        print("La conexion cliente se ha cerrado")    