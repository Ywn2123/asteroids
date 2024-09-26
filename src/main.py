import pygame
from constants import *
from player import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updateable_group, drawable_group)
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_character = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(SCREEN,(0, 0, 0))

        for n in updateable_group:
            n.update(dt)
        for n in drawable_group:
            n.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)
        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()

