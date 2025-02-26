# wumpus-treasure
Treasure of the Wumpus, a variant of Hunt the Wumpus

You are an explorer, searching for a lost treasure said to be found in this system of caves.  These caves, however, are also home to the legendary Wumpus, a creature that has been hunted many times in the past, and has therefore lost all ability to trust or bargain.  If you find the Wumpus, you won't come back alive.  The caves are also home to other hazards as well.  Giant bats will pick you up and fly you around, disorienting you.  And some caves contain pit traps, which allow gravity to do the dirty work.

Use your wits to maneuver the caves, avoid the obstacles, let the Wumpus sleep, and claim its treasure for your own!

How to play:  `python3 main.py [-s] [-l]`

-s (--size) is an int that determines the size of the square grid of the cave system.  It needs to be 6 or greater, and defaults to 7.

-l (--loop) is a bool that decides whether the caves loop on the sides.  It defaults to False.

There are two pits, two bats, one Wumpus, and one treasure that are randomly placed.  All but the treasure have an aura of one square that indicates that it's nearby: a pit has a draft, a bat has sounds of squeaking, and a Wumpus has a bad smell.  The player is then randomly placed in a cave that has no hazard or aura.  Move by inputting one of the directions listed in the cave's exits.

# Potential future improvements

- cave systems of different shapes (ex. hexagonal grid, the original dodecahedron, arbitrary)
- make it visual with Pygame
- allow for varying the number of each hazard
- allowing bats and the Wumpus to move

Written by Katherine Anderson