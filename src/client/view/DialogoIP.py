



import tkinter


"""Esta es la clase que representa la Ventana de dialogo cuando se requiera ingresar la direccion IP"""

class DialogoIP():
    """Constantes de la clase"""
    
    TITULO_DIALOGO = "Direccion IP"
    COLOR_FONDO_DIALOGO = "white"
    GEOMETRIA_DIALOGO = '400x200'
    IMAGEN = f"../../../resources/images/ip.png"
    
    """Relaciones de la clase"""
    
    
    """Atributos de la clase"""
    
    _panel= None
    _txtLabel1 = None
    _txtBoxIP = None
    _btnConectar = None
    _btnCancelar= None
    _image= None
    _imageLabel = None
    
    """Metodo constructor de la clase"""
    def __init__(self):
        
        """Inicializacion de los atributos de la clase"""
        
        """Configuracion de la ventana"""
        self._panel = tkinter.Tk()
        self._panel.title(self.TITULO_DIALOGO)

        self._panel.geometry(self.GEOMETRIA_DIALOGO)
        self._txtLabel1 = tkinter.Label(self._panel, text="Ingresa la direccion IP" , font=("Agency FB",12), pady = 0).place(x=230, y=70)
        self._image = tkinter.PhotoImage(file = self.IMAGEN)
        
        self._txtBoxIP = tkinter.Entry(self._panel).place(x= 210 , y =100)
        self._imageLabel  =  tkinter.Label(self._panel, image= self._image).place(x= 20, y = 20)
        self._btnConectar = tkinter.Button(self._panel,text="Conectar", font= ("Agency FB",10), width = 20).place(x= 290, y = 150) 
        self._btnConectar = tkinter.Button(self._panel,text="Cancelar", font= ("Agency FB",10), width = 20).place(x= 190, y = 150) 
    
        self._panel.mainloop()
    
        """Metodos relacionados con la clase"""
    
