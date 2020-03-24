import constants as constants


class Character:
    def __init__(self, map):
        self.map = map
        self.position = list(self.map.start)[0]
        self.older_position = list(self.map.start)[0]

# change map.start into a list so we can take the first (and only) element and
# compare it to map.empty
    def pos(self):
        self.position = list(self.position)[0]
        self.older_position = list(self.older_position)[0]

# look if char is on the position of an item, if he is, removes it from
# map.items and add one to constant HAS_ITEM
    def take_item(self):
        if self.position in self.map.items:
            self.map.items.remove(self.position)
            constants.ITEM += 1

    def move(self, direction):
        # get attribute of an object (here, up down left right of Position) and
        # see if it is a valid path
        self.older_position = self.position
        new_position = getattr(self.position, direction)
        if new_position in self.map.empty:
            self.position = new_position
            self.take_item()
