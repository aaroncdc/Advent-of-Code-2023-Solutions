# Full deck with each card's value.
DECK = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}

# Lambda function to filter lists with strings
filterstrlist = lambda lst: [i.strip() for i in filter(lambda x: x != " " and x != "" and x != "", lst)]

# This isn't spaghetti coding. This is carbonara coding.
# Had to rewrite this entirely and couldn't figure out a better way to solve this.
# This might be the worst code you have ever seen... but does it run?
def hand_power(hand):
    handcards = {} # Stores repetitions of cards in the hand, as a dict
    jokes = 0 # Number of jokers
    # Parse the cards in the hand
    for c in hand:
        if c not in handcards.keys():
            handcards[c] = 1
        else: handcards[c] += 1
    # Get how many jokers are in the hand
    if "J" in handcards.keys():
        jokes = handcards["J"]
        if jokes == 5: return 7 # No need to do anything else
        handcards.pop("J") # Removes jokers from the list
    # I could probably just replace handcards with tmp instead and save some memory
    tmp = sorted(list(handcards.items()), key=lambda x: x[1], reverse=True)
    # Calculate the best (higher) amount of repeating cards
    best = jokes + tmp[0][1] if len(tmp) > 0 else 0
    match best:
        case 1: return 1 # High card
        case 2:
            if jokes == 1:
                return 2 # Single pair
            if tmp[1][1] == 2: return 3 # Double pair
            return 2 # Single pair
        case 3:
            if jokes != 0:
                if jokes == 3: return 4 # Three of a kind
                if tmp[0][1] == 2 and tmp[1][1] == 2: return 5 # Full House
            else:
                if tmp[1][1] == 2: return 5 # Full house
            return 4 # Three of a kind
        case 4: return 6 # Four of a kind
        case 5: return 7 # Five of a kind

# Compare two hands. Returns 1 if h1 > h2, -1 if h1 < h2, 0 if equal.
def cmp_hands(h1,h2):
    for i in range(0, len(h1)):
        if DECK[h1[i]] > DECK[h2[i]]:
            return 1 # Hand 1 is stronger
        elif DECK[h1[i]] < DECK[h2[i]]:
            return -1 # Hand 2 is stronger
    return 0 # They are both equal

hands = []
# Parse the puzzle piece
with open("puzzle.txt") as puzzle_input:
    for line in puzzle_input:
        p = filterstrlist(line.split(" "))
        # Store each hand as a triplet: (hand, wagger, hand power)
        hands.append((p[0], p[1], hand_power(p[0])))

# Sort the hands. First by hand power, then by stronger hand.
hands = sorted(hands, key=lambda x: [x[2]] + [DECK[x[0][i]] for i in range(0,5)])

score = 0

# Calculate the score
for i in range(1, len(hands)+1):
    score += i * int(hands[i-1][1])

print(score) # 250057090