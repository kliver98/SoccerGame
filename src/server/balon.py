

class Balon:
    ''' atributos del balon en el servidor'''
    __coordenadas=None
    __usuario=None
    __posesionA=None
    __posesionB=None
    
    def __init__(self,coordenadas_inicio):
        self.__coordenadas = coordenadas_inicio
        self.__usuario = ""
    
    '''funcion que retorna la posicion del balon como una tupla'''  
    def get_coordenadas(self):
        return self.__coordenadas
    
    def set_coordenadas(self,x,y):
        self.__coordenadas = (x,y)
    
    def get_usuario(self):
        return self.__usuario
    
    def set_usuario(self,nuevo_usuario):
        self.__usuario = nuevo_usuario