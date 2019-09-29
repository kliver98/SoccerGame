

class Balon:
    ''' atributos del balon en el servidor'''
    __coordenada=None
    __username=None
    __posesionA=None
    __posesionB=None
    
    def __init__(self):
        pass
    
    
    '''funcion que retorna la posicion del balon como una tupla'''  
    def get_coordenada(self):
        return self.__coordenada