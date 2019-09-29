#Class: VentanaMenu

"""Esta es la clase que representa la ventana del menu"""


"""Inicio de la clase"""

import tkinter

class   PanelMenu():

    """Constantes de la clase"""
    COLOR_FONDO_PANEL = 'medium sea green'
    GEOMETRIA_PANEL = '400x400'
    TITULO_PANEL = "Menu"


    """Atributos de la clase"""
    """Atributo que representa el alto y ancho de una ventana"""
    geometria = None
    panel = None

    """Relaciones de la clase"""
    VentanaPrincipal = None
    
    """Metodo constructor de la clase"""
    def __init__(self):
        
        geometria = self.GEOMETRIA_PANEL
        panel = tkinter.Tk()
        panel.title(self.TITULO_PANEL)
        panel.configure(background = self.COLOR_FONDO_PANEL)
        panel.geometry(self.GEOMETRIA_PANEL)
        panel.mainloop()
        
    
    """Metodos relacionados con la clase"""


        
        