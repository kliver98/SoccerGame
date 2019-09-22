from client.controller import constants as cs
from client.model import Field as m
import pygame as pg
import os 

class MainWindow():
    
    def __init__(self):
        self.setup()
        self.init()
        
    def init(self):
        m.Field().draw(self.window)
        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
            self.redrawWindow()
        
    def redrawWindow(self):
        pg.display.update()
    
    def setup(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1' #To center the window in the middle
        self.window = pg.display.set_mode((int(cs.WIDTH*cs.SCALE),int(cs.HEIGHT*cs.SCALE)))
        pg.display.set_caption(cs.APP_NAME)
        self.clock = pg.time.Clock()
        pg.init()

try:
    MainWindow()
except Exception as e:
    pass