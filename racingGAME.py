import pygame as py
import time,random
from pygame.locals import *
from car import *


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

# CUSTOM EVENTS
SPAWN_CARS = USEREVENT + 1
py.time.set_timer(SPAWN_CARS, 600)

car_colors = (RED, GREEN, WHITE, BLACK)
background = py.image.load("road.jpg")
background = py.transform.scale(background,(700,500))
# upcars = ["ambulance.png","ambulance2.png","blue_convertable_car.png","delorian.png","police_car.png","tinted_black_car.png","Van.png"]
downcars = ["black_car.png","black_convertable_car.png","black_mini_car.png","green_mini_car.png","hotshot.png","Jeep.png","red_car.png","White_car.png","ambulance.png","ambulance2.png","blue_convertable_car.png","delorian.png","police_car.png","tinted_black_car.png","Van.png"]

player_1 = Player("motorcycle.png",250,350, screen)


clock = py.time.Clock()
FPS = 60
loop = True
# global cars_passed
cars_passed = 0

while loop:
    
    for event in py.event.get():
        if event.type == py.QUIT:
            loop = False       
        if event.type == SPAWN_CARS:
            down_cars(downcars[random.randint(0,13)])
            # up_cars(upcars[random.randint(0,6)])
            
            
        elif event.type == py.MOUSEBUTTONDOWN:  # or MOUSEBUTTONDOWN depending on what you want.
            print(py.mouse.get_pos())
                     
    keys = py.key.get_pressed()
    
    clock.tick(FPS)
        
    if keys[py.K_LEFT]:
        player_1.move_left()      
    if keys[py.K_RIGHT]:
        player_1.move_right()
    if keys[py.K_DOWN]:
        player_1.move_down()      
              
    screen.blit(background,(0,0))  
    
    
    # UPDATE         
    player_1.update()
    enemy_cars.update()
    
    player_1_sprite.draw(screen)   
    enemy_cars.draw(screen)
    py.display.update()