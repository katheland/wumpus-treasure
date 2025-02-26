import argparse
from game import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", type=int, default=7)
    parser.add_argument("-l", "--loop", type=bool, default=False)
    args = parser.parse_args()
    
    grid = initialize_grid(args.size, args.loop)
    player = initialize_player(grid)
    
    print("Welcome to Treasure of the Wumpus!")
    print("Let your treasure hunt begin, adventurer!")
    print_location(grid, player)

main()