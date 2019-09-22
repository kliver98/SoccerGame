'''
Created on 22/09/2019

@author: Usuario
'''
import pygame as pg
from . import constants as cs

class Player():
    """Class that contains data of this player"""
    
    def __init__(self, color, x, y, image_file):
        self.color = color
        self.x = x
        self.y = y
        self.image = pg.image.load(image_file)
        self.vel = cs.PLAYER_SPEED
        
    def draw(self,window):
        window.blit(self.image.convert(),[self.x,self.y])
        
    def move(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT]:
            self.x -= self.vel
        if keys[pg.K_RIGHT]:
            self.x += self.vel
        if keys[pg.K_UP]:
            self.y -= self.vel
        if keys[pg.K_DOWN]:
            self.y += self.vel