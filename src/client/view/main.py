from client.controller import constants as cs
import pygame as pg
import sys

class MainWindow():
    
    def __init__(self):
        self.setup()
        self.init()
        
    def init(self):
        run = True
        
        while run:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
            self.redrawWindow()
        
    def redrawWindow(self):
        self.window.fill((0,255,0))
        pg.display.update()
    
    def setup(self):
        self.window = pg.display.set_mode((cs.WIDTH,cs.HEIGHT))
        pg.display.set_caption("SOCCER GAME By CJKS")
        self.clock = pg.time.Clock()

try:
    MainWindow()
except Exception as e:
    pass
finally:
    pg.quit()
    sys.exit()