from classes.labyrinth import Labyrinth
from classes.character import Character
import constants as constants
import pygame
import sys
import random
from pygame.locals import *


def main():

    def display_taken_items():
        img_path = pygame.image.load("resources/floor-tiles-20x20.png")
        myfont = pygame.font.SysFont("monospace", 12)
        item_taken = myfont.render("Item taken :" + str(constants.ITEM), 1, (255,255,255))
        DISPLAYSURF.blit(img_path, (80, 280), (80, 180, 20, 20))
        DISPLAYSURF.blit(item_taken, (0, 290))

    def img_items():
        """Load 3 images, resize them and put them into a list."""
        needle = pygame.image.load("resources/aiguille.png").convert_alpha()
        needle = pygame.transform.scale(needle, (20, 20))
        ether = pygame.image.load("resources/ether.png").convert()
        ether = pygame.transform.scale(ether, (20, 20))
        plastic_tube = pygame.image.load("resources/tube.png").convert()
        plastic_tube = pygame.transform.scale(plastic_tube, (20, 20))
        imgs = [needle, ether, plastic_tube]

        def random_img():
            """Set an image to an item

            Take a random image in the list then delete it.
            Then loop in the list, for each loop, set images to items
            and then put them on the screen.

             """
            while imgs:
                elem = random.choice(imgs)
                imgs.remove(elem)
                return elem
        for position in map.items:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(random_img(), (y, x))

    def img_char():
        """Display the character

        Load character image and add it to the screen, on character position.
        Take character older position, and change it to path image.

        """
        img_path = pygame.image.load("resources/floor-tiles-20x20.png")
        char = pygame.image.load("resources/MacGyver.png").convert_alpha()
        char = pygame.transform.scale(char, (20, 20))
        x, y = mac.older_position.position
        x, y = x * 20, y * 20
        DISPLAYSURF.blit(img_path, (y, x), (60, 240, 20, 20))
        x, y = mac.position.position
        x, y = x * 20, y * 20
        DISPLAYSURF.blit(char, (y, x))

    def not_moving_img():
        """Load and display differents tiles representing path, wall, and ennemy."""
        img_path = pygame.image.load("resources/floor-tiles-20x20.png")
        img_ennemy = pygame.image.load("resources/Gardien.png")
        img_ennemy = pygame.transform.scale(img_ennemy, (20, 20))
        for position in map.empty:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(img_path, (y, x), (60, 240, 20, 20))

        for position in map.wall:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(img_path, (y, x), (80, 180, 20, 20))

        for position in map.end:
            x, y = position.position
            x, y = x * 20, y * 20
            DISPLAYSURF.blit(img_ennemy, (y, x))

    def win_or_lose(char, map):
        """Win or lose display

        if the character position is equal to map end position, check if
        item constant is equat to 3, if it is, the player wins and the
        victory screen is display, by setting the game constant to 2.
        If it is not equal to 3, display losing screen by setting game
        constant to 1.

        """
        if char.position in map.end:
            if constants.ITEM == 3:
                constants.GAME += 2
            else:
                constants.GAME += 1

    def win_back():
        """Load win screen."""
        win_img = pygame.image.load("resources/win.png")
        DISPLAYSURF.blit(win_img, (0, 0))

    def lose_back():
        """Load lose screen."""
        lose_img = pygame.image.load("resources/lose.png")
        DISPLAYSURF.blit(lose_img, (0, 0))

    pygame.init()
    """Start Pygame."""
    DISPLAYSURF = pygame.display.set_mode((300, 300))
    """Set size of the screen."""
    pygame.display.set_caption("Labyrinth")
    """Name the Pygame window."""
    map = Labyrinth("maps/map1.txt")
    mac = Character(map)
    """Create character and labyrinth object from their respectives classes."""
    not_moving_img()
    img_char()
    img_items()
    display_taken_items()
    while constants.GAME == 0:
        """Start game loop."""
        win_or_lose(mac, map)
        for event in pygame.event.get():
            """If we click quit button, quit Pygame and exit system"""
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                """Events to move character

                When an arrow key is pressed, call the character method move, that
                call the position method up, down ,right and left according to
                the pressed key.
                Then call the img_char() function to display character image.

                """
                if event.key == K_UP:
                    mac.move("up")
                    img_char()
                    display_taken_items()
                if event.key == K_DOWN:
                    mac.move("down")
                    img_char()
                    display_taken_items()
                if event.key == K_LEFT:
                    mac.move("left")
                    img_char()
                    display_taken_items()
                if event.key == K_RIGHT:
                    mac.move("right")
                    img_char()
                    display_taken_items()

        pygame.display.update()
        """Update what is display on the screen"""
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
    """When the win or lose screen is displayed, quit the game for any key pressed """

main()
