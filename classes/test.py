from classes.labyrinth import Labyrinth
from classes.position import Position
from classes.character import Character
from classes.item import Item

def main():
    map01 = Labyrinth("maps/map1.txt")
    item1 = Item(map01)
    item2 = Item(map01)
    item3 = Item(map01)
    mac = Character(map01, item1, item2, item3)
    print(len(map01.empty))
main()
