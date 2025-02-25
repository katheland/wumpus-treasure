from cavegrid import *
from cavenode import ContentType
import random

def main():
    grid = CaveGrid(7)
    grid.add_contents(ContentType.WUMPUS, random.randrange(grid.size*grid.size))
    grid.add_contents(ContentType.PIT, random.randrange(grid.size*grid.size))
    grid.add_contents(ContentType.PIT, random.randrange(grid.size*grid.size))
    grid.add_contents(ContentType.BAT, random.randrange(grid.size*grid.size))
    grid.add_contents(ContentType.BAT, random.randrange(grid.size*grid.size))
    grid.add_contents(ContentType.TREASURE, random.randrange(grid.size*grid.size))
    for i in range(0, grid.size):
        for j in range(0, grid.size):
            ptr = grid.grid[i][j]
            print(f"{ptr.id}: ({ptr.point.x},{ptr.point.y}) - {ptr.list_exit_ids()}")
            if (ptr.contents != None):
                print(f"{ptr.id} contains {ptr.contents}")

main()