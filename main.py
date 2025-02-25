import sys
from game import *

def main():
    # default values
    size = 7
    looping = False
    # defaults can be changed with arguments
    if len(sys.argv) >= 2:
        size = int(sys.argv[1])
    if len(sys.argv) == 3:
        looping = bool(sys.argv[2])

    grid = initialize_grid(size, looping)
    player = initialize_player(grid)
    for i in range(0, grid.size):
        for j in range(0, grid.size):
            ptr = grid.grid[i][j]
            print(f"{ptr.id}: ({ptr.point.x},{ptr.point.y}) - {ptr.list_exit_ids()}")
            if (ptr.contents != None):
                print(f"{ptr.id} contains {ptr.contents}")
    print(f"The player is starting at node {player.id}")

main()