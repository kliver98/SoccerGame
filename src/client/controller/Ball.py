'''
Created on 22/09/2019

@author: Usuario
'''
import pygame as pg
from . import constants as cs

class Ball():
    """Class that represents the ball in the match"""
    
    def __init__(self, x, y, window):
        """Builder that sets where it's painted into screen - x,y and the window parameter"""
        self.controlled_by_username = "" #This help to know which player has the ball on it's foots. Help when other player wants to take it over
        self.x = x
        self.y = y
        self.cont = 1
        self.image = pg.image.load(cs.BALL_IMAGE+str(self.cont)+".png")
        self.cont+=1
        self.vel = cs.PLAYER_SPEED
        self.window = window
        self.rect = self.image.get_rect()
        self.angle = 0
        
    def draw(self):
        """Method to draw into screen the ball"""
        self.window.blit(self.image.convert_alpha(),[self.x,self.y])
        
    def move(self,data):
        """Method to move the coordenates of the ball depending where user moves the rows and if it hit both"""
        self.image = pg.image.load(cs.BALL_IMAGE+str(self.cont)+".png")
        self.angle = self.angle+90 if self.angle<361 else 0
        self.image = pg.transform.rotate(self.image, self.angle)
        self.cont = 1 if self.cont>5 else self.cont+1
        if data[0]==0:
            self.x+=data[1]
        else:
            self.y+=data[1]
        