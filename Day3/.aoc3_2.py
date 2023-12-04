grid = []
x_length = 0
y_length = 0

def clamp(val:int ,min: int,max: int)->int:
    if val < min: return min
    if val > max: return max
    return val

with open("puzzle_test.txt") as puzzle_input:
    for line in puzzle_input:
        grid.append([character.strip() for character in line])
x_length = len(grid[0])-1
y_length = len(grid)

def read_num(x,y):
    num = None
    #print(grid[y][x])
    if grid[y][x].isnumeric():
        num = None
        xn = x
        # Rewind (if there are digits before grid[x][y])
        if xn - 1 >= 0:
            while xn >= 0:
                if grid[y][xn-1].isnumeric():
                    xn -= 1
                else: break
        # Read the number
        while xn < x_length:
            if grid[y][xn].isnumeric():
                num += grid[y][xn]
                xn += 1
            else: break
    return num

def check_num(x,y):
    num = None
    star = None
    if grid[y][x].isnumeric():
        num = ""
        # Check if position below is a star
        if y+1 < y_length:
            if grid[y+1][x] == "*":
                star = [x,y+1,1,x,y] # Below (1)
        xn = x
        startx = x
        # Rewind (if there are digits before grid[x][y])
        if xn - 1 >= 0:
            while xn >= 0:
                if grid[y][xn-1].isnumeric():
                    xn -= 1
                    startx = xn
                else: break
        # Read the number
        while xn < x_length:
            if grid[y][xn].isnumeric():
                num += grid[y][xn]
                xn += 1
            else:
                # Check diagonals and right positions
                if grid[y][xn] == "*":
                    star = [xn,y,0,startx,y] # To the right (0)
                if y-1 > 0:
                    if grid[y-1][xn] == "*":
                        star = [xn,y-1,2,startx,y] # Top Diagonal (2)
                if y+1 < y_length:
                    if grid[y+1][xn] == "*":
                        star = [xn,y+1,3,startx,y] # Bottom Diagonal (3)
                if y+1 < y_length and startx-1 > 0:
                    if grid[y+1][startx-1] == "*":
                        star = [startx-1,y+1,4,startx,y] # Bottom Diagonal Left (4)
                break
        # Check star
        if star is not None:
            print(f"Star found: {star}")
            num2 = None
            match star[2]:
                case 0:  # Star is right from num
                    num2 = read_num(star[0],star[1])
                    pass
                case 1: # Star is below num
                    pass
                case 2: # Star is diagonal top of num
                    pass
                case 3: # Star is diagonal bottom of num
                    pass
                case 4: # Star is diagonal left bottom of num
                    pass
    return num

print(check_num(1,0))
print(check_num(7,0))
print(check_num(1,4))
print(check_num(3,9))
print(check_num(7,7))
#print(f"Result: {accum}") # 84051670
            