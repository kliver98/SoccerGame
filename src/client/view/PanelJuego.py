#Class: MainWindow
import pygame
import threading
# Inicializamos pygame
pygame.init()
"""Esta es la clase que representa la ventana de juego(Login) de un cliente"""
   
"""Inicio de la clase"""


class    PanelJuego():    
    """Constantes de la clase"""

    NOMBRE_EQUIPO_UNO = 'EQUIPO ROJO'
    NOMBRE_EQUIPO_DOS = 'EQUIPO AZUL'
    PRIMER_TIMEPO = '1er TIEMPO'
    SEGUNDO_TIMEPO = '2do TIEMPO'
    ANCHO_ALTO = 960,650
    NOMBRE_VENTANA = 'SoccerGame'
    
    #-------COLORES USADOS----
    BLANCO = (255,255,255)
    ROJO = (225,0,0)
    NEGRO = (0,0,0)
    AZUL = (0,0,255)
    
    #--------FUENTES DE LETRA USADOS-----
    FUENTE_LETRAS = 'freesansbold.ttf'
    
    #--------RUTAS DE IMAGENES USADAS-----------
    IMAGEN_CAMPO_DE_JUEGO = "../../../resources/images/soccer_field3.jpg"
    IMAGEN_RELOJ_CRONOMETRO = "../../../resources/images/clock.png"
    
    """Atributos de la clase"""    
    __pantalla = None # variable que almacena la pantalla a mostrar
    __timepoPartido = None # tiempo en que va el partido dado en segundos
    __macadorEquipoUno = None # goles anotados por el equipo uno
    __macadorEquipoDos = None # goles anotados por el equipo dos 
    __parteDeJuego = None # parte en la que se encuentra el partido
    __controlador = None # controlador que conecta con el modelo
    
    """Metodo constructor de la clase"""
    def __init__(self):
        pass
    def ventana(self,controlador):
        self.controlador = controlador
        self.parteDeJuego = self.PRIMER_TIMEPO
        self.timepoPartido = '000'
        self.macadorEquipoUno = '00'
        self.macadorEquipoDos = '00'
        
        #-------------------INICIALIZACION DE LA VENTANA-------------
        self.pantalla = pygame.display.set_mode(self.ANCHO_ALTO) #Muestro una ventana con dimensiones definidas en la constante ANCHO_ALTO 
        self.pantalla.fill(self.BLANCO) #pone fondo blanco a la pantalla
        pygame.display.set_caption(self.NOMBRE_VENTANA) #pone el nombre a la ventana
        pygame.display.flip() #actualiza toda la ventana
        
        #-------------------INICIALIZACION DE LAS FUENTES A USAR-------------        
        fuenteNombresDeEquipo = pygame.font.Font(self.FUENTE_LETRAS, 45)# define el tipo de letra y el tamanho de la letra
        fuenteTiempo = pygame.font.Font(self.FUENTE_LETRAS, 25)# define el tipo de letra y el tamanho de la letra
        fuentePuntaje = pygame.font.Font(self.FUENTE_LETRAS, 45)# define el tipo de letra y el tamanho de la letra
        
        #-------------------------CREACION DE LOS TEXTOS----------------------
        nombreEquipo1 = fuenteNombresDeEquipo.render(self.NOMBRE_EQUIPO_UNO, True, self.ROJO, self.BLANCO) # texto del nombre del equipo 1
        nombreEquipo2 = fuenteNombresDeEquipo.render(self.NOMBRE_EQUIPO_DOS, True, self.AZUL, self.BLANCO) # texto del nombre del equipo 2
        parteDelPartido = fuenteTiempo.render(self.parteDeJuego, True,self.NEGRO, self.BLANCO) # texto de la parte en que va el partido
        tiempo = fuenteTiempo.render(self.timepoPartido, True, self.NEGRO, self.BLANCO)# texto del tiempo transcurrido por el partido
        puntajeEquipoUno= fuentePuntaje.render(self.macadorEquipoUno, True, self.NEGRO,self.BLANCO)# texto del marcador del equipo uno
        puntajeEquipoDos = fuentePuntaje.render(self.macadorEquipoDos, True, self.NEGRO, self.BLANCO)# texto del marcador del equipo dos

        #----------------------------DELINEAR BORDES DE LOS NOMBRES DE EQUIPO-----------
        pygame.draw.rect(nombreEquipo1, self.NEGRO, nombreEquipo1.get_rect(), 1)# pinta el borde del recuadro del nombre del equipo 1
        pygame.draw.rect(nombreEquipo2, self.NEGRO, nombreEquipo2.get_rect(), 1)# pinta el borde del recuadro del nombre del equipo 2
        
        #----------------------------INICIALIZACION DE LAS IMAGENES A MOSTRAR EN EL PANEL--------------------
        imagenCampoDeJuego = pygame.image.load(self.IMAGEN_CAMPO_DE_JUEGO)# cargar la imagen del campo de futbol
        imgagenReloj = pygame.image.load(self.IMAGEN_RELOJ_CRONOMETRO)# cargar la imagen del reloj cronometro
        imgagenReloj = pygame.transform.scale(imgagenReloj, (30,26))# cambiar tamanho de la imagen del reloj cronometro
     
        #------------------------------MOSTRAR TEXTO E IMAGENES EN EL PANEL-----------------
        self.pantalla.blit(nombreEquipo1,(0,0)) # muestra el nombre del equipo uno en la posicion 0,0 del panel
        self.pantalla.blit(nombreEquipo2,(652,0)) # muestra el nombre del equipo dos en la posicion 652,0 del panel
        self.pantalla.blit(parteDelPartido,(400,0)) # muestra en que parte del partido va el juego en la posicion 400,0 del panel
        self.pantalla.blit(tiempo,(450,26)) # muestra el tiempo recorrido en el partido en la posicion 450,26 del panel
        self.pantalla.blit(puntajeEquipoUno,(320,0)) # muestra el puntaje del equipo uno en la posicion 320,0 del panel
        self.pantalla.blit(puntajeEquipoDos,(595,0)) # muestra el puntaje del equipo dos en la posicion 595,0 del panel
        self.pantalla.blit(imagenCampoDeJuego,(0,50)) # muestra la imagen del campo de juego en la posicion 0,50 del panel
        self.pantalla.blit(imgagenReloj,(410,21)) #  muestra la imagen del reloj cronometro en la posicion 410,21 del panel
        
                
        pygame.display.update() #actualiza toda la ventana
        
        salir=False
        while not salir:
        
            for event in pygame.event.get():
                # Si el evento es salir de la ventana, terminamos
                if event.type == pygame.QUIT: salir = True
                """Si el evento es que presiono alguna tecla"""
                if event.type == pygame.KEYDOWN:
                    """verificamos cual fue la que presiono"""
                    if event.key == pygame.K_RIGHT :  
                        controlador.mover_jugador(False,True,False,False)
                    if event.key == pygame.K_LEFT : 
                        controlador.mover_jugador(True,False,False,False)
                    if event.key == pygame.K_UP : 
                        controlador.mover_jugador(False,False,True,False)
                    if event.key == pygame.K_DOWN : 
                        controlador.mover_jugador(False,False,False,True)
                        
            #Traemos el arreglo que contiene  los datos de los jugadores 
            jugadores = controlador.get_datos_jugadores()
            # Se recorre el arreglo 
            for i in jugadores:
                datosJugador = jugadores[i].split('-')
                imagenJugador = pygame.image.load(datosJugador[4]) #se toman la ruta de la imagen
                imagenJugador = pygame.transform.rotate(imagenJugador, int(datosJugador[0])) # se rota la imagen dado el numero del angulo de la rotacion
                self.pantalla.blit(imagenJugador,(int(datosJugador[2]),int(datosJugador[3]))) # se pone la imagen en la pantalla en las coordenadas x-y
             
            posicionBalon = controlador.get_posicion_balon().split('-') # se obtiene la posicion del balon
            rutaImagenBalon = controlador.get_imagen_balon().split('-')[0] # se obtiene la ruta de la imagen del balon
            anguloImagenBalon = controlador.get_imagen_balon().split('-')[1] # se obtiene el angulo de la rotacion de la imagen
            imagenBalon = pygame.image.load(rutaImagenBalon)# se caraga la imagen del balon
            imagenBalon = pygame.transform.rotate(imagenBalon, int(anguloImagenBalon)) # se rota la imagen del balon dado el numero del angulo de la rotacion
            self.pantalla.blit(imagenBalon,(int(posicionBalon[0]),int(posicionBalon[1])))   # se pone la imagen del balon en la pantalla en las coordenadas x-y 
    
            
            pygame.display.update()
        
        
    
panel = PanelJuego()
panel.ventana()