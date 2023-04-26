# Breakout Game Starter File


import pygame as py
from pygame import *
import sys
import os
from random import randint
from time import sleep
mixer.init()
py.init()
screen = py.display.set_mode((800,600))
py.display.set_caption("My Breakout Game")

# Set up sprites and other game variables

# Color constants
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)

font = py.font.SysFont(None,50)


clock = py.time.Clock()
# Set number of frames per second (FPS)
FPS = 60
wall_color = RED
walls = []
for row in range(3):
    for col in range(12):
        wall = py.Rect(col*65+10,row*30+20,60,20)
        walls.append(wall)
        


# WHILE loop is our game loop...
gameover = False
while not gameover:
    clock.tick(FPS)
    for event in py.event.get():
        if event.type == py.KEYDOWN:
            if event.key == py.K_q:
                gameover = True
    screen.fill(BLACK)


    for wall in walls:
        py.draw.rect(screen,wall_color,wall)

# https://stackoverflow.com/questions/65981815/how-would-i-make-color-collision-using-pygame-mask

    py.display.update()
    # sleep(999999)

py.quit()
sys.exit()