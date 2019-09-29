#Class: PanelAyuda

import tkinter
"""Esta es la clase que representa la ventana de ayuda de un cliente"""

"""Inicio de la clase"""

class PanelAyuda():
    
    """Constantes de la clase"""
    
    COLOR_FONDO_PANEL = 'yellow'
    GEOMETRIA_PANEL = '400x400'
    TITULO_PANEL = "Estadisticas"    
    
    
    """Atributos de la clase"""
    """Atributo que representa el alto y ancho de una ventana"""
    geometria = None
    panel = None   
    
    
    
    """Metodo constructor de la clase"""
    def __init__(self):
        
        geometria = self.GEOMETRIA_PANEL
        panel = tkinter.Tk()
        panel.title(self.TITULO_PANEL)
        panel.configure(background = self.COLOR_FONDO_PANEL)
        panel.geometry(self.GEOMETRIA_PANEL)
        panel.mainloop()    
    
    
    """Metodos relacionados con la clase"""

