

init_(self, color, width, height, speed):
# Call the parent class (Sprite) constructor
super()._init_()
# Pass in the color of the car, its (x,y) coordinates, and its width and height
# Set the background color to transparent
self.image = pygame.Surface([width,height])
self.image.fill(WHITE)
self.image.set_colorkey(WHITE)




# Draw the car (a rectangle)
pygame.draw.rect(self.image, self.color, [0,0, self.width, self.height])
# Get the rectangle object that has the same
# dimensions as self.image above
self.rect = self.image.get_rect()

def init_(self, color, width, height, speed): 
    # Call the parent class (Sprite) constructor 
    super(). init_()
