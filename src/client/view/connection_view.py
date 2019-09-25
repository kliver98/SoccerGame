'''
Created on 23/09/2019

@author: JORGE
'''

import pygame

class Connection_View:
    
    ip=input("please set the server ip, it will be localhost for deafault")
    
    def __init__(self,window):
        self.window=window
        
    def get_ip(self):
        if not self.ip :
            self.ip="localhost"
        print(self.ip)
        return self.ip
        