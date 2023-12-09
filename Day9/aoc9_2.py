# Lambda function to filter lists with strings
filterstrlist = lambda lst: [int(i.strip()) for i in filter(lambda x: x != " " and x != "" and x != "", lst)]

"""
This is exactly the same as part 1, except
the last part is inverted. Instead of adding the last
of each row, you subtract the first.
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
        for row in range(len(rows)-1, 0, -1):
            a = rows[row-1][0] - a
        nextsum += a

print(nextsum) # 1026