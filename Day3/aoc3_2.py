# This is a 2-dimensional list that represents the grid of the map
grid = []
# Lengths, just to not be calling len() all the time
x_length = 0
y_length = 0

# Check if the point is bounded (is inside the grid)
def is_bounded(x,y):
    return x >= 0 and x < x_length and y >= 0 and y < y_length

# This function reads a number from the grid at x,y
# Returns None if no number is found at that position
def read_num(x,y):
    num = None
    # Check if there is a number at x,y
    if grid[y][x].isnumeric():
        # num is going to be a string with the number
        num = ""
        # xn is the position of the first digit in the grid
        xn = x
        # Rewind (if there are digits before grid[x][y])
        if xn - 1 >= 0:
            while xn >= 0:
                # BUG: Somehow it works, but I just realized
                # while writting this that it might fall into an OOB exception if xn = 0
                # Needs to be checked. Anyways, it works, so...
                if grid[y][xn-1].isnumeric():
                    xn -= 1
                else: break
        # Read the number (until a dot or symbol is found)
        while xn < x_length:
            if grid[y][xn].isnumeric():
                num += grid[y][xn]
                xn += 1
            else: break
    return num

# Read the puzzle
with open("puzzle.txt") as puzzle_input:
    # Go row by row
    for line in puzzle_input:
        # Append the row to the grid
        grid.append([character.strip() for character in line])
# Set the lengths. The rows have one carriage character that doesn't count.
x_length = len(grid[0])-1
y_length = len(grid)

# This isn't necessary, could be checked directly in the grid
# but makes things easier to structure. Everything step
# is in it's own function this way.
# This returns a subgrid with the adjacent characters
# around the star.
def get_subgrid(x,y):
    # This is the subgrid. The character at 1,1 should always be the star.
    subgrid = [['.','.','.'],['.','.','.'],['.','.','.']]
    for yi in range(-1, 2):
        for xi in range(-1, 2):
            # It doesn't matter if some of the characters are out of
            # bounds with respect to the parent grid, these will be dots
            # in the subgrid and will be ignored anyways. But I set them
            # to None just in case.
            if is_bounded(x+xi,y+yi):
                subgrid[1+yi][1+xi] = grid[y+yi][x+xi]
            else:
                subgrid[1+yi][1+xi] = None
    return subgrid

# Check adjacent characters around the star.
# gx and gy is the offset (the position of the star in the grid) of the subgrid
def check_adj(subgrid, gx, gy):
    nums = []
    # This is a 3x3 grid
    for y in range(0,3):
        x = 0
        while x < 3:
            xn = 1
            # Ignore the star (center)
            if x == 1 and y == 1: pass
            else:
                # Is this a number?
                if subgrid[y][x].isnumeric():
                    xn = x
                    # This part is necessary to skip the number when reading.
                    # It counts how many digits are in the same number. Then
                    # sets xn to the number of digits.
                    while xn < 3:
                        if subgrid[y][xn].isnumeric() and xn + 1 < 3:
                            xn += 1
                        else: break
                    # Read the number from the parent grid
                    nums.append(read_num(gx+(x-1),gy+(y-1)))
            # Skip xn characters
            x += xn
    return list(set(nums)) # It sometimes includes repeating elements, make it a set

accum = 0
# Start reading the grid
for y in range(0, y_length):
    for x in range(0, x_length):
        # Look for a star
        if grid[y][x] == "*":
            # Check for adjacent numbers
            adj = check_adj(get_subgrid(x,y),x,y)
            # If there are exactly two numbers, then
            if len(adj) == 2:
                c = 1
                # Multiply them (also this could be a single product since we know it's two)
                for i in range(0,len(adj)):
                    c *= int(adj[i])
                # And then add it to the accumulator
                accum += c
            # If there are more than 2 numbers adjacent, then we ran into a problem.
            elif len(adj) > 2:
                print(f"PROBLEM: {x} {y} {len(adj)}\n{adj}") # This is for debugging only

print(f"Result: {accum}") # 84051670
            