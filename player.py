import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        #self.position
        #self.velocity
        #self.radius
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt) #-dt to rotate opp dir
            
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) #code provided. dont need understand.
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        fresh_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

        #create default velocity with intial directions of 0,1
        direction_vector = pygame.Vector2(0, 1) 
        
        #rotate it based on player's current direction
        #Assume 'self.angle' holds the player ritation in degrees
        rotated_vector = direction_vector.rotate(self.rotation)

        #Scale it up by PLAYER SHOOT SPEED
        fresh_shot.velocity = rotated_vector * PLAYER_SHOOT_SPEED
