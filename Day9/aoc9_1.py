# Lambda function to filter lists with strings
filterstrlist = lambda lst: [int(i.strip()) for i in filter(lambda x: x != " " and x != "" and x != "", lst)]

"""
Here I'm just following the instructions provided by
the puzzle problem, there isn't much to comment.

Optimizations might be applicable.
"""

nextsum = 0
with open("puzzle.txt") as pinput:
    for line in pinput:
        rows = []
        seq = filterstrlist(line.split(" "))
        rows.append(seq)
        crow = []
        while True:
            for i in range(0, len(seq)-1):
                crow.append(seq[i+1]-seq[i])
            rows.append(crow)
            if len(set(crow)) == 1:
                if crow[0] == 0:
                    break
            seq = crow
            crow = []
        a = 0
        for row in range(len(rows)-1, -1, -1):
            a = a + rows[row-1][-1]
        nextsum += a

print(nextsum) # 1584748274