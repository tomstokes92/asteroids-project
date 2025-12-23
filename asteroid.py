import pygame
import random

from circleshape import *
from constants import *
from logger import *


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

    def split(self, asteroid_container):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            set_angle = random.uniform(20, 50)
            velocity1 = self.velocity.copy().rotate(set_angle)
            velocity2 = self.velocity.copy().rotate(-set_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1*1.2
            asteroid2.velocity = velocity2*1.2
            asteroid_container.add(asteroid1)
            asteroid_container.add(asteroid2)



