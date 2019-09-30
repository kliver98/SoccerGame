#Class: PanelEspera

import tkinter

"""Esta es la clase que representa la ventana de espera de un cliente"""

"""Inicio de la clase"""

class    PanelEspera():

    """Constantes de la clase"""
    
    COLOR_FONDO_PANEL = 'white'
    GEOMETRIA_PANEL = '400x400'
    TITULO_PANEL = "Estableciendo conexion"

    
    """Atributos de la clase"""
    geometria = None
    panel = None
    _txtLabel1 = None
    _txtLabel2 = None
    
    
    
    """Metodo constructor de la clase"""
    def __init__(self):
        
        
        """Inicializo atributos de la clase"""
        """**********************   Configuncion de la ventana   ******************************"""
        geometria = self.GEOMETRIA_PANEL
        panel = tkinter.Tk()
        panel.title(self.TITULO_PANEL)
        panel.configure(background = self.COLOR_FONDO_PANEL)
        panel.geometry(self.GEOMETRIA_PANEL)
        self._txtLabel1 = tkinter.Label(panel, text="Esperando jugadores...", font=("Agency FB",14), bg = 'white', pady = 0).place(x=130, y=180)
        self._txtLabel2= tkinter.Label(panel, text="Estableciendo conexion", font=("Agency FB",9), bg = 'white', pady =0).place(x=150, y=220)
        
        
        """Metodo que inicializa y arranza una ventana. Este es el encargado de mostrar la ventana en pantalla"""
        panel.mainloop()
    
    
    """Metodos relacionados con la clase"""

