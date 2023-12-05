seeds = []
maps = {}

filterstrlist = lambda lst: [i.strip() for i in filter(lambda x: x != " " and x != "" and x != "", lst)]
#sortdict = lambda d: dict(sorted(list(d)))
#zipsets = lambda s1,s2: set(zip(sorted(s1), sorted(s2)))
a_to_b = lambda txt: (filterstrlist(txt.split("-"))[0], filterstrlist(txt.split("-"))[2])

def seed_to_loc(seed):
    y = int(seed)
    keys = list(maps.keys())
    for map in keys:
        x = y
        for mapping in maps[map]:
            d,s,r = mapping
            if s <= y < s+r:
                y = (y-s)+d
                break
    return y

def loc_to_seed(seed):
    y = int(seed)
    keys = list(maps.keys())
    keys.reverse()
    for map in keys:
        x = y
        for mapping in maps[map]:
            d,s,r = mapping
            if d <= y < d+r:
                y = (y-d)+s
                break
    return y

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
            seeds = [int(i) for i in filterstrlist(line.split(":")[1].split(" "))]
            seeds = list(zip(seeds[::2], seeds[1::2]))
        else:
            if line == "" or line == "\n":
                if curmap is not None:
                    pass
            else:
                mapdata = [int(i) for i in filterstrlist(line.split(" "))]
                maps[curmap].append(mapdata)

m = 9999999999999999999
count = 0
"""
This solution is trash, but right now I don't know of a better way to do this
other than brute force my way into it.

How do I know that I should look up from values 411264428 downwards? Well, it's
simple. I ran the code I commented below, which checked only the intervals in
the last map. That told me what value in those intervals has the least value, and
then I figured I should just check from there, below.

Perhaps starting from 0 onwards would have been a much better idea.

Eventually, after a hour or so, it will find the solution. Again, it's trash,
but this is the best I can do right now. Hey, at least it works... ¯\_(ツ)_/¯
"""
for i in range(411264428, 0, -1):
    c = loc_to_seed(i)
    for sint in seeds:
        min,r = sint
        if min <= c < min+r:
            if c < m:
                m = c
        count += 1
        if count % 1000000 == 0:
            print(f"Still working... Step {int(i/1000000)}x10^6 Current: {m if m < 9999999999999999999 else 'Not found'} Iterations: {count/(10**6)}x10^6\n")

#for interv in sorted(list(maps["humidity-to-location"])):
#    print(f"Checking interval {interv}...\n")
#    d,s,r = interv
#    c = loc_to_seed(d)
#    cr = loc_to_seed(d+r)
#    c = cr if cr < c else c
#    for sint in seeds:
#        min,r = sint
#        if min <= c < min+r:
#            if c < m:
#                m = c
#                print(f"{m}\n")
#        count += 1
#        if count % 1000000 == 0:
#            print(f"Still working... Current: {m if m < 9999999999999999999 else 'Not found'} Iterations: {count/(10**6)}x10^6\n")

print(f"Answer: {m}, seed: {seed_to_loc(m)}") # 27992443