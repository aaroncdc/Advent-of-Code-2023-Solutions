moves = None
directions = {}

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

# Number of steps taken
steps = 0
# Current node
current = "AAA"

# Traverse the whole tree until we reach the destination node
while current != "ZZZ":
    # Move one step in the given direction
    current = directions[current][0 if moves[steps%len(moves)] == "L" else 1]
    steps += 1 # Increase the number of steps taken
    # Check if the destination is reachable (Doesn't check for circular paths though)
    if current != "ZZZ" and directions[current][0] == directions[current][1] == current:
        print(f"Destination unreachable after {steps} steps.\nCurrent: {current}, next: {directions[current]}")
        break

# How many steps did we take?
print(f"Destination reached in {steps} steps") # 19951