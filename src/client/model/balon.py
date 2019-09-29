from client.model import aplicacion

class Balon():
    
    #Constantes
    """Constante de la ruta basica y plana de balon"""
    IMAGEN_BALON = f"{aplicacion.LOCACION_RESOURCES}images/ball_roll"
    """Constante string del tipo de extension de las imagenes que representan al jugador"""
    EXTENCION_DE_IMAGEN = ".png"
    
    #Atributos
    """Atributo numero entero que representa el numero de imagen de balon"""
    __numero_de_imagen = None
    """Atributo tupla que tiene informacion de las coordenadas del balon"""
    __coordenadas = None
    """Atributo string que referencia al nombre de usuario unico que tiene el balon"""
    __usuario = None
    """Atributo numero entero que tiene el angulo de rotacion del balon"""
    __angulo = None
    
    def __init__(self):
        """Constructor que inicializa numero de imagen, usuario y angulo del balon"""
        self.__numero_de_imagen = 1
        self.__usuario = ""
        self.__angulo = 0
        
    def configurar_imagen(self):
        """Metodo que crea la ruta de imagen del jugador dependiendo de que imagen cargar, de las tres disponibles, y retorna la ruta generada"""
        self.__numero_de_imagen = self.numero_de_imagen if self.numero_de_imagen<7 else 1
        imagen = f"{self.IMAGEN_BALON}{self.numero_de_imagen}{self.EXTENCION_DE_IMAGEN}"
        self.__numero_de_imagen+=1
        return imagen
    
    def mover(self, x, y):
        """Metodo que mueve las coordenadas de la imagen del balon, cambia el numero de imagen y retorna ruta generada con angulo de imagen"""
        self.__angulo = 0 if self.__angulo<361 else self.__angulo+5
        self.__coordenadas = (x,y)
        imagen = self.configurar_imagen()
        return (imagen,self.__angulo)