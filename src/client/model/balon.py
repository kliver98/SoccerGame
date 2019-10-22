
class Balon():
    
    #Constantes
    LOCACION_RESOURCES = "../../../resources/"
    """Constante de la ruta basica y plana de balon"""
    IMAGEN_BALON = f"{LOCACION_RESOURCES}images/ball_roll"
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
        self.__numero_de_imagen = self.__numero_de_imagen if self.__numero_de_imagen<7 else 1
        imagen = f"{self.IMAGEN_BALON}{self.__numero_de_imagen}{self.EXTENCION_DE_IMAGEN}"
        self.__numero_de_imagen+=1
        return imagen
    
    def actualizar_datos(self, x, y, usuario, tipo = True):
        """Metodo que mueve las coordenadas de la imagen del balon, cambia el numero de imagen, modifica el nombre del jugador que tiene el
            balon y retorna ruta generada con angulo de imagen"""
        if not tipo:
            return (self.configurar_imagen(),self.__angulo)
        self.__angulo = 0 if self.__angulo>360 else self.__angulo+5
        self.__coordenadas = (x,y)
        imagen = self.configurar_imagen()
        self.__usuario = usuario
        return (imagen,self.__angulo)
    
    def set_coordenadas(self,x,y):
        self.__coordenadas = (self.__coordenadas[0]+x,self.__coordenadas[1]+y)
    
    def get_coordenadas(self):
        """Metodo que retorna tupla de las coordenadas x,y del balon"""
        if self.__coordenadas == None:
            self.__coordenadas = (350,300)
        return self.__coordenadas
    
    def get_usuario(self):
        return self.__usuario