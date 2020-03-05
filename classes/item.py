import random
class Item:
    def __init__(self, map):
        self.map = map
        self.spawnable = map.spawnable
        self.position = 0
        self.spawn()

# method spawn takes a random piece of self.spawnable, set self.position to it
#and then delete the position in self.spawnable so it cant be used by another item
    def spawn(self):
        self.position = random.sample(self.spawnable, 1)
        if self.position[0] in self.spawnable:
            self.spawnable.remove(self.position[0])
        self.position = set(self.position)
        print(self.position)
