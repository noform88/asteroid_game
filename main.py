import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    clock = pygame.time.Clock() # magical timekeeper for our game.
    # limit how many frames we draw per second (FPS) using the .tick() method
    # track how much time has passed between frames (delta time)

    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    dt = 0 # dt represent the amount of time that has passed since the last frame was drawn


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt) #updates player's latest action

        screen.fill((0,153,153)) #can also use color directly. eg "black"

        player.draw(screen) #player appears on the interface

        pygame.display.flip()   #use pygame function directly to clear the screen. it will know which screen to reset

        clock.tick(60) #will pause the game loop until 1/60th of a second has passed
                       #also returns the amount of time that has passed since the last time it was called, the dt
        
        dt = clock.tick(60)/1000 #wont see any difference from b4, but will use less of the system's resources

if __name__ == "__main__": # ensures the main() function is only called when this file is run directly
    main()