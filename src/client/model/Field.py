'''
Created on 22/09/2019

@author: Usuario
'''
import pygame as pg
from client.controller import constants as cs

class Field():
    field_image = pg.image.load(cs.FIELD_IMAGE)
    field_image = pg.transform.scale(field_image, (cs.WIDTH, cs.HEIGHT))
    
    def __init__(self):
        pass
    
    def draw(self,Surface):
        print("Hi")
        Surface.blit(self.field_image,[0,0])