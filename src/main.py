import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
from shoot import *
import sys

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)
    Shot.containers = (shots, updateables, drawables)

    player_character = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    # asteroid_character = Asteroid()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(SCREEN,(0, 0, 0))

        for n in updateables:
            n.update(dt)
        for n in drawables:
            n.draw(SCREEN)
        for n in asteroids:
            if n.collision(player_character) == True:
                print('Game over!')
                sys.exit()
        for n in asteroids:
            for i in shots:
                if n.collision(i):
                    n.split()


        pygame.display.flip()
        clock.tick(60)
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()

