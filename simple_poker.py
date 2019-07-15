
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
def start_game():
    deck = copy.deepcopy(DECK)
    p_score = 0
    c_score = 0
    p_hand = set(random.sample(deck, 5))
    for i in p_hand:
        deck.remove(i)
    c_hand = set(random.sample(deck, 5))
    while True:
        print("Player:", p_hand)
        print("Computer:", c_hand)
        if p_hand in royal_flush:
            p_score = 9
        elif p_hand in straight_flush:
            p_score = 8
        elif p_hand in four_of_a_kind:
            p_score = 7
        elif p_hand in full_house:
            p_score = 6
        elif p_hand in flush:
            p_score = 5
        elif p_hand in straight:
            p_score = 4
        elif p_hand in three_of_a_kind:
            p_score = 3
        else:
            p_score = 0
        if c_hand in royal_flush:
            c_score = 9
        elif c_hand in straight_flush:
            c_score = 8
        elif c_hand in four_of_a_kind:
            c_score = 7
        elif c_hand in full_house:
            c_score = 6
        elif c_hand in flush:
            c_score = 5
        elif c_hand in straight:
            c_score = 4
        elif c_hand in three_of_a_kind:
            c_score = 3
        else:
            c_score = 0
        if p_score > c_score:
            print("You win!")
            break
        elif p_score == c_score:
            print("It's a draw!")
            break
        else:
            print("You lose!")
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
    flush = copy.deepcopy(flush.FLUSH)
    straight = copy.deepcopy(straight.STRAIGHT)
    three_of_a_kind = copy.deepcopy(three_of_a_kind.THREE_OF_A_KIND)
    start_game()
    while True:
        if play_again() == True:
            start_game()
        else:
            print("Goodbye!")
            break
