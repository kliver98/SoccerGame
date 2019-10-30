from client.model.aplicacion import Aplicacion

class Controlador():
    
    aplicacion = None
    
    def __init__(self):
        self.aplicacion = Aplicacion()
        
    def get_nombre_aplicacion(self):
        return self.aplicacion.get_nombre_aplicacion()
    
    def iniciar_partido(self, usuario_de_jugador, numero_campo, ip = None):
        """Metodo que crea/instancia un nuevo partido. Recibe el nombre de usuario del cliente (el unico que se puede controlar), 
        numero de la imagen del campo a cargar"""
        self.aplicacion.iniciar_partido(usuario_de_jugador, numero_campo,ip)
        
    def agregar_jugador(self, usuario, equipo):
        """Metodo que agrega un jugador al partido actual que se este jugando"""
        self.aplicacion.agregar_jugador(usuario, equipo)
        
    def esta_jugador_dentro_campo(self, coordenadas_campo):
        """Metodo que verifica si un jugador esta dentro de las coordenadas del campo.
        Recibe coordenadas_campo y coordenadas_jugador que son un arreglo conteniendo informacion respectiva de las coordenas [x,y]
        Para las coordenadas_campo siempre seran las mismas dado que la pantalla no se podra modificar, sin embargo como es una propiedad
        de la vista, no se guarda en esta clase campo.
        Retorna True o False si el jugador esta dentro del campo"""
        return self.aplicacion.esta_jugador_dentro_campo(coordenadas_campo)  
        
    def jugadores_colisionando_con_balon(self):
        return self.aplicacion.jugadores_colisionando()
        
    def get_datos_jugadores(self):
        """Metodo que retorna arreglo de seis datos de la informacion de los usuarios, separados por aplicacion.SEPARADOR
        nombre de usuario, equipo, coordenada en x, coordenada en y, ruta de la imagen, entero para rotar la imagen"""
        return self.aplicacion.get_datos_jugadores()
    
    def set_datos_jugadores(self, datos):
        """Metodo que actualiza las coordenadas de los jugadores que se obtienen por parametro, 
        datos es un arreglo y cada uno tiene get_datos() de clase jugador pero es un string separado por aplicacion.SEPARADOR
        Ejemplo (separador ,): arr = ['jugador1,False,100,200' , 'jugador2,False,150,180' , 'jugador3,True,400,50' , 'jugador4,True,350,149']"""
        self.aplicacion.set_datos_jugadores(datos)
        
    def set_coordenadas_jugador_cliente(self,coord,soltar_balon, anteriores = False):
        self.aplicacion.set_coordenadas_jugador_cliente(coord,soltar_balon, anteriores)
    
    def get_datos_balon(self):
        """Metodo que retorna un string con la posicion (x,y) del balon separado por: aplicacion.SEPARADOR"""
        return self.aplicacion.get_datos_balon()
    
    def get_ruta_imagen_campo(self):
        """Metodo que retorna un string con la ruta de la imagen del campo a cargar"""
        return self.aplicacion.get_ruta_imagen_campo()
    
    def get_usuario_de_jugador(self):
        return self.aplicacion.get_usuario_de_jugador()
    
    def get_separador(self):
        return self.aplicacion.get_separador()
    
    def get_max_jugadores_equipo(self):
        return self.aplicacion.get_max_jugadores_equipo()
    
    def iniciar_bots(self):
        return self.aplicacion.iniciar_bots()
    
    def esta_formatoIP_bien(self,ip):
        return self.aplicacion.esta_formatoIP_bien(ip)
    
    def get_tiempos(self):
        return self.aplicacion.get_tiempos()
    
    def get_velocidad_jugador(self):
        return self.aplicacion.get_velocidad_jugador()
    
    def get_coordenadas_cliente(self):
        return self.aplicacion.get_coordenadas_cliente()
    
    def alguien_tiene_balon(self):
        return self.aplicacion.alguien_tiene_balon()
    
    def jugador_cliente_colisionando_balon(self):
        return self.aplicacion.jugador_cliente_colisionando_balon()
    
    def esta_partido_listo(self):
        return self.aplicacion.esta_partido_listo()
    
    def iniciar_jugadores(self):
        self.aplicacion.iniciar_jugadores()
        
    def mover_balon(self, x, y, nuevo_usuario):
        self.aplicacion.mover_balon(x, y, nuevo_usuario)
        
    def get_tiempo_juego_Online(self):
        return self.aplicacion.get_tiempo_juego_Online()
    
    def get_goles(self):
        return self.aplicacion.get_goles()