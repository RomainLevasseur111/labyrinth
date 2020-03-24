from classes.labyrinth import Labyrinth
from classes.character import Character
import constants as constants
import pygame
import sys
import random
from pygame.locals import *


def main():
    # loading 3 different image for 3 different items and resizing them
    def img_items():
        needle = pygame.image.load("resources/aiguille.png").convert_alpha()
        needle = pygame.transform.scale(needle, (20, 20))
        ether = pygame.image.load("resources/ether.png").convert()
        ether = pygame.transform.scale(ether, (20, 20))
        plastic_tube = pygame.image.load("resources/tube.png").convert()
        plastic_tube = pygame.transform.scale(plastic_tube, (20, 20))
        # into a list
        imgs = [needle, ether, plastic_tube]

        # take a random item in list and delete it
        def random_img():
            while imgs:
                elem = random.choice(imgs)
                imgs.remove(elem)
                return elem
        # for each loop in random_img, gives it a position and adding it to the
        # screen
        for position in map01.items:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(random_img(), (y, x))

    # loading character img and add it to the screen
    # and take older position of char and gives it its original image
    def img_char():
        img_path = pygame.image.load("resources/floor-tiles-20x20.png")
        char = pygame.image.load("resources/MacGyver.png").convert_alpha()
        char = pygame.transform.scale(char, (20, 20))
        x, y = mac.older_position.position
        x, y = x * 20, y * 20
        DISPLAYSURF.blit(img_path, (y, x), (60, 240, 20, 20))
        x, y = mac.position.position
        x, y = x * 20, y * 20
        DISPLAYSURF.blit(char, (y, x))

    # loading differents tiles representing path, wall, and ennemy
    def not_moving_img():
        img_path = pygame.image.load("resources/floor-tiles-20x20.png")
        img_ennemy = pygame.image.load("resources/Gardien.png")
        img_ennemy = pygame.transform.scale(img_ennemy, (20, 20))
        for position in map01.empty:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(img_path, (y, x), (60, 240, 20, 20))

        for position in map01.wall:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(img_path, (y, x), (80, 180, 20, 20))

        for position in map01.end:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(img_ennemy, (y, x))

    # if char has 3 items and is one end position, display winning screen, else
    # losing screen
    def win_or_lose(char, map):
        if char.position in map.end:
            if char.ITEM == 3:
                constants.GAME += 2
            else:
                constants.GAME += 1

    # load win and lose screen
    def win_back():
        win_img = pygame.image.load("resources/win.png")
        DISPLAYSURF.blit(win_img, (0, 0))

    def lose_back():
        lose_img = pygame.image.load("resources/lose.png")
        DISPLAYSURF.blit(lose_img, (0, 0))

    # initialize pygame
    pygame.init()
    # set size of screen
    DISPLAYSURF = pygame.display.set_mode((300, 300))
    # names window
    pygame.display.set_caption("Labyrinth")
    # create map and character
    map01 = Labyrinth("maps/map1.txt")
    mac = Character(map01)
    # calling all images
    not_moving_img()
    img_char()
    img_items()
    # playing game loop
    while constants.GAME == 0:
        win_or_lose(mac, map01)
        # each time we click quit, stops pygame and quit the game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # each time up, down, left and right arrow is pressed,
            # call method move from character
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    mac.move("up")
                    img_char()
                if event.key == K_DOWN:
                    mac.move("down")
                    img_char()
                if event.key == K_LEFT:
                    mac.move("left")
                    img_char()
                if event.key == K_RIGHT:
                    mac.move("right")
                    img_char()
        # updates whats on the screen
        pygame.display.update()
    # lose loop that quit for each key pressed on keyboard
    while constants.GAME == 1:
        lose_back()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    # win loop that qui for each key pressed on keyboard
    while constants.GAME == 2:
        win_back()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
