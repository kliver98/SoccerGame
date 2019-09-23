#All imports
from client.controller import constants as cs
from client.controller import Field as m
import pygame as pg
import os 
from client.controller.Player import Player
from client.controller.Ball import Ball
from client.controller import MatchController as match_c

class MainWindow():
    """Class principal of the GUI"""
    
    def __init__(self):
        """Builder"""
        self.setup()
        self.init()
        
    def init(self):
        """Start the application drawing into screen"""
        self.field = m.Field(self.window)
        self.player = Player("TestUser",cs.WIDTH*cs.SCALE*0.3, (cs.HEIGHT*cs.SCALE/2)-(30), self.window,True)
        self.ball = Ball(self.player.x+self.player.rect.x/2+100,self.player.y+self.player.rect.y/2,self.window)
        run = True
        """Here the application is earing the keywords pressed"""
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
            data = self.player.move()
            if self.match.is_collided_with(self.player,self.ball) and data:
                self.ball.move(data)
                self.ball.controlled_by_username = self.player.username
                self.player.has_ball = True
            else:
                self.ball.controlled_by_username = ""
                self.player.has_ball = False
            if pg.key.get_pressed()[pg.K_z]:
                self.unlink_ball_of_player()
            self.redrawWindow(self.player,self.ball)
    
    def unlink_ball_of_player(self):
        """Method that unlink ball of the player sending the ball a few pixels away like kicking"""
        if not self.match.is_collided_with(self.player,self.ball):
            return
        self.ball.controlled_by_username = ""
        self.player.has_ball = False
        for i in range(0,17):
            self.ball.move((0,i if self.player.team else -i))
            self.redrawWindow(self.player, self.ball)
        
    def redrawWindow(self,player = None, ball = None):
        """Update the window with their new graphics"""
        self.field.draw()
        if player: #Drawing the player into screen
            player.draw()
        if ball:
            ball.draw()
        pg.display.update()
    
    def setup(self):
        """Get ready the main window and others needed"""
        os.environ['SDL_VIDEO_CENTERED'] = '1' #To center the window in the middle
        self.window = pg.display.set_mode((int(cs.WIDTH*cs.SCALE),int(cs.HEIGHT*cs.SCALE)))
        self.match = match_c.MatchController()
        pg.display.set_caption(cs.APP_NAME)
        self.clock = pg.time.Clock()
        pg.init()

"""Start the application"""
try:
    MainWindow()
except Exception as e:
    #print(e.trace_call())
    pass