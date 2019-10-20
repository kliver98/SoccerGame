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

    def ventana_preguntar_usuario(self):
        root = tk.Tk()
        root.withdraw()
        x = ((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2)-120
        y = ((root.winfo_screenheight() - root.winfo_reqheight()) / 2)-60
        root.geometry("+%d+%d" % (x, y))
        root.update()
        text = simpledialog.askstring(title="Informacion",
                                  prompt="Ingrese su nombre de usuario con el cual se identificara: ")
        root.destroy()
        return text
    
    def dibujar_texto(self, text, size,coord):
        pg.font.init()
        mf = pg.font.SysFont('Century',size)
        ts = mf.render(text,False,(0,0,0))
        self.window.blit(ts,coord)

    def mostrar_mensaje(self, title, body):
        ctypes.windll.user32.MessageBoxW(0, body, title, 1)
    
    def cerrar_aplicacion(self):
        sys.exit()
        
    def actualizar_pantalla_jugando(self, jugadores, usuario_de_jugador):
        """Update the window with their new graphics"""
        self.pintar_fondo()
        #Pinto los jugadores. Todos
        pg.display.update()
    
    def pintar_fondo(self):
        imagen= pg.image.load(self.controlador.get_ruta_imagen_campo())
        imagen = pg.transform.scale(imagen,(ANCHO,ALTO))
        self.window.blit(imagen,[0,0])
        pg.display.update()
    
    def iniciar(self):
        self.controlador.iniciar_partido(self.usuario_de_jugador,2)
        self.pintar_fondo()
        #Seleccionar modo
        modo = self.modo_juego()
        print(f"modo: {modo}")
        
    def modo_juego(self):
        self.clock.tick(30)
        modo = MODO_JUEGO_ONLINE
        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
            self.dibujar_texto("Seleccione el modo para jugar", int(ALTO*0.09), (int((ANCHO/2)-ANCHO*0.35),ALTO*0.15))
            max_jug_equipo = self.controlador.get_max_jugadores_equipo()
            self.dibujar_texto(f"A. {max_jug_equipo} vs {max_jug_equipo}", int(ALTO*0.08) , (int((ANCHO/2)-ANCHO*0.07),ALTO*0.35) )
            self.dibujar_texto(f"B. {max_jug_equipo} vs PC", int(ALTO*0.08) , (int((ANCHO/2)-ANCHO*0.07),ALTO*0.55) )
            self.dibujar_texto(
                                "Guia rapida: Esta pantalla te permite seleccionar el modo de juego, online o contra la computadora."
                                ,int(ALTO*0.033) , (ANCHO*0.05,ALTO*0.8) )
            self.dibujar_texto(
                                "Los controles en el juego son: teclas arriba, abajo, izquierda, derecha. Para patear/robar: x/z"
                                ,int(ALTO*0.033) , (ANCHO*0.05,ALTO*0.85) )
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
        while run:
            pass
        
    def setup(self):
        """Get ready the main window and others nee-ded"""
        os.environ['SDL_VIDEO_CENTERED'] = '1' #Para centrar en el medio la ventana
        self.window = pg.display.set_mode((ANCHO,ALTO))
        self.controlador = controlador.Controlador()
        pg.display.set_caption(self.controlador.get_nombre_aplicacion())
        self.usuario_de_jugador = self.ventana_preguntar_usuario()
        self.clock = pg.time.Clock()
        pg.init()

"""Start the application"""
try:
    VentanaPrincipal()
except Exception as e:
    print(e.trace())
    pass