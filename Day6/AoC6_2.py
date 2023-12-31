from math import sqrt, ceil

# Common lambda functions I use for handling sets and arrays
filterstrlist = lambda lst: [i.strip() for i in filter(lambda x: x != " " and x != "" and x != "", lst)]
zipsets = lambda s1,s2: set(zip(s1, s2))

# Quadratic equation solver, returns the velocity in terms of the distance (d) and
# a constant max time for the race (r).
# The formula comes from solving the equation -v^2+rv-d = 0
def solve_v(r,d):
    p1 = (r + sqrt(r**2 - (4*d)))/2
    p2 = (r - sqrt(r**2 - (4*d)))/2
    return set([p1,p2])

# Max race time
r = 0
# Best distance
wd = 0
# Parse the puzzle
with open("puzzle.txt") as puzzle_input:
    for line in puzzle_input:
        spl = filterstrlist(line.split(":"))
        if spl[0] == "Time":
            r = int(''.join(filterstrlist(spl[1].split(" ")))) 
        else:
            wd = int(''.join(filterstrlist(spl[1].split(" "))))

# Calculates how many possible ways of winning there are for the race
r = int(r)
wd = int(wd)
# The critical point of the equation v(r-v) is at v = r/2 (d/dv [v(r-v)] = 0)
mr = r/2
# From here, we asume everything is integers and not real numbers.
# The maximum distance that can be traveled is mr * (r-mr), being mr
# the critical point v = r/2. Rounded to the nearest integer.
mdist = round(mr*(r-mr))
# The race is winnable only if mdist is greater than wd (the best distance)
if mdist > wd:
    # Since the equation of the distance is quadratic, there are two points
    # that can result in the same distance, wv1 and wv2 (wv1 < wv2).
    wv1,wv2 = solve_v(r,wd)
    # If wv1 and wv2 are real numbers, every point in the open interval
    # (wv1, wv2) will result in a greater distance. However, d is an
    # integer, therefore we need to mind the rounding.
    # The number of wins is wv2 - wv1 - 1
    print(f"Total wins: {abs(ceil(wv2) - int(wv1) - 1)}") # 28973936
else:
    print("Not winnable")