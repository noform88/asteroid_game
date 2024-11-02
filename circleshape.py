import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):  #sprites: The base class for visible game objects
    def __init__(self, x, y, radius):
    
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y) 
        self.velocity = pygame.Vector2(0, 0) 
        self.radius = radius                 

    def draw(self, screen):
        pass
    def update(self, dt):
        pass

    def collision(self, other): #self.position is pygame.Vector2(x, y).
                                #it has a method of .distance_to()
                                #it calculates the distance from centre of object1 to that of obj2
        if self.position.distance_to(other.position) <= self.radius+ other.radius:
            return True
        return False