import deck
import copy

S = copy.deepcopy(deck.SPADES)
C = copy.deepcopy(deck.CLUBS)
H = copy.deepcopy(deck.HEARTS)
D = copy.deepcopy(deck.DIAMONDS)

FOUR_OF_A_KIND_AS = []
for i in range(1, 13):
    FOUR_OF_A_KIND_AS.append({S[0], C[0], H[0], D[0], S[i]})
FOUR_OF_A_KIND_AC = []
for i in range(1, 13):
    FOUR_OF_A_KIND_AC.append({S[0], C[0], H[0], D[0], C[i]})
FOUR_OF_A_KIND_AH = []
for i in range(1, 13):
    FOUR_OF_A_KIND_AH.append({S[0], C[0], H[0], D[0], H[i]})
FOUR_OF_A_KIND_AD = []
for i in range(1, 13):
    FOUR_OF_A_KIND_AD.append({S[0], C[0], H[0], D[0], D[i]})

FOUR_OF_A_KIND_KS = [{S[1], C[1], H[1], D[1], S[0]}]
for i in range(2, 13):
    FOUR_OF_A_KIND_KS.append({S[1], C[1], H[1], D[1], S[i]})
FOUR_OF_A_KIND_KC = [{S[1], C[1], H[1], D[1], C[0]}]
for i in range(2, 13):
    FOUR_OF_A_KIND_KC.append({S[1], C[1], H[1], D[1], C[i]})
FOUR_OF_A_KIND_KH = [{S[1], C[1], H[1], D[1], H[0]}]
for i in range(2, 13):
    FOUR_OF_A_KIND_KH.append({S[1], C[1], H[1], D[1], H[i]})
FOUR_OF_A_KIND_KD = [{S[1], C[1], H[1], D[1], D[0]}]
for i in range(2, 13):
    FOUR_OF_A_KIND_KD.append({S[1], C[1], H[1], D[1], D[i]})

FOUR_OF_A_KIND_QS = []
for i in range(2):
    FOUR_OF_A_KIND_QS.append({S[2], C[2], H[2], D[2], S[i]})
for i in range(3, 13):
    FOUR_OF_A_KIND_QS.append({S[2], C[2], H[2], D[2], S[i]})
FOUR_OF_A_KIND_QC = []
for i in range(2):
    FOUR_OF_A_KIND_QC.append({S[2], C[2], H[2], D[2], C[i]})
for i in range(3, 13):
    FOUR_OF_A_KIND_QC.append({S[2], C[2], H[2], D[2], C[i]})
FOUR_OF_A_KIND_QH = []
for i in range(2):
    FOUR_OF_A_KIND_QH.append({S[2], C[2], H[2], D[2], H[i]})
for i in range(3, 13):
    FOUR_OF_A_KIND_QH.append({S[2], C[2], H[2], D[2], H[i]})
FOUR_OF_A_KIND_QD = []
for i in range(2):
    FOUR_OF_A_KIND_QD.append({S[2], C[2], H[2], D[2], D[i]})
for i in range(3, 13):
    FOUR_OF_A_KIND_QD.append({S[2], C[2], H[2], D[2], D[i]})

FOUR_OF_A_KIND_JS = []
for i in range(3):
    FOUR_OF_A_KIND_JS.append({S[3], C[3], H[3], D[3], S[i]})
for i in range(4, 13):
    FOUR_OF_A_KIND_JS.append({S[3], C[3], H[3], D[3], S[i]})
FOUR_OF_A_KIND_JC = []
for i in range(3):
    FOUR_OF_A_KIND_JC.append({S[3], C[3], H[3], D[3], C[i]})
for i in range(4, 13):
    FOUR_OF_A_KIND_JC.append({S[3], C[3], H[3], D[3], C[i]})
FOUR_OF_A_KIND_JH = []
for i in range(3):
    FOUR_OF_A_KIND_JH.append({S[3], C[3], H[3], D[3], H[i]})
for i in range(4, 13):
    FOUR_OF_A_KIND_JH.append({S[3], C[3], H[3], D[3], H[i]})
FOUR_OF_A_KIND_JD = []
for i in range(3):
    FOUR_OF_A_KIND_JD.append({S[3], C[3], H[3], D[3], D[i]})
for i in range(4, 13):
    FOUR_OF_A_KIND_JD.append({S[3], C[3], H[3], D[3], D[i]})

FOUR_OF_A_KIND_10S = []
for i in range(4):
    FOUR_OF_A_KIND_10S.append({S[4], C[4], H[4], D[4], S[i]})
for i in range(5, 13):
    FOUR_OF_A_KIND_10S.append({S[4], C[4], H[4], D[4], S[i]})
FOUR_OF_A_KIND_10C = []
for i in range(4):
    FOUR_OF_A_KIND_10C.append({S[4], C[4], H[4], D[4], C[i]})
for i in range(5, 13):
    FOUR_OF_A_KIND_10C.append({S[4], C[4], H[4], D[4], C[i]})
FOUR_OF_A_KIND_10H = []
for i in range(4):
    FOUR_OF_A_KIND_10H.append({S[4], C[4], H[4], D[4], H[i]})
for i in range(5, 13):
    FOUR_OF_A_KIND_10H.append({S[4], C[4], H[4], D[4], H[i]})
FOUR_OF_A_KIND_10D = []
for i in range(4):
    FOUR_OF_A_KIND_10D.append({S[4], C[4], H[4], D[4], D[i]})
for i in range(5, 13):
    FOUR_OF_A_KIND_10D.append({S[4], C[4], H[4], D[4], D[i]})

FOUR_OF_A_KIND_9S = []
for i in range(5):
    FOUR_OF_A_KIND_9S.append({S[5], C[5], H[5], D[5], S[i]})
for i in range(6, 13):
    FOUR_OF_A_KIND_9S.append({S[5], C[5], H[5], D[5], S[i]})
FOUR_OF_A_KIND_9C = []
for i in range(5):
    FOUR_OF_A_KIND_9C.append({S[5], C[5], H[5], D[5], C[i]})
for i in range(6, 13):
    FOUR_OF_A_KIND_9C.append({S[5], C[5], H[5], D[5], C[i]})
FOUR_OF_A_KIND_9H = []
for i in range(5):
    FOUR_OF_A_KIND_9H.append({S[5], C[5], H[5], D[5], H[i]})
for i in range(6, 13):
    FOUR_OF_A_KIND_9H.append({S[5], C[5], H[5], D[5], H[i]})
FOUR_OF_A_KIND_9D = []
for i in range(5):
    FOUR_OF_A_KIND_9D.append({S[5], C[5], H[5], D[5], D[i]})
for i in range(6, 13):
    FOUR_OF_A_KIND_9D.append({S[5], C[5], H[5], D[5], D[i]})

FOUR_OF_A_KIND_8S = []
for i in range(6):
    FOUR_OF_A_KIND_8S.append({S[6], C[6], H[6], D[6], S[i]})
for i in range(7, 13):
    FOUR_OF_A_KIND_8S.append({S[6], C[6], H[6], D[6], S[i]})
FOUR_OF_A_KIND_8C = []
for i in range(6):
    FOUR_OF_A_KIND_8C.append({S[6], C[6], H[6], D[6], C[i]})
for i in range(7, 13):
    FOUR_OF_A_KIND_8C.append({S[6], C[6], H[6], D[6], C[i]})
FOUR_OF_A_KIND_8H = []
for i in range(6):
    FOUR_OF_A_KIND_8H.append({S[6], C[6], H[6], D[6], H[i]})
for i in range(7, 13):
    FOUR_OF_A_KIND_8H.append({S[6], C[6], H[6], D[6], H[i]})
FOUR_OF_A_KIND_8D = []
for i in range(6):
    FOUR_OF_A_KIND_8D.append({S[6], C[6], H[6], D[6], D[i]})
for i in range(7, 13):
    FOUR_OF_A_KIND_8D.append({S[6], C[6], H[6], D[6], D[i]})

FOUR_OF_A_KIND_7S = []
for i in range(7):
    FOUR_OF_A_KIND_7S.append({S[7], C[7], H[7], D[7], S[i]})
for i in range(8, 13):
    FOUR_OF_A_KIND_7S.append({S[7], C[7], H[7], D[7], S[i]})
FOUR_OF_A_KIND_7C = []
for i in range(7):
    FOUR_OF_A_KIND_7C.append({S[7], C[7], H[7], D[7], C[i]})
for i in range(8, 13):
    FOUR_OF_A_KIND_7C.append({S[7], C[7], H[7], D[7], C[i]})
FOUR_OF_A_KIND_7H = []
for i in range(7):
    FOUR_OF_A_KIND_7H.append({S[7], C[7], H[7], D[7], H[i]})
for i in range(8, 13):
    FOUR_OF_A_KIND_7H.append({S[7], C[7], H[7], D[7], H[i]})
FOUR_OF_A_KIND_7D = []
for i in range(7):
    FOUR_OF_A_KIND_7D.append({S[7], C[7], H[7], D[7], D[i]})
for i in range(8, 13):
    FOUR_OF_A_KIND_7D.append({S[7], C[7], H[7], D[7], D[i]})

FOUR_OF_A_KIND_6S = []
for i in range(8):
    FOUR_OF_A_KIND_6S.append({S[8], C[8], H[8], D[8], S[i]})
for i in range(9, 13):
    FOUR_OF_A_KIND_6S.append({S[8], C[8], H[8], D[8], S[i]})
FOUR_OF_A_KIND_6C = []
for i in range(8):
    FOUR_OF_A_KIND_6C.append({S[8], C[8], H[8], D[8], C[i]})
for i in range(9, 13):
    FOUR_OF_A_KIND_6C.append({S[8], C[8], H[8], D[8], C[i]})
FOUR_OF_A_KIND_6H = []
for i in range(8):
    FOUR_OF_A_KIND_6H.append({S[8], C[8], H[8], D[8], H[i]})
for i in range(9, 13):
    FOUR_OF_A_KIND_6H.append({S[8], C[8], H[8], D[8], H[i]})
FOUR_OF_A_KIND_6D = []
for i in range(8):
    FOUR_OF_A_KIND_6D.append({S[8], C[8], H[8], D[8], D[i]})
for i in range(9, 13):
    FOUR_OF_A_KIND_6D.append({S[8], C[8], H[8], D[8], D[i]})

FOUR_OF_A_KIND_5S = []
for i in range(9):
    FOUR_OF_A_KIND_5S.append({S[9], C[9], H[9], D[9], S[i]})
for i in range(10, 13):
    FOUR_OF_A_KIND_5S.append({S[9], C[9], H[9], D[9], S[i]})
FOUR_OF_A_KIND_5C = []
for i in range(9):
    FOUR_OF_A_KIND_5C.append({S[9], C[9], H[9], D[9], C[i]})
for i in range(10, 13):
    FOUR_OF_A_KIND_5C.append({S[9], C[9], H[9], D[9], C[i]})
FOUR_OF_A_KIND_5H = []
for i in range(9):
    FOUR_OF_A_KIND_5H.append({S[9], C[9], H[9], D[9], H[i]})
for i in range(10, 13):
    FOUR_OF_A_KIND_5H.append({S[9], C[9], H[9], D[9], H[i]})
FOUR_OF_A_KIND_5D = []
for i in range(9):
    FOUR_OF_A_KIND_5D.append({S[9], C[9], H[9], D[9], D[i]})
for i in range(10, 13):
    FOUR_OF_A_KIND_5D.append({S[9], C[9], H[9], D[9], D[i]})

FOUR_OF_A_KIND_4S = []
for i in range(10):
    FOUR_OF_A_KIND_4S.append({S[10], C[10], H[10], D[10], S[i]})
for i in range(11, 13):
    FOUR_OF_A_KIND_4S.append({S[10], C[10], H[10], D[10], S[i]})
FOUR_OF_A_KIND_4C = []
for i in range(10):
    FOUR_OF_A_KIND_4C.append({S[10], C[10], H[10], D[10], C[i]})
for i in range(11, 13):
    FOUR_OF_A_KIND_4C.append({S[10], C[10], H[10], D[10], C[i]})
FOUR_OF_A_KIND_4H = []
for i in range(10):
    FOUR_OF_A_KIND_4H.append({S[10], C[10], H[10], D[10], H[i]})
for i in range(11, 13):
    FOUR_OF_A_KIND_4H.append({S[10], C[10], H[10], D[10], H[i]})
FOUR_OF_A_KIND_4D = []
for i in range(10):
    FOUR_OF_A_KIND_4D.append({S[10], C[10], H[10], D[10], D[i]})
for i in range(11, 13):
    FOUR_OF_A_KIND_4D.append({S[10], C[10], H[10], D[10], D[i]})

FOUR_OF_A_KIND_3S = []
for i in range(11):
    FOUR_OF_A_KIND_3S.append({S[10], C[10], H[10], D[10], S[i]})
FOUR_OF_A_KIND_3S.append({S[10], C[10], H[10], D[10], S[12]})
FOUR_OF_A_KIND_3C = []
for i in range(11):
    FOUR_OF_A_KIND_3C.append({S[10], C[10], H[10], D[10], C[i]})
FOUR_OF_A_KIND_3C.append({S[10], C[10], H[10], D[10], C[12]})
FOUR_OF_A_KIND_3H = []
for i in range(11):
    FOUR_OF_A_KIND_3H.append({S[10], C[10], H[10], D[10], H[i]})
FOUR_OF_A_KIND_3H.append({S[10], C[10], H[10], D[10], H[12]})
FOUR_OF_A_KIND_3D = []
for i in range(11):
    FOUR_OF_A_KIND_3D.append({S[10], C[10], H[10], D[10], D[i]})
FOUR_OF_A_KIND_3D.append({S[10], C[10], H[10], D[10], D[12]})

FOUR_OF_A_KIND_2S = []
for i in range(12):
    FOUR_OF_A_KIND_2S.append({S[12], C[12], H[12], D[12], S[i]})
FOUR_OF_A_KIND_2C = []
for i in range(12):
    FOUR_OF_A_KIND_2C.append({S[12], C[12], H[12], D[12], C[i]})
FOUR_OF_A_KIND_2H = []
for i in range(12):
    FOUR_OF_A_KIND_2H.append({S[12], C[12], H[12], D[12], H[i]})
FOUR_OF_A_KIND_2D = []
for i in range(12):
    FOUR_OF_A_KIND_2D.append({S[12], C[12], H[12], D[12], D[i]})

FOUR_OF_A_KIND_AB = FOUR_OF_A_KIND_AS + FOUR_OF_A_KIND_AC
FOUR_OF_A_KIND_AR = FOUR_OF_A_KIND_AH + FOUR_OF_A_KIND_AD
FOUR_OF_A_KIND_KB = FOUR_OF_A_KIND_KS + FOUR_OF_A_KIND_KC
FOUR_OF_A_KIND_KR = FOUR_OF_A_KIND_KH + FOUR_OF_A_KIND_KD
FOUR_OF_A_KIND_QB = FOUR_OF_A_KIND_QS + FOUR_OF_A_KIND_QC
FOUR_OF_A_KIND_QR = FOUR_OF_A_KIND_QH + FOUR_OF_A_KIND_QD
FOUR_OF_A_KIND_JB = FOUR_OF_A_KIND_JS + FOUR_OF_A_KIND_JC
FOUR_OF_A_KIND_JR = FOUR_OF_A_KIND_JH + FOUR_OF_A_KIND_JD
FOUR_OF_A_KIND_10B = FOUR_OF_A_KIND_10S + FOUR_OF_A_KIND_10C
FOUR_OF_A_KIND_10R = FOUR_OF_A_KIND_10H + FOUR_OF_A_KIND_10D
FOUR_OF_A_KIND_9B = FOUR_OF_A_KIND_9S + FOUR_OF_A_KIND_9C
FOUR_OF_A_KIND_9R = FOUR_OF_A_KIND_9H + FOUR_OF_A_KIND_9D
FOUR_OF_A_KIND_8B = FOUR_OF_A_KIND_8S + FOUR_OF_A_KIND_8C
FOUR_OF_A_KIND_8R = FOUR_OF_A_KIND_8H + FOUR_OF_A_KIND_8D
FOUR_OF_A_KIND_7B = FOUR_OF_A_KIND_7S + FOUR_OF_A_KIND_7C
FOUR_OF_A_KIND_7R = FOUR_OF_A_KIND_7H + FOUR_OF_A_KIND_7D
FOUR_OF_A_KIND_6B = FOUR_OF_A_KIND_6S + FOUR_OF_A_KIND_6C
FOUR_OF_A_KIND_6R = FOUR_OF_A_KIND_6H + FOUR_OF_A_KIND_6D
FOUR_OF_A_KIND_5B = FOUR_OF_A_KIND_5S + FOUR_OF_A_KIND_5C
FOUR_OF_A_KIND_5R = FOUR_OF_A_KIND_5H + FOUR_OF_A_KIND_5D
FOUR_OF_A_KIND_4B = FOUR_OF_A_KIND_4S + FOUR_OF_A_KIND_4C
FOUR_OF_A_KIND_4R = FOUR_OF_A_KIND_4H + FOUR_OF_A_KIND_4D
FOUR_OF_A_KIND_3B = FOUR_OF_A_KIND_3S + FOUR_OF_A_KIND_3C
FOUR_OF_A_KIND_3R = FOUR_OF_A_KIND_3H + FOUR_OF_A_KIND_3D
FOUR_OF_A_KIND_2B = FOUR_OF_A_KIND_2S + FOUR_OF_A_KIND_2C
FOUR_OF_A_KIND_2R = FOUR_OF_A_KIND_2H + FOUR_OF_A_KIND_2D

FOUR_OF_A_KIND_A = FOUR_OF_A_KIND_AB + FOUR_OF_A_KIND_AR
FOUR_OF_A_KIND_K = FOUR_OF_A_KIND_KB + FOUR_OF_A_KIND_KR
FOUR_OF_A_KIND_Q = FOUR_OF_A_KIND_QB + FOUR_OF_A_KIND_QR
FOUR_OF_A_KIND_J = FOUR_OF_A_KIND_JB + FOUR_OF_A_KIND_JR
FOUR_OF_A_KIND_10 = FOUR_OF_A_KIND_10B + FOUR_OF_A_KIND_10R
FOUR_OF_A_KIND_9 = FOUR_OF_A_KIND_9B + FOUR_OF_A_KIND_9R
FOUR_OF_A_KIND_8 = FOUR_OF_A_KIND_8B + FOUR_OF_A_KIND_8R
FOUR_OF_A_KIND_7 = FOUR_OF_A_KIND_7B + FOUR_OF_A_KIND_7R
FOUR_OF_A_KIND_6 = FOUR_OF_A_KIND_6B + FOUR_OF_A_KIND_6R
FOUR_OF_A_KIND_5 = FOUR_OF_A_KIND_5B + FOUR_OF_A_KIND_5R
FOUR_OF_A_KIND_4 = FOUR_OF_A_KIND_4B + FOUR_OF_A_KIND_4R
FOUR_OF_A_KIND_3 = FOUR_OF_A_KIND_3B + FOUR_OF_A_KIND_3R
FOUR_OF_A_KIND_2 = FOUR_OF_A_KIND_2B + FOUR_OF_A_KIND_2R

FOUR_OF_A_KIND = []
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_A)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_K)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_Q)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_J)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_10)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_9)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_8)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_7)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_6)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_5)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_4)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_3)
FOUR_OF_A_KIND.extend(FOUR_OF_A_KIND_2)

print(FOUR_OF_A_KIND)
