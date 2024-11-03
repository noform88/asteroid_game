from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "pink", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        #self.velocity & self.position inherited from Circleshape, so no need define again in constructor
        #self.velocity default is : pygame.Vector2(0, 0)

    def split(self):
        self.kill() # asteroid is destroyed if hit. what comes next depends on its radius

        if self.radius <= ASTEROID_MIN_RADIUS: #if its radius is smaller than the constant ASTEROID_MIN_RADIUS, do nth.
            return 
        
        #if radius bigger than the min_radius, proceed to create 2 new smaller asteroids

        #1. get the angle within which the mini asteroid will move
        random_angle = random.uniform(20,50)

        #1a. '-random_angle' gets you the mirror of random angle.
        #2. assign the angle using current asteroid's velocity
        v1 =self.velocity.rotate(random_angle)
        v2 =self.velocity.rotate(-random_angle)
        
        #3. get radius for the mini asteroid
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #4. create 2 new asteroid instances
        asteroid_mini01 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_mini02 = Asteroid(self.position.x, self.position.y, new_radius)

        #5. multiply v1 * 1.2 and assign it into the new asteroid's velocity.
        asteroid_mini01.velocity = v1 * 1.2
        asteroid_mini02.velocity = v2 * 1.2