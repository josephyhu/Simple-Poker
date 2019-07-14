
import random
import copy
import deck
import straight_flush
import four_of_a_kind
import full_house
import flush
import straight
import three_of_a_kind
import two_pair
import one_pair

S = copy.deepcopy(deck.SPADES)
C = copy.deepcopy(deck.CLUBS)
H = copy.deepcopy(deck.HEARTS)
D = copy.deepcopy(deck.DIAMONDS)

DECK = S + C + H + D


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
        if p1_hand in royal_flush:
            p1_score = 9
        elif p1_hand in straight_flush:
            p1_score = 8
        elif p1_hand in four_of_a_kind:
            p1_score = 7
        elif p1_hand in full_house:
            p1_score = 6
        else:
            p1_score = 0
        if p2_hand in royal_flush:
            p2_score = 9
        elif p2_hand in straight_flush:
            p2_score = 8
        elif p2_hand in four_of_a_kind:
            p2_score = 7
        elif p2_hand in full_house:
            p2_score = 6
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


if __name__ == '__main__':
    royal_flush = copy.deepcopy(straight_flush.ROYAL_FLUSH)
    straight_flush = copy.deepcopy(straight_flush.STRAIGHT_FLUSH)
    four_of_a_kind = copy.deepcopy(four_of_a_kind.FOUR_OF_A_KIND)
    full_house = copy.deepcopy(full_house.FULL_HOUSE)
    start_game()
    while True:
        if play_again() == True:
            start_game()
        else:
            print("Goodbye!")
            break
