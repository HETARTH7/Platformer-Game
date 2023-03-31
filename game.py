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
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

# set up pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))


def get_background(name):
    image = pygame.image.load(join('assets', 'Background', name))
    # _,_, are x and y. _ is used because we dont care about their value
    _, _, width, height = image.get_rect()
    tiles = []

    # WIDTH- screen width divided by width of tile gives approx. number of tiles in x direction to fill the whole screen. 1 is added to fill the gaps if any
    for i in range(WIDTH//width+1):
        # HEIGHT-screen height. same as width.
        for j in range(HEIGHT//height+1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)
    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    run = True
    while run:
        clock.tick(FPS)  # while loop will run 60fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if user quits the game
                run = False
                break

        draw(window, background, bg_image)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
