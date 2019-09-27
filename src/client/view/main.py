
import _thread
from client.controller import constants as cs
from client.controller import field as m
import pygame as pg
import os 
from client.controller.player import Player
from client.controller.ball import Ball
from client.controller import match_controller as match_c
from client.controller import menu_controller
from client.controller import main_controller as main_c
from client.controller import client_connection_controller
from _dummy_thread import start_new_thread
import tkinter as tk
from tkinter import simpledialog

class MainWindow():
    """Class principal of the GUI"""
    
    def __init__(self):
        """Builder"""
        self.setup()
        self.init()
        
    def init(self):
        """Start the application drawing into screen"""
        self.field = m.Field(self.window)
        username_p1 = "A"#self.ask_username()
        username_op = ""#self.ask_username()
        #print(f"p1: {username_p1} - op: {username_op}")
        self.player = Player(username_p1 if username_p1 else "Player1",cs.WIDTH*cs.SCALE*0.3, (cs.HEIGHT*cs.SCALE/2)-(30), self.window,True)
        self.oponent=Player(username_op if username_op else "Oponent",800,100,self.window,False)#oponent definition
        self.ball = Ball(cs.WIDTH*cs.SCALE*0.5,cs.HEIGHT*cs.SCALE*0.5,self.window)
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
         
        run = True
        """Here the application is hearing the keywords pressed"""
        while run:
            
            #self.clock.tick(cs.CLOCK_TICK_RATE)
            if self.network is not None :
                player_pos=self.player.get_pos()
                ball_pos=self.ball.get_position()
                #self.network.sen_data(f"{position[0]},{position[1]}")#,{position[2]}")
                ##self.network.sen_data("1,1")
                #opo_pos=self.network.get_opponent_pos(position[0],position[1])#recibe oponent position
               
                
                info=self.network.get_info(player_pos[0], player_pos[1], ball_pos[0], ball_pos[1])
                
                print(info)
                self.oponent.change_position(info[0], info[1])
                self.ball.change_position(info[2], info[3])
                print(info)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
            
            data = self.player.move() #This do the movement of the player. ONLY PLAYER
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
            self.redrawWindow()
    
    def unlink_ball_of_player(self):
        """Method that unlink ball of the player sending the ball a few pixels away like kicking"""
        if not self.match.is_collided_with(self.player,self.ball):
            return
        self.ball.controlled_by_username = ""
        self.player.has_ball = False
        for i in range(0,17):
            self.ball.unlink_ball((i if self.player.team else -i))
            self.redrawWindow()
            
    
    def ask_username(self):
        root = tk.Tk()
        root.withdraw()
        x = ((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2)-50
        y = ((root.winfo_screenheight() - root.winfo_reqheight()) / 2)-50
        root.geometry("+%d+%d" % (x, y))
        root.update()
        text = simpledialog.askstring(title="Informacion",
                                  prompt="Ingrese nombre de usuario: ")
        root.destroy()
        return text
    
    def redrawWindow(self):
        """Update the window with their new graphics"""
        self.field.draw()
        self.player.draw()
        self.ball.draw()
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
    print(e)
    pass