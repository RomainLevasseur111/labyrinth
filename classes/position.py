class Position:
    """Class that handles position on the grid"""
    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        """Return a position object in string"""
        return str(self.position)

    def __hash__(self):
        """Give a hash for each created object"""
        return hash(self.position)

    def __eq__(self, pos):
        """What happens when we try to compare 2 position object"""
        return self.position == pos.position

    @property
    def up(self):
        """When this method is called, return postion -1 on x"""
        x, y = self.position
        return Position(x-1, y)

    @property
    def down(self):
        """When this method is called, return postion +1 on x"""
        x, y = self.position
        return Position(x+1, y)

    @property
    def left(self):
        """When this method is called, return postion -1 on y"""
        x, y = self.position
        return Position(x, y-1)

    @property
    def right(self):
        """When this method is called, return postion +1 on y"""
        x, y = self.position
        return Position(x, y+1)
