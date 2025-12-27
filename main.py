
import pygame
import sys

# import module section

from constants import *
from logger import *
from player import *
from asteroid import *
from asteroid_field import *
from shot import *
from screen_draws import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # initialise pygame and set display
    pygame.init()
    # screen size testing
    # screen_info = pygame.display.Info()
    # screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h),pygame.NOFRAME)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 48) # None = Default font, 36px size
    # initialise clock before main loop
    game_clock = pygame.time.Clock()
    dt = 0
    # Creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # player instance
    Player.containers = (updatable, drawable) # type: ignore
    player = Player(
        x = SCREEN_WIDTH / 2, 
        y = SCREEN_HEIGHT / 2
    )
    player_score = 0
    # asteroid instance
    Asteroid.containers = (updatable, drawable, asteroids) # type: ignore
    # asteroid field instance
    AsteroidField.containers = (updatable) # type: ignore
    asteroid_field = AsteroidField()
    # shot instance
    Shot.containers = (updatable, drawable, shots) # type: ignore
    # gameloop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for objects in drawable:
            objects.draw(screen)
        draw_score(screen, font, player_score)
        updatable.update(dt)
        for objects in asteroids:
            if objects.collide_with(player): 
                log_event("player_hit")
                print("Game over!")
                print(f"Score: {player_score}")
                sys.exit()
            for bullet in shots:
                if bullet.collide_with(objects):
                    log_event("asteroid_shot")
                    objects.split(asteroids)
                    bullet.kill()
                    player_score += 1
        pygame.display.flip()
        game_clock.tick(60)
        dt = game_clock.tick(60) / 1000

# Keep line below, ensures main is called when main.py is run directly
#PUD TOLD ME TO DO IT!#
if __name__ == "__main__":
    main()
