import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):  #sprites: The base class for visible game objects
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y) #pos
        self.velocity = pygame.Vector2(0, 0) #velocity
        self.radius = radius                 #radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass