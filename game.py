from cavegrid import *
from cavenode import *
import random

def initialize_grid(size, looping = False):
    if size < 6:
        print("That grid is too small.  Pick something bigger.")
        return None
    grid = CaveGrid(size, looping)
    grid.add_contents(ContentType.WUMPUS, random.randrange(grid.full_size))
    grid.add_contents(ContentType.PIT, random.randrange(grid.full_size))
    grid.add_contents(ContentType.PIT, random.randrange(grid.full_size))
    grid.add_contents(ContentType.BAT, random.randrange(grid.full_size))
    grid.add_contents(ContentType.BAT, random.randrange(grid.full_size))
    grid.add_contents(ContentType.TREASURE, random.randrange(grid.full_size))
    return grid

def initialize_player(grid):
    original_id = random.randrange(grid.size*grid.size)
    current_id = original_id
    looped = False
    while looped == False or current_id != original_id:
        player_node = grid.get_node_from_id(current_id)
        if player_node.contents == None:
            return player_node
        current_id += 1
        if current_id == grid.full_size:
            current_id = 0
            looped = True
    raise Exception("The grid is too small!")
