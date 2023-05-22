import pygame as py
import random
WHITE = "#FFFFFF"


player_1_sprite = py.sprite.Group()
class Player(py.sprite.Sprite):
    '''Class representing a car that is derived from the Sprite class in Pygame'''   
    def __init__(self, image,x,y,screen):
        super().__init__()
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        player_1_sprite.add(self)

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed
        
    def update(self):
        if self.rect.x < 115:
            self.rect.x = 115
        if self.rect.x > 595 - self.width - 1:
            self.rect.x = 595 - self.width -1
            
        # detects collision 
        if py.sprite.spritecollideany(self, enemy_cars):
            py.quit()

enemy_cars = py.sprite.Group()

class Car(py.sprite.Sprite):
    '''Class representing a car that is derived from the Sprite class in Pygame'''    
    def __init__(self, image,x,y):
        super().__init__()
        
        py.sprite.Sprite.__init__(self)
        self.image = py.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.speed = random.randint(5,10)
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        enemy_cars.add(self)     
    def update(self):       
        self.rect.y += self.speed
        if self.rect.y > 550:
            self.kill()
    
                    
        
def down_cars(image):
    down_car = Car(image, random.randint(145,555), -50)