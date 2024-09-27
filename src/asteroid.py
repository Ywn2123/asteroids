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