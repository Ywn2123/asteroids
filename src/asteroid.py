import pygame
import random
from constants import *
from circleshape import CircleShape
from main import SCREEN

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN,(255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            vect1, vect2 = pygame.math.Vector2.rotate(self.velocity, random_angle), pygame.math.Vector2.rotate(self.velocity, -random_angle)
            newAst1, newAst2 = Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius)
            newAst1.velocity = vect1 * 1.2
            newAst2.velocity = vect2 * 1.2