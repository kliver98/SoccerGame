'''
File that has all the constants for use in the whole application
'''
import random as r

APP_NAME = "SOCCER GAME By CJKS"
WIDTH = 1280
HEIGHT = 720
SCALE = 0.7
CLOCK_TICK_RATE = 30
RESOURCES_LOCATION = "../../resources/"
#FIELD_IMAGE = f"{RESOURCES_LOCATION}images/soccer_field{r.randrange(1,3)}.jpg"
FIELD_IMAGE = f"{RESOURCES_LOCATION}images/soccer_field1.jpg"
PLAYER_IMAGE_BLACK = (f"{RESOURCES_LOCATION}images/playerBlack1.png",f"{RESOURCES_LOCATION}images/playerBlack2.png",f"{RESOURCES_LOCATION}images/playerBlack3.png")
PLAYER_IMAGE_WHITE = (f"{RESOURCES_LOCATION}images/playerWhite1.png",f"{RESOURCES_LOCATION}images/playerWhite2.png",f"{RESOURCES_LOCATION}images/playerWhite3.png")
BALL_IMAGE = f"{RESOURCES_LOCATION}images/ball_roll"
MENU_OPTION_IMAGE=f"{RESOURCES_LOCATION}images/menu1.png"
MENU_SELECTOR_IMAGE=f"{RESOURCES_LOCATION}images/menu_selector1.png"
MODE_ONLINE=0
MODE_CPU=1
PLAYER_SPEED = 0.7