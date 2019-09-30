from client.model import aplicacion

class Campo():
    
    #Constantes
    """Constante string que tiene la ruta basica y plana de la imagen que representa el jugador"""
    IMAGEN_CAMPO = f"{aplicacion.LOCACION_RESOURCES}images/soccer_field"
    """Constante string que tiene el tipo de extencion de la imagen del campo"""
    EXTENCION_DE_IMAGEN = ".jpg"
    
    #Atributos
    """Atributo string que contiene la ruta de la imagen del campo"""
    __ruta_imagen = None
    
    def __init__(self, numero_campo):
        """Constructor que recibe el numero de campo de imagen a cargar, por defecto es el 3"""
        numero_campo = numero_campo if (numero_campo>0 and numero_campo<3) else 1
        self.__ruta_imagen = f"{self.IMAGEN_CAMPO}{numero_campo}{self.EXTENCION_DE_IMAGEN}"
    
    def get_ruta_imagen(self):
        """Metodo que retorna la ruta de la imagen que representa el campo"""
        return self.__ruta_imagen