import deck
import copy

S = copy.deepcopy(deck.SPADES)
C = copy.deepcopy(deck.CLUBS)
H = copy.deepcopy(deck.HEARTS)
D = copy.deepcopy(deck.DIAMONDS)

ROYAL_FLUSH = [{S[0], S[1], S[2], S[3], S[4]},
               {C[0], C[1], C[2], C[3], C[4]},
               {H[0], H[1], H[2], H[3], H[4]},
               {D[0], D[1], D[2], D[3], D[4]}]

STRAIGHT_FLUSH_S = [{S[1], S[2], S[3], S[4], S[5]},
                    {S[2], S[3], S[4], S[5], S[6]},
                    {S[3], S[4], S[5], S[6], S[7]},
                    {S[4], S[5], S[6], S[7], S[8]},
                    {S[5], S[6], S[7], S[8], S[9]},
                    {S[6], S[7], S[8], S[9], S[10]},
                    {S[7], S[8], S[9], S[10], S[11]},
                    {S[8], S[9], S[10], S[11], S[12]},
                    {S[9], S[10], S[11], S[12], S[0]}]

STRAIGHT_FLUSH_C = [{C[1], C[2], C[3], C[4], C[5]},
                    {C[2], C[3], C[4], C[5], C[6]},
                    {C[3], C[4], C[5], C[6], C[7]},
                    {C[4], C[5], C[6], C[7], C[8]},
                    {C[5], C[6], C[7], C[8], C[9]},
                    {C[6], C[7], C[8], C[9], C[10]},
                    {C[7], C[8], C[9], C[10], C[11]},
                    {C[8], C[9], C[10], C[11], C[12]},
                    {C[9], C[10], C[11], C[12], C[0]}]

STRAIGHT_FLUSH_H = [{H[1], H[2], H[3], H[4], H[5]},
                    {H[2], H[3], H[4], H[5], H[6]},
                    {H[3], H[4], H[5], H[6], H[7]},
                    {H[4], H[5], H[6], H[7], H[8]},
                    {H[5], H[6], H[7], H[8], H[9]},
                    {H[6], H[7], H[8], H[9], H[10]},
                    {H[7], H[8], H[9], H[10], H[11]},
                    {H[8], H[9], H[10], H[11], H[12]},
                    {H[9], H[10], H[11], H[12], H[0]}]

STRAIGHT_FLUSH_D = [{D[1], D[2], D[3], D[4], D[5]},
                    {D[2], D[3], D[4], D[5], D[6]},
                    {D[3], D[4], D[5], D[6], D[7]},
                    {D[4], D[5], D[6], D[7], D[8]},
                    {D[5], D[6], D[7], D[8], D[9]},
                    {D[6], D[7], D[8], D[9], D[10]},
                    {D[7], D[8], D[9], D[10], D[11]},
                    {D[8], D[9], D[10], D[11], D[12]},
                    {D[9], D[10], D[11], D[12], D[0]}]

STRAIGHT_FLUSH = []
STRAIGHT_FLUSH.extend(STRAIGHT_FLUSH_S)
STRAIGHT_FLUSH.extend(STRAIGHT_FLUSH_C)
STRAIGHT_FLUSH.extend(STRAIGHT_FLUSH_H)
STRAIGHT_FLUSH.extend(STRAIGHT_FLUSH_D)
