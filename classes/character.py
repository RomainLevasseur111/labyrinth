
class Character:
    HAS_ITEM = 0
    def __init__(self, map, item):
        self.map = map
        self.item = item
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
            take_item()
            if self.position in self.map.end :
                if self.HAS_ITEM == 3:
                    return print("You won!")
                else:
                    return print("You are dead!")
        else:
            print("Wrong direction!")

    def take_item(self):
        if self.position == self.item.position:
            delete(item)
            HAS_ITEM += 1
# def set_map avec tout _init_ dedans
