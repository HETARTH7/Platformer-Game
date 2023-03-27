import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

# setting caption at the top of the window
pygame.display.set_caption("Platformer")

# global variables
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

# set up pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))


def main(window):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)  # while loop will run 60fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if user quits the game
                run = False
                break

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
