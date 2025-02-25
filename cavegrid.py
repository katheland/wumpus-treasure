from cavenode import *

# a square grid of CaveNodes
# (further shapes of grids can be implemented later)
class CaveGrid():
    def __init__(self, size, looping = False):
        self.size = size
        self.full_size = size*size
        self.grid = self._init_grid()
        self._connect_grid(looping)

    # initializes a square grid of CaveNodes of a given size
    def _init_grid(self):
        id = 0
        grid = []
        for i in range(0, self.size):
            row = []
            for j in range(0, self.size):
                cell = CaveNode(id, Point(i, j))
                row.append(cell)
                id += 1
            grid.append(row)
        return grid

    # adds a CaveNode's adjacent squares to its exits
    # loop: True if the player can loop around the sides of the grid, False if not
    def _connect_grid(self, loop = False):
        # a single room doesn't have anything to connect to...
        if self.size <= 1:
            return
        for i in range(0, self.size):
            for j in range(0, self.size):
                node = self.grid[i][j]
                # left neighbor
                if i > 0:
                    node.exits.append(self.grid[i-1][j])
                elif loop:
                    node.exits.append(self.grid[self.size-1][j])
                # right neighbor
                if i < self.size - 1:
                    node.exits.append(self.grid[i+1][j])
                elif loop:
                    node.exits.append(self.grid[0][j])
                # upper neighbor
                if j > 0:
                    node.exits.append(self.grid[i][j-1])
                elif loop:
                    node.exits.append(self.grid[i][self.size-1])
                # lower neighbor
                if j < self.size - 1:
                    node.exits.append(self.grid[i][j+1])
                elif loop:
                    node.exits.append(self.grid[i][0])
    
    # set the contents at the given id
    # if the area isn't clear, move to the next node until you find a clear area
    def add_contents(self, contents, id):
        current_id = id
        looped = False
        while looped == False or current_id != id:
            current_node = self.get_node_from_id(current_id)
            if contents == ContentType.TREASURE and current_node.contents == None:
                current_node.set_contents(contents)
                return
            if current_node.area_is_clear():
                current_node.set_contents(contents)
                return
            current_id += 1
            if current_id == self.full_size:
                current_id = 0
                looped = True
        raise Exception("The grid is too small!")
            
    # get the cave node that has a given id
    def get_node_from_id(self, id):
        if id < 0 or id >= self.full_size:
            return None
        x = id // self.size
        y = id % self.size
        return self.grid[x][y]