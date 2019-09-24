
import pygame
from client.model import menu
from client.view import menu_view
from client.controller import  constants

class Menu_Controller():
    
    
    def __init__(self,window):
        self.model=menu.Menu()
        self.view=menu_view.Menu_View(window)

    def init(self):
        self.view.draw_menu()
        self.view.move_selector(0)
        wait=True
        selec=0
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    pygame.quit()
            keys=pygame.key.get_pressed()
            
            if keys[pygame.K_UP]:
                selec=constants.MODE_ONLINE
                
            elif keys[pygame.K_DOWN]:
                selec=constants.MODE_CPU
            elif keys[pygame.K_z]:
                wait=False
            self.view.move_selector(selec)
            self.model.change_mode(selec)
            
    def get_mode(self):
        return self.model.get_mode()