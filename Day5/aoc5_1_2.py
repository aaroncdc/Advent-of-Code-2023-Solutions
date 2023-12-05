# Seeds
seeds = []
# Map ranges
maps = {}

# This creates a list that contains no empty elements from a string
filterstrlist = lambda lst: [i.strip() for i in filter(lambda x: x != " " and x != "" and x != "", lst)]

# Lots of unused lambda function:
#sortdict = lambda d: dict(sorted(list(d)))
#zipsets = lambda s1,s2: set(zip(sorted(s1), sorted(s2)))
#a_to_b = lambda txt: (filterstrlist(txt.split("-"))[0], filterstrlist(txt.split("-"))[2])

# Get a location from a seed.
def seed_to_loc(seed):
    y = int(seed)
    keys = list(maps.keys())
    for map in keys:
        for mapping in maps[map]:
            d,s,r = mapping
            if s <= y < s+r:
                # I figured out that, if this is a function, then there has to be
                # a relation. If s is the source and d the destination, then x R y
                # by the formula y = (x-s) + d. In this case I reuse y to create a
                # recursion.
                y = (y-s)+d
                break
    return y

# Believe it or not, this is surprisingly fast for what it is
with open("puzzle.txt") as puzzle_test:
    curmap = None
    curmapsets = []
    xsets = []
    for line in puzzle_test:
        if "map" in line:
            mapname = line.split(" ")[0].strip()
            if mapname not in maps.keys():
                maps[mapname] = []
            curmap = mapname
        elif "seeds" in line:
            seeds = filterstrlist(line.split(":")[1].split(" "))
        else:
            if line == "" or line == "\n":
                if curmap is not None:
                    pass
            else:
                mapdata = [int(i) for i in filterstrlist(line.split(" "))]
                maps[curmap].append(mapdata)

locs = [seed_to_loc(i) for i in seeds]
print(min(locs)) # 379811651