

class Balon:
    ''' atributos del balon en el servidor'''
    __coordenadas=None
    __username=None
    __posesionA=None
    __posesionB=None
    
    def __init__(self,coordenadas_inicio):
        self.__coordenadas = coordenadas_inicio
    
    
    '''funcion que retorna la posicion del balon como una tupla'''  
    def get_coordenadas(self):
        return self.__coordenadas