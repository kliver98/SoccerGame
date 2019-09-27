
from client.model import network
from client.view import connection_view
import client
from test.test_enum import threading

class ClientConnectionController:
    
    
    def __init__(self,window):
        self.view=connection_view.Connection_View(window)
        
    def start_network(self):  
        ip= self.view.get_ip()
        self.model=network.Network(ip)
        print("se ha iniciado el cliente") 
        #self.model.run_network()
      
    def sen_data(self,data):  
        self.model.send(data)
        
    def get_opponent_pos(self,mainx,mainy):
        
        pos=self.model.send(f"{mainx},{mainy}").split(",") 
        return int(pos[0]),int(pos[1])   
    
    def get_info(self,mainx,mainy,ballx,bally):
        data=self.model.send(f"{mainx},{mainy},{ballx},{bally}").split(",")
        return int(data[0]),int(data[1]),int(data[2]),int (data[3]) 