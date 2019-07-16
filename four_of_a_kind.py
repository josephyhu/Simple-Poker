import deck
import copy

S = copy.deepcopy(deck.SPADES)
C = copy.deepcopy(deck.CLUBS)
H = copy.deepcopy(deck.HEARTS)
D = copy.deepcopy(deck.DIAMONDS)

FOUR_OF_A_KIND_S = []
for i in range(13):
    for j in range(13):
        if i != j:
            FOUR_OF_A_KIND_S.append({S[i], C[i], H[i], D[i], S[j]})

FOUR_OF_A_KIND_C = []
for i in range(13):
    for j in range(13):
        if i != j:
            FOUR_OF_A_KIND_C.append({S[i], C[i], H[i], D[i], C[j]})

FOUR_OF_A_KIND_H = []
for i in range(13):
    for j in range(13):
        if i != j:
            FOUR_OF_A_KIND_H.append({S[i], C[i], H[i], D[i], H[j]})

FOUR_OF_A_KIND_D = []
for i in range(13):
    for j in range(13):
        if i != j:
            FOUR_OF_A_KIND_D.append({S[i], C[i], H[i], D[i], D[j]})

FOUR_OF_A_KIND = []
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_S)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_C)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_H)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_D)

print(len(FOUR_OF_A_KIND))
