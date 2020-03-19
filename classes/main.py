from classes.labyrinth import Labyrinth
from classes.position import Position
from classes.character import Character
import pygame, sys, random
from pygame.locals import *




def main():
    def img_items():
        needle = pygame.image.load("resources/aiguille.png").convert_alpha()
        needle = pygame.transform.scale(needle, (20, 20))
        ether = pygame.image.load("resources/ether.png").convert()
        ether = pygame.transform.scale(ether, (20, 20))
        plastic_tube = pygame.image.load("resources/tube_plastique.png").convert()
        plastic_tube = pygame.transform.scale(plastic_tube, (20, 20))
        imgs = [needle, ether, plastic_tube]
        def random_img():
            while imgs:
                elem = random.choice(imgs)
                imgs.remove(elem)
                return elem
        for position in map01.items:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(random_img(), (y, x))

    def img_char():
        char = pygame.image.load("resources/MacGyver.png").convert_alpha()
        char = pygame.transform.scale(char, (20, 20))
        x, y = mac.position.position
        x, y = x * 20, y * 20
        DISPLAYSURF.blit(char, (y, x))


    def not_moving_img():
        img_path = pygame.image.load("resources/floor-tiles-20x20.png")

        for position in map01.empty:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(img_path, (y, x) , (60, 240, 20, 20))

        for position in map01.wall:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(img_path, (y, x) , (80, 180, 20, 20))

        for position in map01.start:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(img_path, (y, x) , (0, 240, 20, 20))

        for position in map01.end:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(img_path, (y, x) , (120, 240, 20, 20))


    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Labyrinth")
    map01 = Labyrinth("maps/map1.txt")
    mac = Character(map01)
    not_moving_img()
    img_char()
    img_items()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
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
        pygame.display.update()
main()
