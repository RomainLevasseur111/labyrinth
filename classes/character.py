import pygame
from pygame.locals import *
class Character:
    ITEM = 0
    def __init__(self, map):
        self.map = map
        self.position = self.map.start
        self.pos()

    #change map.start into a list so we can take the first (and only) element and compare it to map.empty
    def pos(self):
        self.position = list(self.position)[0]

#look if char is on the position of an item, if he is, removes it from map.items
#and add one to constant HAS_ITEM
    def take_item(self):
        if self.position in self.map.items:
            self.map.items.remove(self.position)
            self.ITEM += 1

    def move(self, direction):
        #get attribute of an object (here, up down left right of Position) and see if it a valid path
        new_position = getattr(self.position, direction)
        if new_position in self.map.empty:
            self.position = new_position
            self.take_item()


# def set_map avec tout _init_ dedans
