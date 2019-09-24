
from client.model import network
from client.view import connection_view

class ClientConnectionController:
    
    
    def __init__(self,window):
        self.view=connection_view.Connection_View(window)