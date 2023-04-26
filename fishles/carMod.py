import pygame
pygame.init()

class Car():
    def __init__(self, speed, position, image, color):
        self.speed = speed
        self.image = image
        self.orig_image = image.copy()
        self.position = position
        self.rotation = pygame.Vector2(0, 1)
        self.color = color
    
    def turn(self, angle):
        self.rotation.rotate_ip(angle)
        self.image = pygame.transform.rotate(self.orig_image, self.rotation.angle_to(pygame.Vector2(0, 1)))
        

    def Drive(self):
        self.position += self.rotation * self.speed

    def update(self, screen):
        screen.blit(self.image, self.position)
        #pygame.draw.line(screen, (0, 255, 0), self.position.center, self.position.center + self.rotation * 30, 2)
