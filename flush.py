import deck
import copy
import straight_flush

S = copy.deepcopy(deck.SPADES)
C = copy.deepcopy(deck.CLUBS)
H = copy.deepcopy(deck.HEARTS)
D = copy.deepcopy(deck.DIAMONDS)
straight_flush_s = copy.deepcopy(straight_flush.STRAIGHT_FLUSH_S)
straight_flush_c = copy.deepcopy(straight_flush.STRAIGHT_FLUSH_C)
straight_flush_h = copy.deepcopy(straight_flush.STRAIGHT_FLUSH_H)
straight_flush_d = copy.deepcopy(straight_flush.STRAIGHT_FLUSH_D)


FLUSH_S = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(5, 13):
                    if i < j < k < l < m:
                        if len({S[i], S[j], S[k], S[l], S[m]}) == 5:
                            FLUSH_S.append({S[i], S[j], S[k], S[l], S[m]})

for i in range(9):
    FLUSH_S.remove(straight_flush_s[i])

FLUSH_C = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(5, 13):
                    if i < j < k < l < m:
                        if len({C[i], C[j], C[k], C[l], C[m]}) == 5:
                            FLUSH_C.append({C[i], C[j], C[k], C[l], C[m]})

for i in range(9):
    FLUSH_C.remove(straight_flush_c[i])

FLUSH_H = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(5, 13):
                    if i < j < k < l < m:
                        if len({H[i], H[j], H[k], H[l], H[m]}) == 5:
                            FLUSH_H.append({H[i], H[j], H[k], H[l], H[m]})

for i in range(9):
    FLUSH_H.remove(straight_flush_h[i])

FLUSH_D = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(5, 13):
                    if i < j < k < l < m:
                        if len({D[i], D[j], D[k], D[l], D[m]}) == 5:
                            FLUSH_D.append({D[i], D[j], D[k], D[l], D[m]})

for i in range(9):
    FLUSH_D.remove(straight_flush_d[i])

FLUSH = []
FLUSH.extend(FLUSH_S)
FLUSH.extend(FLUSH_C)
FLUSH.extend(FLUSH_H)
FLUSH.extend(FLUSH_D)
