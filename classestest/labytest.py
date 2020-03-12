import constants as constants
import random
import pygame
from pygame.locals import *


class Labyrinth:
    VALID_MAZE = False
    def __init__(self, filename, maze_length=0):
        self.filename = filename
        self.maze_length = maze_length
        # using sets because it cannot store the same value twice
        self.empty = set()
        self.wall = set()
        self.start = set()
        self.end = set()
        self.items = set()
        self.is_maze_valid()
        self.maze_structure()
        #self.spawn()
#while there is less than 3 items in self.items, it takes a random part of self.empty
#that is not in self.end and self.start, and add it to self.items

    def display(self, wall, path):
        self.empty = pygame.image.load(path).convert()
        self.wall = pygame.image.load(wall).convert()



    #def spawn(self):
        while len(self.items) < 3 :
            position = list(random.sample(self.empty, 1))[0]
            if position not in self.start :
                if position not in self.end :
                    self.items.add(position)
# read a .txt file to verify if all lines are equals
# that permits to not pre-define the size of the maze
# and so we only need to change the .txt file if we want a bigger or smaller maze
    def is_maze_valid(self):
        #open .txt file
        with open(self.filename, "r") as f:
            #read the first line that define the length of the all maze
            #and put it in maze_length
            self.maze_length = len(f.readline().rstrip())
            #loop reading length of all lines
            for line in f:
                #condition that compare the length of each line to maze_length
                #and if there is only one start and end
                #stop the program in not equal

                if len(line.rstrip()) != self.maze_length:
                    raise Exception("Your maze must be a square")
                elif len(self.start) and len(self.end) != 1 :
                    raise Exception("There must be only one start and end")
                else :
                    self.VALID_MAZE = True

    #define what type of cell will be each character or map.txt
    #by creating a new object Position for each char and put it in the corresponding set
    #using doule loop for
    def maze_structure(self):
        with open(self.filename, "r") as f:
            #take line by line and give it a number (starting from 0)
            for x, line in enumerate(f):
                #take each char of a line and give it a number
                for y, char in enumerate(line):
                    if char == constants.EMPTY:
                        self.empty.add((y * 20, x * 20))
                    elif char == constants.WALL:
                        self.wall.add((y * 20, x * 20))
                    elif char == constants.START:
                        self.start.add((y * 20, x * 20))
                    elif char == constants.END:
                        self.end.add((y * 20, x * 20))
