#Class: PanelEstadisticas
import tkinter
"""Esta es la clase que representa la ventana donde se reflejan las estadisticas de un partido"""

"""Inicio de la clase"""

class PanelEstadisticas():


    """Constantes de la clase"""
    
    COLOR_FONDO_PANEL = 'blue'
    GEOMETRIA_PANEL = '400x400'
    TITULO_PANEL = "Estadisticas"

    
    """Atributos de la clase"""
    """Atributo que representa el alto y ancho de una ventana"""
    geometria = None
    """Atributo que representa la ventana"""  
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
