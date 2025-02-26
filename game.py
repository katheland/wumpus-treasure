from cavegrid import *
from cavenode import *
import random

# initialize a grid of the given size and whether it loops around the sides or not
def initialize_grid(size, looping = False):
    if size < 6:
        print("That grid is too small.  Pick something bigger.")
        quit()
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

# print and deal with what's at the player's location
def print_location(grid, player):
    print(f"The player is currently in cave {player.id}.")
    match player.contents:
        case ContentType.WUMPUS:
            print("Oh no!  You woke up the Wumpus!")
            lose()
        case ContentType.STINK:
            print("Something nearby smells really bad.")
            print(f"Exits lead to: {player.list_exits()}")
            game_loop(grid, player)
        case ContentType.PIT:
            print("Oh no!  You fell down a pit!")
            lose()
        case ContentType.BREEZE:
            print("There's a draft in this cave, though it's hard to tell from where.")
            print(f"Exits lead to: {player.list_exits()}")
            game_loop(grid, player)
        case ContentType.BAT:
            print("Before you can react, a giant bat swoops down and grabs you, flying you to a random cave!")
            print_location(grid, initialize_player(grid))
        case ContentType.SQUEAK:
            print("The sound of high-pitched squeaks echoes around you.")
            print(f"Exits lead to: {player.list_exits()}")
            game_loop(grid, player)
        case ContentType.TREASURE:
            print("The cave is filled with gold and jewels!")
            win()
        case None:
            print(f"Exits lead to: {player.list_exits()}")
            game_loop(grid, player)

# waits for and handles player input
def game_loop(grid, player):
    exit_keys = list(player.exits.keys())
    user_input = ""
    while user_input not in exit_keys:
        user_input = input()
        if user_input in exit_keys:
            move_player(grid, player, user_input)
        else:
            print("Please enter a valid exit.")

# moves the player to the selected exit
def move_player(grid, player, go_exit):
    print_location(grid, player.exits[go_exit])

# lose message
def lose():
    print("You lose.  Better luck next time!")

# win message
def win():
    print("You win!  Congratulations!")