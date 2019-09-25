#All imports
import _thread
from client.controller import constants as cs
from client.controller import Field as m
import pygame as pg
import os 
from client.controller.Player import Player
from client.controller.Ball import Ball
from client.controller import MatchController as match_c
from client.controller import menu_controller
from client.controller import MainController as main_c
from client.controller import client_connection_controller
from _dummy_thread import start_new_thread

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
        self.oponent=Player("oponent",800,100,self.window,False)#oponent definition
        self.ball = Ball(self.player.x+self.player.rect.x/2+100,self.player.y+self.player.rect.y/2,self.window)
        self.menu= menu_controller.Menu_Controller(self.window)
        self.network=None
        self.mode=None
        '''show the menu and wait for select a game mode'''
        self.menu.init()
        self.mode=self.menu.get_mode()
        '''verified the game mode'''
        if self.mode==cs.MODE_ONLINE:
            self.network=client_connection_controller.ClientConnectionController(self.window)
            self.network.start_network()
            
        
        clock=pg.time.Clock()   
         
        run = True
        """Here the application is hearing the keywords pressed"""
        while run:
            
            ##clock.tick(30)
            if self.network is not None :
                position=self.player.get_pos()
                self.network.sen_data(f"{position[0]},{position[1]}")
                ##self.network.sen_data("1,1")
                opo_pos=self.network.get_opponent_pos(position[0],position[1])#recibe oponent position
                self.oponent.change_position(opo_pos[0], opo_pos[1])
                print(opo_pos)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
            
            data = self.player.move()
            if self.main_controller.is_ball_inside_screen(self.ball):
                continue
            if self.main_controller.is_player_inside_screen(self.player):
                continue
            if (not pg.key.get_pressed()[pg.K_x]) and self.match.is_collided_with(self.player,self.ball) and data:
                self.ball.move(data,self.player.team)
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
            self.ball.unlink_ball((i if self.player.team else -i))
            self.redrawWindow(self.player, self.ball)
        
    def redrawWindow(self,player = None, ball = None):
        """Update the window with their new graphics"""
        self.field.draw()
        one = player #To do later functionality
        second = ball #To do later functionality
        one.draw()
        second.draw()
        self.oponent.draw()
        pg.display.update()
    
    def setup(self):
        """Get ready the main window and others needed"""
        os.environ['SDL_VIDEO_CENTERED'] = '1' #To center the window in the middle
        self.window = pg.display.set_mode((int(cs.WIDTH*cs.SCALE),int(cs.HEIGHT*cs.SCALE)))
        self.match = match_c.MatchController()
        self.main_controller = main_c.MainController();
        pg.display.set_caption(cs.APP_NAME)
        self.clock = pg.time.Clock()
        pg.init()


"""Start the application"""
try:
    MainWindow()
except Exception as e:
    print(e.trace_call())
    pass