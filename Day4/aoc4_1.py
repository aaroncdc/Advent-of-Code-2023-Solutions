total = 0
with open("puzzle.txt") as puzzle_input:
    # Read each card
    for card in puzzle_input:
        # Split the card number and number rows
        parts = card.split(':')
        # Get the two rows
        cards = parts[1].split('|')
        # Place each number in each row in it's own set
        card1 = set(filter(lambda x: x != ' ' and x != '', cards[0].strip().split(' ')))
        card2 = set(filter(lambda x: x != ' ' and x != '', cards[1].strip().split(' ')))
        # The number of matches is the intersection between the two rows
        intersect = card1.intersection(card2)
        # If the intersection is not an empty set
        if len(intersect) > 0:
            # The score is 2 to the power of the cardinality of the intersection, minus 1
            # add it to the total
            total += 2**(len(intersect)-1)

print(f"Total: {total}") # 25174