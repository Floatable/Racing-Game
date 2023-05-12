import pygame 
WHITE = (0,0,0)


class Car(pygame.sprite.Sprite):
    '''Class representing a car that is derived from the Sprite class in Pygame'''
    
    def __init__(self, image, speed,x,y,xc,screen):
        pygame.sprite.Sprite.__init__(self)
        # Call the parent class(Sprite) constructor 
        # Initialize attributes of the car
        # Pass in the color of the car, its (x,y) coordinates, and its width and height
        # Set the background color to transparent
        self.image = pygame.image.load(image)
        self.image.get_rect()
        self.x = x
        self.y = y
        self.xc = xc
        # Initialize attributes of the car
        self.image.get_rect()
        self.speed = speed

        # Draw the car (a rectangle)
        screen.blit(self.image,(x,y))
        square = self.rect-self.image.get_rect()
        pygame.draw.rect(self.image,WHITE,square)
    # Get the rectangle object that has the same
    # dimensions as self.image above
        
    # def move_right(self, pixels):
    #     self.rect_x+= pixels
    # def move_left(self, pixels):
    #     self.rect.x-= pixels
    # def move_forward(self, speed):
    #     self.rect.y+-self.speed*speed/20
    # def move_backward(self, speed):
    #     self.rect.y-=self.speed * speed /20
    # def change_speed(self,speed):
    #     self.speed-speed

    #     pygame.draw.rect(self.image, self.color, 10, 0, self.width,self.height)


