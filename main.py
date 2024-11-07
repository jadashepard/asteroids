# Project based on Build Asteroids using Python course on boot.dev
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# Import constant variables
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        #Create game clock and delta time variable
        clock = pygame.time.Clock()
        dt = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__=="__main__":
    main()
