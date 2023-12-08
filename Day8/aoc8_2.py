from math import lcm,gcd
moves = None
directions = {}
paths = []

# Built in lcm can't handle lists of integers so I had to make my own.
# Python devs please support lists of integers in lcm.
def llcm(ints: list):
    lcm = 1
    for i in ints:
        lcm = int((lcm*i)/gcd(int(lcm),i))
    return lcm

# Lambda function to filter lists with strings
filterstrlist = lambda lst: [i.strip() for i in filter(lambda x: x != " " and x != "" and x != "", lst)]
# Convert a string tuple into a real tuple
strtup = lambda strn: tuple(filterstrlist(strn.replace("(","").replace(")","").split(",")))

# Parse the puzzle
with open("puzzle.txt") as pinput:
    for l in pinput:
        if not moves:
            moves = l.strip().upper()
        else:
            if "=" in l:
                tmp = filterstrlist(l.split("="))
                directions[tmp[0]] = strtup(tmp[1])

# Find all possible starting paths
spaths = [p[0] for p in directions.items() if p[0][-1] == "A"]

# For all starting paths, figure out where do we end following the given steps
for spath in spaths:
    steps = 0 # Number of steps
    current = spath # Current node
    unreach = False # Is the destination unreachable? (Debug only)

    # While we are not in a destination node
    while current[-1] != "Z":
        # Move one step in the given direction
        current = directions[current][0 if moves[steps%len(moves)] == "L" else 1]
        steps += 1 # Increase the number of steps taken
        # Check if the destination is reachable (Doesn't check for circular paths though)
        if current != "Z" and directions[current][0] == directions[current][1] == current:
            unreach = True
            print(f"Destination unreachable after {steps} steps.\nCurrent: {current}, next: {directions[current]}")
            break
    # Append the path information
    paths.append((spath, current, steps, unreach))

# Calculate the total number of steps required
# For all paths to be at the destination at the same time.
# This is the LCM of all the required steps.
print(llcm(tuple([s[2] for s in paths]))) # 16342438708751