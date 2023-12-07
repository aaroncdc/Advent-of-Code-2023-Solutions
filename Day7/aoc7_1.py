# Full deck with each card's value.
DECK = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

# Lambda function to filter lists with strings
filterstrlist = lambda lst: [i.strip() for i in filter(lambda x: x != " " and x != "" and x != "", lst)]
# Sort by deck value, descending
sort_hand_str = lambda handstr: sorted(handstr, key=lambda x: DECK[x], reverse=True)

# What type of hand is this? (High cards, pair(s), three in a house...)
def hand_type(hand: list):
    # create a list of tuples with each card and it's repetition,
    # ordered by the number of repetitions descending
    reps = { i:hand.count(i) for i in hand}
    l = [(k,reps[k]) for k in reps.keys()]
    o = sorted(l, key=lambda x: x[1])
    o.reverse()
    rank = o[0][1]
    match rank:
        case 1: return 1 # High card
        case 2:
            if o[1][1] == 2: return 3 # Two pairs
            else: return 2 # One pair
        case 3:
            if o[1][1] == 1: return 4 # Three of a kind
            else: return 5 # Full house
        case 4: return 6 # Four of a kind
        case 5: return 7 # Five of a kind

# Compares two hands. Returns 1 if h1 > h2. -1 if h1 < h2. 0 if equal.
def cmp_hands(h1,h2):
    for i in range(0, len(h1)):
        if DECK[h1[i]] > DECK[h2[i]]:
            return 1 # Hand 1 is stronger
        elif DECK[h1[i]] < DECK[h2[i]]:
            return -1 # Hand 2 is stronger
    return 0 # They are both equal

# Parse the hands in the puzzle
hands = []
with open("puzzle.txt") as puzzle_input:
    for line in puzzle_input:
        p = filterstrlist(line.split(" "))
        sh = sort_hand_str(p[0])
        # Don't ask me why I did it this way, hands contains quadruplets
        # made with the hand (sorted), the wagger, the hand type, and the hand (unsorted).
        # This isn't really necessary, and I improved it for part 2. So bear with this for now.
        hands.append((sh, int(p[1]), hand_type(sh), [c for c in p[0]]))

# # Sort the hands. First by hand type, then by stronger hand.
hands = sorted(hands, key=lambda x: [x[2]] + [DECK[x[3][i]] for i in range(0,5)])

# Calculate the score
c = 0
for i in range(1,len(hands)+1):
    c += hands[i-1][1] * i

print(c) # 248812215