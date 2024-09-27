import pygame
import random
from constants import *
from circleshape import CircleShape



class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN,(255,255,255), self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)