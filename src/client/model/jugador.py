import random

class Jugador():

    #Constantes
    LOCACION_RESOURCES = "../../../resources/"
    """Constante string que contiene la ruta basica y plana del recurso de imagen que representa el jugador A, sin numero de imagen ni extension"""
    IMAGEN_JUGADOR_A = f"{LOCACION_RESOURCES}images/playerBlack"
    """Constante string que contiene la ruta basica y plana del recurso de imagen que representa el jugador B, sin numero de imagen ni extension"""
    IMAGEN_JUGADOR_B = f"{LOCACION_RESOURCES}images/playerWhite"
    """Constante string del tipo de extension de las imagenes que representan al jugador"""
    EXTENCION_DE_IMAGEN = ".png"
        
    #Atributos
    """Atributo string para identificar al jugador"""
    __usuario = None #Las dos lineas bajas son para hacer las variables privadas
    """Atributo A o B para identificar a que equipo pertenece el jugador"""
    __equipo = None
    """Atributo tupla para almacenar las coordenadas x,y donde esta la imagen del jugador"""
    __coordenadas = None
    """Atributo numero entero para identificar la imagen del juegador. Son tres imagenes para simular el movimiento"""
    __numero_de_imagen = None
    """Atributo numero para identificar el angulo de rotacion de la imagen del jugador"""
    __angulo_de_imagen = None
    
    def __init__(self, usuario, equipo, coordenadas):
        """Constructor que recibe el nombre de usuario y el equipo al cual pertenece"""
        self.__usuario = usuario
        self.__equipo = equipo
        if not coordenadas:
            self.__coordenadas = (random.randint(10,850),random.randint(10,500)) #Ver como se cuadra lo de las coordenadas que aparece el jugador
        else:
            self.__coordenadas = coordenadas
        self.__numero_de_imagen = 1
        self.__angulo_de_imagen = 270 if equipo=="A" else 90
    
    def configurar_imagen(self):
        """Metodo que crea la ruta de imagen del jugador dependiendo de que imagen cargar, de las tres disponibles, y retorna la ruta generada"""
        imagen = self.IMAGEN_JUGADOR_A+str(self.__numero_de_imagen)+self.EXTENCION_DE_IMAGEN if self.__equipo=="A" else self.IMAGEN_JUGADOR_B+str(self.__numero_de_imagen)+self.EXTENCION_DE_IMAGEN 
        self.__numero_de_imagen = 1 if self.__numero_de_imagen>2 else self.__numero_de_imagen+1
        return (imagen,self.__angulo_de_imagen)
    
    def mover(self, izquierda, derecha, arriba, abajo):
        """Metodo que mueve las coordenadas de la imagen del jugador, cambia el numero de imagen y retorna tupla de ruta generada con angulo de imagen"""
        
        if izquierda:
            self.set_coordenadas(self.__coordenadas[0]-self.VELOCIDAD, 0)
        if derecha:
            self.set_coordenadas(self.__coordenadas[0]+self.VELOCIDAD, 0)
        if arriba:
            self.set_coordenadas(0, self.__coordenadas[1]-self.VELOCIDAD)
        if abajo:
            self.set_coordenadas(0, self.__coordenadas[1]+self.VELOCIDAD)
    
    def get_datos(self):
        """Metodo que retorna una tupla con la informacion del nombre de usuario, equipo, coordenada en x y coordenada en y"""
        return (self.__usuario,self.__equipo,self.__coordenadas[0],self.__coordenadas[1])
    
    def get_usuario(self):
        """Metodo que devuelve el nombre de usuario"""
        return self.__usuario
    
    def set_coordenadas(self,x,y):
        """Metodo que actualiza la tupla con las coordenadas en x y y del jugador"""
        xx = self.__coordenadas[0] if x==0 else self.__coordenadas[0]+x
        yy = self.__coordenadas[1] if y==0 else self.__coordenadas[1]+y
        self.__coordenadas = (xx,yy)
        
    def reset_coordenadas(self, coord_ant):
        self.__coordenadas = coord_ant
        
    def get_coordenadas(self):
        """Metodo que retorna una tupla con las coordenadas del jugador"""
        return self.__coordenadas
    