from cavenode import *

# a square grid of CaveNodes
# (further shapes of grids can be implemented later)
class CaveGrid():
    def __init__(self, size, looping = False):
        self.size = size
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
    
    # get the cave node that has a given id
    def get_node_from_id(self, id):
        if id < 0 or id >= self.size * self.size:
            return None
        x = id // self.size
        y = id % self.size
        return self.grid[x][y]