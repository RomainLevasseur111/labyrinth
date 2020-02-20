class Position:
    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, pos):
        return self.position == pos.position


    def up(self):
        return Position(x-1, y)

    def down(self):
        return Position(x+1, y)

    def left(self):
        return Position(x, y-1)

    def right(self):
        return Position(x, y+1)
