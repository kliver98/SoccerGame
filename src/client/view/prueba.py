
import pygame as pg
import os 
import tkinter as tk
from tkinter import simpledialog
import sys
import ctypes
from client.model import aplicacion

class MainWindow():#Hay equipo A y B
    
    ANCHO = 900
    ALTO = 550
    
    """Class principal of the GUI"""
    
    def __init__(self):
        """Builder"""
        self.setup()
        self.init()
        
    def init(self):
        
        self.agregar_jugador("PruebaKG", True)
        self.agregar_jugador("Pepito", True)
        self.agregar_jugador("Juan", False)
        self.agregar_jugador("Alex", False)
         
        run = True
        """Here the application is hearing the keywords pressed"""
        while run:
            """Debo actualizar los datos de los demas jugadores y tambien info del balon"""
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
            """Despues muevo las coordenadas del jugador si el usuario a presionado una tecla. Solo jugador cliente. HACER!!"""
            jugadores = self.model.get_datos_jugadores()
            usuario_de_jugador = self.model.get_usuario_de_jugador()
            """for i in jugadores:
                usuario_cliente = i.split(self.model.get_separador())[0]
                if usuario_cliente!=usuario_de_jugador:
                    self.redrawWindow() #pinto jugadores"""
            self.redraw(jugadores,usuario_de_jugador)
    
    def show_message(self, title, body):
        ctypes.windll.user32.MessageBoxW(0, body, title, 1)
    
    def close_ap(self):
        sys.exit()
    
    def ask_username(self):
        root = tk.Tk()
        root.withdraw()
        x = ((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2)-50
        y = ((root.winfo_screenheight() - root.winfo_reqheight()) / 2)-50
        root.geometry("+%d+%d" % (x, y))
        root.update()
        text = simpledialog.askstring(title="Informacion",
                                  prompt="Ingrese nombre de usuario: ")
        root.destroy()
        return text
    
    def drawText(self, text, size,coord):
        pg.font.init()
        mf = pg.font.SysFont('Century',size)
        ts = mf.render(text,False,(0,0,0))
        self.window.blit(ts,coord)
    
    def agregar_jugador(self, usuario, equipo):
        self.model.agregar_jugador(usuario, equipo)
    
    def redraw(self, jugadores, usuario_de_jugador):
        """Update the window with their new graphics"""
        imagen= pg.image.load(self.model.get_ruta_imagen_campo())
        imagen = pg.transform.scale(imagen,(self.ANCHO,self.ALTO))
        self.window.blit(imagen,[0,0])
        #Pinto los jugadores. Todos
        pg.display.update()
    
    def setup(self):
        """Get ready the main window and others needed"""
        os.environ['SDL_VIDEO_CENTERED'] = '1' #To center the window in the middle
        self.window = pg.display.set_mode((self.ANCHO,self.ALTO))
        pg.display.set_caption("Prueba - Juego")
        self.clock = pg.time.Clock()
        self.model = aplicacion.Aplicacion();
        user = "PruebaKG"
        self.model.iniciar_partido(user,1)
        for i in range(0,100):
            b = self.model.set_datos_balon(i, 0, user)
            print(f"Ruta imagen balon:{b}")
        pg.init()

"""Start the application"""
try:
    m = MainWindow()
except Exception as e:
    print(e.trace())
    pass