from openCvTools import loader
from server import servidor_UDP
import _thread
import pickle
import time

class PublicidadController:
    
    
    def __init__(self,server):
        self.server=server
        self.udp=servidor_UDP.Servidor_UDP()
        self.vid=loader.VideoLoader("publicidad1.mp4")
        self.clientes_activos=[]
    
    def correr(self):
        _thread.start_new_thread(self.__gestionar_clientes, ())
        
        
    def __enviar_publicidad(self,server,port):
        print('inicia a enviar publicidad')
        address=(server,port)
        try:
            for frame in self.vid.get_encode_frames():
                if address in self.clientes_activos:
                    self.udp.enviar(pickle.dumps(frame), address)
                    time.sleep(self.vid.get_dealy())
            self.udp.enviar(bytes('close','utf-8'), address)
        except Exception as e:
            print(e)

    def __gestionar_clientes(self):
        while True:
            data,address =self.udp.recibir()
            #print(f'{address} dice {data}')
            if 'close' in str(data):
                self.clientes_activos.remove(address)
            elif not address in self.clientes_activos :
                self.clientes_activos.append(address)
                _thread.start_new_thread(self.__enviar_publicidad, address)
    


