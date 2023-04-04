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


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count/fps)*self.GRAVITY)
        self.move(self.x_vel, self.y_vel)
        self.fall_count += 1

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)


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


def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)
    pygame.display.update()


def handle_move(player):
    keys = pygame.key.get_pressed()
    player.x_vel = 0
    if keys[pygame.K_a]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_d]:
        player.move_right(PLAYER_VEL)


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    player = Player(100, 100, 50, 50)

    run = True
    while run:
        clock.tick(FPS)  # while loop will run 60fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if user quits the game
                run = False
                break

        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
