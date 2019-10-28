from client.model import cliente_UDP
import _thread
import numpy
import pickle
import cv2

class CapturadorUDP():
  
    
    def __init__(self):
        self.reproducir=True
        self.cliente=cliente_UDP.ClienteUDP()
        
    def correr(self):
        _thread.start_new_thread(self.__solicitar_publicidad, ())
       
        
    
    def __solicitar_publicidad(self):
        self.cliente.enviar(bytes('conectar','utf-8'))
        try:
            while True:
                data,address=self.cliente.recibir()
                #print(data)
                if data is None:
                    break
                raw = numpy.frombuffer(pickle.loads(data),numpy.uint8)
                frame=cv2.imdecode(raw,cv2.IMREAD_COLOR)
                if self.reproducir :
                    cv2.imshow('Ad',frame)
                else:
                    break
                
                salir=cv2.waitKey(33)
                if salir==27: # tecla esc para detener ventana de publicidad
                    break
        except Exception as e:
            print(e)
        self.finish()           
        
    def finish(self):
        self.cliente.enviar(bytes('close','utf-8'))
        self.reproducir=False
        cv2.destroyAllWindows()
        self.cliente.close()  
             
        
   