from cavegrid import *
from cavenode import *
import random

# initialize a grid of the given size and whether it loops around the sides or not
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

# randomly place the player on the map in a node that doesn't yet have contents
# if there's something there, move to the next one until you find an empty node
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

# the game loop
def game_loop(player):
    exit_keys = list(player.exits.keys())
    print(f"The player is currently in cave {player.id}")
    if player.contents != None:
        print(f"This cave contains: {player.contents}")
    print(f"Exits lead to: {exit_keys}")
    user_input = ""
    while user_input not in exit_keys:
        user_input = input()
        if user_input in exit_keys:
            move_player(player, user_input)
        else:
            print("Please enter a valid exit.")

# moves the player to the selected exit
def move_player(player, go_exit):
    game_loop(player.exits[go_exit])