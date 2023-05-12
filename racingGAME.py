import pygame as py
import sys
from pygame.locals import *
from car import Car
from random import randint

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


upcars = ["ambulance.png","ambulance2.png","blue_convertable_car.png","delorian.png","police_car.png","tinted_black_car.png","Van.png"]

downcars = ["black_car.png","black_convertable_car.png","black_mini_car.png","green_mini_car.png","hotshot.png","Jeep.png","red_car.png","White_car.png"]

player = Car("motorcycle.png",70,27,61,0,screen)
#up
a1 = Car("ambulance.png",70,27,61,0,screen)
a2 = Car("ambulance2.png",70,27,61,0,screen)
bkcc = Car("blue_convertable_car.png",70,27,61,0,screen)
d = Car("delorian.png",70,27,61,0,screen)
pc = Car("police_car.png",70,27,61,0,screen)
tbc = Car("tinted_black_car.png",70,27,61,0,screen)
v = Car("Van.png",70,27,61,0,screen)
#down
bc = Car("black_car.png",70,27,61,0,screen)
becc = Car("black_convertable_car.png",70,27,61,0,screen)
bmc = Car("black_mini_car.png",70,27,61,0,screen)
gmc = Car("green_mini_car.png",70,27,61,0,screen)
h = Car("hotshot.png",70,27,61,0,screen)
j = Car("Jeep.png",70,27,61,0,screen)
rc = Car("red_car.png",70,27,61,0,screen)
wc = Car("White_car.png",70,27,61,0,screen)


asl = py.sprite.Group()
asl.add(player,a1,a2,bkcc,d,pc,tbc,v,bc,becc,bmc,gmc,h,j,rc,wc)

oncoming_cars_down = py.sprite.Group()
oncoming_cars_down.add(bc,becc,bmc,gmc,h,j,rc,wc)
oncoming_cars_up = py.sprite.Group()
oncoming_cars_up.add(a1,a2,bkcc,d,pc,tbc,v)

clock = py.time.Clock()
FPS = 60
loop = True
global cars_passed
cars_passed = 0

global coll
coll = 0
carsleft = []
if coll == 0:
    for value in range(2):
        coll += 1
        cc = randint(0,7)
        carsleft.append(cc)
        



while loop:
    
    for event in py.event.get():
        if event.type == py.QUIT:
            loop = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                print("LEFT")
                player.xc = -0.5
            if event.key == py.K_RIGHT:
                print("RIGHT")
                player.xc = 0.5
        if event.type == py.KEYUP:
            if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                player.xc = 0
                print("AIR")
                
    if coll == 0:
        for value in range(2):
            coll += 1
            cc = randint(0,7)
            carsleft.append(cc)
        
    asl.draw(screen)    
    asl.update(carsleft)
    screen.blit(background,(0,0))
    py.display.update()