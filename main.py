import pygame
import carMod
import random


pygame.init()

screenSize = (800, 500)
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

carImage = pygame.image.load("car.png")
playerCar = carMod.Car(5, carImage, (255, 0, 0))
BLACK = (255, 255, 255)
RED = (255, 0, 0)
WHITE  = (0, 0, 0)


loop = True
while loop:
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        
        
    screen.fill(BLACK)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerCar.Drive()
    if keys[pygame.K_a]:
        playerCar.turn(-5)
    if keys[pygame.K_d]:
        playerCar.turn(5)

    playerCar.update(screen)


    pygame.display.flip()