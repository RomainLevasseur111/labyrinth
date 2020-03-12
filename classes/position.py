class Position:
    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)
#permits to compare two instances of position
    def __eq__(self, pos):
        return self.position == pos.position

#define what happens when moving
    @property
    def up(self):
        x, y = self.position
        return Position(x-1, y)

    @property
    def down(self):
        x, y = self.position
        return Position(x+1, y)

    @property
    def left(self):
        x, y = self.position
        return Position(x, y-1)

    @property
    def right(self):
        x, y = self.position
        return Position(x, y+1)
