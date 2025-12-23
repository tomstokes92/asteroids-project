
import pygame
import sys

# import module section

from constants import *
from logger import *
from player import *
from asteroid import *
from asteroid_field import *
from shot import *


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # initialise pygame and set display
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # initialise clock before main loop
    game_clock = pygame.time.Clock()
    dt = 0
    # Creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # player instance
    Player.containers = (updatable, drawable)
    player = Player(
        x = SCREEN_WIDTH / 2, 
        y = SCREEN_HEIGHT / 2
    ) 
    # asteroid instance
    Asteroid.containers = (updatable, drawable, asteroids)
    # asteroid field instance
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    # shot instance
    Shot.containers = (updatable, drawable, shots)
    # gameloop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for objects in drawable:
            objects.draw(screen)
        updatable.update(dt)
        for objects in asteroids:
            if objects.collide_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.collide_with(objects):
                    log_event("asteroid_shot")
                    objects.split(asteroidsw)
                    bullet.kill()
        pygame.display.flip()
        game_clock.tick(60)
        dt = game_clock.tick(60) / 1000


# Keep line below, ensures main is called when main.py is run directly
#PUD TOLD ME TO DO IT!#
if __name__ == "__main__":
    main()
