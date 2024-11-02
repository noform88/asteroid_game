import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    clock = pygame.time.Clock() 

    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() #new group specifically for asteroids, for later use

    Asteroid.containers = (updatable, drawable, asteroids) #all asteroids automatically added to these 3 groups at birth
    AsteroidField.containers = (updatable) #astrofield only needs updating.
    Player.containers = (updatable, drawable) 

    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidfield = AsteroidField() #initialize the field before the loop. loop just updates each cycle.
    dt = 0 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:  #collisions checks after updating movements but b4 being drawn onto screen
            if asteroid.collision(player):
                print("Game over!")
                sys.exit() #shuts game.

        screen.fill((0,153,153)) 

        for obj in drawable: 
            obj.draw(screen)
        pygame.display.flip()  
      
        dt = clock.tick(60)/1000 #limit framerate to 60fps

if __name__ == "__main__": 
    main()