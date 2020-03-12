from classestest.labytest import Labyrinth
from classestest.chartest import Character
import pygame, sys
from pygame.locals import *

def main():

    def maze(position):
        img_path = pygame.image.load("resources/floor-tiles-20x20.png")
        for x in position.empty:
            DISPLAYSURF.blit(img_path, (x[0],x[1]) , (60, 240, 20, 20))
        for x in position.wall:
            DISPLAYSURF.blit(img_path, (x[0],x[1]) , (80, 180, 20, 20))
        for x in position.start:
            DISPLAYSURF.blit(img_path, (x[0],x[1]) , (0, 240, 20, 20))
        for x in position.end:
            DISPLAYSURF.blit(img_path, (x[0],x[1]) , (120, 240, 20, 20))

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Labyrinth")
    map01 = Labyrinth("maps/map1.txt")
    mac = Character(map01, "resources/MacGyver.png")
    maze(map01)
    while True:
        up = (mac.position[0] - 20, mac.position[1])
        down = (mac.position[0] + 20, mac.position[1])
        right = (mac.position[0], mac.position[1] + 20)
        left = (mac.position[0], mac.position[1] - 20)
        print(map01.empty)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    print(mac.position[0])
                elif event.key == K_DOWN:
                    mac.move(down)
                elif event.key == K_RIGHT:
                    mac.move(right)
                elif event.key == K_LEFT:
                    mac.move(left)
        pygame.display.update()

main()
