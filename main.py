import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    clock = pygame.time.Clock() 

    updatable = pygame.sprite.Group() # we create a group called updatable so we can update all objects in 1 shot.
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable) #all 'Player' class instances will be added to the groups its container mentions

    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()
    dt = 0 # dt represent the amount of time that has passed since the last frame was drawn

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable: #replace player with group 'updatable'. all class instances with update() will get executed cleanly
            obj.update(dt)

        screen.fill((0,153,153)) 

        for obj in drawable: #using group "drawwable" instead of player. all onscreen objects drawn in 1 go.
            obj.draw(screen)
        pygame.display.flip()  
      
        dt = clock.tick(60)/1000 #liimit framerate to 60fps

if __name__ == "__main__": 
    main()