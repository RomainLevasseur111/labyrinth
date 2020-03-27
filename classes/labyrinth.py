import constants as constants
from classes.position import Position
import random


class Labyrinth:
    VALID_MAZE = False
    def __init__(self, filename, maze_length=0, maze_height=0):

        self.filename = filename
        self.maze_length = maze_length
        self.maze_height = maze_height
        self.empty = set()
        self.wall = set()
        self.start = set()
        self.end = set()
        self.items = set()
        self.is_maze_valid()
        self.maze_structure()
        self.spawn()

    def spawn(self):
        """Spawn items

        As long as self.items length if below 3, take a random position object
        of self.empty that is not in self.start or self.end and add it to
        self.items

        """
        while len(self.items) < 3:
            position = list(random.sample(self.empty, 1))[0]
            if position not in self.start:
                if position not in self.end:
                    self.items.add(position)

    def is_maze_valid(self):
        """Check if map.txt file is valid

        first open txt file, count how long is the first line without the /n
        set attribute maze_length to this number. Then read all other lines,
        if they have the same lentgh as the first line, length is valid.

        Count the number of lines.

        Look in self.start and self.end if there is only one value, so this
        means there is only one start and one end, and that the txt file is
        valid.


        """
        with open(self.filename, "r") as f:
            self.maze_length = len(f.readline().rstrip())
            self.maze_height = 1
            for line in f:
                self.maze_height += 1
                if len(line.rstrip()) != self.maze_length:
                    raise Exception("Your maze must be a square or rectangle")
                elif len(self.start) and len(self.end) != 1:
                    raise Exception("There must be only one start and end")
                else:
                    self.VALID_MAZE = True

    def maze_structure(self):
        """Build the maze

        In constants, we define what means each character in map.txt (here,
        1 = empty, 0 = wall, 2 = start, and 3 = end). Then add them is each
        corresponding property of the labyrinth object.

        Start with opening txt file, for each line, read each character and
        for each character, give it a number (x) and for each line, gives it
        another number (y), put both in a tuple (x, y) and creates a Position
        object for each tuple, and eventually put them in corresponding
        sets. (self.empty, self.wall, self.end, self.start.)

        """
        with open(self.filename, "r") as f:
            for x, line in enumerate(f):
                for y, char in enumerate(line):
                    if char == constants.EMPTY:
                        self.empty.add(Position(x, y))
                    elif char == constants.WALL:
                        self.wall.add(Position(x, y))
                    elif char == constants.START:
                        self.start.add(Position(x, y))
                        self.empty.add(Position(x, y))
                    elif char == constants.END:
                        self.end.add(Position(x, y))
                        self.empty.add(Position(x, y))
