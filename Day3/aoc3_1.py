# This is a 2-dimensional list that represents the grid of the map
grid = []
# Lengths, just to not be calling len() all the time
x_length = 0
y_length = 0

# Determine if this is a valid symbol
def issymbol(s: str)->bool:
    return not s.isalpha() and not s.isnumeric() and s != '.'

# Clamp a value. Can be replaced with the built in
# functions min and max, wherever necessary
def clamp(val:int ,min: int,max: int)->int:
    if val < min: return min
    if val > max: return max
    return val

# Read the puzzle
with open("puzzle.txt") as puzzle_input:
    # Go row by row
    for line in puzzle_input:
        # Append the row to the grid
        grid.append([character.strip() for character in line])
# Set the lengths. The rows have one carriage character that doesn't count.
x_length = len(grid[0])-1
y_length = len(grid)

total_sum = 0
# Iterate through the grid (column (y), row (x))
for y in range(0, y_length):
    x = 0
    # We need to be able to modify x so that we can skip what we already
    # processed.
    while x < x_length:
        # Number of characters (x) to skip
        xi = 1
        # If the character is a number
        if grid[y][x].isnumeric():
            # Start building the number string
            numstr = grid[y][x]
            # Check if the adjacent characters in the row are also numbers
            for i in range(x+1, x_length):
                if grid[y][i].isnumeric():
                    # Append them to the number string
                    numstr += grid[y][i]
                    # We will skip xi characters later
                    xi = len(numstr)
                else:
                    # Not a digit, stop
                    break
            # Is this a symbol?
            symb = False
            # Check for adjacent symbols by reading from the top row to the
            # bottom row of the number, len(numstr) characters each time.
            # (Yes, it performs unnecessary operations, it's not optimized)
            for yj in range(-1,2):
                # If we find one symbol, that's enough
                if symb: break
                # Check each character in the row
                for xk in range(-1,len(numstr)+1):
                    # If this is a symbol
                    if issymbol(grid[clamp(y+yj,0,y_length-1)][clamp(x+xk,0,x_length-1)]):
                        # Then the number goes into the sum
                        total_sum += int(numstr)
                        # And we raise the flag
                        symb = True
                        # We're done
                        break
        # Skip xi characters (1 by default, unless a number was found)
        x += xi

print(f"Result: {total_sum}") # 532428
            