"""
This is a Work in Progress and I left it aside for now because,
in all honesty, I'm not feeling too well, it's late, and I don't
feel like working on this right now because I have a headache.

Might work on it later.

The problem is a little bit more complicated than it looks like
at first. In theory it should be solved with some kind of
flood-fill or depth-first search algorithm. But again, it's late
and I'm a little bit sick rn so I'm goin to leave this incomplete
for now.

Some people says that you can count if the number of loop walls
to the left of any . is odd. If so, it counts. That's not true.

Consider the following example:

.F-------7.
.|...F--7|.
.L---J..L7.

The last row has 5 walls, then 2 dots. However, those dots are
outside and not inside. Then it has 2 walls, and another dot (also
outise). This is why this method won't work (It's the first thing
I tried, the answer is 2 which is clearly not right).

Counting walls like | won't work either. You might find interior
spots next to L7 or FJ junctions for instance.

I considered several methods. Flood filling is one, the other one
is shrinking the walls, removing those that overlap. The path after
shrinking it can only contain interior points so following the path
would only have interior points. But you have to deal with walls
overlapping and it's more complicated. Flood filling seems more correct,
but the junctions might be a problem. You'd need to find which side from
you direction is looking inside and fetch those points while traversing
the loop.

I also considered other ideas like using the junctions as vertices and
checking points inside the lines intersecting 4 of them each time. But
that seems complicated as well.
"""

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
    "S": ((-1,-1),(-1,-1))
}

grid = []
grid_width, grid_height = 0,0

# Parse the puzzle input
with open("puzzle_test4.txt") as pinput:
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

loop_tiles = {}

while tuple(ctile) != start or tiles == 0:
    # Add this tile to the loop tile list
    if str(ctile[1]) not in loop_tiles:
        loop_tiles[str(ctile[1])] = [ctile[0]]
    else:
        loop_tiles[str(ctile[1])].append(ctile[0])

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

#print(f"{ceil(tiles/2)}") # 6867

# Sort the tile list in the loop
for k in loop_tiles.keys():
    loop_tiles[k] = sorted(loop_tiles[k])

loop_min_y = min([int(c) for c in list(loop_tiles.keys())])
loop_max_y = max([int(c) for c in list(loop_tiles.keys())])
loop_min_x = 99999
loop_max_x = 0

for row in loop_tiles:
    tl = [int(x) for x in row]
    loop_min_x = min(tl) if min(tl) < loop_min_x else loop_min_x
    loop_max_x = max(tl) if max(tl) > loop_max_x else loop_max_x

print(loop_tiles)

"""
L7  FJ
"""
on_wall = False
inside = False
possible_nests = 0
for y in range(loop_min_y, loop_max_y+1, 1):
    inside = False
    for x in range(loop_min_x, loop_max_x+1, 1):
        if grid[y][x] in list(TILES.keys()) and x in loop_tiles[str(y)]:
            inside = not inside
        elif inside:
            possible_nests += 1
print(possible_nests)