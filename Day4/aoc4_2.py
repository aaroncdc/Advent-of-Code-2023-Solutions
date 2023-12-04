# Make a list with enough space for all the cards
# The number of cards is an integer in its respective position
cards = [0 for i in range(0,204)]

with open("puzzle.txt") as puzzle_input:
    # Read each card
    for card in puzzle_input:
        # Split the card number and number rows
        parts = card.split(':')
        # Read the card number (can be perfectly done with a counter though
        # since they are in order, but just in case they are not...)
        cardno = int(list(filter(lambda x: x != ' ' and x != '', parts[0].split(' ')))[1])
        # We have one original copy of this card. Set it to (or add to it) 1
        cards[cardno] = 1 if cards[cardno] == 0 else cards[cardno] + 1
        # Get the number rows
        nlines = parts[1].split('|')
        # Place each number in each row in it's own set
        nline1 = set(filter(lambda x: x != ' ' and x != '', nlines[0].strip().split(' ')))
        nline2 = set(filter(lambda x: x != ' ' and x != '', nlines[1].strip().split(' ')))
        # The number of matches is the intersection between the two rows
        intersect = list(nline1.intersection(nline2))
        # How many copies do we have already of this card?
        copies = cards[cardno]
        # We win one copy of the subsecuent n matches. n is the number of matches (The
        # cardinality of the intersection of the rows)
        for n in range(cardno+1, cardno + len(intersect) + 1):
            # We win one copy of each, times the number of copies we already have
            cards[n] = copies if cards[n] == 0 else cards[n] + copies

print(sum(cards)) # 6420979