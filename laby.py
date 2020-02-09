class Labyrinth :

    CELLS = []
    MIN_WIDTH = 0
    MAX_WIDTH = 15
    MIN_HEIGHT = 0
    MAX_HEIGHT = 15
    STEP = 1

    def __init__(self,corner1,corner2):
        self.corner1 = corner1
        self.corner2 = corner2

    @classmethod
    def initialize_grid(cls):
        for height in range(cls.MIN_HEIGHT, cls.MAX_HEIGHT,cls.STEP):
            for width in range(cls.MIN_WIDTH, cls.MAX_WIDTH, cls.STEP):
                bottom_left_corner = width, height
                top_right_corner = width + cls.STEP, height + cls.STEP
                cell = Labyrinth(bottom_left_corner, top_right_corner)
                cls.CELLS.append(cell)
        print(len(cls.CELLS))

def main():
    Labyrinth.initialize_grid()

main()
