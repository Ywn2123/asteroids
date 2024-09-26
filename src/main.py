import pygame
from constants import *
from player import *


def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_character = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player_character.update(dt)
        pygame.Surface.fill(SCREEN,(0, 0, 0))
        player_character.draw(SCREEN)
        pygame.display.flip()
        clock.tick(60)
        dt = (clock.tick(60) * 1000)

if __name__ == "__main__":
    main()

