#All imports
from client.controller import constants as cs
from client.controller import Field as m
import pygame as pg
import os 
from client.controller.Player import Player

class MainWindow():
    """Class principal of the GUI"""
    
    def __init__(self):
        """Builder"""
        self.setup()
        self.init()
        
    def init(self):
        """Start the application drawing into screen"""
        p = Player(None, cs.WIDTH/2, cs.HEIGHT/2,cs.PLAYER_TEST_IMAGE)
        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
            p.move()
            self.redrawWindow(p)
        
    def redrawWindow(self,player = None):
        """Update the window with their new graphics"""
        m.Field().draw(self.window)
        if player: #Drawing the player into screen
            player.draw(self.window)
        pg.display.update()
    
    def setup(self):
        """Get ready the main window and others needed"""
        os.environ['SDL_VIDEO_CENTERED'] = '1' #To center the window in the middle
        self.window = pg.display.set_mode((int(cs.WIDTH*cs.SCALE),int(cs.HEIGHT*cs.SCALE)))
        pg.display.set_caption(cs.APP_NAME)
        self.clock = pg.time.Clock()
        pg.init()

"""Start the application"""
try:
    MainWindow()
except Exception as e:
    print(e)