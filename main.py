from cavegrid import *
import random

def main():
    grid = CaveGrid(7)
    for i in range(0, grid.size):
        for j in range(0, grid.size):
            ptr = grid.grid[i][j]
            print(f"{ptr.id}: ({ptr.point.x},{ptr.point.y}) - {ptr.list_exit_ids()}")
            if (ptr.contents != None):
                print(f"{ptr.id} contains {ptr.contents}")

main()