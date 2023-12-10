from math import ceil, sqrt
import random
# Lambda function to filter lists with strings
filterstrlist = lambda lst: [i.strip() for i in filter(lambda x: x != " " and x != "" and x != "", lst)]

# 0 UP 1 DOWN 2 LEFT 3 RIGHT, None NOWHERE (Void) ,-1 UNKNOWN
# Each tuple is in the format:
# (Your direction, direction you can go from your direction)
# Example: (1,3) indicates that if your direction is up, you must turn right.
TILES = {
    "|": ((0,0),(1,1)),
    "-": ((2,2),(3,3)),
    "L": ((1,3),(2,0)),
    "J": ((1,2),(3,0)),
    "7": ((3,1), (0,2)),
    "F": ((2,1),(0,3)),
    ".": (None, None),
    "S": ((-1,-1),(-1,-1))
}

grid = []
grid_width, grid_height = 0,0

# Parse the puzzle input
with open("puzzle.txt") as pinput:
    for line in pinput:
        grid.append(filterstrlist([c.strip() for c in line]))

# Find the grid dimensions
grid_width,grid_height = len(grid[0]), len(grid)

# Find the starting tile in the grid
start = None
for y in range(0,grid_height):
    if start: break
    for x in range(0, grid_width):
        if grid[y][x] == "S":
            start = (x,y)
            break

# Set the current tile to the start
ctile = [start[0], start[1]]
tiles = 0
cdir = 0
#max_traversed = 0

#max_dist = 0
#f_tile = [start[0], start[1]]

while tuple(ctile) != start or tiles == 0:
    # Find what directions we can go from the current tile
    if tuple(ctile) == start:
        # This only executes at the start since we don't know where we can go from here.
        directions = []
        # There might be better ways to do this, but it works
        if ctile[1] + 1 < grid_height:
            if grid[ctile[1]+1][ctile[0]] in ["|", "J", "L"]: directions.append(1) # We can go down
        if start[1] - 1 >= 0:
            if grid[ctile[1]-1][ctile[0]] in ["|", "F", "7"]: directions.append(0) # We can go up
        if start[0] + 1 < grid_width:
            if grid[ctile[1]][ctile[0]+1] in ["-", "7"]: directions.append(3) # We can go right
        if start[0] - 1 >= 0:
            if grid[ctile[1]][ctile[0]-1] in ["-", "F"]: directions.append(2) # We can go left
        # Select one direction randomly, since it doesn't matter
        if len(directions) == 0: raise Exception(f"ERROR: No directions from tile {ctile}.")
        cdir = random.choice(directions)
    else:
        # If we are not at the start, this is where we find the next direction
        directions = TILES[grid[ctile[1]][ctile[0]]]
        if cdir == directions[0][0]: cdir = directions[0][1]
        elif cdir == directions[1][0]: cdir = directions[1][1]
        else: raise Exception(f"No directions from {ctile} going {cdir}: {directions}")

    # Traverse the pipe
    match cdir:
        case 0: ctile[1] -= 1
        case 1: ctile[1] += 1
        case 2: ctile[0] -= 1
        case 3: ctile[0] += 1

    # Increase the number of tiles traversed.
    tiles += 1

    """
    I'll leave this piece of code commented here. The problem asks for the number of
    steps from the starting position to the farthest. While it's true that the farthest
    might be halfway through the loop, and one of the examples mentions that, it's not true
    that the farthest point is necessarily halfway through the loop. This point is the point
    where the length of the position vector in the loop is at it's highest. Which is what this
    piece of code right here was looking for.

    Apparently, the problem proposed only wants the point halfway of the loop. Which is
    ambiguous and not technically correct the way the problem is proposed. Or maybe I didn't
    understand it correctly at first.
    """
    # Check how far we are from the start
    #dist = sqrt((start[0]-ctile[0])**2 + (start[1]-ctile[1])**2)
    #if dist > max_dist:
    #    print(f"New max: {ctile} after {tiles} tiles traversed, with a distance of {dist} from the origin")
    #    f_tile = ctile
    #    max_dist = dist
    #    max_traversed = tiles

# Show the solution, which is half of the distance traveled.
print(f"{ceil(tiles/2)}") # 6867