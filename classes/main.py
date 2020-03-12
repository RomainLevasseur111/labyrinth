from classes.labyrinth import Labyrinth
from classes.position import Position
from classes.character import Character
import pygame, sys
from pygame.locals import *




def main():

    def pos_to_px(position):
        img_path = pygame.image.load("resources/floor-tiles-20x20.png")
        for x in position.empty_img:
            DISPLAYSURF.blit(img_path, (x[0],x[1]) , (60, 240, 20, 20))
        for x in position.wall_img:
            DISPLAYSURF.blit(img_path, (x[0],x[1]) , (80, 180, 20, 20))
        for x in position.start_img:
            DISPLAYSURF.blit(img_path, (x[0],x[1]) , (0, 240, 20, 20))
        for x in position.end_img:
            DISPLAYSURF.blit(img_path, (x[0],x[1]) , (120, 240, 20, 20))

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Labyrinth")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        map01 = Labyrinth("maps/map1.txt")
        mac = Character(map01, "resources/MacGyver.png")
        print(mac.position(x))
        #pos_to_px(map01)
        pygame.display.update()
main()
