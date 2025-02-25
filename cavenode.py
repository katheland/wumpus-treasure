from enum import Enum

# a helper class to hold a point on the xy plane
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# types of things a CaveNode's contents can contain
class ContentType(Enum):
    WUMPUS = "wumpus",
    STINK = "stink",
    PIT = "pit",
    BREEZE = "breeze",
    BAT = "bat",
    SQUEAK = "squeak",
    TREASURE = "treasure",
    PLAYER = "player"

# a node of the cave system
# contains an ID, a point on the xy plane, any inhabitants or auras, and a list of CaveNodes it connects to
class CaveNode():
    def __init__(self, id, point):
        self.id = id
        self.point = point
        self.contents = None
        self.exits = []
    
    def list_exit_ids(self):
        exit_ids = []
        for exit in self.exits:
            exit_ids.append(exit.id)
        return exit_ids

