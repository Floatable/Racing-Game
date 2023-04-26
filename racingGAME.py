import pygame as py
import sys
from pygame.locals import *

py.init()
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = py.display.set_mode(size)
py.display.set_caption('Speedy gonzales')

font = py.font.SysFont(None, 30)

BLACK = (0,0,0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (210, 210, 210)

car_colors = (RED, GREEN, WHITE, BLACK)
background = py.image.load("road.jpg")
background = py.transform.scale(background,(700,500))

clock = py.time.Clock()
FPS = 60
loop = True
while loop:
    screen.blit(background,(0,0))
    
    for event in py.event.get():
        if event.type == py.QUIT:
            loop = False

    py.display.update()