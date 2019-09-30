#Class: VentanaMenu

"""Esta es la clase que representa la ventana del menu"""
from cProfile import label
from pygame import font
#!/usr/bin/env python
# -*- coding: utf-8 -*-




"""Inicio de la clase"""

import tkinter

class   PanelMenu():

    """Constantes de la clase"""
    COLOR_FONDO_PANEL = 'white'
    GEOMETRIA_PANEL = '400x400'
    TITULO_PANEL = "Menu"
    
    IMAGEN_BALON = f"ballLogin.png"


    """Atributos de la clase"""
    """Atributo que representa el alto y ancho de una ventana"""
    _geometria = None
    _panel = None
    _txtLabel1 = None
    _txtLabel2 = None
    _btnPartido1= None
    _btnPartido2 = None
    _btnAyuda = None
    _btnSalir= None
    _imgLabel1 = None
    _image1 = None

    """Relaciones de la clase"""
    _VentanaPrincipal = None
    
    """Metodo constructor de la clase"""
    def __init__(self):
        
        """Inicializo atributos de la clase"""
        """**********************   Configuncion de la ventana   ******************************"""
        geometria = self.GEOMETRIA_PANEL
        panel = tkinter.Tk()
        panel.title(self.TITULO_PANEL)
        panel.configure(background = self.COLOR_FONDO_PANEL)
        panel.geometry(self.GEOMETRIA_PANEL)
    
        self._image1 = tkinter.PhotoImage(file = self.IMAGEN_BALON )
        self._txtLabel1 = tkinter.Label(panel, text="The Best SoccerGame", font=("Agency FB",14), bg = 'white', pady = 0).place(x=130, y=160)
        self._txtLabel2= tkinter.Label(panel, text="Que quieres hacer?", font=("Agency FB",14), bg = 'white', pady =0).place(x=140, y=200)
        
        self._imgLabel1 = tkinter.Label(panel,image = self._image1 ).place(x=160, y=30)
        self._btnPartido1 = tkinter.Button(panel,text="Partido n x n", font= ("Agency FB",10), width = 20).place(x= 150, y = 240)
        self._btnPartido2 = tkinter.Button(panel,text="Partido n x CPU", font= ("Agency FB",10), width = 20).place(x= 150, y = 275)
        self._btnAyuda = tkinter.Button(panel,text="Ayuda", font= ("Agency FB",10), width = 20).place(x= 150, y = 310)
        self._btnSalir = tkinter.Button(panel,text="Salir", font= ("Agency FB",10), width = 20).place(x= 150, y = 345)    
        
        """Metodo que inicializa y arranza una ventana. Este es el encargado de mostrar la ventana en pantalla"""
        panel.mainloop()
        
    
    """Metodos relacionados con la clase"""


        
        