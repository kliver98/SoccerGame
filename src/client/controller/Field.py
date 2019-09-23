'''
Created on 22/09/2019

@author: Usuario
'''
import pygame as pg
from client.controller import constants as cs

class Field():
    """Class that represents the field of the soccer game"""
    
    #Variables that load the background image and resize to screen
    field_image = pg.image.load(cs.FIELD_IMAGE)
    field_image = pg.transform.scale(field_image, (int(cs.WIDTH*cs.SCALE), int(cs.HEIGHT*cs.SCALE)))
    
    def __init__(self,window):
        """Builder"""
        self.window = window
    
    def draw(self):
        """Draw the field into the screen named Surface by parameter"""
        self.window.blit(self.field_image,[0,0])