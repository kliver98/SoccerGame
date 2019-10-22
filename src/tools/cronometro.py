from time import sleep
import _thread

class Cronometro:
    MODO_CRONOMETRO="C"
    MODO_TEMPORIZADOR="T"
    
    def __init__(self):
        self.cuenta=-1
    
    def iniciar(self,tiempo,modo):
        _thread.start_new_thread(self.__correr_hilo, (tiempo,modo))
    
    def __correr_hilo(self,tiempo,modo):
        if modo == self.MODO_CRONOMETRO:
            self.__iniciar_cronometro(tiempo)
        elif modo == self.MODO_TEMPORIZADOR:
            self.__iniciar_temporizador(tiempo)    
        
        
            
    def __iniciar_temporizador(self,tiempo):
        for i in range(0,tiempo):
            self.cuenta=tiempo-i
            sleep(1)
            
    def __iniciar_cronometro(self,tiempo):
        for i in range(0,tiempo):
            self.cuenta=i
            sleep(1)
            
    def get_cuenta(self):
        return self.cuenta