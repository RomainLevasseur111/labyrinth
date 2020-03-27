import constants as constants


class Character:
    def __init__(self, map):
        self.map = map
        self.position = list(self.map.start)[0]
        self.older_position = list(self.map.start)[0]

    def pos(self):
        """Take position of char and change it so we can compare it"""
        self.position = list(self.position)[0]
        self.older_position = list(self.older_position)[0]

    def take_item(self):
        """Character takes item

        if character position is same as any position of map.items,
        delete that item and add 1 to ITEM constant

        """
        if self.position in self.map.items:
            self.map.items.remove(self.position)
            constants.ITEM += 1

    def move(self, direction):
        """How the character moves

        Get attribute of a position object, according on how we name 'direction'
        (in this project, up, down ,left or right.) See if this position
        object is in map.empty, is he is, that means the path is valid.
        So it sets the position of character to this new position. Each time
        move is called, we also call method take_item.

        """
        self.older_position = self.position
        new_position = getattr(self.position, direction)
        if new_position in self.map.empty:
            self.position = new_position
            self.take_item()
