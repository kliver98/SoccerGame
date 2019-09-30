#Class: PanelAyuda

import tkinter
"""Esta es la clase que representa la ventana de ayuda de un cliente"""




"""Inicio de la clase"""

class PanelAyuda():
    
    """Constantes de la clase"""
    
    COLOR_FONDO_PANEL = 'white'
    GEOMETRIA_PANEL = '400x600'
    TITULO_PANEL = "Ayuda"    
    IMAGEN_FLECHA_IZQUIERDA =  f"../../../resources/images/flechaIzquierda.png"
    IMAGEN_FLECHA_DERECHA = f"../../../resources/images/flechaDerecha.png"
    IMAGEN_FLECHA_ABAJO = f"../../../resources/images/flechaAbajo.png"
    IMAGEN_FLECHA_ARRIBA = f"../../../resources/images/flechaArriba.png"
    IMAGEN_PATEAR =  f"../../../resources/images/teclaPatear.png"
                
    
    
    """Atributos de la clase"""
    """Atributo que representa el alto y ancho de una ventana"""
    _geometria = None
    _panel = None   
    _labelTxt = None
    _labelCom1 = None
    _labelCom2 = None
    _labelCom3 = None
    _labelCom4 = None
    _labelCom5 = None
    _labelCreditos = None
    _labelNombresCreditos = None
 
    
    _imageFlechaArriba= None
    _imageFlechaAbajo = None
    _imageFlechaDerecha = None
    _imageFlechaIzquierda= None
    _imageLabelArriba = None
    _imageLabelAbajo = None
    _imageLabelIzquierda = None
    _imageLabelDerecha = None
    _imageLabelPatear= None
    
    
    _imageFlechaAbajo = None
    _imageFlechaArriba = None
    _imageFlechaDerecha = None
    _imageFlechaIzquierda = None
    _imagePatear= None
    
    
    _btnVolver= None
    """Metodo constructor de la clase"""
    def __init__(self):
        
        
        
        
        
        """Inicializando atributos de la clase """
        
        
        """**********************   Configuncion de la ventana   ******************************"""
        geometria = self.GEOMETRIA_PANEL
        self._panel = tkinter.Tk()
        self._panel.title(self.TITULO_PANEL)
        self._panel.configure(background = self.COLOR_FONDO_PANEL)
        self._panel.geometry(self.GEOMETRIA_PANEL)
        self._labelTxt = tkinter.Label(self._panel, text="Hola!."+ '\n'+ "A continuacion encontraras los comandos de teclado"+ '\n' + "para jugar. Recuerdalos para tener una partida increible!", font=("Agency FB",12), bg = 'white', pady = 0).place(x=80, y=30)
        
             
        self._labelCom1 = tkinter.Label(self._panel, text="Avanzar hacia adelante" , font=("Agency FB",12), bg = 'white', pady = 0).place(x=80, y=120)
        self._labelCom2 = tkinter.Label(self._panel, text="Avanzar hacia atras" , font=("Agency FB",12), bg = 'white', pady = 0).place(x=80, y=170)
        self._labelCom3 = tkinter.Label(self._panel, text="Avanzar hacia la arriba" , font=("Agency FB",12), bg = 'white', pady = 0).place(x=80, y=220)
        self._labelCom4 = tkinter.Label(self._panel, text="Avanzar hacia abajo" , font=("Agency FB",12), bg = 'white', pady = 0).place(x=80, y=270)      
        self._labelCom5 = tkinter.Label(self._panel, text="Patear Balon" , font=("Agency FB",12), bg = 'white', pady = 0).place(x=80, y=320)      
        
        self._imageFlechaAbajo = tkinter.PhotoImage(file = self.IMAGEN_FLECHA_ABAJO )  
        self._imageFlechaArriba = tkinter.PhotoImage(file = self.IMAGEN_FLECHA_ARRIBA ) 
        self._imageFlechaDerecha = tkinter.PhotoImage(file = self.IMAGEN_FLECHA_DERECHA ) 
        self._imageFlechaIzquierda = tkinter.PhotoImage(file = self.IMAGEN_FLECHA_IZQUIERDA ) 
        self._imagePatear = tkinter.PhotoImage(file = self.IMAGEN_PATEAR ) 
        

        self._imageLabelDerecha = tkinter.Label(self._panel, image= self._imageFlechaDerecha).place(x= 300, y = 120)
        self._imageLabelIzquierda= tkinter.Label(self._panel, image= self._imageFlechaIzquierda).place(x= 300, y = 170)
        self._imageLabelArriba = tkinter.Label(self._panel, image= self._imageFlechaArriba).place(x= 300, y = 220)
        self._imageLabelAbajo = tkinter.Label(self._panel, image= self._imageFlechaAbajo).place(x= 300, y = 270)
        self._imageLabelPatear = tkinter.Label(self._panel, image= self._imagePatear).place(x= 300, y = 320)        
        
        self._btnVolver = tkinter.Button(self._panel,text="Volver atras", font= ("Agency FB",10), width = 20).place(x= 150, y = 500) 
        
        self._labelCreditos = tkinter.Label(self._panel, text="Creditos:" , font=("Agency FB",8), bg = 'white', pady = 0).place(x=170, y=530) 
        self._labelCom4 = tkinter.Label(self._panel, text="Jorge Lievano-Kliver Giron"+ '\n' + "Sergio lozada - Cristian Cobo"+ '\n'+ "2019 " , font=("Agency FB",6), bg = 'white', pady = 0).place(x=150, y=550) 
        
        
        """Metodo que inicializa y arranza una ventana. Este es el encargado de mostrar la ventana en pantalla"""
        self._panel.mainloop()    
    
    
    """Metodos relacionados con la clase"""

