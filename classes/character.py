
class Character:
    def __init__(self, map):
        self.map = map
        self.position = self.map.start
        self.pos()

#change map.start into a list so we can take the first (and only) element and compare it to map.empty
    def pos(self):
        self.position = list(self.position)[0]


    def move(self, direction):
        #get attribute of an object (here, up down left right of Position) and see if it a valid path
        new_position = getattr(self.position, direction)
        if new_position in self.map.empty:
            self.position = new_position
            # if the position of the character is the same as map.end, character wins
            if self.position in self.map.end :
                return print("You won!")
        else:
            print("Wrong direction!")
