import constants as constants
from classes.position import Position
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

        self.maze_structure()

# read a .txt file to verify if all lines are equals
# that permits to not pre-define the size of the maze
# and so we only need to change the .txt file if we want a bigger or smaller maze
    @property
    def is_maze_valid(self):
        #open .txt file
        with open(self.filename, "r") as f:
            #read the first line that define the length of the all maze
            #and put it in maze_length
            self.maze_length = len(f.readline().rstrip())
            #loop reading length of all lines
            for line in f:
                #condition that compare the length of each line to maze_length
                #stop the program in not equal
                if len(line.rstrip()) != self.maze_length:
                    raise Exception("Your maze must be a square or a rectangle")
                #elif len(self.start) and len(self.end) != "1" :
                #    raise Exception("There must be only one start and end")
                else :
                    self.VALID_MAZE = True

    def maze_structure(self):
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

    def is_position_valid(self, position):
        return position in self.empty



def main():
    map01 = Labyrinth("maps/map1.txt")
    map01.is_maze_valid
    print(map01.VALID_MAZE)
    p = Position(0, 0)
    print(len(map01.end))
    print(type(map01.empty))
    print(map01.is_position_valid(p))
main()







"""
1 utilise settings.txt pour définir les bases du labyrinthe
    boucle for pour lire chaque caractère de settings.txt et lui attribuer une
    caractèristique selon la valeur définie dans constants.py
        start : début du niveau
        end : fin du niveau
        wall : position non atteignable
        empty : chemin
        (peut-être ajouter une 5éme constante pour définir un certain nombre de
        case ou les items apparaitrons aléatoirement)

3 pour définir coords : lire chaque caractère, lui donnée une coord et l'envoyer dans la liste correspondant au carac
4 readline.rstripe pour vérifier nb caractère/ligne si ligne diff stop prog, et pour voir si char et Ennemy
sont present une seule fois

"""
