from cavegrid import *

def main():
    grid = CaveGrid(7)
    for i in range(0, grid.size):
        for j in range(0, grid.size):
            print(f"{grid.grid[i][j].id}: ({grid.grid[i][j].point.x},{grid.grid[i][j].point.y}) - {grid.grid[i][j].exits}")

main()