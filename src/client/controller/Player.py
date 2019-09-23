'''
Created on 22/09/2019

@author: Usuario
'''
import pygame as pg
from . import constants as cs

class Player():
    """Class that contains data of this player"""
    
    def __init__(self, username, x, y, window, team):
        """Builder. receives username to identify, it's x and y position into screen, the image that will represents object, screen window
        and the team that belongs, True for Blacks and False for white"""
        self.username = username
        self.x = x
        self.y = y
        self.image = pg.image.load(cs.PLAYER_IMAGE_BLACK[0] if team else cs.PLAYER_IMAGE_WHITE[0])
        angle = 270 if team else 90
        self.image = pg.transform.rotate(self.image, angle)
        self.vel = cs.PLAYER_SPEED
        self.window = window
        self.rect = self.image.get_rect()
        self.has_ball = False
        self.team = team #True for Black and False for White
        
    def draw(self):
        """Method that draw the player into the screen"""
        self.window.blit(self.image.convert_alpha(),[self.x,self.y])
        
    def move(self):
        """Method that move the position of player according the arrows user pressed. Also return where the ball has to move if both hitted"""
        keys = pg.key.get_pressed()
        data = None
        
        if keys[pg.K_LEFT]:
            data = (0,-self.vel)
            self.x -= self.vel
        elif keys[pg.K_RIGHT]:
            data = (0,self.vel)
            self.x += self.vel
        elif keys[pg.K_UP]:
            data = (1,-self.vel)
            self.y -= self.vel
        elif keys[pg.K_DOWN]:
            data = (1,self.vel)
            self.y += self.vel
            
        return data