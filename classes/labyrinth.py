class Labyrinth:
    VALID_MAZE = True
    def __init__(self, filename, maze_length=0):
        self.filename = filename
        self.maze_length = maze_length

    @property
    def is_maze_valid(self):
        with open(self.filename, "r") as self.filename:
            self.maze_length = len(self.filename.readline().rstrip())
            for line in self.filename:
                if len(line.rstrip()) != self.maze_length:
                    self.VALID_MAZE = False
                    raise Exception("Your maze must be a square or a rectangle")
                else :
                    self.VALID_MAZE = True
def main():
    map01 = Labyrinth("maps/map1.txt")
    map01.is_maze_valid
    print(map01.VALID_MAZE)
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
2 character se déplace sur labyrinth
3 définir des coordonnées ?
4 readline.rstripe pour vérifier nb caractère/ligne si ligne diff stop prog, et pour voir si char et Ennemy
sont present une seule fois
"""
