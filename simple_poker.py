import random
import copy

S = ['A\u2660', 'K\u2660', 'Q\u2660', 'J\u2660', '10\u2660', '9\u2660',
     '8\u2660', '7\u2660', '6\u2660', '5\u2660', '4\u2660', '3\u2660',
     '2\u2660']

C = ['A\u2663', 'K\u2663', 'Q\u2663', 'J\u2663', '10\u2663', '9\u2663',
     '8\u2663', '7\u2663', '6\u2663', '5\u2663', '4\u2663', '3\u2663',
     '2\u2663']

H = ['A\u2665', 'K\u2665', 'Q\u2665', 'J\u2665', '10\u2665', '9\u2665',
     '8\u2665', '7\u2665', '6\u2665', '5\u2665', '4\u2665', '3\u2665',
     '2\u2665']

D = ['A\u2666', 'K\u2666', 'Q\u2666', 'J\u2666', '10\u2666', '9\u2666',
     '8\u2666', '7\u2666', '6\u2666', '5\u2666', '4\u2666', '3\u2666',
     '2\u2666']

DECK = S + C + H + D

num1 = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
num2 = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
num3 = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
num4 = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]
num5 = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
num6 = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]
num7 = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
num8 = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]
num9 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
num10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
num11 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

ROYAL_FLUSH = ({S[0], S[1], S[2], S[3], S[4]},
               {C[0], C[1], C[2], C[3], C[4]},
               {H[0], H[1], H[2], H[3], H[4]},
               {D[0], D[1], D[2], D[3], D[4]})

STRAIGHT_FLUSH = ({S[0], S[1], S[2], S[3], S[4]},
                  {C[0], C[1], C[2], C[3], C[4]},
                  {H[0], H[1], H[2], H[3], H[4]},
                  {D[0], D[1], D[2], D[3], D[4]},
                  {S[1], S[2], S[3], S[4], S[5]},
                  {C[1], C[2], C[3], C[4], C[5]},
                  {H[1], H[2], H[3], H[4], H[5]},
                  {D[1], D[2], D[3], D[4], D[5]},
                  {S[2], S[3], S[4], S[5], S[6]},
                  {C[2], C[3], C[4], C[5], C[6]},
                  {H[2], H[3], H[4], H[5], H[6]},
                  {D[2], D[3], D[4], D[5], D[6]},
                  {S[3], S[4], S[5], S[6], S[7]},
                  {C[3], C[4], C[5], C[6], C[7]},
                  {H[3], H[4], H[5], H[6], H[7]},
                  {D[3], D[4], D[5], D[6], D[7]},
                  {S[4], S[5], S[6], S[7], S[8]},
                  {C[4], C[5], C[6], C[7], C[8]},
                  {H[4], H[5], H[6], H[7], H[8]},
                  {D[4], D[5], D[6], D[7], D[8]},
                  {S[5], S[6], S[7], S[8], S[9]},
                  {C[5], C[6], C[7], C[8], C[9]},
                  {H[5], H[6], H[7], H[8], H[9]},
                  {D[5], D[6], D[7], D[8], D[9]},
                  {S[6], S[7], S[8], S[9], S[10]},
                  {C[6], C[7], C[8], C[9], C[10]},
                  {H[6], H[7], H[8], H[9], H[10]},
                  {D[6], D[7], D[8], D[9], D[10]},
                  {S[7], S[8], S[9], S[10], S[11]},
                  {C[7], C[8], C[9], C[10], C[11]},
                  {H[7], H[8], H[9], H[10], H[11]},
                  {D[7], D[8], D[9], D[10], D[11]},
                  {S[8], S[9], S[10], S[11], S[12]},
                  {C[8], C[9], C[10], C[11], C[12]},
                  {H[8], H[9], H[10], H[11], H[12]},
                  {D[8], D[9], D[10], D[11], D[12]},
                  {S[9], S[10], S[11], S[12], S[0]},
                  {C[9], C[10], C[11], C[12], C[0]},
                  {H[9], H[10], H[11], H[12], H[0]},
                  {D[9], D[10], D[11], D[12], D[0]})

# To do: Complete the FOUR_OF_A_KIND tuple.
FOUR_OF_A_KIND = ({S[0], C[0], H[0], D[0],
                   random.choice([S, C, H, D])[random.randint(1, 12)]},
                  {S[1], C[1], H[1], D[1],
                   random.choice([S, C, H, D])[random.choice(num1)]},
                  {S[2], C[2], H[2], D[2],
                   random.choice([S, C, H, D])[random.choice(num2)]},
                  {S[3], C[3], H[3], D[3],
                   random.choice([S, C, H, D])[random.choice(num3)]},
                  {S[4], C[4], H[4], D[4],
                   random.choice([S, C, H, D])[random.choice(num4)]},
                  {S[5], C[5], H[5], D[5],
                   random.choice([S, C, H, D])[random.choice(num5)]},
                  {S[6], C[6], H[6], D[6],
                   random.choice([S, C, H, D])[random.choice(num6)]},
                  {S[7], C[7], H[7], D[7],
                   random.choice([S, C, H, D])[random.choice(num7)]},
                  {S[8], C[8], H[8], D[8],
                   random.choice([S, C, H, D])[random.choice(num8)]},
                  {S[9], C[9], H[9], D[9],
                   random.choice([S, C, H, D])[random.choice(num9)]},
                  {S[10], C[10], H[10], D[10],
                   random.choice([S, C, H, D])[random.choice(num10)]},
                  {S[11], C[11], H[11], D[11],
                   random.choice([S, C, H, D])[random.choice(num11)]},
                  {S[12], C[12], H[12], D[12],
                   random.choice([S, C, H, D])[random.randint(0, 11)]})

# To do: Add the FULL_HOUSE tuple.

# To do: Complete the FLUSH tuple.
FLUSH = (set(random.sample(S, 5)), set(random.sample(C, 5)),
         set(random.sample(H, 5)), set(random.sample(D, 5)))

# To do: Complete the STRAIGHT tuple.
STRAIGHT = ({random.choice([S, C, H, D])[0], random.choice([S, C, H, D])[1],
             random.choice([S, C, H, D])[2], random.choice([S, C, H, D])[3],
             random.choice([S, C, H, D])[4]},
            {random.choice([S, C, H, D])[1], random.choice([S, C, H, D])[2],
             random.choice([S, C, H, D])[3], random.choice([S, C, H, D])[4],
             random.choice([S, C, H, D])[5]},
            {random.choice([S, C, H, D])[2], random.choice([S, C, H, D])[3],
             random.choice([S, C, H, D])[4], random.choice([S, C, H, D])[5],
             random.choice([S, C, H, D])[6]},
            {random.choice([S, C, H, D])[3], random.choice([S, C, H, D])[4],
             random.choice([S, C, H, D])[5], random.choice([S, C, H, D])[6],
             random.choice([S, C, H, D])[7]},
            {random.choice([S, C, H, D])[4], random.choice([S, C, H, D])[5],
             random.choice([S, C, H, D])[6], random.choice([S, C, H, D])[7],
             random.choice([S, C, H, D])[8]},
            {random.choice([S, C, H, D])[5], random.choice([S, C, H, D])[6],
             random.choice([S, C, H, D])[7], random.choice([S, C, H, D])[8],
             random.choice([S, C, H, D])[9]},
            {random.choice([S, C, H, D])[6], random.choice([S, C, H, D])[7],
             random.choice([S, C, H, D])[8], random.choice([S, C, H, D])[9],
             random.choice([S, C, H, D])[10]},
            {random.choice([S, C, H, D])[7], random.choice([S, C, H, D])[8],
             random.choice([S, C, H, D])[9], random.choice([S, C, H, D])[10],
             random.choice([S, C, H, D])[11]},
            {random.choice([S, C, H, D])[8], random.choice([S, C, H, D])[9],
             random.choice([S, C, H, D])[10], random.choice([S, C, H, D])[11],
             random.choice([S, C, H, D])[12]},
            {random.choice([S, C, H, D])[9], random.choice([S, C, H, D])[10],
             random.choice([S, C, H, D])[11], random.choice([S, C, H, D])[12],
             random.choice([S, C, H, D])[0]})

# To do: Add the THREE_OF_A_KIND tuple.

# To do: Add the TWO_PAIR tuple.

# To do: Add the ONE_PAIR tuple.


# To do: Modify the game so that the higher card
#        (in case of both hands of the same type (e.g., two flushes)) wins.
# Also: Add a betting system.
def start_game():
    deck = copy.deepcopy(DECK)
    p1_score = 0
    p2_score = 0
    p1_hand = set(random.sample(deck, 5))
    for i in p1_hand:
        deck.remove(i)
    p2_hand = set(random.sample(deck, 5))
    while True:
        print("Player 1:", p1_hand)
        print("Player 2:", p2_hand)
        if p1_hand in ROYAL_FLUSH:
            p1_score = 5
        elif p1_hand in STRAIGHT_FLUSH and p1_hand not in ROYAL_FLUSH:
            p1_score = 4
        elif p1_hand in FOUR_OF_A_KIND:
            p1_score = 3
        elif p1_hand in FLUSH and p1_hand not in STRAIGHT_FLUSH:
            p1_score = 2
        elif p1_hand in STRAIGHT and p1_hand not in STRAIGHT_FLUSH:
            p1_score = 1
        else:
            p1_score = 0
        if p2_hand in ROYAL_FLUSH:
            p2_score = 5
        elif p2_hand in STRAIGHT_FLUSH and p2_hand not in ROYAL_FLUSH:
            p2_score = 4
        elif p2_hand in FOUR_OF_A_KIND:
            p2_score = 3
        elif p2_hand in FLUSH and p2_hand not in STRAIGHT_FLUSH:
            p2_score = 2
        elif c_hand in STRAIGHT and p2_hand not in STRAIGHT_FLUSH:
            p2_score = 1
        else:
            p2_score = 0
        if p1_score > p2_score:
            print("Player 1 wins!")
            break
        elif p1_score == p2_score:
            print("It's a draw!")
            break
        else:
            print("Player 2 wins!")
            break


def play_again():
    replay = input("Play again (y/n)? ")
    while replay.lower() != 'y' and replay.lower() != 'n':
        replay = input("Play again (y/n)? ")
    if replay.lower() == 'y':
        return True
    else:
        return False


start_game()
while True:
    if play_again() == True:
        start_game()
    else:
        print("Goodbye!")
        break
