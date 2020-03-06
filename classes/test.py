from classes.labyrinth import Labyrinth
from classes.position import Position
from classes.character import Character

def main():
    map01 = Labyrinth("maps/map1.txt")
    mac = Character(map01)
main()
