# The total sum of the powers
power_sum = 0
# Open the puzzle input
with open("games.txt") as puzzle_input:
    # Read each record
    for record in puzzle_input:
        # The current power
        power = 0
        # Total cubes in each subset
        total_sub = {"red": 0, "green": 0, "blue": 0}
        # Separate the number of the game from the subsets
        ls1 = [i.strip() for i in record.split(":")]
        # Now separate each subset.
        ls2 = [i.strip() for i in ls1[1].split(";")]
        for subset in ls2:
            # Separate each color in the subset
            ls3 = [i.strip() for i in subset.split(",")]
            # Read each color
            for color in ls3:
                data = [i.strip() for i in color.split(" ")]
                # We want the minimum number of cubes required for each game to be possible.
                # So we store the biggest number of cubes for each color obtained in each
                # subset.
                if(total_sub[data[1].lower()] < int(data[0])):
                    total_sub[data[1].lower()] = int(data[0])
        # Calculate the power
        power = total_sub["red"] * total_sub["green"] * total_sub["blue"]
        # Sum the total power
        power_sum += power
            
# Display the sum.
print(f"The sum is {power_sum}") # Should be 62241