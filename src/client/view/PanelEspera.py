#Class: PanelEspera

import tkinter


"""Esta es la clase que representa la ventana de espera de un cliente"""

"""Inicio de la clase"""

class    PanelEspera():

    """Constantes de la clase"""
    
    COLOR_FONDO_PANEL = 'white'
    GEOMETRIA_PANEL = '400x400'
    TITULO_PANEL = "Estableciendo conexion"
    IMAGEN_CONEXION = f"../../../resources/images/conexion.png"

    
    """Atributos de la clase"""
    geometria = None
    panel = None
    _txtLabel1 = None
    _txtLabel2 = None
    _image = None
    _imageLabel = None
    
    
    
    """Metodo constructor de la clase"""
    def __init__(self):
        
        
        """Inicializo atributos de la clase"""
        """**********************   Configuncion de la ventana   ******************************"""
        geometria = self.GEOMETRIA_PANEL
        panel = tkinter.Tk()
        panel.title(self.TITULO_PANEL)

        panel.geometry(self.GEOMETRIA_PANEL)
        self._txtLabel1 = tkinter.Label(panel, text="Esperando jugadores...", font=("Agency FB",14), pady = 0).place(x=130, y=180)
        self._txtLabel2= tkinter.Label(panel, text="Estableciendo conexion", font=("Agency FB",9), pady =0).place(x=150, y=220)
        self._image = tkinter.PhotoImage(file= self.IMAGEN_CONEXION)
        self._imageLabel  =  tkinter.Label(panel, image= self._image).place(x= 170, y = 70)
        
        """Metodo que inicializa y arranza una ventana. Este es el encargado de mostrar la ventana en pantalla"""
        panel.mainloop()
    
    
    """Metodos relacionados con la clase"""

