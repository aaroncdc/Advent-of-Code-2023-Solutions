import sys

# This dictionary is used to convert text integers to numeric integers
numbs = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
         "six": 6, "seven": 7, "eight": 8, "nine": 9}
# This list contains all the numbers, including the words
numbs2 = list(numbs.keys())
numbs2.extend([str(i) for i in numbs.values()])
# Accumulator
accum = 0

# Open the puzzle input
with open("input_1.txt") as input_text:
    # Read line by line
    for line in input_text:
        # Make a list filled with several None elements, one per character
        numbern = [None for i in range(0,len(line)+1)]
        # Iterate through all the elements in numbs2
        for k in numbs2:
            try:
                # Get the first and last occurence of the number k
                # in the string.
                li = line.index(k)
                ri = line.rindex(k)
                # Add them to the numbern list at the place they were found
                # as an integer
                numbern[li] = numbs[k] if k in numbs.keys() else int(k)
                numbern[ri] = numbs[k] if k in numbs.keys() else int(k)
            # If no occurences are found, ValueError is raised.
            # Just ignore and continue.
            except ValueError as ve:
                continue
            # This should never happen.
            except IndexError as ie:
                print(f"IndexError\n{line}\n{len(line)}\n{li}\n{numbern}")
                sys.exit(-1)
        # numbern is going to contain a lot of None items. Remove them and
        # place everything into a new list.
        allres = list(filter(lambda i: i is not None, numbern))
        # The first element of allres is the first digit, and the last element
        # is the last digit. Asuming every number is two digits only,
        number = allres[0] * 10 + allres[-1]
        # It works even if there is a single number!
        # Add the number to the accumulator.
        accum += number
        # print(f"{line}\n{number}\n{accum}")

# Print the final answer
print(f"Answer: {accum}") # Answer: 53268