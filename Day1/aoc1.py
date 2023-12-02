# Open the puzzle input
with open("input_1.txt") as input_text:
    accum = 0 # Accumulator
    # Read line by line
    for line in input_text:
        # List with all the numbers in the text
        nums = []
        # Go character by character
        for chara in line:
            # If the character is a number
            if chara.isnumeric():
                # Append it
                nums.append(chara)
        # If only one number is found, the two digits are the same.
        if len(nums) == 1:
            accum += int(nums[0] + nums[0])
            #print(f"{line}\n {nums[0]}{nums[0]}  {accum}")
        # The first element of allres is the first digit, and the last element
        # is the last digit. Asuming every number is two digits only:
        else:
            accum += int(nums[0] + nums[-1])
            #print(f"{line}\n {nums[0]}{nums[-1:][0]} {accum}")
    # Print the final answer
    print(f"Answer: {accum}") #Answer: 53080

"""
NOTE: This works just fine, but it would be better to use index() and rindex()
like in the second part.
"""