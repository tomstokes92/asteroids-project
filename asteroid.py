import pygame

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, # screen object
            "white", # object colour
            self.position, # list of points
            self.radius,
            LINE_WIDTH # line width.duh
        )
    def update(self, dt):
        self.position += self.velocity * dt