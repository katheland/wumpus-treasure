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
    TREASURE = "treasure"

# a node of the cave system
# contains an ID, a point on the xy plane, any inhabitants or auras, and a list of CaveNodes it connects to
class CaveNode():
    def __init__(self, id, point):
        self.id = id
        self.point = point
        self.contents = None
        self.exits = {}
    
    # get a list of the ids of the exit nodes
    def list_exit_ids(self):
        exit_ids = []
        for exit in self.exits:
            exit_ids.append(self.exits[exit].id)
        return exit_ids
    
    # set the contents of a node, and extend its aura to its neighbors
    def set_contents(self, contents):
        self.contents = contents
        for exit in self.exits:
            match contents:
                case ContentType.WUMPUS:
                    self.exits[exit].contents = ContentType.STINK
                case ContentType.PIT:
                    self.exits[exit].contents = ContentType.BREEZE
                case ContentType.BAT:
                    self.exits[exit].contents = ContentType.SQUEAK
    
    # check whether the node and its exits are all empty of contents
    def area_is_clear(self):
        if self.contents != None:
            return False
        for exit in self.exits:
            if self.exits[exit].contents != None:
                return False
        return True

