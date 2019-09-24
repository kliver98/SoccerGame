import pygame as pg

class MainController():
    
    def __init__(self):
        pass
    
    def is_ball_inside_screen(self,ball):
        surface = pg.display.get_surface()
        if ball.x<surface.get_width()-25 and ball.x>10:
            if ball.y<surface.get_height()-20 and ball.y>10:
                print("Ball inside")
                
    def is_player_inside_screen(self,player):
        surface = pg.display.get_surface()
        if player.x<surface.get_width()-25 and player.x>5:
            if player.y<surface.get_height()-55 and player.y>0:
                print("Player inside")