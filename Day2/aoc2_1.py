# Total of cubes in the bag
RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

# Total of possible games
possible = 0
# Open the puzzle input
with open("games.txt") as puzzle_input:
    # Read each record
    for record in puzzle_input:
        # Flag that indicates if a game is possible
        is_possible = True
        # Total cubes in each subset
        total_sub = {"red": 0, "green": 0, "blue": 0}
        # Separate the number of the game from the subsets
        ls1 = [i.strip() for i in record.split(":")]
        # Obtain the game number. Could also use a counter since they are in reading order.
        game = int(ls1[0].split(" ")[1])
        # Now separate each subset
        ls2 = [i.strip() for i in ls1[1].split(";")]
        for subset in ls2:
            # Separate each color in the subset
            ls3 = [i.strip() for i in subset.split(",")]
            # Read each color
            for color in ls3:
                data = [i.strip() for i in color.split(" ")]
                total_sub[data[1].lower()] = int(data[0])
            # Check if the game is possible by comparing each cube with the number
            # of cubes in the bag
            if total_sub["red"] > RED_CUBES or total_sub["green"] > GREEN_CUBES or total_sub["blue"] > BLUE_CUBES:
                # If one subset has more colors than the ones in the bag, it's not possible
                is_possible = False
                # break the loop
                break
        # If the subset is possible, then add the number of the game to possible
        possible += game if is_possible else 0
# Show the total sum.
print(f"The sum is {possible}") # Should be 2207