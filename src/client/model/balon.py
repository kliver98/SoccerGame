
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
    VECES_CAMBIAR_IMAGEN = 500
    __contador_cambiar_imagen = None
    
    def __init__(self):
        """Constructor que inicializa numero de imagen, usuario y angulo del balon"""
        self.__numero_de_imagen = 1
        self.__usuario = ""
        self.__angulo = 0
        self.__contador_cambiar_imagen = 0
        
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
        if self.VECES_CAMBIAR_IMAGEN==self.__contador_cambiar_imagen:
            self.__angulo = 0 if self.__angulo>360 else self.__angulo+5
        else:
            self.__contador_cambiar_imagen = self.__contador_cambiar_imagen+1 if self.__contador_cambiar_imagen<self.VECES_CAMBIAR_IMAGEN else 0
        
        self.__coordenadas = (x,y)
        imagen = self.configurar_imagen()
        self.__usuario = usuario
        return (imagen,self.__angulo)
    
    def update_coordenadas(self,coord):
        self.__coordenadas = (coord[0],coord[1])
    
    def set_coordenadas(self,x,y):
        self.__coordenadas = (self.__coordenadas[0]+x,self.__coordenadas[1]+y)
    
    def get_coordenadas(self):
        """Metodo que retorna tupla de las coordenadas x,y del balon"""
        return self.__coordenadas
    
    def get_usuario(self):
        return self.__usuario
    
    def set_usuario(self,nuevo_usuario):
        self.__usuario = nuevo_usuario