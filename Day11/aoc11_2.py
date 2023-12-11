from math import factorial

# This is a distance multiplier
PADDING = 10**6 - 1

grid = []

# Lambda function to filter lists with strings
filterstrlist = lambda lst: [i.strip() for i in filter(lambda x: x != " " and x != "" and x != "", lst)]

with open("puzzle.txt") as puzzle_input:
    for line in puzzle_input:
        grid.append(filterstrlist([c.strip() for c in line]))

# Find the grid dimensions
grid_width,grid_height = len(grid[0]), len(grid)

# In the first part, I expanded the grid thinking it was going to be necessary for some reason.
# But the thing is, this isn't necessary! We only need to know the x and y positions of the
# rows and columns that are all dots though, so we'll find these:

rows_to_append = []
for y in range(0, grid_height):
    if len(set(grid[y])) == 1 and grid[y][0] == ".":
        rows_to_append.append(y)

# Now we do the same with the columns:
cols_to_append = []
for x in range(0, grid_width):
    col = [] # I don't know if python can read columns in some way, I don't think so,
    # so here is a temporary list containing the column items
    for y in range(0, grid_width):
        col.append(grid[y][x])
    if len(set(col)) == 1 and col[0] == ".":
        cols_to_append.append(x)

# Instead of expanding the grid, calculate how much space padding we have
# (And multiply it by PADDING later)
def calc_expansion(x,y):
    exp_x = [i for i in cols_to_append if i <= x]
    exp_y = [j for j in rows_to_append if j <= y]
    return(len(exp_x),len(exp_y))

galaxies = {} # Dictionary containing the galaxies and their position, in a tuple.
gc = 0 # Galaxy counter. This is also the total number of galaxies.

# Look for galaxies in the expanded grid. For optimization purposes, this should
# be done during the expansion. But to make things easier, I'll just do it here.
# It adds another xy iteration but, whatever.
# We have into account the expansion.

for y in range(0,grid_height):
    for x in range(0,grid_width):
        if grid[y][x] == "#":
            if str(gc) not in list(galaxies.keys()):
                exp = calc_expansion(x,y)
                galaxies[str(gc)] = (x + (exp[0] * PADDING),y + (exp[1] * PADDING))
                gc += 1

# Now calculate the distance between all galaxies
# The number of pairs is gc choose 2. This is a binomial coefficient.

slengths = 0
maxpairs = factorial(gc)/(2*factorial(gc-2)) # This is unnecessary though.

for i in galaxies.keys():
    for j in galaxies.keys():
        if j != i:
            # If A and B are vectors representing each galaxy, calculate B-A
            A = galaxies[i]
            B = galaxies[j]
            ba = (B[0] - A[0], B[1] - A[1])
            # The distance is the sum of the components of B - A.
            # Because these components can be negative, we compute the absolute value.
            slengths += abs(ba[1]) + abs(ba[0])
        else: break # Break after j reaches i

print(slengths) # 553224415344