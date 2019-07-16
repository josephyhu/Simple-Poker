
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


def play_again():
    replay = input("Play again (y/n)? ")
    while replay.lower() != 'y' and replay.lower() != 'n':
        replay = input("Play again (y/n)? ")
    if replay.lower() == 'y':
        return True
    else:
        return False


def display_score(p_score, c_score):
    print("Score")
    print("You: {} | Computer: {}".format(p_score, c_score))


if __name__ == '__main__':
    royal_flush = copy.deepcopy(straight_flush.ROYAL_FLUSH)
    straight_flush = copy.deepcopy(straight_flush.STRAIGHT_FLUSH)
    four_of_a_kind = copy.deepcopy(four_of_a_kind.FOUR_OF_A_KIND)
    full_house = copy.deepcopy(full_house.FULL_HOUSE)
    flush = copy.deepcopy(flush.FLUSH)
    straight = copy.deepcopy(straight.STRAIGHT)
    three_of_a_kind = copy.deepcopy(three_of_a_kind.THREE_OF_A_KIND)
    two_pair = copy.deepcopy(two_pair.TWO_PAIR)
    p_points = 0
    c_points = 0
    p_score = 0
    c_score = 0
    while True:
        display_score(p_score, c_score)
        deck = copy.deepcopy(DECK)
        p_hand = set(random.sample(deck, 5))
        for i in p_hand:
            deck.remove(i)
        c_hand = set(random.sample(deck, 5))
        print("You:", p_hand)
        print("Computer:", c_hand)
        if p_hand in royal_flush:
            p_points = 9
        elif p_hand in straight_flush:
            p_points = 8
        elif p_hand in four_of_a_kind:
            p_points = 7
        elif p_hand in full_house:
            p_points = 6
        elif p_hand in flush:
            p_points = 5
        elif p_hand in straight:
            p_points = 4
        elif p_hand in three_of_a_kind:
            p_points = 3
        elif p_hand in two_pair:
            p_points = 2
        else:
            p_points = 0
        if c_hand in royal_flush:
            c_points = 9
        elif c_hand in straight_flush:
            c_points = 8
        elif c_hand in four_of_a_kind:
            c_points = 7
        elif c_hand in full_house:
            c_points = 6
        elif c_hand in flush:
            c_points = 5
        elif c_hand in straight:
            c_points = 4
        elif c_hand in three_of_a_kind:
            c_points = 3
        elif c_hand in two_pair:
            c_points = 2
        else:
            c_points = 0
        if p_points > c_points:
            print("You win!")
            p_score += 1
            if play_again() == True:
                continue
            else:
                print("Goodbye!")
                break
        elif p_points == c_points:
            print("It's a draw!")
            if play_again() == True:
                continue
            else:
                print("Goodbye!")
                break
        else:
            print("You lose!")
            c_score += 1
            if play_again() == True:
                continue
            else:
                print("Goodbye!")
                break
