import pygame
from constants import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,153,153)) #can also use color directly. eg "black"
        pygame.display.flip()   #use pygame function directly to clear the screen. it will know which screen to reset


if __name__ == "__main__": # ensures the main() function is only called when this file is run directly
    main()