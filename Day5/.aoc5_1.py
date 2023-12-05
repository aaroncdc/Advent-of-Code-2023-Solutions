"""
I tried using set theory first to solve this problem.
I ended with a very cute 'fork' bomb or memory flooder.
Then I figured I didn't need set theory, I could just
find the relation and use a piece-wise function
to figure out the y value according to a seed x.

The final answer is in aoc5_1_2.py

If you need to memtest your computer, you can try
running this script... at your own risk!

Maybe in 200 years computers will have enough memory
to run this script.
"""
seeds = []
maps = {}

filterstrlist = lambda lst: [i.strip() for i in filter(lambda x: x != " " and x != "" and x != "", lst)]
sortdict = lambda d: dict(sorted(list(d)))
zipsets = lambda s1,s2: set(zip(sorted(s1), sorted(s2)))
a_to_b = lambda txt: (filterstrlist(txt.split("-"))[0], filterstrlist(txt.split("-"))[2])

def seed_to_loc(seed):
    print(f"Seed {seed}")
    s = int(seed)
    keys = list(maps.keys())
    for map in keys:
        if s in maps[map]:
            s = maps[map][s]
    print(f"loc {s}")
    return s

with open("puzzle.txt") as puzzle_test:
    curmap = None
    curmapsets = []
    xsets = []
    for line in puzzle_test:
        if "map" in line:
            mapname = line.split(" ")[0].strip()
            if mapname not in maps.keys():
                maps[mapname] = None
            curmap = mapname
        elif "seeds" in line:
            seeds = filterstrlist(line.split(":")[1].split(" "))
        else:
            if line == "" or line == "\n":
                if curmap is not None:
                    bset = []
                    for ma in curmapsets:
                        bset.extend(ma)
                    #maps[curmap] = sortdict(bset)
                    curmap = None
                    curmapsets = []
                    xsets = []
                    print(f"Completed {curmap}")
            else:
                # Here we have the mapping information
                mapdata = [int(i) for i in filterstrlist(line.split(" "))]
                S = [i for i in range(mapdata[1],mapdata[1]+mapdata[2])]
                xsets.extend(S)
                D = [i for i in range(mapdata[0],mapdata[0]+mapdata[2])]
                curmapsets.append(zipsets(S,D))

locs = [seed_to_loc(i) for i in seeds]
#print(locs)
print(min(locs)) # 379811651