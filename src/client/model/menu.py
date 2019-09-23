'''
Created on 23/09/2019

@author: JORGE
'''
import pygame
from client.controller import constants

'''class that represent the logic of the menu'''
class Menu():
    def __init__(self):
        self.mode=constants.MODE_ONLINE
    
    def change_mode(self, mode): 
            self.mode=mode
            
    def get_mode(self):
        return self.mode