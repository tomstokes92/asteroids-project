# imports
import pygame
from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        # parent class constructor
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

# in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        print(a, b, c)
        return [a, b, c]
    # draw function
    def draw(self, screen):
        pygame.draw.polygon(
            screen, # screen object
            "white", # object colour
            self.triangle(), # list of points
            LINE_WIDTH # line width.duh
        )
    #movement
    def move(self,dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    #update self position on keypress
    def update (self, dt):
        keys = pygame.key.get_pressed()
        #turn left (key a)
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        #turn right (key d)
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        #move forward (key w) 
        if keys[pygame.K_w]:
           self.move(dt)
        #move backward (key s)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shot_cooldown_timer <= 0:
            self.shoot()
            self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        if self.shot_cooldown_timer > 0:
            self.shot_cooldown_timer -= dt

    # add shooting!
    def shoot(self):
        shot=Shot(self.position.copy())
        direction = pygame.Vector2(0, 1)
        direction.rotate_ip(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED


    



