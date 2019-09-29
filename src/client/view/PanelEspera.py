#Class: PanelEspera

import tkinter

"""Esta es la clase que representa la ventana de espera de un cliente"""

"""Inicio de la clase"""

class    PanelEspera():

    """Constantes de la clase"""
    
    COLOR_FONDO_PANEL = 'red'
    GEOMETRIA_PANEL = '400x400'
    TITULO_PANEL = "Esperando"

    
    """Atributos de la clase"""
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

