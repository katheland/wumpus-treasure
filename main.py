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
    
    game_loop(player)

main()