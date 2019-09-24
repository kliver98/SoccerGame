
import pygame as pg
from . import constants as cs

class Player():
    """Class that contains data of this player"""
    
    def __init__(self, username, x, y, window, team):
        """Builder. receives username to identify, it's x and y position into screen, the image that will represents object, screen window
        and the team that belongs, True for Blacks and False for white"""
        self.username = username
        self.team = team #True for Black and False for White
        self.x = x
        self.y = y
        self.img_number = 1
        self.image = pg.image.load(cs.PLAYER_IMAGE_BLACK[self.img_number-1] if self.team else cs.PLAYER_IMAGE_WHITE[self.img_number-1])
        self.setupPlayer()
        self.vel = cs.PLAYER_SPEED
        self.window = window
        self.rect = self.image.get_rect()
        self.has_ball = False
        
    def draw(self):
        """Method that draw the player into the screen"""
        self.window.blit(self.image.convert_alpha(),[self.x,self.y])
    
    def setupPlayer(self, img_number = 0):
        angle = 270 if self.team else 90
        self.img_number = self.img_number if img_number==0 else img_number
        self.image = pg.image.load(cs.PLAYER_IMAGE_BLACK[self.img_number-1] if self.team else cs.PLAYER_IMAGE_WHITE[self.img_number-1])
        self.image = pg.transform.rotate(self.image,angle)
        self.img_number += 1
        if self.img_number>3:
            self.img_number = 1
    
    def move(self):
        """Method that move the position of player according the arrows user pressed. Also return where the ball has to move if both hitted"""
        keys = pg.key.get_pressed()
        data = None
        datax=0
        datay=0
        self.setupPlayer() #Allways moving foots
        """if self.has_ball: #Just moving foots when hits the ball
            self.setupPlayer()
        else:
            self.setupPlayer(1)"""
            
        if keys[pg.K_LEFT]:
            datax=-self.vel
            data = (datax,datay)
            self.x -= self.vel
        if keys[pg.K_RIGHT]:
            datax=self.vel
            data = (datax,datay)
            self.x += self.vel
        if keys[pg.K_UP]:
            datay=-self.vel
            data = (datax,datay)
            self.y -= self.vel
        if keys[pg.K_DOWN]:
            datay=self.vel
            data = (datax,datay)
            self.y += self.vel
            
        return data