#import pygame line
import pygame

#import module section

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #initialise pygame and set display
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
    #gameloop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()




#Keep line below, ensures main is called when main.py is run directly
if __name__ == "__main__":
    main()
