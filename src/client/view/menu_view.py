
import pygame
from client.controller import constants


class Menu_View():
    
    menu_image = pygame.image.load(constants.MENU_OPTION_IMAGE)
    menu_image = pygame.transform.scale(menu_image, (int(constants.WIDTH*constants.SCALE), int(constants.HEIGHT*constants.SCALE)))
    selector_image=pygame.image.load(constants.MENU_SELECTOR_IMAGE)
    field_image = pygame.image.load(constants.FIELD_IMAGE)
    field_image = pygame.transform.scale(field_image, (int(constants.WIDTH*constants.SCALE), int(constants.HEIGHT*constants.SCALE)))

    pos_online=[0,150]
    pos_cpu=[0,250]
    
    def __init__(self , window):
        self.window=window
        
    def draw_menu(self):
        self.window.blit(self.field_image.convert_alpha(),[0,0])
        self.window.blit(self.menu_image.convert_alpha(),[0,0])
        pygame.display.update()
        
    def move_selector(self,position):
        self.draw_menu()
        if position==0:
            self.window.blit(self.selector_image,self.pos_online)
        elif position==1:
            self.window.blit(self.selector_image.convert_alpha(),self.pos_cpu)
        pygame.display.update()