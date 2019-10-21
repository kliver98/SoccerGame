import tkinter as tk
from tkinter import simpledialog
import pygame as pg
import os
from client.controller import controlador
import sys
import ctypes
ALTO = 550
ANCHO = 900
MODO_JUEGO_ONLINE = 1
MODO_JUEGO_LOCAL = 2

class VentanaPrincipal():
    
    window = None
    controlador = None
    
    def __init__(self):
        self.setup()
        self.iniciar()

    def ventana_preguntar(self, msj):
        root = tk.Tk()
        root.withdraw()
        x = ((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2)-128
        y = ((root.winfo_screenheight() - root.winfo_reqheight()) / 2)-60
        root.geometry("+%d+%d" % (x, y))
        root.update()
        text = simpledialog.askstring(title="Informacion",
                                  prompt=msj)
        root.destroy()
        return text
    
    def dibujar_texto(self, text, size,coord, color = (0,0,0), negrita = False):
        pg.font.init()
        mf = pg.font.SysFont('Century',size)
        ts = mf.render(text,negrita,color)
        self.window.blit(ts,coord)

    def mostrar_mensaje(self, title, body):
        ctypes.windll.user32.MessageBoxW(0, body, title, 1)
    
    def cerrar_aplicacion(self):
        sys.exit()
    
    def actualizar_pantalla_jugando(self, jugadores):
        """Update the window with their new graphics"""
        self.pintar_fondo()
        self.dibujar_texto(f"Tiempo: {int(self.sg)}", int(ANCHO*0.025), [ANCHO*0.43,ALTO*0.02], (0, 0, 0), True)
        #Pinto los jugadores. Todos
        separador = self.controlador.get_separador()
        for j in jugadores:
            datos = j.split(separador)
            imagen = pg.image.load(datos[4])
            imagen = pg.transform.rotate(imagen, int(datos[5]))
            eje_x = int(datos[2]) 
            eje_y = int(datos[3])
            self.window.blit(imagen.convert_alpha(),[eje_x,eje_y])
        pg.display.update()
    
    def pintar_fondo(self, menu = False):
        if menu:
            imagen= pg.image.load("../../../resources/images/fondo.jpg")
            imagen = pg.transform.scale(imagen,(ANCHO,ALTO))
            self.window.blit(imagen,[0,0])
            pg.display.update()
            return
        imagen= pg.image.load(self.controlador.get_ruta_imagen_campo())
        imagen = pg.transform.scale(imagen,(ANCHO,ALTO))
        self.window.blit(imagen,[0,0])
        pg.display.update()
    
    def iniciar(self):
        if not self.usuario_de_jugador:
            self.cerrar_aplicacion()
        self.pintar_fondo(menu = True)
        ip = None
        while not ip:
            #Seleccionar modo
            modo = self.modo_juego()
            #Preparar partido
            if modo==MODO_JUEGO_LOCAL: #Preparar bots
                self.controlador.iniciar_partido(self.usuario_de_jugador,2)
                self.controlador.iniciar_bots() #Crea los jugadores bots al igual que el jugador del equipo del cliente
                self.jugando()
                self.pintar_fondo(menu = True)
            else: #Quiere jugar online
                ip = self.ventana_preguntar("Ingrese la direccion IP del servidor a conectarse: ")
                if not ip or not self.controlador.esta_formatoIP_bien(ip):
                    ip = None
                    continue
                self.pintar_fondo(menu = True)
                self.dibujar_texto("Esperando jugadores...", int(ANCHO*0.06), (int(ANCHO*0.1855),int(ALTO*0.45)))
                pg.display.update()
                self.controlador.iniciar_partido(self.usuario_de_jugador,2,ip) #DESCOMENTAR PARTE QUE INICIA EL SERVIDOR <-------------------- OJO. Ahi inicia conexion
                #for i in range(0,500000): #Para probar pantalla espera
                 #   print(f"Probando{i}")
                
        self.iniciar() #Para que se cierre la aplicacion solo cuando el usuario de clic en x de la ventana
        
    def modo_juego(self):
        modo = MODO_JUEGO_ONLINE
        run = True
        while run:
            self.clock.tick(15)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
            self.dibujar_texto("Seleccione el modo para jugar", int(ANCHO*0.055), (int((ANCHO/2)-ANCHO*0.37),ALTO*0.15))
            max_jug_equipo = self.controlador.get_max_jugadores_equipo()
            self.dibujar_texto(f"a. {max_jug_equipo} vs {max_jug_equipo}", int(ANCHO*0.053) , (int((ANCHO/2)-ANCHO*0.102),ALTO*0.35) )
            self.dibujar_texto(f"b. {max_jug_equipo} vs PC", int(ANCHO*0.05) , (int((ANCHO/2)-ANCHO*0.112),ALTO*0.55) )
            self.dibujar_texto(
                                "Guia rapida: Esta pantalla te permite seleccionar el modo de juego, presione la tecla correspondiente."
                                ,int(ANCHO*0.02) , (ANCHO*0.05,ALTO*0.8))
            self.dibujar_texto(
                                "Los controles en el juego son: teclas arriba, abajo, izquierda, derecha. Para patear/robar: x/z"
                                ,int(ANCHO*0.02) , (ANCHO*0.05,ALTO*0.85))
            pg.display.update()
            if pg.key.get_pressed()[pg.K_a]:
                modo = MODO_JUEGO_ONLINE
                run = False
            elif pg.key.get_pressed()[pg.K_b]:
                modo = MODO_JUEGO_LOCAL
                run = False
            
        return modo
        
    def jugando(self):
        run = True
        start_ticks = pg.time.get_ticks()
        tiempos = self.controlador.get_tiempos() #Arreglo, en 0 esta tiempo juego de 1 tiempo partido, en 1 tiempo para anuncio
        while run:
            self.clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
            coord_ant = self.controlador.get_coordenadas_cliente()
            c = (0,0)
            keys = pg.key.get_pressed()
            if keys[pg.K_UP]:
                c = (0,-1)
                self.controlador.set_coordenadas_jugador_cliente(c)
            if keys[pg.K_DOWN]:
                c = (0,1)
                self.controlador.set_coordenadas_jugador_cliente(c)
            if keys[pg.K_LEFT]:
                c = (-1,0)
                self.controlador.set_coordenadas_jugador_cliente(c)
            if keys[pg.K_RIGHT]:
                c = (1,0)
                self.controlador.set_coordenadas_jugador_cliente(c)
            if not self.controlador.esta_jugador_dentro_campo((ANCHO,ALTO)):
                self.controlador.set_coordenadas_jugador_cliente(coord_ant, True)
                continue
            self.sg = (pg.time.get_ticks()-start_ticks)/1000 #Segundos transcurridos del juego
            if int(self.sg)==tiempos[0]:
                self.cargar_anuncio(tiempos[1])
            elif int(self.sg)>(tiempos[0]*2+tiempos[1]):
                run = False
            self.actualizar_pantalla_jugando(self.controlador.get_datos_jugadores())
    
    def cargar_anuncio(self, tiempo):
        start_ticks = pg.time.get_ticks()
        run = True
        while run:
            self.clock.tick(5) #Dado que solo se reproducira audio no hay problema con 5fps
            sg = (pg.time.get_ticks()-start_ticks)/1000 #Segundos transcurridos del juego
            self.pintar_fondo(True)
            self.dibujar_texto(f"Tiempo restante: {int(tiempo-sg)}", int(ANCHO*0.02), [ANCHO*0.42,10])
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
            if sg>tiempo:
                run = False
                continue
    
    def setup(self):
        """Get ready the main window and others nee-ded"""
        os.environ['SDL_VIDEO_CENTERED'] = '1' #Para centrar en el medio la ventana
        self.window = pg.display.set_mode((ANCHO,ALTO))
        self.controlador = controlador.Controlador()
        pg.display.set_caption(self.controlador.get_nombre_aplicacion())
        self.usuario_de_jugador = self.ventana_preguntar("Ingrese su nombre de usuario con el cual se identificara: ")
        self.clock = pg.time.Clock()
        pg.init()

"""Start the application"""
try:
    VentanaPrincipal()
except Exception as e:
    #print(e.trace())
    pass