import deck
import copy

S = copy.deepcopy(deck.SPADES)
C = copy.deepcopy(deck.CLUBS)
H = copy.deepcopy(deck.HEARTS)
D = copy.deepcopy(deck.DIAMONDS)

STRAIGHT_SSSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSSC.append({S[i], S[j], S[k], S[l], C[m]})
STRAIGHT_SSSSC.append({S[9], S[10], S[11], S[12], C[0]})

STRAIGHT_SSSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSSH.append({S[i], S[j], S[k], S[l], H[m]})
STRAIGHT_SSSSH.append({S[9], S[10], S[11], S[12], H[0]})

STRAIGHT_SSSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSSD.append({S[i], S[j], S[k], S[l], D[m]})
STRAIGHT_SSSSD.append({S[9], S[10], S[11], S[12], D[0]})

STRAIGHT_SSSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSCS.append({S[i], S[j], S[k], C[l], S[m]})
STRAIGHT_SSSCS.append({S[9], S[10], S[11], C[12], S[0]})

STRAIGHT_SSSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSCC.append({S[i], S[j], S[k], C[l], C[m]})
STRAIGHT_SSSCC.append({S[9], S[10], S[11], C[12], C[0]})

STRAIGHT_SSSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSCH.append({S[i], S[j], S[k], C[l], H[m]})
STRAIGHT_SSSCH.append({S[9], S[10], S[11], C[12], H[0]})

STRAIGHT_SSSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSCD.append({S[i], S[j], S[k], C[l], D[m]})
STRAIGHT_SSSCD.append({S[9], S[10], S[11], C[12], D[0]})

STRAIGHT_SSSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSHS.append({S[i], S[j], S[k], H[l], S[m]})
STRAIGHT_SSSHS.append({S[9], S[10], S[11], H[12], S[0]})

STRAIGHT_SSSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSHC.append({S[i], S[j], S[k], H[l], C[m]})
STRAIGHT_SSSHC.append({S[9], S[10], S[11], H[12], C[0]})

STRAIGHT_SSSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSHH.append({S[i], S[j], S[k], H[l], H[m]})
STRAIGHT_SSSHH.append({S[9], S[10], S[11], H[12], H[0]})

STRAIGHT_SSSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSHD.append({S[i], S[j], S[k], H[l], D[m]})
STRAIGHT_SSSHD.append({S[9], S[10], S[11], H[12], D[0]})

STRAIGHT_SSSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSDS.append({S[i], S[j], S[k], D[l], S[m]})
STRAIGHT_SSSDS.append({S[9], S[10], S[11], D[12], S[0]})

STRAIGHT_SSSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSDC.append({S[i], S[j], S[k], D[l], C[m]})
STRAIGHT_SSSDC.append({S[9], S[10], S[11], D[12], C[0]})

STRAIGHT_SSSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSDH.append({S[i], S[j], S[k], D[l], H[m]})
STRAIGHT_SSSDH.append({S[9], S[10], S[11], D[12], H[0]})

STRAIGHT_SSSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSSDD.append({S[i], S[j], S[k], D[l], D[m]})
STRAIGHT_SSSDD.append({S[9], S[10], S[11], D[12], D[0]})

STRAIGHT_SSCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCSS.append({S[i], S[j], C[k], S[l], S[m]})
STRAIGHT_SSCSS.append({S[9], S[10], C[11], S[12], S[0]})

STRAIGHT_SSCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCSC.append({S[i], S[j], C[k], S[l], C[m]})
STRAIGHT_SSCSC.append({S[9], S[10], C[11], S[12], C[0]})

STRAIGHT_SSCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCSH.append({S[i], S[j], C[k], S[l], H[m]})
STRAIGHT_SSCSH.append({S[9], S[10], C[11], S[12], H[0]})

STRAIGHT_SSCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCSD.append({S[i], S[j], C[k], S[l], D[m]})
STRAIGHT_SSCSD.append({S[9], S[10], C[11], S[12], D[0]})

STRAIGHT_SSCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCCS.append({S[i], S[j], C[k], C[l], S[m]})
STRAIGHT_SSCCS.append({S[9], S[10], C[11], C[12], S[0]})

STRAIGHT_SSCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCCC.append({S[i], S[j], C[k], C[l], C[m]})
STRAIGHT_SSCCC.append({S[9], S[10], C[11], C[12], C[0]})

STRAIGHT_SSCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCCH.append({S[i], S[j], C[k], C[l], H[m]})
STRAIGHT_SSCCH.append({S[9], S[10], C[11], C[12], H[0]})

STRAIGHT_SSCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCCD.append({S[i], S[j], C[k], C[l], D[m]})
STRAIGHT_SSCCD.append({S[9], S[10], C[11], C[12], D[0]})

STRAIGHT_SSCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCHS.append({S[i], S[j], C[k], H[l], S[m]})
STRAIGHT_SSCHS.append({S[9], S[10], C[11], H[12], S[0]})

STRAIGHT_SSCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCHC.append({S[i], S[j], C[k], H[l], C[m]})
STRAIGHT_SSCHC.append({S[9], S[10], C[11], H[12], C[0]})

STRAIGHT_SSCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCHH.append({S[i], S[j], C[k], H[l], H[m]})
STRAIGHT_SSCHH.append({S[9], S[10], C[11], H[12], H[0]})

STRAIGHT_SSCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCHD.append({S[i], S[j], C[k], H[l], D[m]})
STRAIGHT_SSCHD.append({S[9], S[10], C[11], H[12], D[0]})

STRAIGHT_SSCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCDS.append({S[i], S[j], C[k], D[l], S[m]})
STRAIGHT_SSCDS.append({S[9], S[10], C[11], D[12], S[0]})

STRAIGHT_SSCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCDC.append({S[i], S[j], C[k], D[l], C[m]})
STRAIGHT_SSCDC.append({S[9], S[10], C[11], D[12], C[0]})

STRAIGHT_SSCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCDH.append({S[i], S[j], C[k], D[l], H[m]})
STRAIGHT_SSCDH.append({S[9], S[10], C[11], D[12], H[0]})

STRAIGHT_SSCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSCDD.append({S[i], S[j], C[k], D[l], D[m]})
STRAIGHT_SSCDD.append({S[9], S[10], C[11], D[12], D[0]})

STRAIGHT_SSHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHSS.append({S[i], S[j], H[k], S[l], S[m]})
STRAIGHT_SSHSS.append({S[9], S[10], H[11], S[12], S[0]})

STRAIGHT_SSHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHSC.append({S[i], S[j], H[k], S[l], C[m]})
STRAIGHT_SSHSC.append({S[9], S[10], H[11], S[12], C[0]})

STRAIGHT_SSHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHSH.append({S[i], S[j], H[k], S[l], H[m]})
STRAIGHT_SSHSH.append({S[9], S[10], H[11], S[12], H[0]})

STRAIGHT_SSHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHSD.append({S[i], S[j], H[k], S[l], D[m]})
STRAIGHT_SSHSD.append({S[9], S[10], H[11], S[12], D[0]})

STRAIGHT_SSHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHCS.append({S[i], S[j], H[k], C[l], S[m]})
STRAIGHT_SSHCS.append({S[9], S[10], H[11], C[12], S[0]})

STRAIGHT_SSHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHCC.append({S[i], S[j], H[k], C[l], C[m]})
STRAIGHT_SSHCC.append({S[9], S[10], H[11], C[12], C[0]})

STRAIGHT_SSHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHCH.append({S[i], S[j], H[k], C[l], H[m]})
STRAIGHT_SSHCH.append({S[9], S[10], H[11], C[12], H[0]})

STRAIGHT_SSHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHCD.append({S[i], S[j], H[k], C[l], D[m]})
STRAIGHT_SSHCD.append({S[9], S[10], H[11], C[12], D[0]})

STRAIGHT_SSHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHHS.append({S[i], S[j], H[k], H[l], S[m]})
STRAIGHT_SSHHS.append({S[9], S[10], H[11], H[12], S[0]})

STRAIGHT_SSHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHHC.append({S[i], S[j], H[k], H[l], C[m]})
STRAIGHT_SSHHC.append({S[9], S[10], H[11], H[12], C[0]})

STRAIGHT_SSHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHHH.append({S[i], S[j], H[k], H[l], H[m]})
STRAIGHT_SSHHH.append({S[9], S[10], H[11], H[12], H[0]})

STRAIGHT_SSHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHHD.append({S[i], S[j], H[k], H[l], D[m]})
STRAIGHT_SSHHD.append({S[9], S[10], H[11], H[12], D[0]})

STRAIGHT_SSHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHDS.append({S[i], S[j], H[k], D[l], S[m]})
STRAIGHT_SSHDS.append({S[9], S[10], H[11], D[12], S[0]})

STRAIGHT_SSHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHDC.append({S[i], S[j], H[k], D[l], C[m]})
STRAIGHT_SSHDC.append({S[9], S[10], H[11], D[12], C[0]})

STRAIGHT_SSHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHDH.append({S[i], S[j], H[k], D[l], H[m]})
STRAIGHT_SSHDH.append({S[9], S[10], H[11], D[12], H[0]})

STRAIGHT_SSHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSHDD.append({S[i], S[j], H[k], D[l], D[m]})
STRAIGHT_SSHDD.append({S[9], S[10], H[11], D[12], D[0]})

STRAIGHT_SSDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDSS.append({S[i], S[j], D[k], S[l], S[m]})
STRAIGHT_SSDSS.append({S[9], S[10], D[11], S[12], S[0]})

STRAIGHT_SSDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDSC.append({S[i], S[j], D[k], S[l], C[m]})
STRAIGHT_SSDSC.append({S[9], S[10], D[11], S[12], C[0]})

STRAIGHT_SSDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDSH.append({S[i], S[j], D[k], S[l], H[m]})
STRAIGHT_SSDSH.append({S[9], S[10], D[11], S[12], H[0]})

STRAIGHT_SSDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDSD.append({S[i], S[j], D[k], S[l], D[m]})
STRAIGHT_SSDSD.append({S[9], S[10], D[11], S[12], D[0]})

STRAIGHT_SSDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDCS.append({S[i], S[j], D[k], C[l], S[m]})
STRAIGHT_SSDCS.append({S[9], S[10], D[11], C[12], S[0]})

STRAIGHT_SSDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDCC.append({S[i], S[j], D[k], C[l], C[m]})
STRAIGHT_SSDCC.append({S[9], S[10], D[11], C[12], C[0]})

STRAIGHT_SSDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDCH.append({S[i], S[j], D[k], C[l], H[m]})
STRAIGHT_SSDCH.append({S[9], S[10], D[11], C[12], H[0]})

STRAIGHT_SSDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDCD.append({S[i], S[j], D[k], C[l], D[m]})
STRAIGHT_SSDCD.append({S[9], S[10], D[11], C[12], D[0]})

STRAIGHT_SSDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDHS.append({S[i], S[j], D[k], H[l], S[m]})
STRAIGHT_SSDHS.append({S[9], S[10], D[11], H[12], S[0]})

STRAIGHT_SSDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDHC.append({S[i], S[j], D[k], H[l], C[m]})
STRAIGHT_SSDHC.append({S[9], S[10], D[11], H[12], C[0]})

STRAIGHT_SSDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDHH.append({S[i], S[j], D[k], H[l], H[m]})
STRAIGHT_SSDHH.append({S[9], S[10], D[11], H[12], H[0]})

STRAIGHT_SSDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDHD.append({S[i], S[j], D[k], H[l], D[m]})
STRAIGHT_SSDHD.append({S[9], S[10], D[11], H[12], D[0]})

STRAIGHT_SSDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDDS.append({S[i], S[j], D[k], D[l], S[m]})
STRAIGHT_SSDDS.append({S[9], S[10], D[11], D[12], S[0]})

STRAIGHT_SSDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDDC.append({S[i], S[j], D[k], D[l], C[m]})
STRAIGHT_SSDDC.append({S[9], S[10], D[11], D[12], C[0]})

STRAIGHT_SSDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDDH.append({S[i], S[j], D[k], D[l], H[m]})
STRAIGHT_SSDDH.append({S[9], S[10], D[11], D[12], H[0]})

STRAIGHT_SSDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SSDDD.append({S[i], S[j], D[k], D[l], D[m]})
STRAIGHT_SSDDD.append({S[9], S[10], D[11], D[12], D[0]})

STRAIGHT_SCSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSSS.append({S[i], C[j], S[k], S[l], S[m]})
STRAIGHT_SCSSS.append({S[9], C[10], S[11], S[12], S[0]})

STRAIGHT_SCSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSSC.append({S[i], C[j], S[k], S[l], C[m]})
STRAIGHT_SCSSC.append({S[9], C[10], S[11], S[12], C[0]})

STRAIGHT_SCSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSSH.append({S[i], C[j], S[k], S[l], H[m]})
STRAIGHT_SCSSH.append({S[9], C[10], S[11], S[12], H[0]})

STRAIGHT_SCSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSSD.append({S[i], C[j], S[k], S[l], D[m]})
STRAIGHT_SCSSD.append({S[9], C[10], S[11], S[12], D[0]})

STRAIGHT_SCSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSCS.append({S[i], C[j], S[k], C[l], S[m]})
STRAIGHT_SCSCS.append({S[9], C[10], S[11], C[12], S[0]})

STRAIGHT_SCSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSCC.append({S[i], C[j], S[k], C[l], C[m]})
STRAIGHT_SCSCC.append({S[9], C[10], S[11], C[12], C[0]})

STRAIGHT_SCSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSCH.append({S[i], C[j], S[k], C[l], H[m]})
STRAIGHT_SCSCH.append({S[9], C[10], S[11], C[12], H[0]})

STRAIGHT_SCSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSCD.append({S[i], C[j], S[k], C[l], D[m]})
STRAIGHT_SCSCD.append({S[9], C[10], S[11], C[12], D[0]})

STRAIGHT_SCSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSHS.append({S[i], C[j], S[k], H[l], S[m]})
STRAIGHT_SCSHS.append({S[9], C[10], S[11], H[12], S[0]})

STRAIGHT_SCSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSHC.append({S[i], C[j], S[k], H[l], C[m]})
STRAIGHT_SCSHC.append({S[9], C[10], S[11], H[12], C[0]})

STRAIGHT_SCSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSHH.append({S[i], C[j], S[k], H[l], H[m]})
STRAIGHT_SCSHH.append({S[9], C[10], S[11], H[12], H[0]})

STRAIGHT_SCSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSHD.append({S[i], C[j], S[k], H[l], D[m]})
STRAIGHT_SCSHD.append({S[9], C[10], S[11], H[12], D[0]})

STRAIGHT_SCSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSDS.append({S[i], C[j], S[k], D[l], S[m]})
STRAIGHT_SCSDS.append({S[9], C[10], S[11], D[12], S[0]})

STRAIGHT_SCSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSDC.append({S[i], C[j], S[k], D[l], C[m]})
STRAIGHT_SCSDC.append({S[9], C[10], S[11], D[12], C[0]})

STRAIGHT_SCSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSDH.append({S[i], C[j], S[k], D[l], H[m]})
STRAIGHT_SCSDH.append({S[9], C[10], S[11], D[12], H[0]})

STRAIGHT_SCSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCSDD.append({S[i], C[j], S[k], D[l], D[m]})
STRAIGHT_SCSDD.append({S[9], C[10], S[11], D[12], D[0]})

STRAIGHT_SCCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCSS.append({S[i], C[j], C[k], S[l], S[m]})
STRAIGHT_SCCSS.append({S[9], C[10], C[11], S[12], S[0]})

STRAIGHT_SCCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCSC.append({S[i], C[j], C[k], S[l], C[m]})
STRAIGHT_SCCSC.append({S[9], C[10], C[11], S[12], C[0]})

STRAIGHT_SCCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCSH.append({S[i], C[j], C[k], S[l], H[m]})
STRAIGHT_SCCSH.append({S[9], C[10], C[11], S[12], H[0]})

STRAIGHT_SCCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCSD.append({S[i], C[j], C[k], S[l], D[m]})
STRAIGHT_SCCSD.append({S[9], C[10], C[11], S[12], D[0]})

STRAIGHT_SCCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCCS.append({S[i], C[j], C[k], C[l], S[m]})
STRAIGHT_SCCCS.append({S[9], C[10], C[11], C[12], S[0]})

STRAIGHT_SCCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCCC.append({S[i], C[j], C[k], C[l], C[m]})
STRAIGHT_SCCCC.append({S[9], C[10], C[11], C[12], C[0]})

STRAIGHT_SCCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCCH.append({S[i], C[j], C[k], C[l], H[m]})
STRAIGHT_SCCCH.append({S[9], C[10], C[11], C[12], H[0]})

STRAIGHT_SCCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCCD.append({S[i], C[j], C[k], C[l], D[m]})
STRAIGHT_SCCCD.append({S[9], C[10], C[11], C[12], D[0]})

STRAIGHT_SCCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCHS.append({S[i], C[j], C[k], H[l], S[m]})
STRAIGHT_SCCHS.append({S[9], C[10], C[11], H[12], S[0]})

STRAIGHT_SCCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCHC.append({S[i], C[j], C[k], H[l], C[m]})
STRAIGHT_SCCHC.append({S[9], C[10], C[11], H[12], C[0]})

STRAIGHT_SCCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCHH.append({S[i], C[j], C[k], H[l], H[m]})
STRAIGHT_SCCHH.append({S[9], C[10], C[11], H[12], H[0]})

STRAIGHT_SCCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCHD.append({S[i], C[j], C[k], H[l], D[m]})
STRAIGHT_SCCHD.append({S[9], C[10], C[11], H[12], D[0]})

STRAIGHT_SCCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCDS.append({S[i], C[j], C[k], D[l], S[m]})
STRAIGHT_SCCDS.append({S[9], C[10], C[11], D[12], S[0]})

STRAIGHT_SCCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCDC.append({S[i], C[j], C[k], D[l], C[m]})
STRAIGHT_SCCDC.append({S[9], C[10], C[11], D[12], C[0]})

STRAIGHT_SCCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCDH.append({S[i], C[j], C[k], D[l], H[m]})
STRAIGHT_SCCDH.append({S[9], C[10], C[11], D[12], H[0]})

STRAIGHT_SCCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCCDD.append({S[i], C[j], C[k], D[l], D[m]})
STRAIGHT_SCCDD.append({S[9], C[10], C[11], D[12], D[0]})

STRAIGHT_SCHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHSS.append({S[i], C[j], H[k], S[l], S[m]})
STRAIGHT_SCHSS.append({S[9], C[10], H[11], S[12], S[0]})

STRAIGHT_SCHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHSC.append({S[i], C[j], H[k], S[l], C[m]})
STRAIGHT_SCHSC.append({S[9], C[10], H[11], S[12], C[0]})

STRAIGHT_SCHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHSH.append({S[i], C[j], H[k], S[l], H[m]})
STRAIGHT_SCHSH.append({S[9], C[10], H[11], S[12], H[0]})

STRAIGHT_SCHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHSD.append({S[i], C[j], H[k], S[l], D[m]})
STRAIGHT_SCHSD.append({S[9], C[10], H[11], S[12], D[0]})

STRAIGHT_SCHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHCS.append({S[i], C[j], H[k], C[l], S[m]})
STRAIGHT_SCHCS.append({S[9], C[10], H[11], C[12], S[0]})

STRAIGHT_SCHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHCC.append({S[i], C[j], H[k], C[l], C[m]})
STRAIGHT_SCHCC.append({S[9], C[10], H[11], C[12], C[0]})

STRAIGHT_SCHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHCH.append({S[i], C[j], H[k], C[l], H[m]})
STRAIGHT_SCHCH.append({S[9], C[10], H[11], C[12], H[0]})

STRAIGHT_SCHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHCD.append({S[i], C[j], H[k], C[l], D[m]})
STRAIGHT_SCHCD.append({S[9], C[10], H[11], C[12], D[0]})

STRAIGHT_SCHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHHS.append({S[i], C[j], H[k], H[l], S[m]})
STRAIGHT_SCHHS.append({S[9], C[10], H[11], H[12], S[0]})

STRAIGHT_SCHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHHC.append({S[i], C[j], H[k], H[l], C[m]})
STRAIGHT_SCHHC.append({S[9], C[10], H[11], H[12], C[0]})

STRAIGHT_SCHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHHH.append({S[i], C[j], H[k], H[l], H[m]})
STRAIGHT_SCHHH.append({S[9], C[10], H[11], H[12], H[0]})

STRAIGHT_SCHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHHD.append({S[i], C[j], H[k], H[l], D[m]})
STRAIGHT_SCHHD.append({S[9], C[10], H[11], H[12], D[0]})

STRAIGHT_SCHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHDS.append({S[i], C[j], H[k], D[l], S[m]})
STRAIGHT_SCHDS.append({S[9], C[10], H[11], D[12], S[0]})

STRAIGHT_SCHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHDC.append({S[i], C[j], H[k], D[l], C[m]})
STRAIGHT_SCHDC.append({S[9], C[10], H[11], D[12], C[0]})

STRAIGHT_SCHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHDH.append({S[i], C[j], H[k], D[l], H[m]})
STRAIGHT_SCHDH.append({S[9], C[10], H[11], D[12], H[0]})

STRAIGHT_SCHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCHDD.append({S[i], C[j], H[k], D[l], D[m]})
STRAIGHT_SCHDD.append({S[9], C[10], H[11], D[12], D[0]})

STRAIGHT_SCDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDSS.append({S[i], C[j], D[k], S[l], S[m]})
STRAIGHT_SCDSS.append({S[9], C[10], D[11], S[12], S[0]})

STRAIGHT_SCDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDSC.append({S[i], C[j], D[k], S[l], C[m]})
STRAIGHT_SCDSC.append({S[9], C[10], D[11], S[12], C[0]})

STRAIGHT_SCDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDSH.append({S[i], C[j], D[k], S[l], H[m]})
STRAIGHT_SCDSH.append({S[9], C[10], D[11], S[12], H[0]})

STRAIGHT_SCDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDSD.append({S[i], C[j], D[k], S[l], D[m]})
STRAIGHT_SCDSD.append({S[9], C[10], D[11], S[12], D[0]})

STRAIGHT_SCDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDCS.append({S[i], C[j], D[k], C[l], S[m]})
STRAIGHT_SCDCS.append({S[9], C[10], D[11], C[12], S[0]})

STRAIGHT_SCDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDCC.append({S[i], C[j], D[k], C[l], C[m]})
STRAIGHT_SCDCC.append({S[9], C[10], D[11], C[12], C[0]})

STRAIGHT_SCDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDCH.append({S[i], C[j], D[k], C[l], H[m]})
STRAIGHT_SCDCH.append({S[9], C[10], D[11], C[12], H[0]})

STRAIGHT_SCDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDCD.append({S[i], C[j], D[k], C[l], D[m]})
STRAIGHT_SCDCD.append({S[9], C[10], D[11], C[12], D[0]})

STRAIGHT_SCDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDHS.append({S[i], C[j], D[k], H[l], S[m]})
STRAIGHT_SCDHS.append({S[9], C[10], D[11], H[12], S[0]})

STRAIGHT_SCDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDHC.append({S[i], C[j], D[k], H[l], C[m]})
STRAIGHT_SCDHC.append({S[9], C[10], D[11], H[12], C[0]})

STRAIGHT_SCDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDHH.append({S[i], C[j], D[k], H[l], H[m]})
STRAIGHT_SCDHH.append({S[9], C[10], D[11], H[12], H[0]})

STRAIGHT_SCDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDHD.append({S[i], C[j], D[k], H[l], D[m]})
STRAIGHT_SCDHD.append({S[9], C[10], D[11], H[12], D[0]})

STRAIGHT_SCDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDDS.append({S[i], C[j], D[k], D[l], S[m]})
STRAIGHT_SCDDS.append({S[9], C[10], D[11], D[12], S[0]})

STRAIGHT_SCDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDDC.append({S[i], C[j], D[k], D[l], C[m]})
STRAIGHT_SCDDC.append({S[9], C[10], D[11], D[12], C[0]})

STRAIGHT_SCDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDDH.append({S[i], C[j], D[k], D[l], H[m]})
STRAIGHT_SCDDH.append({S[9], C[10], D[11], D[12], H[0]})

STRAIGHT_SCDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SCDDD.append({S[i], C[j], D[k], D[l], D[m]})
STRAIGHT_SCDDD.append({S[9], C[10], D[11], D[12], D[0]})

STRAIGHT_SHSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSSS.append({S[i], H[j], S[k], S[l], S[m]})
STRAIGHT_SHSSS.append({S[9], H[10], S[11], S[12], S[0]})

STRAIGHT_SHSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSSC.append({S[i], H[j], S[k], S[l], C[m]})
STRAIGHT_SHSSC.append({S[9], H[10], S[11], S[12], C[0]})

STRAIGHT_SHSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSSH.append({S[i], H[j], S[k], S[l], H[m]})
STRAIGHT_SHSSH.append({S[9], H[10], S[11], S[12], H[0]})

STRAIGHT_SHSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSSD.append({S[i], H[j], S[k], S[l], D[m]})
STRAIGHT_SHSSD.append({S[9], H[10], S[11], S[12], D[0]})

STRAIGHT_SHSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSCS.append({S[i], H[j], S[k], C[l], S[m]})
STRAIGHT_SHSCS.append({S[9], H[10], S[11], C[12], S[0]})

STRAIGHT_SHSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSCC.append({S[i], H[j], S[k], C[l], C[m]})
STRAIGHT_SHSCC.append({S[9], H[10], S[11], C[12], C[0]})

STRAIGHT_SHSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSCH.append({S[i], H[j], S[k], C[l], H[m]})
STRAIGHT_SHSCH.append({S[9], H[10], S[11], C[12], H[0]})

STRAIGHT_SHSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSCD.append({S[i], H[j], S[k], C[l], D[m]})
STRAIGHT_SHSCD.append({S[9], H[10], S[11], C[12], D[0]})

STRAIGHT_SHSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSHS.append({S[i], H[j], S[k], H[l], S[m]})
STRAIGHT_SHSHS.append({S[9], H[10], S[11], H[12], S[0]})

STRAIGHT_SHSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSHC.append({S[i], H[j], S[k], H[l], C[m]})
STRAIGHT_SHSHC.append({S[9], H[10], S[11], H[12], C[0]})

STRAIGHT_SHSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSHH.append({S[i], H[j], S[k], H[l], H[m]})
STRAIGHT_SHSHH.append({S[9], H[10], S[11], H[12], H[0]})

STRAIGHT_SHSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSHD.append({S[i], H[j], S[k], H[l], D[m]})
STRAIGHT_SHSHD.append({S[9], H[10], S[11], H[12], D[0]})

STRAIGHT_SHSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSDS.append({S[i], H[j], S[k], D[l], S[m]})
STRAIGHT_SHSDS.append({S[9], H[10], S[11], D[12], S[0]})

STRAIGHT_SHSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSDC.append({S[i], H[j], S[k], D[l], C[m]})
STRAIGHT_SHSDC.append({S[9], H[10], S[11], D[12], C[0]})

STRAIGHT_SHSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSDH.append({S[i], H[j], S[k], D[l], H[m]})
STRAIGHT_SHSDH.append({S[9], H[10], S[11], D[12], H[0]})

STRAIGHT_SHSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHSDD.append({S[i], H[j], S[k], D[l], D[m]})
STRAIGHT_SHSDD.append({S[9], H[10], S[11], D[12], D[0]})

STRAIGHT_SHCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCSS.append({S[i], H[j], C[k], S[l], S[m]})
STRAIGHT_SHCSS.append({S[9], H[10], C[11], S[12], S[0]})

STRAIGHT_SHCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCSC.append({S[i], H[j], C[k], S[l], C[m]})
STRAIGHT_SHCSC.append({S[9], H[10], C[11], S[12], C[0]})

STRAIGHT_SHCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCSH.append({S[i], H[j], C[k], S[l], H[m]})
STRAIGHT_SHCSH.append({S[9], H[10], C[11], S[12], H[0]})

STRAIGHT_SHCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCSD.append({S[i], H[j], C[k], S[l], D[m]})
STRAIGHT_SHCSD.append({S[9], H[10], C[11], S[12], D[0]})

STRAIGHT_SHCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCCS.append({S[i], H[j], C[k], C[l], S[m]})
STRAIGHT_SHCCS.append({S[9], H[10], C[11], C[12], S[0]})

STRAIGHT_SHCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCCC.append({S[i], H[j], C[k], C[l], C[m]})
STRAIGHT_SHCCC.append({S[9], H[10], C[11], C[12], C[0]})

STRAIGHT_SHCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCCH.append({S[i], H[j], C[k], C[l], H[m]})
STRAIGHT_SHCCH.append({S[9], H[10], C[11], C[12], H[0]})

STRAIGHT_SHCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCCD.append({S[i], H[j], C[k], C[l], D[m]})
STRAIGHT_SHCCD.append({S[9], H[10], C[11], C[12], D[0]})

STRAIGHT_SHCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCHS.append({S[i], H[j], C[k], H[l], S[m]})
STRAIGHT_SHCHS.append({S[9], H[10], C[11], H[12], S[0]})

STRAIGHT_SHCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCHC.append({S[i], H[j], C[k], H[l], C[m]})
STRAIGHT_SHCHC.append({S[9], H[10], C[11], H[12], C[0]})

STRAIGHT_SHCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCHH.append({S[i], H[j], C[k], H[l], H[m]})
STRAIGHT_SHCHH.append({S[9], H[10], C[11], H[12], H[0]})

STRAIGHT_SHCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCHD.append({S[i], H[j], C[k], H[l], D[m]})
STRAIGHT_SHCHD.append({S[9], H[10], C[11], H[12], D[0]})

STRAIGHT_SHCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCDS.append({S[i], H[j], C[k], D[l], S[m]})
STRAIGHT_SHCDS.append({S[9], H[10], C[11], D[12], S[0]})

STRAIGHT_SHCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCDC.append({S[i], H[j], C[k], D[l], C[m]})
STRAIGHT_SHCDC.append({S[9], H[10], C[11], D[12], C[0]})

STRAIGHT_SHCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCDH.append({S[i], H[j], C[k], D[l], H[m]})
STRAIGHT_SHCDH.append({S[9], H[10], C[11], D[12], H[0]})

STRAIGHT_SHCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHCDD.append({S[i], H[j], C[k], D[l], D[m]})
STRAIGHT_SHCDD.append({S[9], H[10], C[11], D[12], D[0]})

STRAIGHT_SHHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHSS.append({S[i], H[j], H[k], S[l], S[m]})
STRAIGHT_SHHSS.append({S[9], H[10], H[11], S[12], S[0]})

STRAIGHT_SHHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHSC.append({S[i], H[j], H[k], S[l], C[m]})
STRAIGHT_SHHSC.append({S[9], H[10], H[11], S[12], C[0]})

STRAIGHT_SHHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHSH.append({S[i], H[j], H[k], S[l], H[m]})
STRAIGHT_SHHSH.append({S[9], H[10], H[11], S[12], H[0]})

STRAIGHT_SHHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHSD.append({S[i], H[j], H[k], S[l], D[m]})
STRAIGHT_SHHSD.append({S[9], H[10], H[11], S[12], D[0]})

STRAIGHT_SHHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHCS.append({S[i], H[j], H[k], C[l], S[m]})
STRAIGHT_SHHCS.append({S[9], H[10], H[11], C[12], S[0]})

STRAIGHT_SHHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHCC.append({S[i], H[j], H[k], C[l], C[m]})
STRAIGHT_SHHCC.append({S[9], H[10], H[11], C[12], C[0]})

STRAIGHT_SHHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHCH.append({S[i], H[j], H[k], C[l], H[m]})
STRAIGHT_SHHCH.append({S[9], H[10], H[11], C[12], H[0]})

STRAIGHT_SHHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHCD.append({S[i], H[j], H[k], C[l], D[m]})
STRAIGHT_SHHCD.append({S[9], H[10], H[11], C[12], D[0]})

STRAIGHT_SHHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHHS.append({S[i], H[j], H[k], H[l], S[m]})
STRAIGHT_SHHHS.append({S[9], H[10], H[11], H[12], S[0]})

STRAIGHT_SHHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHHC.append({S[i], H[j], H[k], H[l], C[m]})
STRAIGHT_SHHHC.append({S[9], H[10], H[11], H[12], C[0]})

STRAIGHT_SHHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHHH.append({S[i], H[j], H[k], H[l], H[m]})
STRAIGHT_SHHHH.append({S[9], H[10], H[11], H[12], H[0]})

STRAIGHT_SHHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHHD.append({S[i], H[j], H[k], H[l], D[m]})
STRAIGHT_SHHHD.append({S[9], H[10], H[11], H[12], D[0]})

STRAIGHT_SHHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHDS.append({S[i], H[j], H[k], D[l], S[m]})
STRAIGHT_SHHDS.append({S[9], H[10], H[11], D[12], S[0]})

STRAIGHT_SHHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHDC.append({S[i], H[j], H[k], D[l], C[m]})
STRAIGHT_SHHDC.append({S[9], H[10], H[11], D[12], C[0]})

STRAIGHT_SHHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHDH.append({S[i], H[j], H[k], D[l], H[m]})
STRAIGHT_SHHDH.append({S[9], H[10], H[11], D[12], H[0]})

STRAIGHT_SHHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHHDD.append({S[i], H[j], H[k], D[l], D[m]})
STRAIGHT_SHHDD.append({S[9], H[10], H[11], D[12], D[0]})

STRAIGHT_SHDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDSS.append({S[i], H[j], D[k], S[l], S[m]})
STRAIGHT_SHDSS.append({S[9], H[10], D[11], S[12], S[0]})

STRAIGHT_SHDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDSC.append({S[i], H[j], D[k], S[l], C[m]})
STRAIGHT_SHDSC.append({S[9], H[10], D[11], S[12], C[0]})

STRAIGHT_SHDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDSH.append({S[i], H[j], D[k], S[l], H[m]})
STRAIGHT_SHDSH.append({S[9], H[10], D[11], S[12], H[0]})

STRAIGHT_SHDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDSD.append({S[i], H[j], D[k], S[l], D[m]})
STRAIGHT_SHDSD.append({S[9], H[10], D[11], S[12], D[0]})

STRAIGHT_SHDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDCS.append({S[i], H[j], D[k], C[l], S[m]})
STRAIGHT_SHDCS.append({S[9], H[10], D[11], C[12], S[0]})

STRAIGHT_SHDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDCC.append({S[i], H[j], D[k], C[l], C[m]})
STRAIGHT_SHDCC.append({S[9], H[10], D[11], C[12], C[0]})

STRAIGHT_SHDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDCH.append({S[i], H[j], D[k], C[l], H[m]})
STRAIGHT_SHDCH.append({S[9], H[10], D[11], C[12], H[0]})

STRAIGHT_SHDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDCD.append({S[i], H[j], D[k], C[l], D[m]})
STRAIGHT_SHDCD.append({S[9], H[10], D[11], C[12], D[0]})

STRAIGHT_SHDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDHS.append({S[i], H[j], D[k], H[l], S[m]})
STRAIGHT_SHDHS.append({S[9], H[10], D[11], H[12], S[0]})

STRAIGHT_SHDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDHC.append({S[i], H[j], D[k], H[l], C[m]})
STRAIGHT_SHDHC.append({S[9], H[10], D[11], H[12], C[0]})

STRAIGHT_SHDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDHH.append({S[i], H[j], D[k], H[l], H[m]})
STRAIGHT_SHDHH.append({S[9], H[10], D[11], H[12], H[0]})

STRAIGHT_SHDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDHD.append({S[i], H[j], D[k], H[l], D[m]})
STRAIGHT_SHDHD.append({S[9], H[10], D[11], H[12], D[0]})

STRAIGHT_SHDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDDS.append({S[i], H[j], D[k], D[l], S[m]})
STRAIGHT_SHDDS.append({S[9], H[10], D[11], D[12], S[0]})

STRAIGHT_SHDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDDC.append({S[i], H[j], D[k], D[l], C[m]})
STRAIGHT_SHDDC.append({S[9], H[10], D[11], D[12], C[0]})

STRAIGHT_SHDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDDH.append({S[i], H[j], D[k], D[l], H[m]})
STRAIGHT_SHDDH.append({S[9], H[10], D[11], D[12], H[0]})

STRAIGHT_SHDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SHDDD.append({S[i], H[j], D[k], D[l], D[m]})
STRAIGHT_SHDDD.append({S[9], H[10], D[11], D[12], D[0]})

STRAIGHT_SDSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSSS.append({S[i], D[j], S[k], S[l], S[m]})
STRAIGHT_SDSSS.append({S[9], D[10], S[11], S[12], S[0]})

STRAIGHT_SDSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSSC.append({S[i], D[j], S[k], S[l], C[m]})
STRAIGHT_SDSSC.append({S[9], D[10], S[11], S[12], C[0]})

STRAIGHT_SDSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSSH.append({S[i], D[j], S[k], S[l], H[m]})
STRAIGHT_SDSSH.append({S[9], D[10], S[11], S[12], H[0]})

STRAIGHT_SDSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSSD.append({S[i], D[j], S[k], S[l], D[m]})
STRAIGHT_SDSSD.append({S[9], D[10], S[11], S[12], D[0]})

STRAIGHT_SDSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSCS.append({S[i], D[j], S[k], C[l], S[m]})
STRAIGHT_SDSCS.append({S[9], D[10], S[11], C[12], S[0]})

STRAIGHT_SDSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSCC.append({S[i], D[j], S[k], C[l], C[m]})
STRAIGHT_SDSCC.append({S[9], D[10], S[11], C[12], C[0]})

STRAIGHT_SDSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSCH.append({S[i], D[j], S[k], C[l], H[m]})
STRAIGHT_SDSCH.append({S[9], D[10], S[11], C[12], H[0]})

STRAIGHT_SDSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSCD.append({S[i], D[j], S[k], C[l], D[m]})
STRAIGHT_SDSCD.append({S[9], D[10], S[11], C[12], D[0]})

STRAIGHT_SDSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSHS.append({S[i], D[j], S[k], H[l], S[m]})
STRAIGHT_SDSHS.append({S[9], D[10], S[11], H[12], S[0]})

STRAIGHT_SDSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSHC.append({S[i], D[j], S[k], H[l], C[m]})
STRAIGHT_SDSHC.append({S[9], D[10], S[11], H[12], C[0]})

STRAIGHT_SDSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSHH.append({S[i], D[j], S[k], H[l], H[m]})
STRAIGHT_SDSHH.append({S[9], D[10], S[11], H[12], H[0]})

STRAIGHT_SDSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSHD.append({S[i], D[j], S[k], H[l], D[m]})
STRAIGHT_SDSHD.append({S[9], D[10], S[11], H[12], D[0]})

STRAIGHT_SDSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSDS.append({S[i], D[j], S[k], D[l], S[m]})
STRAIGHT_SDSDS.append({S[9], D[10], S[11], D[12], S[0]})

STRAIGHT_SDSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSDC.append({S[i], D[j], S[k], D[l], C[m]})
STRAIGHT_SDSDC.append({S[9], D[10], S[11], D[12], C[0]})

STRAIGHT_SDSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSDH.append({S[i], D[j], S[k], D[l], H[m]})
STRAIGHT_SDSDH.append({S[9], D[10], S[11], D[12], H[0]})

STRAIGHT_SDSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDSDD.append({S[i], D[j], S[k], D[l], D[m]})
STRAIGHT_SDSDD.append({S[9], D[10], S[11], D[12], D[0]})

STRAIGHT_SDCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCSS.append({S[i], D[j], C[k], S[l], S[m]})
STRAIGHT_SDCSS.append({S[9], D[10], C[11], S[12], S[0]})

STRAIGHT_SDCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCSC.append({S[i], D[j], C[k], S[l], C[m]})
STRAIGHT_SDCSC.append({S[9], D[10], C[11], S[12], C[0]})

STRAIGHT_SDCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCSH.append({S[i], D[j], C[k], S[l], H[m]})
STRAIGHT_SDCSH.append({S[9], D[10], C[11], S[12], H[0]})

STRAIGHT_SDCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCSD.append({S[i], D[j], C[k], S[l], D[m]})
STRAIGHT_SDCSD.append({S[9], D[10], C[11], S[12], D[0]})

STRAIGHT_SDCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCCS.append({S[i], D[j], C[k], C[l], S[m]})
STRAIGHT_SDCCS.append({S[9], D[10], C[11], C[12], S[0]})

STRAIGHT_SDCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCCC.append({S[i], D[j], C[k], C[l], C[m]})
STRAIGHT_SDCCC.append({S[9], D[10], C[11], C[12], C[0]})

STRAIGHT_SDCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCCH.append({S[i], D[j], C[k], C[l], H[m]})
STRAIGHT_SDCCH.append({S[9], D[10], C[11], C[12], H[0]})

STRAIGHT_SDCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCCD.append({S[i], D[j], C[k], C[l], D[m]})
STRAIGHT_SDCCD.append({S[9], D[10], C[11], C[12], D[0]})

STRAIGHT_SDCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCHS.append({S[i], D[j], C[k], H[l], S[m]})
STRAIGHT_SDCHS.append({S[9], D[10], C[11], H[12], S[0]})

STRAIGHT_SDCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCHC.append({S[i], D[j], C[k], H[l], C[m]})
STRAIGHT_SDCHC.append({S[9], D[10], C[11], H[12], C[0]})

STRAIGHT_SDCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCHH.append({S[i], D[j], C[k], H[l], H[m]})
STRAIGHT_SDCHH.append({S[9], D[10], C[11], H[12], H[0]})

STRAIGHT_SDCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCHD.append({S[i], D[j], C[k], H[l], D[m]})
STRAIGHT_SDCHD.append({S[9], D[10], C[11], H[12], D[0]})

STRAIGHT_SDCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCDS.append({S[i], D[j], C[k], D[l], S[m]})
STRAIGHT_SDCDS.append({S[9], D[10], C[11], D[12], S[0]})

STRAIGHT_SDCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCDC.append({S[i], D[j], C[k], D[l], C[m]})
STRAIGHT_SDCDC.append({S[9], D[10], C[11], D[12], C[0]})

STRAIGHT_SDCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCDH.append({S[i], D[j], C[k], D[l], H[m]})
STRAIGHT_SDCDH.append({S[9], D[10], C[11], D[12], H[0]})

STRAIGHT_SDCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDCDD.append({S[i], D[j], C[k], D[l], D[m]})
STRAIGHT_SDCDD.append({S[9], D[10], C[11], D[12], D[0]})

STRAIGHT_SDHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHSS.append({S[i], D[j], H[k], S[l], S[m]})
STRAIGHT_SDHSS.append({S[9], D[10], H[11], S[12], S[0]})

STRAIGHT_SDHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHSC.append({S[i], D[j], H[k], S[l], C[m]})
STRAIGHT_SDHSC.append({S[9], D[10], H[11], S[12], C[0]})

STRAIGHT_SDHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHSH.append({S[i], D[j], H[k], S[l], H[m]})
STRAIGHT_SDHSH.append({S[9], D[10], H[11], S[12], H[0]})

STRAIGHT_SDHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHSD.append({S[i], D[j], H[k], S[l], D[m]})
STRAIGHT_SDHSD.append({S[9], D[10], H[11], S[12], D[0]})

STRAIGHT_SDHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHCS.append({S[i], D[j], H[k], C[l], S[m]})
STRAIGHT_SDHCS.append({S[9], D[10], H[11], C[12], S[0]})

STRAIGHT_SDHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHCC.append({S[i], D[j], H[k], C[l], C[m]})
STRAIGHT_SDHCC.append({S[9], D[10], H[11], C[12], C[0]})

STRAIGHT_SDHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHCH.append({S[i], D[j], H[k], C[l], H[m]})
STRAIGHT_SDHCH.append({S[9], D[10], H[11], C[12], H[0]})

STRAIGHT_SDHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHCD.append({S[i], D[j], H[k], C[l], D[m]})
STRAIGHT_SDHCD.append({S[9], D[10], H[11], C[12], D[0]})

STRAIGHT_SDHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHHS.append({S[i], D[j], H[k], H[l], S[m]})
STRAIGHT_SDHHS.append({S[9], D[10], H[11], H[12], S[0]})

STRAIGHT_SDHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHHC.append({S[i], D[j], H[k], H[l], C[m]})
STRAIGHT_SDHHC.append({S[9], D[10], H[11], H[12], C[0]})

STRAIGHT_SDHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHHH.append({S[i], D[j], H[k], H[l], H[m]})
STRAIGHT_SDHHH.append({S[9], D[10], H[11], H[12], H[0]})

STRAIGHT_SDHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHHD.append({S[i], D[j], H[k], H[l], D[m]})
STRAIGHT_SDHHD.append({S[9], D[10], H[11], H[12], D[0]})

STRAIGHT_SDHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHDS.append({S[i], D[j], H[k], D[l], S[m]})
STRAIGHT_SDHDS.append({S[9], D[10], H[11], D[12], S[0]})

STRAIGHT_SDHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHDC.append({S[i], D[j], H[k], D[l], C[m]})
STRAIGHT_SDHDC.append({S[9], D[10], H[11], D[12], C[0]})

STRAIGHT_SDHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHDH.append({S[i], D[j], H[k], D[l], H[m]})
STRAIGHT_SDHDH.append({S[9], D[10], H[11], D[12], H[0]})

STRAIGHT_SDHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDHDD.append({S[i], D[j], H[k], D[l], D[m]})
STRAIGHT_SDHDD.append({S[9], D[10], H[11], D[12], D[0]})

STRAIGHT_SDDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDSS.append({S[i], D[j], D[k], S[l], S[m]})
STRAIGHT_SDDSS.append({S[9], D[10], D[11], S[12], S[0]})

STRAIGHT_SDDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDSC.append({S[i], D[j], D[k], S[l], C[m]})
STRAIGHT_SDDSC.append({S[9], D[10], D[11], S[12], C[0]})

STRAIGHT_SDDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDSH.append({S[i], D[j], D[k], S[l], H[m]})
STRAIGHT_SDDSH.append({S[9], D[10], D[11], S[12], H[0]})

STRAIGHT_SDDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDSD.append({S[i], D[j], D[k], S[l], D[m]})
STRAIGHT_SDDSD.append({S[9], D[10], D[11], S[12], D[0]})

STRAIGHT_SDDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDCS.append({S[i], D[j], D[k], C[l], S[m]})
STRAIGHT_SDDCS.append({S[9], D[10], D[11], C[12], S[0]})

STRAIGHT_SDDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDCC.append({S[i], D[j], D[k], C[l], C[m]})
STRAIGHT_SDDCC.append({S[9], D[10], D[11], C[12], C[0]})

STRAIGHT_SDDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDCH.append({S[i], D[j], D[k], C[l], H[m]})
STRAIGHT_SDDCH.append({S[9], D[10], D[11], C[12], H[0]})

STRAIGHT_SDDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDCD.append({S[i], D[j], D[k], C[l], D[m]})
STRAIGHT_SDDCD.append({S[9], D[10], D[11], C[12], D[0]})

STRAIGHT_SDDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDHS.append({S[i], D[j], D[k], H[l], S[m]})
STRAIGHT_SDDHS.append({S[9], D[10], D[11], H[12], S[0]})

STRAIGHT_SDDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDHC.append({S[i], D[j], D[k], H[l], C[m]})
STRAIGHT_SDDHC.append({S[9], D[10], D[11], H[12], C[0]})

STRAIGHT_SDDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDHH.append({S[i], D[j], D[k], H[l], H[m]})
STRAIGHT_SDDHH.append({S[9], D[10], D[11], H[12], H[0]})

STRAIGHT_SDDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDHD.append({S[i], D[j], D[k], H[l], D[m]})
STRAIGHT_SDDHD.append({S[9], D[10], D[11], H[12], D[0]})

STRAIGHT_SDDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDDS.append({S[i], D[j], D[k], D[l], S[m]})
STRAIGHT_SDDDS.append({S[9], D[10], D[11], D[12], S[0]})

STRAIGHT_SDDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDDC.append({S[i], D[j], D[k], D[l], C[m]})
STRAIGHT_SDDDC.append({S[9], D[10], D[11], D[12], C[0]})

STRAIGHT_SDDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDDH.append({S[i], D[j], D[k], D[l], H[m]})
STRAIGHT_SDDDH.append({S[9], D[10], D[11], D[12], H[0]})

STRAIGHT_SDDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_SDDDD.append({S[i], D[j], D[k], D[l], D[m]})
STRAIGHT_SDDDD.append({S[9], D[10], D[11], D[12], D[0]})

STRAIGHT_CSSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSSS.append({C[i], S[j], S[k], S[l], S[m]})
STRAIGHT_CSSSS.append({C[9], S[10], S[11], S[12], S[0]})

STRAIGHT_CSSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSSC.append({C[i], S[j], S[k], S[l], C[m]})
STRAIGHT_CSSSC.append({C[9], S[10], S[11], S[12], C[0]})

STRAIGHT_CSSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSSH.append({C[i], S[j], S[k], S[l], H[m]})
STRAIGHT_CSSSH.append({C[9], S[10], S[11], S[12], H[0]})

STRAIGHT_CSSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSSD.append({C[i], S[j], S[k], S[l], D[m]})
STRAIGHT_CSSSD.append({C[9], S[10], S[11], S[12], D[0]})

STRAIGHT_CSSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSCS.append({C[i], S[j], S[k], C[l], S[m]})
STRAIGHT_CSSCS.append({C[9], S[10], S[11], C[12], S[0]})

STRAIGHT_CSSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSCC.append({C[i], S[j], S[k], C[l], C[m]})
STRAIGHT_CSSCC.append({C[9], S[10], S[11], C[12], C[0]})

STRAIGHT_CSSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSCH.append({C[i], S[j], S[k], C[l], H[m]})
STRAIGHT_CSSCH.append({C[9], S[10], S[11], C[12], H[0]})

STRAIGHT_CSSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSCD.append({C[i], S[j], S[k], C[l], D[m]})
STRAIGHT_CSSCD.append({C[9], S[10], S[11], C[12], D[0]})

STRAIGHT_CSSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSHS.append({C[i], S[j], S[k], H[l], S[m]})
STRAIGHT_CSSHS.append({C[9], S[10], S[11], H[12], S[0]})

STRAIGHT_CSSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSHC.append({C[i], S[j], S[k], H[l], C[m]})
STRAIGHT_CSSHC.append({C[9], S[10], S[11], H[12], C[0]})

STRAIGHT_CSSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSHH.append({C[i], S[j], S[k], H[l], H[m]})
STRAIGHT_CSSHH.append({C[9], S[10], S[11], H[12], H[0]})

STRAIGHT_CSSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSHD.append({C[i], S[j], S[k], H[l], D[m]})
STRAIGHT_CSSHD.append({C[9], S[10], S[11], H[12], D[0]})

STRAIGHT_CSSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSDS.append({C[i], S[j], S[k], D[l], S[m]})
STRAIGHT_CSSDS.append({C[9], S[10], S[11], D[12], S[0]})

STRAIGHT_CSSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSDC.append({C[i], S[j], S[k], D[l], C[m]})
STRAIGHT_CSSDC.append({C[9], S[10], S[11], D[12], C[0]})

STRAIGHT_CSSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSDH.append({C[i], S[j], S[k], D[l], H[m]})
STRAIGHT_CSSDH.append({C[9], S[10], S[11], D[12], H[0]})

STRAIGHT_CSSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSSDD.append({C[i], S[j], S[k], D[l], D[m]})
STRAIGHT_CSSDD.append({C[9], S[10], S[11], D[12], D[0]})

STRAIGHT_CSCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCSS.append({C[i], S[j], C[k], S[l], S[m]})
STRAIGHT_CSCSS.append({C[9], S[10], C[11], S[12], S[0]})

STRAIGHT_CSCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCSC.append({C[i], S[j], C[k], S[l], C[m]})
STRAIGHT_CSCSC.append({C[9], S[10], C[11], S[12], C[0]})

STRAIGHT_CSCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCSH.append({C[i], S[j], C[k], S[l], H[m]})
STRAIGHT_CSCSH.append({C[9], S[10], C[11], S[12], H[0]})

STRAIGHT_CSCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCSD.append({C[i], S[j], C[k], S[l], D[m]})
STRAIGHT_CSCSD.append({C[9], S[10], C[11], S[12], D[0]})

STRAIGHT_CSCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCCS.append({C[i], S[j], C[k], C[l], S[m]})
STRAIGHT_CSCCS.append({C[9], S[10], C[11], C[12], S[0]})

STRAIGHT_CSCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCCC.append({C[i], S[j], C[k], C[l], C[m]})
STRAIGHT_CSCCC.append({C[9], S[10], C[11], C[12], C[0]})

STRAIGHT_CSCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCCH.append({C[i], S[j], C[k], C[l], H[m]})
STRAIGHT_CSCCH.append({C[9], S[10], C[11], C[12], H[0]})

STRAIGHT_CSCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCCD.append({C[i], S[j], C[k], C[l], D[m]})
STRAIGHT_CSCCD.append({C[9], S[10], C[11], C[12], D[0]})

STRAIGHT_CSCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCHS.append({C[i], S[j], C[k], H[l], S[m]})
STRAIGHT_CSCHS.append({C[9], S[10], C[11], H[12], S[0]})

STRAIGHT_CSCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCHC.append({C[i], S[j], C[k], H[l], C[m]})
STRAIGHT_CSCHC.append({C[9], S[10], C[11], H[12], C[0]})

STRAIGHT_CSCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCHH.append({C[i], S[j], C[k], H[l], H[m]})
STRAIGHT_CSCHH.append({C[9], S[10], C[11], H[12], H[0]})

STRAIGHT_CSCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCHD.append({C[i], S[j], C[k], H[l], D[m]})
STRAIGHT_CSCHD.append({C[9], S[10], C[11], H[12], D[0]})

STRAIGHT_CSCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCDS.append({C[i], S[j], C[k], D[l], S[m]})
STRAIGHT_CSCDS.append({C[9], S[10], C[11], D[12], S[0]})

STRAIGHT_CSCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCDC.append({C[i], S[j], C[k], D[l], C[m]})
STRAIGHT_CSCDC.append({C[9], S[10], C[11], D[12], C[0]})

STRAIGHT_CSCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCDH.append({C[i], S[j], C[k], D[l], H[m]})
STRAIGHT_CSCDH.append({C[9], S[10], C[11], D[12], H[0]})

STRAIGHT_CSCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSCDD.append({C[i], S[j], C[k], D[l], D[m]})
STRAIGHT_CSCDD.append({C[9], S[10], C[11], D[12], D[0]})

STRAIGHT_CSHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHSS.append({C[i], S[j], H[k], S[l], S[m]})
STRAIGHT_CSHSS.append({C[9], S[10], H[11], S[12], S[0]})

STRAIGHT_CSHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHSC.append({C[i], S[j], H[k], S[l], C[m]})
STRAIGHT_CSHSC.append({C[9], S[10], H[11], S[12], C[0]})

STRAIGHT_CSHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHSH.append({C[i], S[j], H[k], S[l], H[m]})
STRAIGHT_CSHSH.append({C[9], S[10], H[11], S[12], H[0]})

STRAIGHT_CSHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHSD.append({C[i], S[j], H[k], S[l], D[m]})
STRAIGHT_CSHSD.append({C[9], S[10], H[11], S[12], D[0]})

STRAIGHT_CSHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHCS.append({C[i], S[j], H[k], C[l], S[m]})
STRAIGHT_CSHCS.append({C[9], S[10], H[11], C[12], S[0]})

STRAIGHT_CSHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHCC.append({C[i], S[j], H[k], C[l], C[m]})
STRAIGHT_CSHCC.append({C[9], S[10], H[11], C[12], C[0]})

STRAIGHT_CSHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHCH.append({C[i], S[j], H[k], C[l], H[m]})
STRAIGHT_CSHCH.append({C[9], S[10], H[11], C[12], H[0]})

STRAIGHT_CSHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHCD.append({C[i], S[j], H[k], C[l], D[m]})
STRAIGHT_CSHCD.append({C[9], S[10], H[11], C[12], D[0]})

STRAIGHT_CSHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHHS.append({C[i], S[j], H[k], H[l], S[m]})
STRAIGHT_CSHHS.append({C[9], S[10], H[11], H[12], S[0]})

STRAIGHT_CSHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHHC.append({C[i], S[j], H[k], H[l], C[m]})
STRAIGHT_CSHHC.append({C[9], S[10], H[11], H[12], C[0]})

STRAIGHT_CSHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHHH.append({C[i], S[j], H[k], H[l], H[m]})
STRAIGHT_CSHHH.append({C[9], S[10], H[11], H[12], H[0]})

STRAIGHT_CSHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHHD.append({C[i], S[j], H[k], H[l], D[m]})
STRAIGHT_CSHHD.append({C[9], S[10], H[11], H[12], D[0]})

STRAIGHT_CSHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHDS.append({C[i], S[j], H[k], D[l], S[m]})
STRAIGHT_CSHDS.append({C[9], S[10], H[11], D[12], S[0]})

STRAIGHT_CSHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHDC.append({C[i], S[j], H[k], D[l], C[m]})
STRAIGHT_CSHDC.append({C[9], S[10], H[11], D[12], C[0]})

STRAIGHT_CSHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHDH.append({C[i], S[j], H[k], D[l], H[m]})
STRAIGHT_CSHDH.append({C[9], S[10], H[11], D[12], H[0]})

STRAIGHT_CSHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSHDD.append({C[i], S[j], H[k], D[l], D[m]})
STRAIGHT_CSHDD.append({C[9], S[10], H[11], D[12], D[0]})

STRAIGHT_CSDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDSS.append({C[i], S[j], D[k], S[l], S[m]})
STRAIGHT_CSDSS.append({C[9], S[10], D[11], S[12], S[0]})

STRAIGHT_CSDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDSC.append({C[i], S[j], D[k], S[l], C[m]})
STRAIGHT_CSDSC.append({C[9], S[10], D[11], S[12], C[0]})

STRAIGHT_CSDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDSH.append({C[i], S[j], D[k], S[l], H[m]})
STRAIGHT_CSDSH.append({C[9], S[10], D[11], S[12], H[0]})

STRAIGHT_CSDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDSD.append({C[i], S[j], D[k], S[l], D[m]})
STRAIGHT_CSDSD.append({C[9], S[10], D[11], S[12], D[0]})

STRAIGHT_CSDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDCS.append({C[i], S[j], D[k], C[l], S[m]})
STRAIGHT_CSDCS.append({C[9], S[10], D[11], C[12], S[0]})

STRAIGHT_CSDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDCC.append({C[i], S[j], D[k], C[l], C[m]})
STRAIGHT_CSDCC.append({C[9], S[10], D[11], C[12], C[0]})

STRAIGHT_CSDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDCH.append({C[i], S[j], D[k], C[l], H[m]})
STRAIGHT_CSDCH.append({C[9], S[10], D[11], C[12], H[0]})

STRAIGHT_CSDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDCD.append({C[i], S[j], D[k], C[l], D[m]})
STRAIGHT_CSDCD.append({C[9], S[10], D[11], C[12], D[0]})

STRAIGHT_CSDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDHS.append({C[i], S[j], D[k], H[l], S[m]})
STRAIGHT_CSDHS.append({C[9], S[10], D[11], H[12], S[0]})

STRAIGHT_CSDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDHC.append({C[i], S[j], D[k], H[l], C[m]})
STRAIGHT_CSDHC.append({C[9], S[10], D[11], H[12], C[0]})

STRAIGHT_CSDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDHH.append({C[i], S[j], D[k], H[l], H[m]})
STRAIGHT_CSDHH.append({C[9], S[10], D[11], H[12], H[0]})

STRAIGHT_CSDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDHD.append({C[i], S[j], D[k], H[l], D[m]})
STRAIGHT_CSDHD.append({C[9], S[10], D[11], H[12], D[0]})

STRAIGHT_CSDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDDS.append({C[i], S[j], D[k], D[l], S[m]})
STRAIGHT_CSDDS.append({C[9], S[10], D[11], D[12], S[0]})

STRAIGHT_CSDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDDC.append({C[i], S[j], D[k], D[l], C[m]})
STRAIGHT_CSDDC.append({C[9], S[10], D[11], D[12], C[0]})

STRAIGHT_CSDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDDH.append({C[i], S[j], D[k], D[l], H[m]})
STRAIGHT_CSDDH.append({C[9], S[10], D[11], D[12], H[0]})

STRAIGHT_CSDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CSDDD.append({C[i], S[j], D[k], D[l], D[m]})
STRAIGHT_CSDDD.append({C[9], S[10], D[11], D[12], D[0]})

STRAIGHT_CCSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSSS.append({C[i], C[j], S[k], S[l], S[m]})
STRAIGHT_CCSSS.append({C[9], C[10], S[11], S[12], S[0]})

STRAIGHT_CCSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSSC.append({C[i], C[j], S[k], S[l], C[m]})
STRAIGHT_CCSSC.append({C[9], C[10], S[11], S[12], C[0]})

STRAIGHT_CCSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSSH.append({C[i], C[j], S[k], S[l], H[m]})
STRAIGHT_CCSSH.append({C[9], C[10], S[11], S[12], H[0]})

STRAIGHT_CCSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSSD.append({C[i], C[j], S[k], S[l], D[m]})
STRAIGHT_CCSSD.append({C[9], C[10], S[11], S[12], D[0]})

STRAIGHT_CCSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSCS.append({C[i], C[j], S[k], C[l], S[m]})
STRAIGHT_CCSCS.append({C[9], C[10], S[11], C[12], S[0]})

STRAIGHT_CCSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSCC.append({C[i], C[j], S[k], C[l], C[m]})
STRAIGHT_CCSCC.append({C[9], C[10], S[11], C[12], C[0]})

STRAIGHT_CCSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSCH.append({C[i], C[j], S[k], C[l], H[m]})
STRAIGHT_CCSCH.append({C[9], C[10], S[11], C[12], H[0]})

STRAIGHT_CCSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSCD.append({C[i], C[j], S[k], C[l], D[m]})
STRAIGHT_CCSCD.append({C[9], C[10], S[11], C[12], D[0]})

STRAIGHT_CCSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSHS.append({C[i], C[j], S[k], H[l], S[m]})
STRAIGHT_CCSHS.append({C[9], C[10], S[11], H[12], S[0]})

STRAIGHT_CCSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSHC.append({C[i], C[j], S[k], H[l], C[m]})
STRAIGHT_CCSHC.append({C[9], C[10], S[11], H[12], C[0]})

STRAIGHT_CCSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSHH.append({C[i], C[j], S[k], H[l], H[m]})
STRAIGHT_CCSHH.append({C[9], C[10], S[11], H[12], H[0]})

STRAIGHT_CCSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSHD.append({C[i], C[j], S[k], H[l], D[m]})
STRAIGHT_CCSHD.append({C[9], C[10], S[11], H[12], D[0]})

STRAIGHT_CCSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSDS.append({C[i], C[j], S[k], D[l], S[m]})
STRAIGHT_CCSDS.append({C[9], C[10], S[11], D[12], S[0]})

STRAIGHT_CCSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSDC.append({C[i], C[j], S[k], D[l], C[m]})
STRAIGHT_CCSDC.append({C[9], C[10], S[11], D[12], C[0]})

STRAIGHT_CCSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSDH.append({C[i], C[j], S[k], D[l], H[m]})
STRAIGHT_CCSDH.append({C[9], C[10], S[11], D[12], H[0]})

STRAIGHT_CCSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCSDD.append({C[i], C[j], S[k], D[l], D[m]})
STRAIGHT_CCSDD.append({C[9], C[10], S[11], D[12], D[0]})

STRAIGHT_CCCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCSS.append({C[i], C[j], C[k], S[l], S[m]})
STRAIGHT_CCCSS.append({C[9], C[10], C[11], S[12], S[0]})

STRAIGHT_CCCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCSC.append({C[i], C[j], C[k], S[l], C[m]})
STRAIGHT_CCCSC.append({C[9], C[10], C[11], S[12], C[0]})

STRAIGHT_CCCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCSH.append({C[i], C[j], C[k], S[l], H[m]})
STRAIGHT_CCCSH.append({C[9], C[10], C[11], S[12], H[0]})

STRAIGHT_CCCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCSD.append({C[i], C[j], C[k], S[l], D[m]})
STRAIGHT_CCCSD.append({C[9], C[10], C[11], S[12], D[0]})

STRAIGHT_CCCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCCS.append({C[i], C[j], C[k], C[l], S[m]})
STRAIGHT_CCCCS.append({C[9], C[10], C[11], C[12], S[0]})

STRAIGHT_CCCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCCH.append({C[i], C[j], C[k], C[l], H[m]})
STRAIGHT_CCCCH.append({C[9], C[10], C[11], C[12], H[0]})

STRAIGHT_CCCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCCD.append({C[i], C[j], C[k], C[l], D[m]})
STRAIGHT_CCCCD.append({C[9], C[10], C[11], C[12], D[0]})

STRAIGHT_CCCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCHS.append({C[i], C[j], C[k], H[l], S[m]})
STRAIGHT_CCCHS.append({C[9], C[10], C[11], H[12], S[0]})

STRAIGHT_CCCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCHC.append({C[i], C[j], C[k], H[l], C[m]})
STRAIGHT_CCCHC.append({C[9], C[10], C[11], H[12], C[0]})

STRAIGHT_CCCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCHH.append({C[i], C[j], C[k], H[l], H[m]})
STRAIGHT_CCCHH.append({C[9], C[10], C[11], H[12], H[0]})

STRAIGHT_CCCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCHD.append({C[i], C[j], C[k], H[l], D[m]})
STRAIGHT_CCCHD.append({C[9], C[10], C[11], H[12], D[0]})

STRAIGHT_CCCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCDS.append({C[i], C[j], C[k], D[l], S[m]})
STRAIGHT_CCCDS.append({C[9], C[10], C[11], D[12], S[0]})

STRAIGHT_CCCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCDC.append({C[i], C[j], C[k], D[l], C[m]})
STRAIGHT_CCCDC.append({C[9], C[10], C[11], D[12], C[0]})

STRAIGHT_CCCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCDH.append({C[i], C[j], C[k], D[l], H[m]})
STRAIGHT_CCCDH.append({C[9], C[10], C[11], D[12], H[0]})

STRAIGHT_CCCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCCDD.append({C[i], C[j], C[k], D[l], D[m]})
STRAIGHT_CCCDD.append({C[9], C[10], C[11], D[12], D[0]})

STRAIGHT_CCHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHSS.append({C[i], C[j], H[k], S[l], S[m]})
STRAIGHT_CCHSS.append({C[9], C[10], H[11], S[12], S[0]})

STRAIGHT_CCHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHSC.append({C[i], C[j], H[k], S[l], C[m]})
STRAIGHT_CCHSC.append({C[9], C[10], H[11], S[12], C[0]})

STRAIGHT_CCHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHSH.append({C[i], C[j], H[k], S[l], H[m]})
STRAIGHT_CCHSH.append({C[9], C[10], H[11], S[12], H[0]})

STRAIGHT_CCHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHSD.append({C[i], C[j], H[k], S[l], D[m]})
STRAIGHT_CCHSD.append({C[9], C[10], H[11], S[12], D[0]})

STRAIGHT_CCHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHCS.append({C[i], C[j], H[k], C[l], S[m]})
STRAIGHT_CCHCS.append({C[9], C[10], H[11], C[12], S[0]})

STRAIGHT_CCHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHCC.append({C[i], C[j], H[k], C[l], C[m]})
STRAIGHT_CCHCC.append({C[9], C[10], H[11], C[12], C[0]})

STRAIGHT_CCHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHCH.append({C[i], C[j], H[k], C[l], H[m]})
STRAIGHT_CCHCH.append({C[9], C[10], H[11], C[12], H[0]})

STRAIGHT_CCHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHCD.append({C[i], C[j], H[k], C[l], D[m]})
STRAIGHT_CCHCD.append({C[9], C[10], H[11], C[12], D[0]})

STRAIGHT_CCHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHHS.append({C[i], C[j], H[k], H[l], S[m]})
STRAIGHT_CCHHS.append({C[9], C[10], H[11], H[12], S[0]})

STRAIGHT_CCHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHHC.append({C[i], C[j], H[k], H[l], C[m]})
STRAIGHT_CCHHC.append({C[9], C[10], H[11], H[12], C[0]})

STRAIGHT_CCHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHHH.append({C[i], C[j], H[k], H[l], H[m]})
STRAIGHT_CCHHH.append({C[9], C[10], H[11], H[12], H[0]})

STRAIGHT_CCHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHHD.append({C[i], C[j], H[k], H[l], D[m]})
STRAIGHT_CCHHD.append({C[9], C[10], H[11], H[12], D[0]})

STRAIGHT_CCHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHDS.append({C[i], C[j], H[k], D[l], S[m]})
STRAIGHT_CCHDS.append({C[9], C[10], H[11], D[12], S[0]})

STRAIGHT_CCHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHDC.append({C[i], C[j], H[k], D[l], C[m]})
STRAIGHT_CCHDC.append({C[9], C[10], H[11], D[12], C[0]})

STRAIGHT_CCHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHDH.append({C[i], C[j], H[k], D[l], H[m]})
STRAIGHT_CCHDH.append({C[9], C[10], H[11], D[12], H[0]})

STRAIGHT_CCHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCHDD.append({C[i], C[j], H[k], D[l], D[m]})
STRAIGHT_CCHDD.append({C[9], C[10], H[11], D[12], D[0]})

STRAIGHT_CCDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDSS.append({C[i], C[j], D[k], S[l], S[m]})
STRAIGHT_CCDSS.append({C[9], C[10], D[11], S[12], S[0]})

STRAIGHT_CCDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDSC.append({C[i], C[j], D[k], S[l], C[m]})
STRAIGHT_CCDSC.append({C[9], C[10], D[11], S[12], C[0]})

STRAIGHT_CCDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDSH.append({C[i], C[j], D[k], S[l], H[m]})
STRAIGHT_CCDSH.append({C[9], C[10], D[11], S[12], H[0]})

STRAIGHT_CCDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDSD.append({C[i], C[j], D[k], S[l], D[m]})
STRAIGHT_CCDSD.append({C[9], C[10], D[11], S[12], D[0]})

STRAIGHT_CCDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDCS.append({C[i], C[j], D[k], C[l], S[m]})
STRAIGHT_CCDCS.append({C[9], C[10], D[11], C[12], S[0]})

STRAIGHT_CCDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDCC.append({C[i], C[j], D[k], C[l], C[m]})
STRAIGHT_CCDCC.append({C[9], C[10], D[11], C[12], C[0]})

STRAIGHT_CCDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDCH.append({C[i], C[j], D[k], C[l], H[m]})
STRAIGHT_CCDCH.append({C[9], C[10], D[11], C[12], H[0]})

STRAIGHT_CCDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDCD.append({C[i], C[j], D[k], C[l], D[m]})
STRAIGHT_CCDCD.append({C[9], C[10], D[11], C[12], D[0]})

STRAIGHT_CCDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDHS.append({C[i], C[j], D[k], H[l], S[m]})
STRAIGHT_CCDHS.append({C[9], C[10], D[11], H[12], S[0]})

STRAIGHT_CCDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDHC.append({C[i], C[j], D[k], H[l], C[m]})
STRAIGHT_CCDHC.append({C[9], C[10], D[11], H[12], C[0]})

STRAIGHT_CCDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDHH.append({C[i], C[j], D[k], H[l], H[m]})
STRAIGHT_CCDHH.append({C[9], C[10], D[11], H[12], H[0]})

STRAIGHT_CCDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDHD.append({C[i], C[j], D[k], H[l], D[m]})
STRAIGHT_CCDHD.append({C[9], C[10], D[11], H[12], D[0]})

STRAIGHT_CCDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDDS.append({C[i], C[j], D[k], D[l], S[m]})
STRAIGHT_CCDDS.append({C[9], C[10], D[11], D[12], S[0]})

STRAIGHT_CCDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDDC.append({C[i], C[j], D[k], D[l], C[m]})
STRAIGHT_CCDDC.append({C[9], C[10], D[11], D[12], C[0]})

STRAIGHT_CCDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDDH.append({C[i], C[j], D[k], D[l], H[m]})
STRAIGHT_CCDDH.append({C[9], C[10], D[11], D[12], H[0]})

STRAIGHT_CCDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CCDDD.append({C[i], C[j], D[k], D[l], D[m]})
STRAIGHT_CCDDD.append({C[9], C[10], D[11], D[12], D[0]})

STRAIGHT_CHSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSSS.append({C[i], H[j], S[k], S[l], S[m]})
STRAIGHT_CHSSS.append({C[9], H[10], S[11], S[12], S[0]})

STRAIGHT_CHSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSSC.append({C[i], H[j], S[k], S[l], C[m]})
STRAIGHT_CHSSC.append({C[9], H[10], S[11], S[12], C[0]})

STRAIGHT_CHSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSSH.append({C[i], H[j], S[k], S[l], H[m]})
STRAIGHT_CHSSH.append({C[9], H[10], S[11], S[12], H[0]})

STRAIGHT_CHSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSSD.append({C[i], H[j], S[k], S[l], D[m]})
STRAIGHT_CHSSD.append({C[9], H[10], S[11], S[12], D[0]})

STRAIGHT_CHSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSCS.append({C[i], H[j], S[k], C[l], S[m]})
STRAIGHT_CHSCS.append({C[9], H[10], S[11], C[12], S[0]})

STRAIGHT_CHSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSCC.append({C[i], H[j], S[k], C[l], C[m]})
STRAIGHT_CHSCC.append({C[9], H[10], S[11], C[12], C[0]})

STRAIGHT_CHSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSCH.append({C[i], H[j], S[k], C[l], H[m]})
STRAIGHT_CHSCH.append({C[9], H[10], S[11], C[12], H[0]})

STRAIGHT_CHSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSCD.append({C[i], H[j], S[k], C[l], D[m]})
STRAIGHT_CHSCD.append({C[9], H[10], S[11], C[12], D[0]})

STRAIGHT_CHSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSHS.append({C[i], H[j], S[k], H[l], S[m]})
STRAIGHT_CHSHS.append({C[9], H[10], S[11], H[12], S[0]})

STRAIGHT_CHSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSHC.append({C[i], H[j], S[k], H[l], C[m]})
STRAIGHT_CHSHC.append({C[9], H[10], S[11], H[12], C[0]})

STRAIGHT_CHSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSHH.append({C[i], H[j], S[k], H[l], H[m]})
STRAIGHT_CHSHH.append({C[9], H[10], S[11], H[12], H[0]})

STRAIGHT_CHSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSHD.append({C[i], H[j], S[k], H[l], D[m]})
STRAIGHT_CHSHD.append({C[9], H[10], S[11], H[12], D[0]})

STRAIGHT_CHSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSDS.append({C[i], H[j], S[k], D[l], S[m]})
STRAIGHT_CHSDS.append({C[9], H[10], S[11], D[12], S[0]})

STRAIGHT_CHSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSDC.append({C[i], H[j], S[k], D[l], C[m]})
STRAIGHT_CHSDC.append({C[9], H[10], S[11], D[12], C[0]})

STRAIGHT_CHSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSDH.append({C[i], H[j], S[k], D[l], H[m]})
STRAIGHT_CHSDH.append({C[9], H[10], S[11], D[12], H[0]})

STRAIGHT_CHSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHSDD.append({C[i], H[j], S[k], D[l], D[m]})
STRAIGHT_CHSDD.append({C[9], H[10], S[11], D[12], D[0]})

STRAIGHT_CHCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCSS.append({C[i], H[j], C[k], S[l], S[m]})
STRAIGHT_CHCSS.append({C[9], H[10], C[11], S[12], S[0]})

STRAIGHT_CHCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCSC.append({C[i], H[j], C[k], S[l], C[m]})
STRAIGHT_CHCSC.append({C[9], H[10], C[11], S[12], C[0]})

STRAIGHT_CHCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCSH.append({C[i], H[j], C[k], S[l], H[m]})
STRAIGHT_CHCSH.append({C[9], H[10], C[11], S[12], H[0]})

STRAIGHT_CHCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCSD.append({C[i], H[j], C[k], S[l], D[m]})
STRAIGHT_CHCSD.append({C[9], H[10], C[11], S[12], D[0]})

STRAIGHT_CHCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCCS.append({C[i], H[j], C[k], C[l], S[m]})
STRAIGHT_CHCCS.append({C[9], H[10], C[11], C[12], S[0]})

STRAIGHT_CHCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCCC.append({C[i], H[j], C[k], C[l], C[m]})
STRAIGHT_CHCCC.append({C[9], H[10], C[11], C[12], C[0]})

STRAIGHT_CHCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCCH.append({C[i], H[j], C[k], C[l], H[m]})
STRAIGHT_CHCCH.append({C[9], H[10], C[11], C[12], H[0]})

STRAIGHT_CHCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCCD.append({C[i], H[j], C[k], C[l], D[m]})
STRAIGHT_CHCCD.append({C[9], H[10], C[11], C[12], D[0]})

STRAIGHT_CHCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCHS.append({C[i], H[j], C[k], H[l], S[m]})
STRAIGHT_CHCHS.append({C[9], H[10], C[11], H[12], S[0]})

STRAIGHT_CHCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCHC.append({C[i], H[j], C[k], H[l], C[m]})
STRAIGHT_CHCHC.append({C[9], H[10], C[11], H[12], C[0]})

STRAIGHT_CHCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCHH.append({C[i], H[j], C[k], H[l], H[m]})
STRAIGHT_CHCHH.append({C[9], H[10], C[11], H[12], H[0]})

STRAIGHT_CHCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCHD.append({C[i], H[j], C[k], H[l], D[m]})
STRAIGHT_CHCHD.append({C[9], H[10], C[11], H[12], D[0]})

STRAIGHT_CHCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCDS.append({C[i], H[j], C[k], D[l], S[m]})
STRAIGHT_CHCDS.append({C[9], H[10], C[11], D[12], S[0]})

STRAIGHT_CHCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCDC.append({C[i], H[j], C[k], D[l], C[m]})
STRAIGHT_CHCDC.append({C[9], H[10], C[11], D[12], C[0]})

STRAIGHT_CHCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCDH.append({C[i], H[j], C[k], D[l], H[m]})
STRAIGHT_CHCDH.append({C[9], H[10], C[11], D[12], H[0]})

STRAIGHT_CHCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHCDD.append({C[i], H[j], C[k], D[l], D[m]})
STRAIGHT_CHCDD.append({C[9], H[10], C[11], D[12], D[0]})

STRAIGHT_CHHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHSS.append({C[i], H[j], H[k], S[l], S[m]})
STRAIGHT_CHHSS.append({C[9], H[10], H[11], S[12], S[0]})

STRAIGHT_CHHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHSC.append({C[i], H[j], H[k], S[l], C[m]})
STRAIGHT_CHHSC.append({C[9], H[10], H[11], S[12], C[0]})

STRAIGHT_CHHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHSH.append({C[i], H[j], H[k], S[l], H[m]})
STRAIGHT_CHHSH.append({C[9], H[10], H[11], S[12], H[0]})

STRAIGHT_CHHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHSD.append({C[i], H[j], H[k], S[l], D[m]})
STRAIGHT_CHHSD.append({C[9], H[10], H[11], S[12], D[0]})

STRAIGHT_CHHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHCS.append({C[i], H[j], H[k], C[l], S[m]})
STRAIGHT_CHHCS.append({C[9], H[10], H[11], C[12], S[0]})

STRAIGHT_CHHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHCC.append({C[i], H[j], H[k], C[l], C[m]})
STRAIGHT_CHHCC.append({C[9], H[10], H[11], C[12], C[0]})

STRAIGHT_CHHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHCH.append({C[i], H[j], H[k], C[l], H[m]})
STRAIGHT_CHHCH.append({C[9], H[10], H[11], C[12], H[0]})

STRAIGHT_CHHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHCD.append({C[i], H[j], H[k], C[l], D[m]})
STRAIGHT_CHHCD.append({C[9], H[10], H[11], C[12], D[0]})

STRAIGHT_CHHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHHS.append({C[i], H[j], H[k], H[l], S[m]})
STRAIGHT_CHHHS.append({C[9], H[10], H[11], H[12], S[0]})

STRAIGHT_CHHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHHC.append({C[i], H[j], H[k], H[l], C[m]})
STRAIGHT_CHHHC.append({C[9], H[10], H[11], H[12], C[0]})

STRAIGHT_CHHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHHH.append({C[i], H[j], H[k], H[l], H[m]})
STRAIGHT_CHHHH.append({C[9], H[10], H[11], H[12], H[0]})

STRAIGHT_CHHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHHD.append({C[i], H[j], H[k], H[l], D[m]})
STRAIGHT_CHHHD.append({C[9], H[10], H[11], H[12], D[0]})

STRAIGHT_CHHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHDS.append({C[i], H[j], H[k], D[l], S[m]})
STRAIGHT_CHHDS.append({C[9], H[10], H[11], D[12], S[0]})

STRAIGHT_CHHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHDC.append({C[i], H[j], H[k], D[l], C[m]})
STRAIGHT_CHHDC.append({C[9], H[10], H[11], D[12], C[0]})

STRAIGHT_CHHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHDH.append({C[i], H[j], H[k], D[l], H[m]})
STRAIGHT_CHHDH.append({C[9], H[10], H[11], D[12], H[0]})

STRAIGHT_CHHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHHDD.append({C[i], H[j], H[k], D[l], D[m]})
STRAIGHT_CHHDD.append({C[9], H[10], H[11], D[12], D[0]})

STRAIGHT_CHDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDSS.append({C[i], H[j], D[k], S[l], S[m]})
STRAIGHT_CHDSS.append({C[9], H[10], D[11], S[12], S[0]})

STRAIGHT_CHDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDSC.append({C[i], H[j], D[k], S[l], C[m]})
STRAIGHT_CHDSC.append({C[9], H[10], D[11], S[12], C[0]})

STRAIGHT_CHDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDSH.append({C[i], H[j], D[k], S[l], H[m]})
STRAIGHT_CHDSH.append({C[9], H[10], D[11], S[12], H[0]})

STRAIGHT_CHDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDSD.append({C[i], H[j], D[k], S[l], D[m]})
STRAIGHT_CHDSD.append({C[9], H[10], D[11], S[12], D[0]})

STRAIGHT_CHDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDCS.append({C[i], H[j], D[k], C[l], S[m]})
STRAIGHT_CHDCS.append({C[9], H[10], D[11], C[12], S[0]})

STRAIGHT_CHDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDCC.append({C[i], H[j], D[k], C[l], C[m]})
STRAIGHT_CHDCC.append({C[9], H[10], D[11], C[12], C[0]})

STRAIGHT_CHDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDCH.append({C[i], H[j], D[k], C[l], H[m]})
STRAIGHT_CHDCH.append({C[9], H[10], D[11], C[12], H[0]})

STRAIGHT_CHDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDCD.append({C[i], H[j], D[k], C[l], D[m]})
STRAIGHT_CHDCD.append({C[9], H[10], D[11], C[12], D[0]})

STRAIGHT_CHDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDHS.append({C[i], H[j], D[k], H[l], S[m]})
STRAIGHT_CHDHS.append({C[9], H[10], D[11], H[12], S[0]})

STRAIGHT_CHDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDHC.append({C[i], H[j], D[k], H[l], C[m]})
STRAIGHT_CHDHC.append({C[9], H[10], D[11], H[12], C[0]})

STRAIGHT_CHDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDHH.append({C[i], H[j], D[k], H[l], H[m]})
STRAIGHT_CHDHH.append({C[9], H[10], D[11], H[12], H[0]})

STRAIGHT_CHDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDHD.append({C[i], H[j], D[k], H[l], D[m]})
STRAIGHT_CHDHD.append({C[9], H[10], D[11], H[12], D[0]})

STRAIGHT_CHDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDDS.append({C[i], H[j], D[k], D[l], S[m]})
STRAIGHT_CHDDS.append({C[9], H[10], D[11], D[12], S[0]})

STRAIGHT_CHDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDDC.append({C[i], H[j], D[k], D[l], C[m]})
STRAIGHT_CHDDC.append({C[9], H[10], D[11], D[12], C[0]})

STRAIGHT_CHDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDDH.append({C[i], H[j], D[k], D[l], H[m]})
STRAIGHT_CHDDH.append({C[9], H[10], D[11], D[12], H[0]})

STRAIGHT_CHDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CHDDD.append({C[i], H[j], D[k], D[l], D[m]})
STRAIGHT_CHDDD.append({C[9], H[10], D[11], D[12], D[0]})

STRAIGHT_CDSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSSS.append({C[i], D[j], S[k], S[l], S[m]})
STRAIGHT_CDSSS.append({C[9], D[10], S[11], S[12], S[0]})

STRAIGHT_CDSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSSC.append({C[i], D[j], S[k], S[l], C[m]})
STRAIGHT_CDSSC.append({C[9], D[10], S[11], S[12], C[0]})

STRAIGHT_CDSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSSH.append({C[i], D[j], S[k], S[l], H[m]})
STRAIGHT_CDSSH.append({C[9], D[10], S[11], S[12], H[0]})

STRAIGHT_CDSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSSD.append({C[i], D[j], S[k], S[l], D[m]})
STRAIGHT_CDSSD.append({C[9], D[10], S[11], S[12], D[0]})

STRAIGHT_CDSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSCS.append({C[i], D[j], S[k], C[l], S[m]})
STRAIGHT_CDSCS.append({C[9], D[10], S[11], C[12], S[0]})

STRAIGHT_CDSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSCC.append({C[i], D[j], S[k], C[l], C[m]})
STRAIGHT_CDSCC.append({C[9], D[10], S[11], C[12], C[0]})

STRAIGHT_CDSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSCH.append({C[i], D[j], S[k], C[l], H[m]})
STRAIGHT_CDSCH.append({C[9], D[10], S[11], C[12], H[0]})

STRAIGHT_CDSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSCD.append({C[i], D[j], S[k], C[l], D[m]})
STRAIGHT_CDSCD.append({C[9], D[10], S[11], C[12], D[0]})

STRAIGHT_CDSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSHS.append({C[i], D[j], S[k], H[l], S[m]})
STRAIGHT_CDSHS.append({C[9], D[10], S[11], H[12], S[0]})

STRAIGHT_CDSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSHC.append({C[i], D[j], S[k], H[l], C[m]})
STRAIGHT_CDSHC.append({C[9], D[10], S[11], H[12], C[0]})

STRAIGHT_CDSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSHH.append({C[i], D[j], S[k], H[l], H[m]})
STRAIGHT_CDSHH.append({C[9], D[10], S[11], H[12], H[0]})

STRAIGHT_CDSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSHD.append({C[i], D[j], S[k], H[l], D[m]})
STRAIGHT_CDSHD.append({C[9], D[10], S[11], H[12], D[0]})

STRAIGHT_CDSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSDS.append({C[i], D[j], S[k], D[l], S[m]})
STRAIGHT_CDSDS.append({C[9], D[10], S[11], D[12], S[0]})

STRAIGHT_CDSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSDC.append({C[i], D[j], S[k], D[l], C[m]})
STRAIGHT_CDSDC.append({C[9], D[10], S[11], D[12], C[0]})

STRAIGHT_CDSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSDH.append({C[i], D[j], S[k], D[l], H[m]})
STRAIGHT_CDSDH.append({C[9], D[10], S[11], D[12], H[0]})

STRAIGHT_CDSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDSDD.append({C[i], D[j], S[k], D[l], D[m]})
STRAIGHT_CDSDD.append({C[9], D[10], S[11], D[12], D[0]})

STRAIGHT_CDCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCSS.append({C[i], D[j], C[k], S[l], S[m]})
STRAIGHT_CDCSS.append({C[9], D[10], C[11], S[12], S[0]})

STRAIGHT_CDCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCSC.append({C[i], D[j], C[k], S[l], C[m]})
STRAIGHT_CDCSC.append({C[9], D[10], C[11], S[12], C[0]})

STRAIGHT_CDCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCSH.append({C[i], D[j], C[k], S[l], H[m]})
STRAIGHT_CDCSH.append({C[9], D[10], C[11], S[12], H[0]})

STRAIGHT_CDCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCSD.append({C[i], D[j], C[k], S[l], D[m]})
STRAIGHT_CDCSD.append({C[9], D[10], C[11], S[12], D[0]})

STRAIGHT_CDCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCCS.append({C[i], D[j], C[k], C[l], S[m]})
STRAIGHT_CDCCS.append({C[9], D[10], C[11], C[12], S[0]})

STRAIGHT_CDCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCCC.append({C[i], D[j], C[k], C[l], C[m]})
STRAIGHT_CDCCC.append({C[9], D[10], C[11], C[12], C[0]})

STRAIGHT_CDCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCCH.append({C[i], D[j], C[k], C[l], H[m]})
STRAIGHT_CDCCH.append({C[9], D[10], C[11], C[12], H[0]})

STRAIGHT_CDCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCCD.append({C[i], D[j], C[k], C[l], D[m]})
STRAIGHT_CDCCD.append({C[9], D[10], C[11], C[12], D[0]})

STRAIGHT_CDCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCHS.append({C[i], D[j], C[k], H[l], S[m]})
STRAIGHT_CDCHS.append({C[9], D[10], C[11], H[12], S[0]})

STRAIGHT_CDCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCHC.append({C[i], D[j], C[k], H[l], C[m]})
STRAIGHT_CDCHC.append({C[9], D[10], C[11], H[12], C[0]})

STRAIGHT_CDCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCHH.append({C[i], D[j], C[k], H[l], H[m]})
STRAIGHT_CDCHH.append({C[9], D[10], C[11], H[12], H[0]})

STRAIGHT_CDCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCHD.append({C[i], D[j], C[k], H[l], D[m]})
STRAIGHT_CDCHD.append({C[9], D[10], C[11], H[12], D[0]})

STRAIGHT_CDCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCDS.append({C[i], D[j], C[k], D[l], S[m]})
STRAIGHT_CDCDS.append({C[9], D[10], C[11], D[12], S[0]})

STRAIGHT_CDCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCDC.append({C[i], D[j], C[k], D[l], C[m]})
STRAIGHT_CDCDC.append({C[9], D[10], C[11], D[12], C[0]})

STRAIGHT_CDCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCDH.append({C[i], D[j], C[k], D[l], H[m]})
STRAIGHT_CDCDH.append({C[9], D[10], C[11], D[12], H[0]})

STRAIGHT_CDCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDCDD.append({C[i], D[j], C[k], D[l], D[m]})
STRAIGHT_CDCDD.append({C[9], D[10], C[11], D[12], D[0]})

STRAIGHT_CDHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHSS.append({C[i], D[j], H[k], S[l], S[m]})
STRAIGHT_CDHSS.append({C[9], D[10], H[11], S[12], S[0]})

STRAIGHT_CDHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHSC.append({C[i], D[j], H[k], S[l], C[m]})
STRAIGHT_CDHSC.append({C[9], D[10], H[11], S[12], C[0]})

STRAIGHT_CDHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHSH.append({C[i], D[j], H[k], S[l], H[m]})
STRAIGHT_CDHSH.append({C[9], D[10], H[11], S[12], H[0]})

STRAIGHT_CDHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHSD.append({C[i], D[j], H[k], S[l], D[m]})
STRAIGHT_CDHSD.append({C[9], D[10], H[11], S[12], D[0]})

STRAIGHT_CDHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHCS.append({C[i], D[j], H[k], C[l], S[m]})
STRAIGHT_CDHCS.append({C[9], D[10], H[11], C[12], S[0]})

STRAIGHT_CDHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHCC.append({C[i], D[j], H[k], C[l], C[m]})
STRAIGHT_CDHCC.append({C[9], D[10], H[11], C[12], C[0]})

STRAIGHT_CDHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHCH.append({C[i], D[j], H[k], C[l], H[m]})
STRAIGHT_CDHCH.append({C[9], D[10], H[11], C[12], H[0]})

STRAIGHT_CDHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHCD.append({C[i], D[j], H[k], C[l], D[m]})
STRAIGHT_CDHCD.append({C[9], D[10], H[11], C[12], D[0]})

STRAIGHT_CDHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHHS.append({C[i], D[j], H[k], H[l], S[m]})
STRAIGHT_CDHHS.append({C[9], D[10], H[11], H[12], S[0]})

STRAIGHT_CDHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHHC.append({C[i], D[j], H[k], H[l], C[m]})
STRAIGHT_CDHHC.append({C[9], D[10], H[11], H[12], C[0]})

STRAIGHT_CDHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHHH.append({C[i], D[j], H[k], H[l], H[m]})
STRAIGHT_CDHHH.append({C[9], D[10], H[11], H[12], H[0]})

STRAIGHT_CDHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHHD.append({C[i], D[j], H[k], H[l], D[m]})
STRAIGHT_CDHHD.append({C[9], D[10], H[11], H[12], D[0]})

STRAIGHT_CDHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHDS.append({C[i], D[j], H[k], D[l], S[m]})
STRAIGHT_CDHDS.append({C[9], D[10], H[11], D[12], S[0]})

STRAIGHT_CDHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHDC.append({C[i], D[j], H[k], D[l], C[m]})
STRAIGHT_CDHDC.append({C[9], D[10], H[11], D[12], C[0]})

STRAIGHT_CDHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHDH.append({C[i], D[j], H[k], D[l], H[m]})
STRAIGHT_CDHDH.append({C[9], D[10], H[11], D[12], H[0]})

STRAIGHT_CDHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDHDD.append({C[i], D[j], H[k], D[l], D[m]})
STRAIGHT_CDHDD.append({C[9], D[10], H[11], D[12], D[0]})

STRAIGHT_CDDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDSS.append({C[i], D[j], D[k], S[l], S[m]})
STRAIGHT_CDDSS.append({C[9], D[10], D[11], S[12], S[0]})

STRAIGHT_CDDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDSC.append({C[i], D[j], D[k], S[l], C[m]})
STRAIGHT_CDDSC.append({C[9], D[10], D[11], S[12], C[0]})

STRAIGHT_CDDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDSH.append({C[i], D[j], D[k], S[l], H[m]})
STRAIGHT_CDDSH.append({C[9], D[10], D[11], S[12], H[0]})

STRAIGHT_CDDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDSD.append({C[i], D[j], D[k], S[l], D[m]})
STRAIGHT_CDDSD.append({C[9], D[10], D[11], S[12], D[0]})

STRAIGHT_CDDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDCS.append({C[i], D[j], D[k], C[l], S[m]})
STRAIGHT_CDDCS.append({C[9], D[10], D[11], C[12], S[0]})

STRAIGHT_CDDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDCC.append({C[i], D[j], D[k], C[l], C[m]})
STRAIGHT_CDDCC.append({C[9], D[10], D[11], C[12], C[0]})

STRAIGHT_CDDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDCH.append({C[i], D[j], D[k], C[l], H[m]})
STRAIGHT_CDDCH.append({C[9], D[10], D[11], C[12], H[0]})

STRAIGHT_CDDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDCD.append({C[i], D[j], D[k], C[l], D[m]})
STRAIGHT_CDDCD.append({C[9], D[10], D[11], C[12], D[0]})

STRAIGHT_CDDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDHS.append({C[i], D[j], D[k], H[l], S[m]})
STRAIGHT_CDDHS.append({C[9], D[10], D[11], H[12], S[0]})

STRAIGHT_CDDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDHC.append({C[i], D[j], D[k], H[l], C[m]})
STRAIGHT_CDDHC.append({C[9], D[10], D[11], H[12], C[0]})

STRAIGHT_CDDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDHH.append({C[i], D[j], D[k], H[l], H[m]})
STRAIGHT_CDDHH.append({C[9], D[10], D[11], H[12], H[0]})

STRAIGHT_CDDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDHD.append({C[i], D[j], D[k], H[l], D[m]})
STRAIGHT_CDDHD.append({C[9], D[10], D[11], H[12], D[0]})

STRAIGHT_CDDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDDS.append({C[i], D[j], D[k], D[l], S[m]})
STRAIGHT_CDDDS.append({C[9], D[10], D[11], D[12], S[0]})

STRAIGHT_CDDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDDC.append({C[i], D[j], D[k], D[l], C[m]})
STRAIGHT_CDDDC.append({C[9], D[10], D[11], D[12], C[0]})

STRAIGHT_CDDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDDH.append({C[i], D[j], D[k], D[l], H[m]})
STRAIGHT_CDDDH.append({C[9], D[10], D[11], D[12], H[0]})

STRAIGHT_CDDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_CDDDD.append({C[i], D[j], D[k], D[l], D[m]})
STRAIGHT_CDDDD.append({C[9], D[10], D[11], D[12], D[0]})

STRAIGHT_HSSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSSS.append({H[i], S[j], S[k], S[l], S[m]})
STRAIGHT_HSSSS.append({H[9], S[10], S[11], S[12], S[0]})

STRAIGHT_HSSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSSC.append({H[i], S[j], S[k], S[l], C[m]})
STRAIGHT_HSSSC.append({H[9], S[10], S[11], S[12], C[0]})

STRAIGHT_HSSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSSH.append({H[i], S[j], S[k], S[l], H[m]})
STRAIGHT_HSSSH.append({H[9], S[10], S[11], S[12], H[0]})

STRAIGHT_HSSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSSD.append({H[i], S[j], S[k], S[l], D[m]})
STRAIGHT_HSSSD.append({H[9], S[10], S[11], S[12], D[0]})

STRAIGHT_HSSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSCS.append({H[i], S[j], S[k], C[l], S[m]})
STRAIGHT_HSSCS.append({H[9], S[10], S[11], C[12], S[0]})

STRAIGHT_HSSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSCC.append({H[i], S[j], S[k], C[l], C[m]})
STRAIGHT_HSSCC.append({H[9], S[10], S[11], C[12], C[0]})

STRAIGHT_HSSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSCH.append({H[i], S[j], S[k], C[l], H[m]})
STRAIGHT_HSSCH.append({H[9], S[10], S[11], C[12], H[0]})

STRAIGHT_HSSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSCD.append({H[i], S[j], S[k], C[l], D[m]})
STRAIGHT_HSSCD.append({H[9], S[10], S[11], C[12], D[0]})

STRAIGHT_HSSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSHS.append({H[i], S[j], S[k], H[l], S[m]})
STRAIGHT_HSSHS.append({H[9], S[10], S[11], H[12], S[0]})

STRAIGHT_HSSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSHC.append({H[i], S[j], S[k], H[l], C[m]})
STRAIGHT_HSSHC.append({H[9], S[10], S[11], H[12], C[0]})

STRAIGHT_HSSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSHH.append({H[i], S[j], S[k], H[l], H[m]})
STRAIGHT_HSSHH.append({H[9], S[10], S[11], H[12], H[0]})

STRAIGHT_HSSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSHD.append({H[i], S[j], S[k], H[l], D[m]})
STRAIGHT_HSSHD.append({H[9], S[10], S[11], H[12], D[0]})

STRAIGHT_HSSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSDS.append({H[i], S[j], S[k], D[l], S[m]})
STRAIGHT_HSSDS.append({H[9], S[10], S[11], D[12], S[0]})

STRAIGHT_HSSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSDC.append({H[i], S[j], S[k], D[l], C[m]})
STRAIGHT_HSSDC.append({H[9], S[10], S[11], D[12], C[0]})

STRAIGHT_HSSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSDH.append({H[i], S[j], S[k], D[l], H[m]})
STRAIGHT_HSSDH.append({H[9], S[10], S[11], D[12], H[0]})

STRAIGHT_HSSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSSDD.append({H[i], S[j], S[k], D[l], D[m]})
STRAIGHT_HSSDD.append({H[9], S[10], S[11], D[12], D[0]})

STRAIGHT_HSCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCSS.append({H[i], S[j], C[k], S[l], S[m]})
STRAIGHT_HSCSS.append({H[9], S[10], C[11], S[12], S[0]})

STRAIGHT_HSCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCSC.append({H[i], S[j], C[k], S[l], C[m]})
STRAIGHT_HSCSC.append({H[9], S[10], C[11], S[12], C[0]})

STRAIGHT_HSCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCSH.append({H[i], S[j], C[k], S[l], H[m]})
STRAIGHT_HSCSH.append({H[9], S[10], C[11], S[12], H[0]})

STRAIGHT_HSCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCSD.append({H[i], S[j], C[k], S[l], D[m]})
STRAIGHT_HSCSD.append({H[9], S[10], C[11], S[12], D[0]})

STRAIGHT_HSCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCCS.append({H[i], S[j], C[k], C[l], S[m]})
STRAIGHT_HSCCS.append({H[9], S[10], C[11], C[12], S[0]})

STRAIGHT_HSCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCCC.append({H[i], S[j], C[k], C[l], C[m]})
STRAIGHT_HSCCC.append({H[9], S[10], C[11], C[12], C[0]})

STRAIGHT_HSCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCCH.append({H[i], S[j], C[k], C[l], H[m]})
STRAIGHT_HSCCH.append({H[9], S[10], C[11], C[12], H[0]})

STRAIGHT_HSCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCCD.append({H[i], S[j], C[k], C[l], D[m]})
STRAIGHT_HSCCD.append({H[9], S[10], C[11], C[12], D[0]})

STRAIGHT_HSCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCHS.append({H[i], S[j], C[k], H[l], S[m]})
STRAIGHT_HSCHS.append({H[9], S[10], C[11], H[12], S[0]})

STRAIGHT_HSCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCHC.append({H[i], S[j], C[k], H[l], C[m]})
STRAIGHT_HSCHC.append({H[9], S[10], C[11], H[12], C[0]})

STRAIGHT_HSCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCHH.append({H[i], S[j], C[k], H[l], H[m]})
STRAIGHT_HSCHH.append({H[9], S[10], C[11], H[12], H[0]})

STRAIGHT_HSCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCHD.append({H[i], S[j], C[k], H[l], D[m]})
STRAIGHT_HSCHD.append({H[9], S[10], C[11], H[12], D[0]})

STRAIGHT_HSCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCDS.append({H[i], S[j], C[k], D[l], S[m]})
STRAIGHT_HSCDS.append({H[9], S[10], C[11], D[12], S[0]})

STRAIGHT_HSCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCDC.append({H[i], S[j], C[k], D[l], C[m]})
STRAIGHT_HSCDC.append({H[9], S[10], C[11], D[12], C[0]})

STRAIGHT_HSCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCDH.append({H[i], S[j], C[k], D[l], H[m]})
STRAIGHT_HSCDH.append({H[9], S[10], C[11], D[12], H[0]})

STRAIGHT_HSCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSCDD.append({H[i], S[j], C[k], D[l], D[m]})
STRAIGHT_HSCDD.append({H[9], S[10], C[11], D[12], D[0]})

STRAIGHT_HSHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHSS.append({H[i], S[j], H[k], S[l], S[m]})
STRAIGHT_HSHSS.append({H[9], S[10], H[11], S[12], S[0]})

STRAIGHT_HSHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHSC.append({H[i], S[j], H[k], S[l], C[m]})
STRAIGHT_HSHSC.append({H[9], S[10], H[11], S[12], C[0]})

STRAIGHT_HSHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHSH.append({H[i], S[j], H[k], S[l], H[m]})
STRAIGHT_HSHSH.append({H[9], S[10], H[11], S[12], H[0]})

STRAIGHT_HSHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHSD.append({H[i], S[j], H[k], S[l], D[m]})
STRAIGHT_HSHSD.append({H[9], S[10], H[11], S[12], D[0]})

STRAIGHT_HSHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHCS.append({H[i], S[j], H[k], C[l], S[m]})
STRAIGHT_HSHCS.append({H[9], S[10], H[11], C[12], S[0]})

STRAIGHT_HSHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHCC.append({H[i], S[j], H[k], C[l], C[m]})
STRAIGHT_HSHCC.append({H[9], S[10], H[11], C[12], C[0]})

STRAIGHT_HSHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHCH.append({H[i], S[j], H[k], C[l], H[m]})
STRAIGHT_HSHCH.append({H[9], S[10], H[11], C[12], H[0]})

STRAIGHT_HSHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHCD.append({H[i], S[j], H[k], C[l], D[m]})
STRAIGHT_HSHCD.append({H[9], S[10], H[11], C[12], D[0]})

STRAIGHT_HSHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHHS.append({H[i], S[j], H[k], H[l], S[m]})
STRAIGHT_HSHHS.append({H[9], S[10], H[11], H[12], S[0]})

STRAIGHT_HSHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHHC.append({H[i], S[j], H[k], H[l], C[m]})
STRAIGHT_HSHHC.append({H[9], S[10], H[11], H[12], C[0]})

STRAIGHT_HSHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHHH.append({H[i], S[j], H[k], H[l], H[m]})
STRAIGHT_HSHHH.append({H[9], S[10], H[11], H[12], H[0]})

STRAIGHT_HSHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHHD.append({H[i], S[j], H[k], H[l], D[m]})
STRAIGHT_HSHHD.append({H[9], S[10], H[11], H[12], D[0]})

STRAIGHT_HSHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHDS.append({H[i], S[j], H[k], D[l], S[m]})
STRAIGHT_HSHDS.append({H[9], S[10], H[11], D[12], S[0]})

STRAIGHT_HSHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHDC.append({H[i], S[j], H[k], D[l], C[m]})
STRAIGHT_HSHDC.append({H[9], S[10], H[11], D[12], C[0]})

STRAIGHT_HSHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHDH.append({H[i], S[j], H[k], D[l], H[m]})
STRAIGHT_HSHDH.append({H[9], S[10], H[11], D[12], H[0]})

STRAIGHT_HSHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSHDD.append({H[i], S[j], H[k], D[l], D[m]})
STRAIGHT_HSHDD.append({H[9], S[10], H[11], D[12], D[0]})

STRAIGHT_HSDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDSS.append({H[i], S[j], D[k], S[l], S[m]})
STRAIGHT_HSDSS.append({H[9], S[10], D[11], S[12], S[0]})

STRAIGHT_HSDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDSC.append({H[i], S[j], D[k], S[l], C[m]})
STRAIGHT_HSDSC.append({H[9], S[10], D[11], S[12], C[0]})

STRAIGHT_HSDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDSH.append({H[i], S[j], D[k], S[l], H[m]})
STRAIGHT_HSDSH.append({H[9], S[10], D[11], S[12], H[0]})

STRAIGHT_HSDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDSD.append({H[i], S[j], D[k], S[l], D[m]})
STRAIGHT_HSDSD.append({H[9], S[10], D[11], S[12], D[0]})

STRAIGHT_HSDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDCS.append({H[i], S[j], D[k], C[l], S[m]})
STRAIGHT_HSDCS.append({H[9], S[10], D[11], C[12], S[0]})

STRAIGHT_HSDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDCC.append({H[i], S[j], D[k], C[l], C[m]})
STRAIGHT_HSDCC.append({H[9], S[10], D[11], C[12], C[0]})

STRAIGHT_HSDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDCH.append({H[i], S[j], D[k], C[l], H[m]})
STRAIGHT_HSDCH.append({H[9], S[10], D[11], C[12], H[0]})

STRAIGHT_HSDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDCD.append({H[i], S[j], D[k], C[l], D[m]})
STRAIGHT_HSDCD.append({H[9], S[10], D[11], C[12], D[0]})

STRAIGHT_HSDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDHS.append({H[i], S[j], D[k], H[l], S[m]})
STRAIGHT_HSDHS.append({H[9], S[10], D[11], H[12], S[0]})

STRAIGHT_HSDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDHC.append({H[i], S[j], D[k], H[l], C[m]})
STRAIGHT_HSDHC.append({H[9], S[10], D[11], H[12], C[0]})

STRAIGHT_HSDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDHH.append({H[i], S[j], D[k], H[l], H[m]})
STRAIGHT_HSDHH.append({H[9], S[10], D[11], H[12], H[0]})

STRAIGHT_HSDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDHD.append({H[i], S[j], D[k], H[l], D[m]})
STRAIGHT_HSDHD.append({H[9], S[10], D[11], H[12], D[0]})

STRAIGHT_HSDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDDS.append({H[i], S[j], D[k], D[l], S[m]})
STRAIGHT_HSDDS.append({H[9], S[10], D[11], D[12], S[0]})

STRAIGHT_HSDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDDC.append({H[i], S[j], D[k], D[l], C[m]})
STRAIGHT_HSDDC.append({H[9], S[10], D[11], D[12], C[0]})

STRAIGHT_HSDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDDH.append({H[i], S[j], D[k], D[l], H[m]})
STRAIGHT_HSDDH.append({H[9], S[10], D[11], D[12], H[0]})

STRAIGHT_HSDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HSDDD.append({H[i], S[j], D[k], D[l], D[m]})
STRAIGHT_HSDDD.append({H[9], S[10], D[11], D[12], D[0]})

STRAIGHT_HCSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSSS.append({H[i], C[j], S[k], S[l], S[m]})
STRAIGHT_HCSSS.append({H[9], C[10], S[11], S[12], S[0]})

STRAIGHT_HCSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSSC.append({H[i], C[j], S[k], S[l], C[m]})
STRAIGHT_HCSSC.append({H[9], C[10], S[11], S[12], C[0]})

STRAIGHT_HCSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSSH.append({H[i], C[j], S[k], S[l], H[m]})
STRAIGHT_HCSSH.append({H[9], C[10], S[11], S[12], H[0]})

STRAIGHT_HCSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSSD.append({H[i], C[j], S[k], S[l], D[m]})
STRAIGHT_HCSSD.append({H[9], C[10], S[11], S[12], D[0]})

STRAIGHT_HCSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSCS.append({H[i], C[j], S[k], C[l], S[m]})
STRAIGHT_HCSCS.append({H[9], C[10], S[11], C[12], S[0]})

STRAIGHT_HCSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSCC.append({H[i], C[j], S[k], C[l], C[m]})
STRAIGHT_HCSCC.append({H[9], C[10], S[11], C[12], C[0]})

STRAIGHT_HCSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSCH.append({H[i], C[j], S[k], C[l], H[m]})
STRAIGHT_HCSCH.append({H[9], C[10], S[11], C[12], H[0]})

STRAIGHT_HCSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSCD.append({H[i], C[j], S[k], C[l], D[m]})
STRAIGHT_HCSCD.append({H[9], C[10], S[11], C[12], D[0]})

STRAIGHT_HCSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSHS.append({H[i], C[j], S[k], H[l], S[m]})
STRAIGHT_HCSHS.append({H[9], C[10], S[11], H[12], S[0]})

STRAIGHT_HCSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSHC.append({H[i], C[j], S[k], H[l], C[m]})
STRAIGHT_HCSHC.append({H[9], C[10], S[11], H[12], C[0]})

STRAIGHT_HCSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSHH.append({H[i], C[j], S[k], H[l], H[m]})
STRAIGHT_HCSHH.append({H[9], C[10], S[11], H[12], H[0]})

STRAIGHT_HCSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSHD.append({H[i], C[j], S[k], H[l], D[m]})
STRAIGHT_HCSHD.append({H[9], C[10], S[11], H[12], D[0]})

STRAIGHT_HCSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSDS.append({H[i], C[j], S[k], D[l], S[m]})
STRAIGHT_HCSDS.append({H[9], C[10], S[11], D[12], S[0]})

STRAIGHT_HCSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSDC.append({H[i], C[j], S[k], D[l], C[m]})
STRAIGHT_HCSDC.append({H[9], C[10], S[11], D[12], C[0]})

STRAIGHT_HCSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSDH.append({H[i], C[j], S[k], D[l], H[m]})
STRAIGHT_HCSDH.append({H[9], C[10], S[11], D[12], H[0]})

STRAIGHT_HCSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCSDD.append({H[i], C[j], S[k], D[l], D[m]})
STRAIGHT_HCSDD.append({H[9], C[10], S[11], D[12], D[0]})

STRAIGHT_HCCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCSS.append({H[i], C[j], C[k], S[l], S[m]})
STRAIGHT_HCCSS.append({H[9], C[10], C[11], S[12], S[0]})

STRAIGHT_HCCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCSC.append({H[i], C[j], C[k], S[l], C[m]})
STRAIGHT_HCCSC.append({H[9], C[10], C[11], S[12], C[0]})

STRAIGHT_HCCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCSH.append({H[i], C[j], C[k], S[l], H[m]})
STRAIGHT_HCCSH.append({H[9], C[10], C[11], S[12], H[0]})

STRAIGHT_HCCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCSD.append({H[i], C[j], C[k], S[l], D[m]})
STRAIGHT_HCCSD.append({H[9], C[10], C[11], S[12], D[0]})

STRAIGHT_HCCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCCS.append({H[i], C[j], C[k], C[l], S[m]})
STRAIGHT_HCCCS.append({H[9], C[10], C[11], C[12], S[0]})

STRAIGHT_HCCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCCC.append({H[i], C[j], C[k], C[l], C[m]})
STRAIGHT_HCCCC.append({H[9], C[10], C[11], C[12], C[0]})

STRAIGHT_HCCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCCH.append({H[i], C[j], C[k], C[l], H[m]})
STRAIGHT_HCCCH.append({H[9], C[10], C[11], C[12], H[0]})

STRAIGHT_HCCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCCD.append({H[i], C[j], C[k], C[l], D[m]})
STRAIGHT_HCCCD.append({H[9], C[10], C[11], C[12], D[0]})

STRAIGHT_HCCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCHS.append({H[i], C[j], C[k], H[l], S[m]})
STRAIGHT_HCCHS.append({H[9], C[10], C[11], H[12], S[0]})

STRAIGHT_HCCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCHC.append({H[i], C[j], C[k], H[l], C[m]})
STRAIGHT_HCCHC.append({H[9], C[10], C[11], H[12], C[0]})

STRAIGHT_HCCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCHH.append({H[i], C[j], C[k], H[l], H[m]})
STRAIGHT_HCCHH.append({H[9], C[10], C[11], H[12], H[0]})

STRAIGHT_HCCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCHD.append({H[i], C[j], C[k], H[l], D[m]})
STRAIGHT_HCCHD.append({H[9], C[10], C[11], H[12], D[0]})

STRAIGHT_HCCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCDS.append({H[i], C[j], C[k], D[l], S[m]})
STRAIGHT_HCCDS.append({H[9], C[10], C[11], D[12], S[0]})

STRAIGHT_HCCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCDC.append({H[i], C[j], C[k], D[l], C[m]})
STRAIGHT_HCCDC.append({H[9], C[10], C[11], D[12], C[0]})

STRAIGHT_HCCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCDH.append({H[i], C[j], C[k], D[l], H[m]})
STRAIGHT_HCCDH.append({H[9], C[10], C[11], D[12], H[0]})

STRAIGHT_HCCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCCDD.append({H[i], C[j], C[k], D[l], D[m]})
STRAIGHT_HCCDD.append({H[9], C[10], C[11], D[12], D[0]})

STRAIGHT_HCHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHSS.append({H[i], C[j], H[k], S[l], S[m]})
STRAIGHT_HCHSS.append({H[9], C[10], H[11], S[12], S[0]})

STRAIGHT_HCHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHSC.append({H[i], C[j], H[k], S[l], C[m]})
STRAIGHT_HCHSC.append({H[9], C[10], H[11], S[12], C[0]})

STRAIGHT_HCHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHSH.append({H[i], C[j], H[k], S[l], H[m]})
STRAIGHT_HCHSH.append({H[9], C[10], H[11], S[12], H[0]})

STRAIGHT_HCHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHSD.append({H[i], C[j], H[k], S[l], D[m]})
STRAIGHT_HCHSD.append({H[9], C[10], H[11], S[12], D[0]})

STRAIGHT_HCHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHCS.append({H[i], C[j], H[k], C[l], S[m]})
STRAIGHT_HCHCS.append({H[9], C[10], H[11], C[12], S[0]})

STRAIGHT_HCHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHCC.append({H[i], C[j], H[k], C[l], C[m]})
STRAIGHT_HCHCC.append({H[9], C[10], H[11], C[12], C[0]})

STRAIGHT_HCHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHCH.append({H[i], C[j], H[k], C[l], H[m]})
STRAIGHT_HCHCH.append({H[9], C[10], H[11], C[12], H[0]})

STRAIGHT_HCHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHCD.append({H[i], C[j], H[k], C[l], D[m]})
STRAIGHT_HCHCD.append({H[9], C[10], H[11], C[12], D[0]})

STRAIGHT_HCHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHHS.append({H[i], C[j], H[k], H[l], S[m]})
STRAIGHT_HCHHS.append({H[9], C[10], H[11], H[12], S[0]})

STRAIGHT_HCHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHHC.append({H[i], C[j], H[k], H[l], C[m]})
STRAIGHT_HCHHC.append({H[9], C[10], H[11], H[12], C[0]})

STRAIGHT_HCHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHHH.append({H[i], C[j], H[k], H[l], H[m]})
STRAIGHT_HCHHH.append({H[9], C[10], H[11], H[12], H[0]})

STRAIGHT_HCHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHHD.append({H[i], C[j], H[k], H[l], D[m]})
STRAIGHT_HCHHD.append({H[9], C[10], H[11], H[12], D[0]})

STRAIGHT_HCHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHDS.append({H[i], C[j], H[k], D[l], S[m]})
STRAIGHT_HCHDS.append({H[9], C[10], H[11], D[12], S[0]})

STRAIGHT_HCHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHDC.append({H[i], C[j], H[k], D[l], C[m]})
STRAIGHT_HCHDC.append({H[9], C[10], H[11], D[12], C[0]})

STRAIGHT_HCHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHDH.append({H[i], C[j], H[k], D[l], H[m]})
STRAIGHT_HCHDH.append({H[9], C[10], H[11], D[12], H[0]})

STRAIGHT_HCHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCHDD.append({H[i], C[j], H[k], D[l], D[m]})
STRAIGHT_HCHDD.append({H[9], C[10], H[11], D[12], D[0]})

STRAIGHT_HCDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDSS.append({H[i], C[j], D[k], S[l], S[m]})
STRAIGHT_HCDSS.append({H[9], C[10], D[11], S[12], S[0]})

STRAIGHT_HCDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDSC.append({H[i], C[j], D[k], S[l], C[m]})
STRAIGHT_HCDSC.append({H[9], C[10], D[11], S[12], C[0]})

STRAIGHT_HCDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDSH.append({H[i], C[j], D[k], S[l], H[m]})
STRAIGHT_HCDSH.append({H[9], C[10], D[11], S[12], H[0]})

STRAIGHT_HCDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDSD.append({H[i], C[j], D[k], S[l], D[m]})
STRAIGHT_HCDSD.append({H[9], C[10], D[11], S[12], D[0]})

STRAIGHT_HCDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDCS.append({H[i], C[j], D[k], C[l], S[m]})
STRAIGHT_HCDCS.append({H[9], C[10], D[11], C[12], S[0]})

STRAIGHT_HCDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDCC.append({H[i], C[j], D[k], C[l], C[m]})
STRAIGHT_HCDCC.append({H[9], C[10], D[11], C[12], C[0]})

STRAIGHT_HCDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDCH.append({H[i], C[j], D[k], C[l], H[m]})
STRAIGHT_HCDCH.append({H[9], C[10], D[11], C[12], H[0]})

STRAIGHT_HCDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDCD.append({H[i], C[j], D[k], C[l], D[m]})
STRAIGHT_HCDCD.append({H[9], C[10], D[11], C[12], D[0]})

STRAIGHT_HCDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDHS.append({H[i], C[j], D[k], H[l], S[m]})
STRAIGHT_HCDHS.append({H[9], C[10], D[11], H[12], S[0]})

STRAIGHT_HCDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDHC.append({H[i], C[j], D[k], H[l], C[m]})
STRAIGHT_HCDHC.append({H[9], C[10], D[11], H[12], C[0]})

STRAIGHT_HCDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDHH.append({H[i], C[j], D[k], H[l], H[m]})
STRAIGHT_HCDHH.append({H[9], C[10], D[11], H[12], H[0]})

STRAIGHT_HCDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDHD.append({H[i], C[j], D[k], H[l], D[m]})
STRAIGHT_HCDHD.append({H[9], C[10], D[11], H[12], D[0]})

STRAIGHT_HCDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDDS.append({H[i], C[j], D[k], D[l], S[m]})
STRAIGHT_HCDDS.append({H[9], C[10], D[11], D[12], S[0]})

STRAIGHT_HCDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDDC.append({H[i], C[j], D[k], D[l], C[m]})
STRAIGHT_HCDDC.append({H[9], C[10], D[11], D[12], C[0]})

STRAIGHT_HCDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDDH.append({H[i], C[j], D[k], D[l], H[m]})
STRAIGHT_HCDDH.append({H[9], C[10], D[11], D[12], H[0]})

STRAIGHT_HCDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HCDDD.append({H[i], C[j], D[k], D[l], D[m]})
STRAIGHT_HCDDD.append({H[9], C[10], D[11], D[12], D[0]})

STRAIGHT_HHSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSSS.append({H[i], H[j], S[k], S[l], S[m]})
STRAIGHT_HHSSS.append({H[9], H[10], S[11], S[12], S[0]})

STRAIGHT_HHSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSSC.append({H[i], H[j], S[k], S[l], C[m]})
STRAIGHT_HHSSC.append({H[9], H[10], S[11], S[12], C[0]})

STRAIGHT_HHSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSSH.append({H[i], H[j], S[k], S[l], H[m]})
STRAIGHT_HHSSH.append({H[9], H[10], S[11], S[12], H[0]})

STRAIGHT_HHSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSSD.append({H[i], H[j], S[k], S[l], D[m]})
STRAIGHT_HHSSD.append({H[9], H[10], S[11], S[12], D[0]})

STRAIGHT_HHSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSCS.append({H[i], H[j], S[k], C[l], S[m]})
STRAIGHT_HHSCS.append({H[9], H[10], S[11], C[12], S[0]})

STRAIGHT_HHSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSCC.append({H[i], H[j], S[k], C[l], C[m]})
STRAIGHT_HHSCC.append({H[9], H[10], S[11], C[12], C[0]})

STRAIGHT_HHSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSCH.append({H[i], H[j], S[k], C[l], H[m]})
STRAIGHT_HHSCH.append({H[9], H[10], S[11], C[12], H[0]})

STRAIGHT_HHSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSCD.append({H[i], H[j], S[k], C[l], D[m]})
STRAIGHT_HHSCD.append({H[9], H[10], S[11], C[12], D[0]})

STRAIGHT_HHSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSHS.append({H[i], H[j], S[k], H[l], S[m]})
STRAIGHT_HHSHS.append({H[9], H[10], S[11], H[12], S[0]})

STRAIGHT_HHSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSHC.append({H[i], H[j], S[k], H[l], C[m]})
STRAIGHT_HHSHC.append({H[9], H[10], S[11], H[12], C[0]})

STRAIGHT_HHSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSHH.append({H[i], H[j], S[k], H[l], H[m]})
STRAIGHT_HHSHH.append({H[9], H[10], S[11], H[12], H[0]})

STRAIGHT_HHSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSHD.append({H[i], H[j], S[k], H[l], D[m]})
STRAIGHT_HHSHD.append({H[9], H[10], S[11], H[12], D[0]})

STRAIGHT_HHSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSDS.append({H[i], H[j], S[k], D[l], S[m]})
STRAIGHT_HHSDS.append({H[9], H[10], S[11], D[12], S[0]})

STRAIGHT_HHSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSDC.append({H[i], H[j], S[k], D[l], C[m]})
STRAIGHT_HHSDC.append({H[9], H[10], S[11], D[12], C[0]})

STRAIGHT_HHSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSDH.append({H[i], H[j], S[k], D[l], H[m]})
STRAIGHT_HHSDH.append({H[9], H[10], S[11], D[12], H[0]})

STRAIGHT_HHSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHSDD.append({H[i], H[j], S[k], D[l], D[m]})
STRAIGHT_HHSDD.append({H[9], H[10], S[11], D[12], D[0]})

STRAIGHT_HHCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCSS.append({H[i], H[j], C[k], S[l], S[m]})
STRAIGHT_HHCSS.append({H[9], H[10], C[11], S[12], S[0]})

STRAIGHT_HHCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCSC.append({H[i], H[j], C[k], S[l], C[m]})
STRAIGHT_HHCSC.append({H[9], H[10], C[11], S[12], C[0]})

STRAIGHT_HHCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCSH.append({H[i], H[j], C[k], S[l], H[m]})
STRAIGHT_HHCSH.append({H[9], H[10], C[11], S[12], H[0]})

STRAIGHT_HHCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCSD.append({H[i], H[j], C[k], S[l], D[m]})
STRAIGHT_HHCSD.append({H[9], H[10], C[11], S[12], D[0]})

STRAIGHT_HHCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCCS.append({H[i], H[j], C[k], C[l], S[m]})
STRAIGHT_HHCCS.append({H[9], H[10], C[11], C[12], S[0]})

STRAIGHT_HHCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCCC.append({H[i], H[j], C[k], C[l], C[m]})
STRAIGHT_HHCCC.append({H[9], H[10], C[11], C[12], C[0]})

STRAIGHT_HHCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCCH.append({H[i], H[j], C[k], C[l], H[m]})
STRAIGHT_HHCCH.append({H[9], H[10], C[11], C[12], H[0]})

STRAIGHT_HHCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCCD.append({H[i], H[j], C[k], C[l], D[m]})
STRAIGHT_HHCCD.append({H[9], H[10], C[11], C[12], D[0]})

STRAIGHT_HHCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCHS.append({H[i], H[j], C[k], H[l], S[m]})
STRAIGHT_HHCHS.append({H[9], H[10], C[11], H[12], S[0]})

STRAIGHT_HHCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCHC.append({H[i], H[j], C[k], H[l], C[m]})
STRAIGHT_HHCHC.append({H[9], H[10], C[11], H[12], C[0]})

STRAIGHT_HHCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCHH.append({H[i], H[j], C[k], H[l], H[m]})
STRAIGHT_HHCHH.append({H[9], H[10], C[11], H[12], H[0]})

STRAIGHT_HHCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCHD.append({H[i], H[j], C[k], H[l], D[m]})
STRAIGHT_HHCHD.append({H[9], H[10], C[11], H[12], D[0]})

STRAIGHT_HHCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCDS.append({H[i], H[j], C[k], D[l], S[m]})
STRAIGHT_HHCDS.append({H[9], H[10], C[11], D[12], S[0]})

STRAIGHT_HHCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCDC.append({H[i], H[j], C[k], D[l], C[m]})
STRAIGHT_HHCDC.append({H[9], H[10], C[11], D[12], C[0]})

STRAIGHT_HHCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCDH.append({H[i], H[j], C[k], D[l], H[m]})
STRAIGHT_HHCDH.append({H[9], H[10], C[11], D[12], H[0]})

STRAIGHT_HHCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHCDD.append({H[i], H[j], C[k], D[l], D[m]})
STRAIGHT_HHCDD.append({H[9], H[10], C[11], D[12], D[0]})

STRAIGHT_HHHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHSS.append({H[i], H[j], H[k], S[l], S[m]})
STRAIGHT_HHHSS.append({H[9], H[10], H[11], S[12], S[0]})

STRAIGHT_HHHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHSC.append({H[i], H[j], H[k], S[l], C[m]})
STRAIGHT_HHHSC.append({H[9], H[10], H[11], S[12], C[0]})

STRAIGHT_HHHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHSH.append({H[i], H[j], H[k], S[l], H[m]})
STRAIGHT_HHHSH.append({H[9], H[10], H[11], S[12], H[0]})

STRAIGHT_HHHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHSD.append({H[i], H[j], H[k], S[l], D[m]})
STRAIGHT_HHHSD.append({H[9], H[10], H[11], S[12], D[0]})

STRAIGHT_HHHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHCS.append({H[i], H[j], H[k], C[l], S[m]})
STRAIGHT_HHHCS.append({H[9], H[10], H[11], C[12], S[0]})

STRAIGHT_HHHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHCC.append({H[i], H[j], H[k], C[l], C[m]})
STRAIGHT_HHHCC.append({H[9], H[10], H[11], C[12], C[0]})

STRAIGHT_HHHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHCH.append({H[i], H[j], H[k], C[l], H[m]})
STRAIGHT_HHHCH.append({H[9], H[10], H[11], C[12], H[0]})

STRAIGHT_HHHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHCD.append({H[i], H[j], H[k], C[l], D[m]})
STRAIGHT_HHHCD.append({H[9], H[10], H[11], C[12], D[0]})

STRAIGHT_HHHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHHS.append({H[i], H[j], H[k], H[l], S[m]})
STRAIGHT_HHHHS.append({H[9], H[10], H[11], H[12], S[0]})

STRAIGHT_HHHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHHC.append({H[i], H[j], H[k], H[l], C[m]})
STRAIGHT_HHHHC.append({H[9], H[10], H[11], H[12], C[0]})

STRAIGHT_HHHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHHD.append({H[i], H[j], H[k], H[l], D[m]})
STRAIGHT_HHHHD.append({H[9], H[10], H[11], H[12], D[0]})

STRAIGHT_HHHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHDS.append({H[i], H[j], H[k], D[l], S[m]})
STRAIGHT_HHHDS.append({H[9], H[10], H[11], D[12], S[0]})

STRAIGHT_HHHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHDC.append({H[i], H[j], H[k], D[l], C[m]})
STRAIGHT_HHHDC.append({H[9], H[10], H[11], D[12], C[0]})

STRAIGHT_HHHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHDH.append({H[i], H[j], H[k], D[l], H[m]})
STRAIGHT_HHHDH.append({H[9], H[10], H[11], D[12], H[0]})

STRAIGHT_HHHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHHDD.append({H[i], H[j], H[k], D[l], D[m]})
STRAIGHT_HHHDD.append({H[9], H[10], H[11], D[12], D[0]})

STRAIGHT_HHDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDSS.append({H[i], H[j], D[k], S[l], S[m]})
STRAIGHT_HHDSS.append({H[9], H[10], D[11], S[12], S[0]})

STRAIGHT_HHDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDSC.append({H[i], H[j], D[k], S[l], C[m]})
STRAIGHT_HHDSC.append({H[9], H[10], D[11], S[12], C[0]})

STRAIGHT_HHDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDSH.append({H[i], H[j], D[k], S[l], H[m]})
STRAIGHT_HHDSH.append({H[9], H[10], D[11], S[12], H[0]})

STRAIGHT_HHDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDSD.append({H[i], H[j], D[k], S[l], D[m]})
STRAIGHT_HHDSD.append({H[9], H[10], D[11], S[12], D[0]})

STRAIGHT_HHDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDCS.append({H[i], H[j], D[k], C[l], S[m]})
STRAIGHT_HHDCS.append({H[9], H[10], D[11], C[12], S[0]})

STRAIGHT_HHDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDCC.append({H[i], H[j], D[k], C[l], C[m]})
STRAIGHT_HHDCC.append({H[9], H[10], D[11], C[12], C[0]})

STRAIGHT_HHDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDCH.append({H[i], H[j], D[k], C[l], H[m]})
STRAIGHT_HHDCH.append({H[9], H[10], D[11], C[12], H[0]})

STRAIGHT_HHDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDCD.append({H[i], H[j], D[k], C[l], D[m]})
STRAIGHT_HHDCD.append({H[9], H[10], D[11], C[12], D[0]})

STRAIGHT_HHDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDHS.append({H[i], H[j], D[k], H[l], S[m]})
STRAIGHT_HHDHS.append({H[9], H[10], D[11], H[12], S[0]})

STRAIGHT_HHDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDHC.append({H[i], H[j], D[k], H[l], C[m]})
STRAIGHT_HHDHC.append({H[9], H[10], D[11], H[12], C[0]})

STRAIGHT_HHDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDHH.append({H[i], H[j], D[k], H[l], H[m]})
STRAIGHT_HHDHH.append({H[9], H[10], D[11], H[12], H[0]})

STRAIGHT_HHDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDHD.append({H[i], H[j], D[k], H[l], D[m]})
STRAIGHT_HHDHD.append({H[9], H[10], D[11], H[12], D[0]})

STRAIGHT_HHDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDDS.append({H[i], H[j], D[k], D[l], S[m]})
STRAIGHT_HHDDS.append({H[9], H[10], D[11], D[12], S[0]})

STRAIGHT_HHDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDDC.append({H[i], H[j], D[k], D[l], C[m]})
STRAIGHT_HHDDC.append({H[9], H[10], D[11], D[12], C[0]})

STRAIGHT_HHDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDDH.append({H[i], H[j], D[k], D[l], H[m]})
STRAIGHT_HHDDH.append({H[9], H[10], D[11], D[12], H[0]})

STRAIGHT_HHDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HHDDD.append({H[i], H[j], D[k], D[l], D[m]})
STRAIGHT_HHDDD.append({H[9], H[10], D[11], D[12], D[0]})

STRAIGHT_HDSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSSS.append({H[i], D[j], S[k], S[l], S[m]})
STRAIGHT_HDSSS.append({H[9], D[10], S[11], S[12], S[0]})

STRAIGHT_HDSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSSC.append({H[i], D[j], S[k], S[l], C[m]})
STRAIGHT_HDSSC.append({H[9], D[10], S[11], S[12], C[0]})

STRAIGHT_HDSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSSH.append({H[i], D[j], S[k], S[l], H[m]})
STRAIGHT_HDSSH.append({H[9], D[10], S[11], S[12], H[0]})

STRAIGHT_HDSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSSD.append({H[i], D[j], S[k], S[l], D[m]})
STRAIGHT_HDSSD.append({H[9], D[10], S[11], S[12], D[0]})

STRAIGHT_HDSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSCS.append({H[i], D[j], S[k], C[l], S[m]})
STRAIGHT_HDSCS.append({H[9], D[10], S[11], C[12], S[0]})

STRAIGHT_HDSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSCC.append({H[i], D[j], S[k], C[l], C[m]})
STRAIGHT_HDSCC.append({H[9], D[10], S[11], C[12], C[0]})

STRAIGHT_HDSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSCH.append({H[i], D[j], S[k], C[l], H[m]})
STRAIGHT_HDSCH.append({H[9], D[10], S[11], C[12], H[0]})

STRAIGHT_HDSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSCD.append({H[i], D[j], S[k], C[l], D[m]})
STRAIGHT_HDSCD.append({H[9], D[10], S[11], C[12], D[0]})

STRAIGHT_HDSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSHS.append({H[i], D[j], S[k], H[l], S[m]})
STRAIGHT_HDSHS.append({H[9], D[10], S[11], H[12], S[0]})

STRAIGHT_HDSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSHC.append({H[i], D[j], S[k], H[l], C[m]})
STRAIGHT_HDSHC.append({H[9], D[10], S[11], H[12], C[0]})

STRAIGHT_HDSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSHH.append({H[i], D[j], S[k], H[l], H[m]})
STRAIGHT_HDSHH.append({H[9], D[10], S[11], H[12], H[0]})

STRAIGHT_HDSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSHD.append({H[i], D[j], S[k], H[l], D[m]})
STRAIGHT_HDSHD.append({H[9], D[10], S[11], H[12], D[0]})

STRAIGHT_HDSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSDS.append({H[i], D[j], S[k], D[l], S[m]})
STRAIGHT_HDSDS.append({H[9], D[10], S[11], D[12], S[0]})

STRAIGHT_HDSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSDC.append({H[i], D[j], S[k], D[l], C[m]})
STRAIGHT_HDSDC.append({H[9], D[10], S[11], D[12], C[0]})

STRAIGHT_HDSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSDH.append({H[i], D[j], S[k], D[l], H[m]})
STRAIGHT_HDSDH.append({H[9], D[10], S[11], D[12], H[0]})

STRAIGHT_HDSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDSDD.append({H[i], D[j], S[k], D[l], D[m]})
STRAIGHT_HDSDD.append({H[9], D[10], S[11], D[12], D[0]})

STRAIGHT_HDCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCSS.append({H[i], D[j], C[k], S[l], S[m]})
STRAIGHT_HDCSS.append({H[9], D[10], C[11], S[12], S[0]})

STRAIGHT_HDCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCSC.append({H[i], D[j], C[k], S[l], C[m]})
STRAIGHT_HDCSC.append({H[9], D[10], C[11], S[12], C[0]})

STRAIGHT_HDCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCSH.append({H[i], D[j], C[k], S[l], H[m]})
STRAIGHT_HDCSH.append({H[9], D[10], C[11], S[12], H[0]})

STRAIGHT_HDCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCSD.append({H[i], D[j], C[k], S[l], D[m]})
STRAIGHT_HDCSD.append({H[9], D[10], C[11], S[12], D[0]})

STRAIGHT_HDCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCCS.append({H[i], D[j], C[k], C[l], S[m]})
STRAIGHT_HDCCS.append({H[9], D[10], C[11], C[12], S[0]})

STRAIGHT_HDCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCCC.append({H[i], D[j], C[k], C[l], C[m]})
STRAIGHT_HDCCC.append({H[9], D[10], C[11], C[12], C[0]})

STRAIGHT_HDCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCCH.append({H[i], D[j], C[k], C[l], H[m]})
STRAIGHT_HDCCH.append({H[9], D[10], C[11], C[12], H[0]})

STRAIGHT_HDCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCCD.append({H[i], D[j], C[k], C[l], D[m]})
STRAIGHT_HDCCD.append({H[9], D[10], C[11], C[12], D[0]})

STRAIGHT_HDCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCHS.append({H[i], D[j], C[k], H[l], S[m]})
STRAIGHT_HDCHS.append({H[9], D[10], C[11], H[12], S[0]})

STRAIGHT_HDCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCHC.append({H[i], D[j], C[k], H[l], C[m]})
STRAIGHT_HDCHC.append({H[9], D[10], C[11], H[12], C[0]})

STRAIGHT_HDCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCHH.append({H[i], D[j], C[k], H[l], H[m]})
STRAIGHT_HDCHH.append({H[9], D[10], C[11], H[12], H[0]})

STRAIGHT_HDCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCHD.append({H[i], D[j], C[k], H[l], D[m]})
STRAIGHT_HDCHD.append({H[9], D[10], C[11], H[12], D[0]})

STRAIGHT_HDCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCDS.append({H[i], D[j], C[k], D[l], S[m]})
STRAIGHT_HDCDS.append({H[9], D[10], C[11], D[12], S[0]})

STRAIGHT_HDCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCDC.append({H[i], D[j], C[k], D[l], C[m]})
STRAIGHT_HDCDC.append({H[9], D[10], C[11], D[12], C[0]})

STRAIGHT_HDCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCDH.append({H[i], D[j], C[k], D[l], H[m]})
STRAIGHT_HDCDH.append({H[9], D[10], C[11], D[12], H[0]})

STRAIGHT_HDCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDCDD.append({H[i], D[j], C[k], D[l], D[m]})
STRAIGHT_HDCDD.append({H[9], D[10], C[11], D[12], D[0]})

STRAIGHT_HDHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHSS.append({H[i], D[j], H[k], S[l], S[m]})
STRAIGHT_HDHSS.append({H[9], D[10], H[11], S[12], S[0]})

STRAIGHT_HDHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHSC.append({H[i], D[j], H[k], S[l], C[m]})
STRAIGHT_HDHSC.append({H[9], D[10], H[11], S[12], C[0]})

STRAIGHT_HDHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHSH.append({H[i], D[j], H[k], S[l], H[m]})
STRAIGHT_HDHSH.append({H[9], D[10], H[11], S[12], H[0]})

STRAIGHT_HDHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHSD.append({H[i], D[j], H[k], S[l], D[m]})
STRAIGHT_HDHSD.append({H[9], D[10], H[11], S[12], D[0]})

STRAIGHT_HDHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHCS.append({H[i], D[j], H[k], C[l], S[m]})
STRAIGHT_HDHCS.append({H[9], D[10], H[11], C[12], S[0]})

STRAIGHT_HDHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHCC.append({H[i], D[j], H[k], C[l], C[m]})
STRAIGHT_HDHCC.append({H[9], D[10], H[11], C[12], C[0]})

STRAIGHT_HDHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHCH.append({H[i], D[j], H[k], C[l], H[m]})
STRAIGHT_HDHCH.append({H[9], D[10], H[11], C[12], H[0]})

STRAIGHT_HDHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHCD.append({H[i], D[j], H[k], C[l], D[m]})
STRAIGHT_HDHCD.append({H[9], D[10], H[11], C[12], D[0]})

STRAIGHT_HDHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHHS.append({H[i], D[j], H[k], H[l], S[m]})
STRAIGHT_HDHHS.append({H[9], D[10], H[11], H[12], S[0]})

STRAIGHT_HDHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHHC.append({H[i], D[j], H[k], H[l], C[m]})
STRAIGHT_HDHHC.append({H[9], D[10], H[11], H[12], C[0]})

STRAIGHT_HDHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHHH.append({H[i], D[j], H[k], H[l], H[m]})
STRAIGHT_HDHHH.append({H[9], D[10], H[11], H[12], H[0]})

STRAIGHT_HDHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHHD.append({H[i], D[j], H[k], H[l], D[m]})
STRAIGHT_HDHHD.append({H[9], D[10], H[11], H[12], D[0]})

STRAIGHT_HDHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHDS.append({H[i], D[j], H[k], D[l], S[m]})
STRAIGHT_HDHDS.append({H[9], D[10], H[11], D[12], S[0]})

STRAIGHT_HDHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHDC.append({H[i], D[j], H[k], D[l], C[m]})
STRAIGHT_HDHDC.append({H[9], D[10], H[11], D[12], C[0]})

STRAIGHT_HDHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHDH.append({H[i], D[j], H[k], D[l], H[m]})
STRAIGHT_HDHDH.append({H[9], D[10], H[11], D[12], H[0]})

STRAIGHT_HDHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDHDD.append({H[i], D[j], H[k], D[l], D[m]})
STRAIGHT_HDHDD.append({H[9], D[10], H[11], D[12], D[0]})

STRAIGHT_HDDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDSS.append({H[i], D[j], D[k], S[l], S[m]})
STRAIGHT_HDDSS.append({H[9], D[10], D[11], S[12], S[0]})

STRAIGHT_HDDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDSC.append({H[i], D[j], D[k], S[l], C[m]})
STRAIGHT_HDDSC.append({H[9], D[10], D[11], S[12], C[0]})

STRAIGHT_HDDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDSH.append({H[i], D[j], D[k], S[l], H[m]})
STRAIGHT_HDDSH.append({H[9], D[10], D[11], S[12], H[0]})

STRAIGHT_HDDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDSD.append({H[i], D[j], D[k], S[l], D[m]})
STRAIGHT_HDDSD.append({H[9], D[10], D[11], S[12], D[0]})

STRAIGHT_HDDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDCS.append({H[i], D[j], D[k], C[l], S[m]})
STRAIGHT_HDDCS.append({H[9], D[10], D[11], C[12], S[0]})

STRAIGHT_HDDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDCC.append({H[i], D[j], D[k], C[l], C[m]})
STRAIGHT_HDDCC.append({H[9], D[10], D[11], C[12], C[0]})

STRAIGHT_HDDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDCH.append({H[i], D[j], D[k], C[l], H[m]})
STRAIGHT_HDDCH.append({H[9], D[10], D[11], C[12], H[0]})

STRAIGHT_HDDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDCD.append({H[i], D[j], D[k], C[l], D[m]})
STRAIGHT_HDDCD.append({H[9], D[10], D[11], C[12], D[0]})

STRAIGHT_HDDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDHS.append({H[i], D[j], D[k], H[l], S[m]})
STRAIGHT_HDDHS.append({H[9], D[10], D[11], H[12], S[0]})

STRAIGHT_HDDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDHC.append({H[i], D[j], D[k], H[l], C[m]})
STRAIGHT_HDDHC.append({H[9], D[10], D[11], H[12], C[0]})

STRAIGHT_HDDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDHH.append({H[i], D[j], D[k], H[l], H[m]})
STRAIGHT_HDDHH.append({H[9], D[10], D[11], H[12], H[0]})

STRAIGHT_HDDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDHD.append({H[i], D[j], D[k], H[l], D[m]})
STRAIGHT_HDDHD.append({H[9], D[10], D[11], H[12], D[0]})

STRAIGHT_HDDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDDS.append({H[i], D[j], D[k], D[l], S[m]})
STRAIGHT_HDDDS.append({H[9], D[10], D[11], D[12], S[0]})

STRAIGHT_HDDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDDC.append({H[i], D[j], D[k], D[l], C[m]})
STRAIGHT_HDDDC.append({H[9], D[10], D[11], D[12], C[0]})

STRAIGHT_HDDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDDH.append({H[i], D[j], D[k], D[l], H[m]})
STRAIGHT_HDDDH.append({H[9], D[10], D[11], D[12], H[0]})

STRAIGHT_HDDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_HDDDD.append({H[i], D[j], D[k], D[l], D[m]})
STRAIGHT_HDDDD.append({H[9], D[10], D[11], D[12], D[0]})

STRAIGHT_DSSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSSS.append({D[i], S[j], S[k], S[l], S[m]})
STRAIGHT_DSSSS.append({D[9], S[10], S[11], S[12], S[0]})

STRAIGHT_DSSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSSC.append({D[i], S[j], S[k], S[l], C[m]})
STRAIGHT_DSSSC.append({D[9], S[10], S[11], S[12], C[0]})

STRAIGHT_DSSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSSH.append({D[i], S[j], S[k], S[l], H[m]})
STRAIGHT_DSSSH.append({D[9], S[10], S[11], S[12], H[0]})

STRAIGHT_DSSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSSD.append({D[i], S[j], S[k], S[l], D[m]})
STRAIGHT_DSSSD.append({D[9], S[10], S[11], S[12], D[0]})

STRAIGHT_DSSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSCS.append({D[i], S[j], S[k], C[l], S[m]})
STRAIGHT_DSSCS.append({D[9], S[10], S[11], C[12], S[0]})

STRAIGHT_DSSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSCC.append({D[i], S[j], S[k], C[l], C[m]})
STRAIGHT_DSSCC.append({D[9], S[10], S[11], C[12], C[0]})

STRAIGHT_DSSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSCH.append({D[i], S[j], S[k], C[l], H[m]})
STRAIGHT_DSSCH.append({D[9], S[10], S[11], C[12], H[0]})

STRAIGHT_DSSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSCD.append({D[i], S[j], S[k], C[l], D[m]})
STRAIGHT_DSSCD.append({D[9], S[10], S[11], C[12], D[0]})

STRAIGHT_DSSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSHS.append({D[i], S[j], S[k], H[l], S[m]})
STRAIGHT_DSSHS.append({D[9], S[10], S[11], H[12], S[0]})

STRAIGHT_DSSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSHC.append({D[i], S[j], S[k], H[l], C[m]})
STRAIGHT_DSSHC.append({D[9], S[10], S[11], H[12], C[0]})

STRAIGHT_DSSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSHH.append({D[i], S[j], S[k], H[l], H[m]})
STRAIGHT_DSSHH.append({D[9], S[10], S[11], H[12], H[0]})

STRAIGHT_DSSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSHD.append({D[i], S[j], S[k], H[l], D[m]})
STRAIGHT_DSSHD.append({D[9], S[10], S[11], H[12], D[0]})

STRAIGHT_DSSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSDS.append({D[i], S[j], S[k], D[l], S[m]})
STRAIGHT_DSSDS.append({D[9], S[10], S[11], D[12], S[0]})

STRAIGHT_DSSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSDC.append({D[i], S[j], S[k], D[l], C[m]})
STRAIGHT_DSSDC.append({D[9], S[10], S[11], D[12], C[0]})

STRAIGHT_DSSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSDH.append({D[i], S[j], S[k], D[l], H[m]})
STRAIGHT_DSSDH.append({D[9], S[10], S[11], D[12], H[0]})

STRAIGHT_DSSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSSDD.append({D[i], S[j], S[k], D[l], D[m]})
STRAIGHT_DSSDD.append({D[9], S[10], S[11], D[12], D[0]})

STRAIGHT_DSCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCSS.append({D[i], S[j], C[k], S[l], S[m]})
STRAIGHT_DSCSS.append({D[9], S[10], C[11], S[12], S[0]})

STRAIGHT_DSCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCSC.append({D[i], S[j], C[k], S[l], C[m]})
STRAIGHT_DSCSC.append({D[9], S[10], C[11], S[12], C[0]})

STRAIGHT_DSCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCSH.append({D[i], S[j], C[k], S[l], H[m]})
STRAIGHT_DSCSH.append({D[9], S[10], C[11], S[12], H[0]})

STRAIGHT_DSCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCSD.append({D[i], S[j], C[k], S[l], D[m]})
STRAIGHT_DSCSD.append({D[9], S[10], C[11], S[12], D[0]})

STRAIGHT_DSCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCCS.append({D[i], S[j], C[k], C[l], S[m]})
STRAIGHT_DSCCS.append({D[9], S[10], C[11], C[12], S[0]})

STRAIGHT_DSCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCCC.append({D[i], S[j], C[k], C[l], C[m]})
STRAIGHT_DSCCC.append({D[9], S[10], C[11], C[12], C[0]})

STRAIGHT_DSCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCCH.append({D[i], S[j], C[k], C[l], H[m]})
STRAIGHT_DSCCH.append({D[9], S[10], C[11], C[12], H[0]})

STRAIGHT_DSCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCCD.append({D[i], S[j], C[k], C[l], D[m]})
STRAIGHT_DSCCD.append({D[9], S[10], C[11], C[12], D[0]})

STRAIGHT_DSCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCHS.append({D[i], S[j], C[k], H[l], S[m]})
STRAIGHT_DSCHS.append({D[9], S[10], C[11], H[12], S[0]})

STRAIGHT_DSCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCHC.append({D[i], S[j], C[k], H[l], C[m]})
STRAIGHT_DSCHC.append({D[9], S[10], C[11], H[12], C[0]})

STRAIGHT_DSCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCHH.append({D[i], S[j], C[k], H[l], H[m]})
STRAIGHT_DSCHH.append({D[9], S[10], C[11], H[12], H[0]})

STRAIGHT_DSCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCHD.append({D[i], S[j], C[k], H[l], D[m]})
STRAIGHT_DSCHD.append({D[9], S[10], C[11], H[12], D[0]})

STRAIGHT_DSCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCDS.append({D[i], S[j], C[k], D[l], S[m]})
STRAIGHT_DSCDS.append({D[9], S[10], C[11], D[12], S[0]})

STRAIGHT_DSCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCDC.append({D[i], S[j], C[k], D[l], C[m]})
STRAIGHT_DSCDC.append({D[9], S[10], C[11], D[12], C[0]})

STRAIGHT_DSCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCDH.append({D[i], S[j], C[k], D[l], H[m]})
STRAIGHT_DSCDH.append({D[9], S[10], C[11], D[12], H[0]})

STRAIGHT_DSCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSCDD.append({D[i], S[j], C[k], D[l], D[m]})
STRAIGHT_DSCDD.append({D[9], S[10], C[11], D[12], D[0]})

STRAIGHT_DSHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHSS.append({D[i], S[j], H[k], S[l], S[m]})
STRAIGHT_DSHSS.append({D[9], S[10], H[11], S[12], S[0]})

STRAIGHT_DSHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHSC.append({D[i], S[j], H[k], S[l], C[m]})
STRAIGHT_DSHSC.append({D[9], S[10], H[11], S[12], C[0]})

STRAIGHT_DSHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHSH.append({D[i], S[j], H[k], S[l], H[m]})
STRAIGHT_DSHSH.append({D[9], S[10], H[11], S[12], H[0]})

STRAIGHT_DSHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHSD.append({D[i], S[j], H[k], S[l], D[m]})
STRAIGHT_DSHSD.append({D[9], S[10], H[11], S[12], D[0]})

STRAIGHT_DSHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHCS.append({D[i], S[j], H[k], C[l], S[m]})
STRAIGHT_DSHCS.append({D[9], S[10], H[11], C[12], S[0]})

STRAIGHT_DSHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHCC.append({D[i], S[j], H[k], C[l], C[m]})
STRAIGHT_DSHCC.append({D[9], S[10], H[11], C[12], C[0]})

STRAIGHT_DSHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHCH.append({D[i], S[j], H[k], C[l], H[m]})
STRAIGHT_DSHCH.append({D[9], S[10], H[11], C[12], H[0]})

STRAIGHT_DSHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHCD.append({D[i], S[j], H[k], C[l], D[m]})
STRAIGHT_DSHCD.append({D[9], S[10], H[11], C[12], D[0]})

STRAIGHT_DSHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHHS.append({D[i], S[j], H[k], H[l], S[m]})
STRAIGHT_DSHHS.append({D[9], S[10], H[11], H[12], S[0]})

STRAIGHT_DSHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHHC.append({D[i], S[j], H[k], H[l], C[m]})
STRAIGHT_DSHHC.append({D[9], S[10], H[11], H[12], C[0]})

STRAIGHT_DSHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHHH.append({D[i], S[j], H[k], H[l], H[m]})
STRAIGHT_DSHHH.append({D[9], S[10], H[11], H[12], H[0]})

STRAIGHT_DSHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHHD.append({D[i], S[j], H[k], H[l], D[m]})
STRAIGHT_DSHHD.append({D[9], S[10], H[11], H[12], D[0]})

STRAIGHT_DSHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHDS.append({D[i], S[j], H[k], D[l], S[m]})
STRAIGHT_DSHDS.append({D[9], S[10], H[11], D[12], S[0]})

STRAIGHT_DSHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHDC.append({D[i], S[j], H[k], D[l], C[m]})
STRAIGHT_DSHDC.append({D[9], S[10], H[11], D[12], C[0]})

STRAIGHT_DSHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHDH.append({D[i], S[j], H[k], D[l], H[m]})
STRAIGHT_DSHDH.append({D[9], S[10], H[11], D[12], H[0]})

STRAIGHT_DSHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSHDD.append({D[i], S[j], H[k], D[l], D[m]})
STRAIGHT_DSHDD.append({D[9], S[10], H[11], D[12], D[0]})

STRAIGHT_DSDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDSS.append({D[i], S[j], D[k], S[l], S[m]})
STRAIGHT_DSDSS.append({D[9], S[10], D[11], S[12], S[0]})

STRAIGHT_DSDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDSC.append({D[i], S[j], D[k], S[l], C[m]})
STRAIGHT_DSDSC.append({D[9], S[10], D[11], S[12], C[0]})

STRAIGHT_DSDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDSH.append({D[i], S[j], D[k], S[l], H[m]})
STRAIGHT_DSDSH.append({D[9], S[10], D[11], S[12], H[0]})

STRAIGHT_DSDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDSD.append({D[i], S[j], D[k], S[l], D[m]})
STRAIGHT_DSDSD.append({D[9], S[10], D[11], S[12], D[0]})

STRAIGHT_DSDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDCS.append({D[i], S[j], D[k], C[l], S[m]})
STRAIGHT_DSDCS.append({D[9], S[10], D[11], C[12], S[0]})

STRAIGHT_DSDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDCC.append({D[i], S[j], D[k], C[l], C[m]})
STRAIGHT_DSDCC.append({D[9], S[10], D[11], C[12], C[0]})

STRAIGHT_DSDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDCH.append({D[i], S[j], D[k], C[l], H[m]})
STRAIGHT_DSDCH.append({D[9], S[10], D[11], C[12], H[0]})

STRAIGHT_DSDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDCD.append({D[i], S[j], D[k], C[l], D[m]})
STRAIGHT_DSDCD.append({D[9], S[10], D[11], C[12], D[0]})

STRAIGHT_DSDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDHS.append({D[i], S[j], D[k], H[l], S[m]})
STRAIGHT_DSDHS.append({D[9], S[10], D[11], H[12], S[0]})

STRAIGHT_DSDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDHC.append({D[i], S[j], D[k], H[l], C[m]})
STRAIGHT_DSDHC.append({D[9], S[10], D[11], H[12], C[0]})

STRAIGHT_DSDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDHH.append({D[i], S[j], D[k], H[l], H[m]})
STRAIGHT_DSDHH.append({D[9], S[10], D[11], H[12], H[0]})

STRAIGHT_DSDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDHD.append({D[i], S[j], D[k], H[l], D[m]})
STRAIGHT_DSDHD.append({D[9], S[10], D[11], H[12], D[0]})

STRAIGHT_DSDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDDS.append({D[i], S[j], D[k], D[l], S[m]})
STRAIGHT_DSDDS.append({D[9], S[10], D[11], D[12], S[0]})

STRAIGHT_DSDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDDC.append({D[i], S[j], D[k], D[l], C[m]})
STRAIGHT_DSDDC.append({D[9], S[10], D[11], D[12], C[0]})

STRAIGHT_DSDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDDH.append({D[i], S[j], D[k], D[l], H[m]})
STRAIGHT_DSDDH.append({D[9], S[10], D[11], D[12], H[0]})

STRAIGHT_DSDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DSDDD.append({D[i], S[j], D[k], D[l], D[m]})
STRAIGHT_DSDDD.append({D[9], S[10], D[11], D[12], D[0]})

STRAIGHT_DCSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSSS.append({D[i], C[j], S[k], S[l], S[m]})
STRAIGHT_DCSSS.append({D[9], C[10], S[11], S[12], S[0]})

STRAIGHT_DCSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSSC.append({D[i], C[j], S[k], S[l], C[m]})
STRAIGHT_DCSSC.append({D[9], C[10], S[11], S[12], C[0]})

STRAIGHT_DCSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSSH.append({D[i], C[j], S[k], S[l], H[m]})
STRAIGHT_DCSSH.append({D[9], C[10], S[11], S[12], H[0]})

STRAIGHT_DCSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSSD.append({D[i], C[j], S[k], S[l], D[m]})
STRAIGHT_DCSSD.append({D[9], C[10], S[11], S[12], D[0]})

STRAIGHT_DCSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSCS.append({D[i], C[j], S[k], C[l], S[m]})
STRAIGHT_DCSCS.append({D[9], C[10], S[11], C[12], S[0]})

STRAIGHT_DCSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSCC.append({D[i], C[j], S[k], C[l], C[m]})
STRAIGHT_DCSCC.append({D[9], C[10], S[11], C[12], C[0]})

STRAIGHT_DCSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSCH.append({D[i], C[j], S[k], C[l], H[m]})
STRAIGHT_DCSCH.append({D[9], C[10], S[11], C[12], H[0]})

STRAIGHT_DCSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSCD.append({D[i], C[j], S[k], C[l], D[m]})
STRAIGHT_DCSCD.append({D[9], C[10], S[11], C[12], D[0]})

STRAIGHT_DCSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSHS.append({D[i], C[j], S[k], H[l], S[m]})
STRAIGHT_DCSHS.append({D[9], C[10], S[11], H[12], S[0]})

STRAIGHT_DCSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSHC.append({D[i], C[j], S[k], H[l], C[m]})
STRAIGHT_DCSHC.append({D[9], C[10], S[11], H[12], C[0]})

STRAIGHT_DCSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSHH.append({D[i], C[j], S[k], H[l], H[m]})
STRAIGHT_DCSHH.append({D[9], C[10], S[11], H[12], H[0]})

STRAIGHT_DCSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSHD.append({D[i], C[j], S[k], H[l], D[m]})
STRAIGHT_DCSHD.append({D[9], C[10], S[11], H[12], D[0]})

STRAIGHT_DCSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSDS.append({D[i], C[j], S[k], D[l], S[m]})
STRAIGHT_DCSDS.append({D[9], C[10], S[11], D[12], S[0]})

STRAIGHT_DCSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSDC.append({D[i], C[j], S[k], D[l], C[m]})
STRAIGHT_DCSDC.append({D[9], C[10], S[11], D[12], C[0]})

STRAIGHT_DCSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSDH.append({D[i], C[j], S[k], D[l], H[m]})
STRAIGHT_DCSDH.append({D[9], C[10], S[11], D[12], H[0]})

STRAIGHT_DCSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCSDD.append({D[i], C[j], S[k], D[l], D[m]})
STRAIGHT_DCSDD.append({D[9], C[10], S[11], D[12], D[0]})

STRAIGHT_DCCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCSS.append({D[i], C[j], C[k], S[l], S[m]})
STRAIGHT_DCCSS.append({D[9], C[10], C[11], S[12], S[0]})

STRAIGHT_DCCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCSC.append({D[i], C[j], C[k], S[l], C[m]})
STRAIGHT_DCCSC.append({D[9], C[10], C[11], S[12], C[0]})

STRAIGHT_DCCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCSH.append({D[i], C[j], C[k], S[l], H[m]})
STRAIGHT_DCCSH.append({D[9], C[10], C[11], S[12], H[0]})

STRAIGHT_DCCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCSD.append({D[i], C[j], C[k], S[l], D[m]})
STRAIGHT_DCCSD.append({D[9], C[10], C[11], S[12], D[0]})

STRAIGHT_DCCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCCS.append({D[i], C[j], C[k], C[l], S[m]})
STRAIGHT_DCCCS.append({D[9], C[10], C[11], C[12], S[0]})

STRAIGHT_DCCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCCC.append({D[i], C[j], C[k], C[l], C[m]})
STRAIGHT_DCCCC.append({D[9], C[10], C[11], C[12], C[0]})

STRAIGHT_DCCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCCH.append({D[i], C[j], C[k], C[l], H[m]})
STRAIGHT_DCCCH.append({D[9], C[10], C[11], C[12], H[0]})

STRAIGHT_DCCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCCD.append({D[i], C[j], C[k], C[l], D[m]})
STRAIGHT_DCCCD.append({D[9], C[10], C[11], C[12], D[0]})

STRAIGHT_DCCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCHS.append({D[i], C[j], C[k], H[l], S[m]})
STRAIGHT_DCCHS.append({D[9], C[10], C[11], H[12], S[0]})

STRAIGHT_DCCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCHC.append({D[i], C[j], C[k], H[l], C[m]})
STRAIGHT_DCCHC.append({D[9], C[10], C[11], H[12], C[0]})

STRAIGHT_DCCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCHH.append({D[i], C[j], C[k], H[l], H[m]})
STRAIGHT_DCCHH.append({D[9], C[10], C[11], H[12], H[0]})

STRAIGHT_DCCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCHD.append({D[i], C[j], C[k], H[l], D[m]})
STRAIGHT_DCCHD.append({D[9], C[10], C[11], H[12], D[0]})

STRAIGHT_DCCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCDS.append({D[i], C[j], C[k], D[l], S[m]})
STRAIGHT_DCCDS.append({D[9], C[10], C[11], D[12], S[0]})

STRAIGHT_DCCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCDC.append({D[i], C[j], C[k], D[l], C[m]})
STRAIGHT_DCCDC.append({D[9], C[10], C[11], D[12], C[0]})

STRAIGHT_DCCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCDH.append({D[i], C[j], C[k], D[l], H[m]})
STRAIGHT_DCCDH.append({D[9], C[10], C[11], D[12], H[0]})

STRAIGHT_DCCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCCDD.append({D[i], C[j], C[k], D[l], D[m]})
STRAIGHT_DCCDD.append({D[9], C[10], C[11], D[12], D[0]})

STRAIGHT_DCHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHSS.append({D[i], C[j], H[k], S[l], S[m]})
STRAIGHT_DCHSS.append({D[9], C[10], H[11], S[12], S[0]})

STRAIGHT_DCHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHSC.append({D[i], C[j], H[k], S[l], C[m]})
STRAIGHT_DCHSC.append({D[9], C[10], H[11], S[12], C[0]})

STRAIGHT_DCHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHSH.append({D[i], C[j], H[k], S[l], H[m]})
STRAIGHT_DCHSH.append({D[9], C[10], H[11], S[12], H[0]})

STRAIGHT_DCHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHSD.append({D[i], C[j], H[k], S[l], D[m]})
STRAIGHT_DCHSD.append({D[9], C[10], H[11], S[12], D[0]})

STRAIGHT_DCHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHCS.append({D[i], C[j], H[k], C[l], S[m]})
STRAIGHT_DCHCS.append({D[9], C[10], H[11], C[12], S[0]})

STRAIGHT_DCHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHCC.append({D[i], C[j], H[k], C[l], C[m]})
STRAIGHT_DCHCC.append({D[9], C[10], H[11], C[12], C[0]})

STRAIGHT_DCHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHCH.append({D[i], C[j], H[k], C[l], H[m]})
STRAIGHT_DCHCH.append({D[9], C[10], H[11], C[12], H[0]})

STRAIGHT_DCHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHCD.append({D[i], C[j], H[k], C[l], D[m]})
STRAIGHT_DCHCD.append({D[9], C[10], H[11], C[12], D[0]})

STRAIGHT_DCHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHHS.append({D[i], C[j], H[k], H[l], S[m]})
STRAIGHT_DCHHS.append({D[9], C[10], H[11], H[12], S[0]})

STRAIGHT_DCHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHHC.append({D[i], C[j], H[k], H[l], C[m]})
STRAIGHT_DCHHC.append({D[9], C[10], H[11], H[12], C[0]})

STRAIGHT_DCHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHHH.append({D[i], C[j], H[k], H[l], H[m]})
STRAIGHT_DCHHH.append({D[9], C[10], H[11], H[12], H[0]})

STRAIGHT_DCHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHHD.append({D[i], C[j], H[k], H[l], D[m]})
STRAIGHT_DCHHD.append({D[9], C[10], H[11], H[12], D[0]})

STRAIGHT_DCHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHDS.append({D[i], C[j], H[k], D[l], S[m]})
STRAIGHT_DCHDS.append({D[9], C[10], H[11], D[12], S[0]})

STRAIGHT_DCHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHDC.append({D[i], C[j], H[k], D[l], C[m]})
STRAIGHT_DCHDC.append({D[9], C[10], H[11], D[12], C[0]})

STRAIGHT_DCHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHDH.append({D[i], C[j], H[k], D[l], H[m]})
STRAIGHT_DCHDH.append({D[9], C[10], H[11], D[12], H[0]})

STRAIGHT_DCHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCHDD.append({D[i], C[j], H[k], D[l], D[m]})
STRAIGHT_DCHDD.append({D[9], C[10], H[11], D[12], D[0]})

STRAIGHT_DCDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDSS.append({D[i], C[j], D[k], S[l], S[m]})
STRAIGHT_DCDSS.append({D[9], C[10], D[11], S[12], S[0]})

STRAIGHT_DCDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDSC.append({D[i], C[j], D[k], S[l], C[m]})
STRAIGHT_DCDSC.append({D[9], C[10], D[11], S[12], C[0]})

STRAIGHT_DCDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDSH.append({D[i], C[j], D[k], S[l], H[m]})
STRAIGHT_DCDSH.append({D[9], C[10], D[11], S[12], H[0]})

STRAIGHT_DCDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDSD.append({D[i], C[j], D[k], S[l], D[m]})
STRAIGHT_DCDSD.append({D[9], C[10], D[11], S[12], D[0]})

STRAIGHT_DCDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDCS.append({D[i], C[j], D[k], C[l], S[m]})
STRAIGHT_DCDCS.append({D[9], C[10], D[11], C[12], S[0]})

STRAIGHT_DCDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDCC.append({D[i], C[j], D[k], C[l], C[m]})
STRAIGHT_DCDCC.append({D[9], C[10], D[11], C[12], C[0]})

STRAIGHT_DCDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDCH.append({D[i], C[j], D[k], C[l], H[m]})
STRAIGHT_DCDCH.append({D[9], C[10], D[11], C[12], H[0]})

STRAIGHT_DCDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDCD.append({D[i], C[j], D[k], C[l], D[m]})
STRAIGHT_DCDCD.append({D[9], C[10], D[11], C[12], D[0]})

STRAIGHT_DCDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDHS.append({D[i], C[j], D[k], H[l], S[m]})
STRAIGHT_DCDHS.append({D[9], C[10], D[11], H[12], S[0]})

STRAIGHT_DCDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDHC.append({D[i], C[j], D[k], H[l], C[m]})
STRAIGHT_DCDHC.append({D[9], C[10], D[11], H[12], C[0]})

STRAIGHT_DCDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDHH.append({D[i], C[j], D[k], H[l], H[m]})
STRAIGHT_DCDHH.append({D[9], C[10], D[11], H[12], H[0]})

STRAIGHT_DCDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDHD.append({D[i], C[j], D[k], H[l], D[m]})
STRAIGHT_DCDHD.append({D[9], C[10], D[11], H[12], D[0]})

STRAIGHT_DCDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDDS.append({D[i], C[j], D[k], D[l], S[m]})
STRAIGHT_DCDDS.append({D[9], C[10], D[11], D[12], S[0]})

STRAIGHT_DCDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDDC.append({D[i], C[j], D[k], D[l], C[m]})
STRAIGHT_DCDDC.append({D[9], C[10], D[11], D[12], C[0]})

STRAIGHT_DCDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDDH.append({D[i], C[j], D[k], D[l], H[m]})
STRAIGHT_DCDDH.append({D[9], C[10], D[11], D[12], H[0]})

STRAIGHT_DCDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DCDDD.append({D[i], C[j], D[k], D[l], D[m]})
STRAIGHT_DCDDD.append({D[9], C[10], D[11], D[12], D[0]})

STRAIGHT_DHSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSSS.append({D[i], H[j], S[k], S[l], S[m]})
STRAIGHT_DHSSS.append({D[9], H[10], S[11], S[12], S[0]})

STRAIGHT_DHSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSSC.append({D[i], H[j], S[k], S[l], C[m]})
STRAIGHT_DHSSC.append({D[9], H[10], S[11], S[12], C[0]})

STRAIGHT_DHSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSSH.append({D[i], H[j], S[k], S[l], H[m]})
STRAIGHT_DHSSH.append({D[9], H[10], S[11], S[12], H[0]})

STRAIGHT_DHSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSSD.append({D[i], H[j], S[k], S[l], D[m]})
STRAIGHT_DHSSD.append({D[9], H[10], S[11], S[12], D[0]})

STRAIGHT_DHSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSCS.append({D[i], H[j], S[k], C[l], S[m]})
STRAIGHT_DHSCS.append({D[9], H[10], S[11], C[12], S[0]})

STRAIGHT_DHSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSCC.append({D[i], H[j], S[k], C[l], C[m]})
STRAIGHT_DHSCC.append({D[9], H[10], S[11], C[12], C[0]})

STRAIGHT_DHSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSCH.append({D[i], H[j], S[k], C[l], H[m]})
STRAIGHT_DHSCH.append({D[9], H[10], S[11], C[12], H[0]})

STRAIGHT_DHSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSCD.append({D[i], H[j], S[k], C[l], D[m]})
STRAIGHT_DHSCD.append({D[9], H[10], S[11], C[12], D[0]})

STRAIGHT_DHSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSHS.append({D[i], H[j], S[k], H[l], S[m]})
STRAIGHT_DHSHS.append({D[9], H[10], S[11], H[12], S[0]})

STRAIGHT_DHSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSHC.append({D[i], H[j], S[k], H[l], C[m]})
STRAIGHT_DHSHC.append({D[9], H[10], S[11], H[12], C[0]})

STRAIGHT_DHSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSHH.append({D[i], H[j], S[k], H[l], H[m]})
STRAIGHT_DHSHH.append({D[9], H[10], S[11], H[12], H[0]})

STRAIGHT_DHSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSHD.append({D[i], H[j], S[k], H[l], D[m]})
STRAIGHT_DHSHD.append({D[9], H[10], S[11], H[12], D[0]})

STRAIGHT_DHSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSDS.append({D[i], H[j], S[k], D[l], S[m]})
STRAIGHT_DHSDS.append({D[9], H[10], S[11], D[12], S[0]})

STRAIGHT_DHSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSDC.append({D[i], H[j], S[k], D[l], C[m]})
STRAIGHT_DHSDC.append({D[9], H[10], S[11], D[12], C[0]})

STRAIGHT_DHSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSDH.append({D[i], H[j], S[k], D[l], H[m]})
STRAIGHT_DHSDH.append({D[9], H[10], S[11], D[12], H[0]})

STRAIGHT_DHSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHSDD.append({D[i], H[j], S[k], D[l], D[m]})
STRAIGHT_DHSDD.append({D[9], H[10], S[11], D[12], D[0]})

STRAIGHT_DHCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCSS.append({D[i], H[j], C[k], S[l], S[m]})
STRAIGHT_DHCSS.append({D[9], H[10], C[11], S[12], S[0]})

STRAIGHT_DHCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCSC.append({D[i], H[j], C[k], S[l], C[m]})
STRAIGHT_DHCSC.append({D[9], H[10], C[11], S[12], C[0]})

STRAIGHT_DHCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCSH.append({D[i], H[j], C[k], S[l], H[m]})
STRAIGHT_DHCSH.append({D[9], H[10], C[11], S[12], H[0]})

STRAIGHT_DHCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCSD.append({D[i], H[j], C[k], S[l], D[m]})
STRAIGHT_DHCSD.append({D[9], H[10], C[11], S[12], D[0]})

STRAIGHT_DHCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCCS.append({D[i], H[j], C[k], C[l], S[m]})
STRAIGHT_DHCCS.append({D[9], H[10], C[11], C[12], S[0]})

STRAIGHT_DHCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCCC.append({D[i], H[j], C[k], C[l], C[m]})
STRAIGHT_DHCCC.append({D[9], H[10], C[11], C[12], C[0]})

STRAIGHT_DHCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCCH.append({D[i], H[j], C[k], C[l], H[m]})
STRAIGHT_DHCCH.append({D[9], H[10], C[11], C[12], H[0]})

STRAIGHT_DHCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCCD.append({D[i], H[j], C[k], C[l], D[m]})
STRAIGHT_DHCCD.append({D[9], H[10], C[11], C[12], D[0]})

STRAIGHT_DHCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCHS.append({D[i], H[j], C[k], H[l], S[m]})
STRAIGHT_DHCHS.append({D[9], H[10], C[11], H[12], S[0]})

STRAIGHT_DHCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCHC.append({D[i], H[j], C[k], H[l], C[m]})
STRAIGHT_DHCHC.append({D[9], H[10], C[11], H[12], C[0]})

STRAIGHT_DHCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCHH.append({D[i], H[j], C[k], H[l], H[m]})
STRAIGHT_DHCHH.append({D[9], H[10], C[11], H[12], H[0]})

STRAIGHT_DHCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCHD.append({D[i], H[j], C[k], H[l], D[m]})
STRAIGHT_DHCHD.append({D[9], H[10], C[11], H[12], D[0]})

STRAIGHT_DHCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCDS.append({D[i], H[j], C[k], D[l], S[m]})
STRAIGHT_DHCDS.append({D[9], H[10], C[11], D[12], S[0]})

STRAIGHT_DHCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCDC.append({D[i], H[j], C[k], D[l], C[m]})
STRAIGHT_DHCDC.append({D[9], H[10], C[11], D[12], C[0]})

STRAIGHT_DHCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCDH.append({D[i], H[j], C[k], D[l], H[m]})
STRAIGHT_DHCDH.append({D[9], H[10], C[11], D[12], H[0]})

STRAIGHT_DHCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHCDD.append({D[i], H[j], C[k], D[l], D[m]})
STRAIGHT_DHCDD.append({D[9], H[10], C[11], D[12], D[0]})

STRAIGHT_DHHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHSS.append({D[i], H[j], H[k], S[l], S[m]})
STRAIGHT_DHHSS.append({D[9], H[10], H[11], S[12], S[0]})

STRAIGHT_DHHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHSC.append({D[i], H[j], H[k], S[l], C[m]})
STRAIGHT_DHHSC.append({D[9], H[10], H[11], S[12], C[0]})

STRAIGHT_DHHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHSH.append({D[i], H[j], H[k], S[l], H[m]})
STRAIGHT_DHHSH.append({D[9], H[10], H[11], S[12], H[0]})

STRAIGHT_DHHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHSD.append({D[i], H[j], H[k], S[l], D[m]})
STRAIGHT_DHHSD.append({D[9], H[10], H[11], S[12], D[0]})

STRAIGHT_DHHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHCS.append({D[i], H[j], H[k], C[l], S[m]})
STRAIGHT_DHHCS.append({D[9], H[10], H[11], C[12], S[0]})

STRAIGHT_DHHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHCC.append({D[i], H[j], H[k], C[l], C[m]})
STRAIGHT_DHHCC.append({D[9], H[10], H[11], C[12], C[0]})

STRAIGHT_DHHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHCH.append({D[i], H[j], H[k], C[l], H[m]})
STRAIGHT_DHHCH.append({D[9], H[10], H[11], C[12], H[0]})

STRAIGHT_DHHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHCD.append({D[i], H[j], H[k], C[l], D[m]})
STRAIGHT_DHHCD.append({D[9], H[10], H[11], C[12], D[0]})

STRAIGHT_DHHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHHS.append({D[i], H[j], H[k], H[l], S[m]})
STRAIGHT_DHHHS.append({D[9], H[10], H[11], H[12], S[0]})

STRAIGHT_DHHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHHC.append({D[i], H[j], H[k], H[l], C[m]})
STRAIGHT_DHHHC.append({D[9], H[10], H[11], H[12], C[0]})

STRAIGHT_DHHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHHH.append({D[i], H[j], H[k], H[l], H[m]})
STRAIGHT_DHHHH.append({D[9], H[10], H[11], H[12], H[0]})

STRAIGHT_DHHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHHD.append({D[i], H[j], H[k], H[l], D[m]})
STRAIGHT_DHHHD.append({D[9], H[10], H[11], H[12], D[0]})

STRAIGHT_DHHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHDS.append({D[i], H[j], H[k], D[l], S[m]})
STRAIGHT_DHHDS.append({D[9], H[10], H[11], D[12], S[0]})

STRAIGHT_DHHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHDC.append({D[i], H[j], H[k], D[l], C[m]})
STRAIGHT_DHHDC.append({D[9], H[10], H[11], D[12], C[0]})

STRAIGHT_DHHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHDH.append({D[i], H[j], H[k], D[l], H[m]})
STRAIGHT_DHHDH.append({D[9], H[10], H[11], D[12], H[0]})

STRAIGHT_DHHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHHDD.append({D[i], H[j], H[k], D[l], D[m]})
STRAIGHT_DHHDD.append({D[9], H[10], H[11], D[12], D[0]})

STRAIGHT_DHDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDSS.append({D[i], H[j], D[k], S[l], S[m]})
STRAIGHT_DHDSS.append({D[9], H[10], D[11], S[12], S[0]})

STRAIGHT_DHDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDSC.append({D[i], H[j], D[k], S[l], C[m]})
STRAIGHT_DHDSC.append({D[9], H[10], D[11], S[12], C[0]})

STRAIGHT_DHDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDSH.append({D[i], H[j], D[k], S[l], H[m]})
STRAIGHT_DHDSH.append({D[9], H[10], D[11], S[12], H[0]})

STRAIGHT_DHDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDSD.append({D[i], H[j], D[k], S[l], D[m]})
STRAIGHT_DHDSD.append({D[9], H[10], D[11], S[12], D[0]})

STRAIGHT_DHDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDCS.append({D[i], H[j], D[k], C[l], S[m]})
STRAIGHT_DHDCS.append({D[9], H[10], D[11], C[12], S[0]})

STRAIGHT_DHDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDCC.append({D[i], H[j], D[k], C[l], C[m]})
STRAIGHT_DHDCC.append({D[9], H[10], D[11], C[12], C[0]})

STRAIGHT_DHDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDCH.append({D[i], H[j], D[k], C[l], H[m]})
STRAIGHT_DHDCH.append({D[9], H[10], D[11], C[12], H[0]})

STRAIGHT_DHDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDCD.append({D[i], H[j], D[k], C[l], D[m]})
STRAIGHT_DHDCD.append({D[9], H[10], D[11], C[12], D[0]})

STRAIGHT_DHDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDHS.append({D[i], H[j], D[k], H[l], S[m]})
STRAIGHT_DHDHS.append({D[9], H[10], D[11], H[12], S[0]})

STRAIGHT_DHDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDHC.append({D[i], H[j], D[k], H[l], C[m]})
STRAIGHT_DHDHC.append({D[9], H[10], D[11], H[12], C[0]})

STRAIGHT_DHDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDHH.append({D[i], H[j], D[k], H[l], H[m]})
STRAIGHT_DHDHH.append({D[9], H[10], D[11], H[12], H[0]})

STRAIGHT_DHDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDHD.append({D[i], H[j], D[k], H[l], D[m]})
STRAIGHT_DHDHD.append({D[9], H[10], D[11], H[12], D[0]})

STRAIGHT_DHDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDDS.append({D[i], H[j], D[k], D[l], S[m]})
STRAIGHT_DHDDS.append({D[9], H[10], D[11], D[12], S[0]})

STRAIGHT_DHDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDDC.append({D[i], H[j], D[k], D[l], C[m]})
STRAIGHT_DHDDC.append({D[9], H[10], D[11], D[12], C[0]})

STRAIGHT_DHDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDDH.append({D[i], H[j], D[k], D[l], H[m]})
STRAIGHT_DHDDH.append({D[9], H[10], D[11], D[12], H[0]})

STRAIGHT_DHDDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DHDDD.append({D[i], H[j], D[k], D[l], D[m]})
STRAIGHT_DHDDD.append({D[9], H[10], D[11], D[12], D[0]})

STRAIGHT_DDSSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSSS.append({D[i], D[j], S[k], S[l], S[m]})
STRAIGHT_DDSSS.append({D[9], D[10], S[11], S[12], S[0]})

STRAIGHT_DDSSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSSC.append({D[i], D[j], S[k], S[l], C[m]})
STRAIGHT_DDSSC.append({D[9], D[10], S[11], S[12], C[0]})

STRAIGHT_DDSSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSSH.append({D[i], D[j], S[k], S[l], H[m]})
STRAIGHT_DDSSH.append({D[9], D[10], S[11], S[12], H[0]})

STRAIGHT_DDSSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSSD.append({D[i], D[j], S[k], S[l], D[m]})
STRAIGHT_DDSSD.append({D[9], D[10], S[11], S[12], D[0]})

STRAIGHT_DDSCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSCS.append({D[i], D[j], S[k], C[l], S[m]})
STRAIGHT_DDSCS.append({D[9], D[10], S[11], C[12], S[0]})

STRAIGHT_DDSCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSCC.append({D[i], D[j], S[k], C[l], C[m]})
STRAIGHT_DDSCC.append({D[9], D[10], S[11], C[12], C[0]})

STRAIGHT_DDSCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSCH.append({D[i], D[j], S[k], C[l], H[m]})
STRAIGHT_DDSCH.append({D[9], D[10], S[11], C[12], H[0]})

STRAIGHT_DDSCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSCD.append({D[i], D[j], S[k], C[l], D[m]})
STRAIGHT_DDSCD.append({D[9], D[10], S[11], C[12], D[0]})

STRAIGHT_DDSHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSHS.append({D[i], D[j], S[k], H[l], S[m]})
STRAIGHT_DDSHS.append({D[9], D[10], S[11], H[12], S[0]})

STRAIGHT_DDSHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSHC.append({D[i], D[j], S[k], H[l], C[m]})
STRAIGHT_DDSHC.append({D[9], D[10], S[11], H[12], C[0]})

STRAIGHT_DDSHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSHH.append({D[i], D[j], S[k], H[l], H[m]})
STRAIGHT_DDSHH.append({D[9], D[10], S[11], H[12], H[0]})

STRAIGHT_DDSHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSHD.append({D[i], D[j], S[k], H[l], D[m]})
STRAIGHT_DDSHD.append({D[9], D[10], S[11], H[12], D[0]})

STRAIGHT_DDSDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSDS.append({D[i], D[j], S[k], D[l], S[m]})
STRAIGHT_DDSDS.append({D[9], D[10], S[11], D[12], S[0]})

STRAIGHT_DDSDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSDC.append({D[i], D[j], S[k], D[l], C[m]})
STRAIGHT_DDSDC.append({D[9], D[10], S[11], D[12], C[0]})

STRAIGHT_DDSDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSDH.append({D[i], D[j], S[k], D[l], H[m]})
STRAIGHT_DDSDH.append({D[9], D[10], S[11], D[12], H[0]})

STRAIGHT_DDSDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDSDD.append({D[i], D[j], S[k], D[l], D[m]})
STRAIGHT_DDSDD.append({D[9], D[10], S[11], D[12], D[0]})

STRAIGHT_DDCSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCSS.append({D[i], D[j], C[k], S[l], S[m]})
STRAIGHT_DDCSS.append({D[9], D[10], C[11], S[12], S[0]})

STRAIGHT_DDCSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCSC.append({D[i], D[j], C[k], S[l], C[m]})
STRAIGHT_DDCSC.append({D[9], D[10], C[11], S[12], C[0]})

STRAIGHT_DDCSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCSH.append({D[i], D[j], C[k], S[l], H[m]})
STRAIGHT_DDCSH.append({D[9], D[10], C[11], S[12], H[0]})

STRAIGHT_DDCSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCSD.append({D[i], D[j], C[k], S[l], D[m]})
STRAIGHT_DDCSD.append({D[9], D[10], C[11], S[12], D[0]})

STRAIGHT_DDCCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCCS.append({D[i], D[j], C[k], C[l], S[m]})
STRAIGHT_DDCCS.append({D[9], D[10], C[11], C[12], S[0]})

STRAIGHT_DDCCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCCC.append({D[i], D[j], C[k], C[l], C[m]})
STRAIGHT_DDCCC.append({D[9], D[10], C[11], C[12], C[0]})

STRAIGHT_DDCCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCCH.append({D[i], D[j], C[k], C[l], H[m]})
STRAIGHT_DDCCH.append({D[9], D[10], C[11], C[12], H[0]})

STRAIGHT_DDCCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCCD.append({D[i], D[j], C[k], C[l], D[m]})
STRAIGHT_DDCCD.append({D[9], D[10], C[11], C[12], D[0]})

STRAIGHT_DDCHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCHS.append({D[i], D[j], C[k], H[l], S[m]})
STRAIGHT_DDCHS.append({D[9], D[10], C[11], H[12], S[0]})

STRAIGHT_DDCHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCHC.append({D[i], D[j], C[k], H[l], C[m]})
STRAIGHT_DDCHC.append({D[9], D[10], C[11], H[12], C[0]})

STRAIGHT_DDCHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCHH.append({D[i], D[j], C[k], H[l], H[m]})
STRAIGHT_DDCHH.append({D[9], D[10], C[11], H[12], H[0]})

STRAIGHT_DDCHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCHD.append({D[i], D[j], C[k], H[l], D[m]})
STRAIGHT_DDCHD.append({D[9], D[10], C[11], H[12], D[0]})

STRAIGHT_DDCDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCDS.append({D[i], D[j], C[k], D[l], S[m]})
STRAIGHT_DDCDS.append({D[9], D[10], C[11], D[12], S[0]})

STRAIGHT_DDCDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCDC.append({D[i], D[j], C[k], D[l], C[m]})
STRAIGHT_DDCDC.append({D[9], D[10], C[11], D[12], C[0]})

STRAIGHT_DDCDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCDH.append({D[i], D[j], C[k], D[l], H[m]})
STRAIGHT_DDCDH.append({D[9], D[10], C[11], D[12], H[0]})

STRAIGHT_DDCDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDCDD.append({D[i], D[j], C[k], D[l], D[m]})
STRAIGHT_DDCDD.append({D[9], D[10], C[11], D[12], D[0]})

STRAIGHT_DDHSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHSS.append({D[i], D[j], H[k], S[l], S[m]})
STRAIGHT_DDHSS.append({D[9], D[10], H[11], S[12], S[0]})

STRAIGHT_DDHSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHSC.append({D[i], D[j], H[k], S[l], C[m]})
STRAIGHT_DDHSC.append({D[9], D[10], H[11], S[12], C[0]})

STRAIGHT_DDHSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHSH.append({D[i], D[j], H[k], S[l], H[m]})
STRAIGHT_DDHSH.append({D[9], D[10], H[11], S[12], H[0]})

STRAIGHT_DDHSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHSD.append({D[i], D[j], H[k], S[l], D[m]})
STRAIGHT_DDHSD.append({D[9], D[10], H[11], S[12], D[0]})

STRAIGHT_DDHCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHCS.append({D[i], D[j], H[k], C[l], S[m]})
STRAIGHT_DDHCS.append({D[9], D[10], H[11], C[12], S[0]})

STRAIGHT_DDHCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHCC.append({D[i], D[j], H[k], C[l], C[m]})
STRAIGHT_DDHCC.append({D[9], D[10], H[11], C[12], C[0]})

STRAIGHT_DDHCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHCH.append({D[i], D[j], H[k], C[l], H[m]})
STRAIGHT_DDHCH.append({D[9], D[10], H[11], C[12], H[0]})

STRAIGHT_DDHCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHCD.append({D[i], D[j], H[k], C[l], D[m]})
STRAIGHT_DDHCD.append({D[9], D[10], H[11], C[12], D[0]})

STRAIGHT_DDHHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHHS.append({D[i], D[j], H[k], H[l], S[m]})
STRAIGHT_DDHHS.append({D[9], D[10], H[11], H[12], S[0]})

STRAIGHT_DDHHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHHC.append({D[i], D[j], H[k], H[l], C[m]})
STRAIGHT_DDHHC.append({D[9], D[10], H[11], H[12], C[0]})

STRAIGHT_DDHHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHHH.append({D[i], D[j], H[k], H[l], H[m]})
STRAIGHT_DDHHH.append({D[9], D[10], H[11], H[12], H[0]})

STRAIGHT_DDHHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHHD.append({D[i], D[j], H[k], H[l], D[m]})
STRAIGHT_DDHHD.append({D[9], D[10], H[11], H[12], D[0]})

STRAIGHT_DDHDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHDS.append({D[i], D[j], H[k], D[l], S[m]})
STRAIGHT_DDHDS.append({D[9], D[10], H[11], D[12], S[0]})

STRAIGHT_DDHDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHDC.append({D[i], D[j], H[k], D[l], C[m]})
STRAIGHT_DDHDC.append({D[9], D[10], H[11], D[12], C[0]})

STRAIGHT_DDHDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHDH.append({D[i], D[j], H[k], D[l], H[m]})
STRAIGHT_DDHDH.append({D[9], D[10], H[11], D[12], H[0]})

STRAIGHT_DDHDD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDHDD.append({D[i], D[j], H[k], D[l], D[m]})
STRAIGHT_DDHDD.append({D[9], D[10], H[11], D[12], D[0]})

STRAIGHT_DDDSS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDSS.append({D[i], D[j], D[k], S[l], S[m]})
STRAIGHT_DDDSS.append({D[9], D[10], D[11], S[12], S[0]})

STRAIGHT_DDDSC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDSC.append({D[i], D[j], D[k], S[l], C[m]})
STRAIGHT_DDDSC.append({D[9], D[10], D[11], S[12], C[0]})

STRAIGHT_DDDSH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDSH.append({D[i], D[j], D[k], S[l], H[m]})
STRAIGHT_DDDSH.append({D[9], D[10], D[11], S[12], H[0]})

STRAIGHT_DDDSD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDSD.append({D[i], D[j], D[k], S[l], D[m]})
STRAIGHT_DDDSD.append({D[9], D[10], D[11], S[12], D[0]})

STRAIGHT_DDDCS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDCS.append({D[i], D[j], D[k], C[l], S[m]})
STRAIGHT_DDDCS.append({D[9], D[10], D[11], C[12], S[0]})

STRAIGHT_DDDCC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDCC.append({D[i], D[j], D[k], C[l], C[m]})
STRAIGHT_DDDCC.append({D[9], D[10], D[11], C[12], C[0]})

STRAIGHT_DDDCH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDCH.append({D[i], D[j], D[k], C[l], H[m]})
STRAIGHT_DDDCH.append({D[9], D[10], D[11], C[12], H[0]})

STRAIGHT_DDDCD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDCD.append({D[i], D[j], D[k], C[l], D[m]})
STRAIGHT_DDDCD.append({D[9], D[10], D[11], C[12], D[0]})

STRAIGHT_DDDHS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDHS.append({D[i], D[j], D[k], H[l], S[m]})
STRAIGHT_DDDHS.append({D[9], D[10], D[11], H[12], S[0]})

STRAIGHT_DDDHC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDHC.append({D[i], D[j], D[k], H[l], C[m]})
STRAIGHT_DDDHC.append({D[9], D[10], D[11], H[12], C[0]})

STRAIGHT_DDDHH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDHH.append({D[i], D[j], D[k], H[l], H[m]})
STRAIGHT_DDDHH.append({D[9], D[10], D[11], H[12], H[0]})

STRAIGHT_DDDHD = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDHD.append({D[i], D[j], D[k], H[l], D[m]})
STRAIGHT_DDDHD.append({D[9], D[10], D[11], H[12], D[0]})

STRAIGHT_DDDDS = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDDS.append({D[i], D[j], D[k], D[l], S[m]})
STRAIGHT_DDDDS.append({D[9], D[10], D[11], D[12], S[0]})

STRAIGHT_DDDDC = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDDC.append({D[i], D[j], D[k], D[l], C[m]})
STRAIGHT_DDDDC.append({D[9], D[10], D[11], D[12], C[0]})

STRAIGHT_DDDDH = []
for i in range(13):
    for j in range(1, 13):
        for k in range(2, 13):
            for l in range(3, 13):
                for m in range(4, 13):
                    if m == l + 1 and l == k + 1 and k == j + 1 and j == i + 1:
                        STRAIGHT_DDDDH.append({D[i], D[j], D[k], D[l], H[m]})
STRAIGHT_DDDDH.append({D[9], D[10], D[11], D[12], H[0]})

STRAIGHT = []
STRAIGHT.extend(STRAIGHT_SSSSC)
STRAIGHT.extend(STRAIGHT_SSSSH)
STRAIGHT.extend(STRAIGHT_SSSSD)
STRAIGHT.extend(STRAIGHT_SSSCS)
STRAIGHT.extend(STRAIGHT_SSSCC)
STRAIGHT.extend(STRAIGHT_SSSCH)
STRAIGHT.extend(STRAIGHT_SSSCD)
STRAIGHT.extend(STRAIGHT_SSSHS)
STRAIGHT.extend(STRAIGHT_SSSHC)
STRAIGHT.extend(STRAIGHT_SSSHH)
STRAIGHT.extend(STRAIGHT_SSSHD)
STRAIGHT.extend(STRAIGHT_SSSDS)
STRAIGHT.extend(STRAIGHT_SSSDC)
STRAIGHT.extend(STRAIGHT_SSSDH)
STRAIGHT.extend(STRAIGHT_SSSDD)
STRAIGHT.extend(STRAIGHT_SSCSS)
STRAIGHT.extend(STRAIGHT_SSCSC)
STRAIGHT.extend(STRAIGHT_SSCSH)
STRAIGHT.extend(STRAIGHT_SSCSD)
STRAIGHT.extend(STRAIGHT_SSCCS)
STRAIGHT.extend(STRAIGHT_SSCCC)
STRAIGHT.extend(STRAIGHT_SSCCH)
STRAIGHT.extend(STRAIGHT_SSCCD)
STRAIGHT.extend(STRAIGHT_SSCHS)
STRAIGHT.extend(STRAIGHT_SSCHC)
STRAIGHT.extend(STRAIGHT_SSCHH)
STRAIGHT.extend(STRAIGHT_SSCHD)
STRAIGHT.extend(STRAIGHT_SSCDS)
STRAIGHT.extend(STRAIGHT_SSCDC)
STRAIGHT.extend(STRAIGHT_SSCDH)
STRAIGHT.extend(STRAIGHT_SSCDD)
STRAIGHT.extend(STRAIGHT_SSHSS)
STRAIGHT.extend(STRAIGHT_SSHSC)
STRAIGHT.extend(STRAIGHT_SSHSH)
STRAIGHT.extend(STRAIGHT_SSHSD)
STRAIGHT.extend(STRAIGHT_SSHCS)
STRAIGHT.extend(STRAIGHT_SSHCC)
STRAIGHT.extend(STRAIGHT_SSHCH)
STRAIGHT.extend(STRAIGHT_SSHCD)
STRAIGHT.extend(STRAIGHT_SSHHS)
STRAIGHT.extend(STRAIGHT_SSHHC)
STRAIGHT.extend(STRAIGHT_SSHHH)
STRAIGHT.extend(STRAIGHT_SSHHD)
STRAIGHT.extend(STRAIGHT_SSHDS)
STRAIGHT.extend(STRAIGHT_SSHDC)
STRAIGHT.extend(STRAIGHT_SSHDH)
STRAIGHT.extend(STRAIGHT_SSHDD)
STRAIGHT.extend(STRAIGHT_SSDSS)
STRAIGHT.extend(STRAIGHT_SSDSC)
STRAIGHT.extend(STRAIGHT_SSDSH)
STRAIGHT.extend(STRAIGHT_SSDSD)
STRAIGHT.extend(STRAIGHT_SSDCS)
STRAIGHT.extend(STRAIGHT_SSDCC)
STRAIGHT.extend(STRAIGHT_SSDCH)
STRAIGHT.extend(STRAIGHT_SSDCD)
STRAIGHT.extend(STRAIGHT_SSDHS)
STRAIGHT.extend(STRAIGHT_SSDHC)
STRAIGHT.extend(STRAIGHT_SSDHH)
STRAIGHT.extend(STRAIGHT_SSDHD)
STRAIGHT.extend(STRAIGHT_SSDDS)
STRAIGHT.extend(STRAIGHT_SSDDC)
STRAIGHT.extend(STRAIGHT_SSDDH)
STRAIGHT.extend(STRAIGHT_SSDDD)
STRAIGHT.extend(STRAIGHT_SCSSS)
STRAIGHT.extend(STRAIGHT_SCSSC)
STRAIGHT.extend(STRAIGHT_SCSSH)
STRAIGHT.extend(STRAIGHT_SCSSD)
STRAIGHT.extend(STRAIGHT_SCSCS)
STRAIGHT.extend(STRAIGHT_SCSCC)
STRAIGHT.extend(STRAIGHT_SCSCH)
STRAIGHT.extend(STRAIGHT_SCSCD)
STRAIGHT.extend(STRAIGHT_SCSHS)
STRAIGHT.extend(STRAIGHT_SCSHC)
STRAIGHT.extend(STRAIGHT_SCSHH)
STRAIGHT.extend(STRAIGHT_SCSHD)
STRAIGHT.extend(STRAIGHT_SCSDS)
STRAIGHT.extend(STRAIGHT_SCSDC)
STRAIGHT.extend(STRAIGHT_SCSDH)
STRAIGHT.extend(STRAIGHT_SCSDD)
STRAIGHT.extend(STRAIGHT_SCCSS)
STRAIGHT.extend(STRAIGHT_SCCSC)
STRAIGHT.extend(STRAIGHT_SCCSH)
STRAIGHT.extend(STRAIGHT_SCCSD)
STRAIGHT.extend(STRAIGHT_SCCCS)
STRAIGHT.extend(STRAIGHT_SCCCC)
STRAIGHT.extend(STRAIGHT_SCCCH)
STRAIGHT.extend(STRAIGHT_SCCCD)
STRAIGHT.extend(STRAIGHT_SCCHS)
STRAIGHT.extend(STRAIGHT_SCCHC)
STRAIGHT.extend(STRAIGHT_SCCHH)
STRAIGHT.extend(STRAIGHT_SCCHD)
STRAIGHT.extend(STRAIGHT_SCCDS)
STRAIGHT.extend(STRAIGHT_SCCDC)
STRAIGHT.extend(STRAIGHT_SCCDH)
STRAIGHT.extend(STRAIGHT_SCCDD)
STRAIGHT.extend(STRAIGHT_SCHSS)
STRAIGHT.extend(STRAIGHT_SCHSC)
STRAIGHT.extend(STRAIGHT_SCHSH)
STRAIGHT.extend(STRAIGHT_SCHSD)
STRAIGHT.extend(STRAIGHT_SCHCS)
STRAIGHT.extend(STRAIGHT_SCHCC)
STRAIGHT.extend(STRAIGHT_SCHCH)
STRAIGHT.extend(STRAIGHT_SCHCD)
STRAIGHT.extend(STRAIGHT_SCHHS)
STRAIGHT.extend(STRAIGHT_SCHHC)
STRAIGHT.extend(STRAIGHT_SCHHH)
STRAIGHT.extend(STRAIGHT_SCHHD)
STRAIGHT.extend(STRAIGHT_SCHDS)
STRAIGHT.extend(STRAIGHT_SCHDC)
STRAIGHT.extend(STRAIGHT_SCHDH)
STRAIGHT.extend(STRAIGHT_SCHDD)
STRAIGHT.extend(STRAIGHT_SCDSS)
STRAIGHT.extend(STRAIGHT_SCDSC)
STRAIGHT.extend(STRAIGHT_SCDSH)
STRAIGHT.extend(STRAIGHT_SCDSD)
STRAIGHT.extend(STRAIGHT_SCDCS)
STRAIGHT.extend(STRAIGHT_SCDCC)
STRAIGHT.extend(STRAIGHT_SCDCH)
STRAIGHT.extend(STRAIGHT_SCDCD)
STRAIGHT.extend(STRAIGHT_SCDHS)
STRAIGHT.extend(STRAIGHT_SCDHC)
STRAIGHT.extend(STRAIGHT_SCDHH)
STRAIGHT.extend(STRAIGHT_SCDHD)
STRAIGHT.extend(STRAIGHT_SCDDS)
STRAIGHT.extend(STRAIGHT_SCDDC)
STRAIGHT.extend(STRAIGHT_SCDDH)
STRAIGHT.extend(STRAIGHT_SCDDD)
STRAIGHT.extend(STRAIGHT_SHSSS)
STRAIGHT.extend(STRAIGHT_SHSSC)
STRAIGHT.extend(STRAIGHT_SHSSH)
STRAIGHT.extend(STRAIGHT_SHSSD)
STRAIGHT.extend(STRAIGHT_SHSCS)
STRAIGHT.extend(STRAIGHT_SHSCC)
STRAIGHT.extend(STRAIGHT_SHSCH)
STRAIGHT.extend(STRAIGHT_SHSCD)
STRAIGHT.extend(STRAIGHT_SHSHS)
STRAIGHT.extend(STRAIGHT_SHSHC)
STRAIGHT.extend(STRAIGHT_SHSHH)
STRAIGHT.extend(STRAIGHT_SHSHD)
STRAIGHT.extend(STRAIGHT_SHSDS)
STRAIGHT.extend(STRAIGHT_SHSDC)
STRAIGHT.extend(STRAIGHT_SHSDH)
STRAIGHT.extend(STRAIGHT_SHSDD)
STRAIGHT.extend(STRAIGHT_SHCSS)
STRAIGHT.extend(STRAIGHT_SHCSC)
STRAIGHT.extend(STRAIGHT_SHCSH)
STRAIGHT.extend(STRAIGHT_SHCSD)
STRAIGHT.extend(STRAIGHT_SHCCS)
STRAIGHT.extend(STRAIGHT_SHCCC)
STRAIGHT.extend(STRAIGHT_SHCCH)
STRAIGHT.extend(STRAIGHT_SHCCD)
STRAIGHT.extend(STRAIGHT_SHCHS)
STRAIGHT.extend(STRAIGHT_SHCHC)
STRAIGHT.extend(STRAIGHT_SHCHH)
STRAIGHT.extend(STRAIGHT_SHCHD)
STRAIGHT.extend(STRAIGHT_SHCDS)
STRAIGHT.extend(STRAIGHT_SHCDC)
STRAIGHT.extend(STRAIGHT_SHCDH)
STRAIGHT.extend(STRAIGHT_SHCDD)
STRAIGHT.extend(STRAIGHT_SHHSS)
STRAIGHT.extend(STRAIGHT_SHHSC)
STRAIGHT.extend(STRAIGHT_SHHSH)
STRAIGHT.extend(STRAIGHT_SHHSD)
STRAIGHT.extend(STRAIGHT_SHHCS)
STRAIGHT.extend(STRAIGHT_SHHCC)
STRAIGHT.extend(STRAIGHT_SHHCH)
STRAIGHT.extend(STRAIGHT_SHHCD)
STRAIGHT.extend(STRAIGHT_SHHHS)
STRAIGHT.extend(STRAIGHT_SHHHC)
STRAIGHT.extend(STRAIGHT_SHHHH)
STRAIGHT.extend(STRAIGHT_SHHHD)
STRAIGHT.extend(STRAIGHT_SHHDS)
STRAIGHT.extend(STRAIGHT_SHHDC)
STRAIGHT.extend(STRAIGHT_SHHDH)
STRAIGHT.extend(STRAIGHT_SHHDD)
STRAIGHT.extend(STRAIGHT_SHDSS)
STRAIGHT.extend(STRAIGHT_SHDSC)
STRAIGHT.extend(STRAIGHT_SHDSH)
STRAIGHT.extend(STRAIGHT_SHDSD)
STRAIGHT.extend(STRAIGHT_SHDCS)
STRAIGHT.extend(STRAIGHT_SHDCC)
STRAIGHT.extend(STRAIGHT_SHDCH)
STRAIGHT.extend(STRAIGHT_SHDCD)
STRAIGHT.extend(STRAIGHT_SHDHS)
STRAIGHT.extend(STRAIGHT_SHDHC)
STRAIGHT.extend(STRAIGHT_SHDHH)
STRAIGHT.extend(STRAIGHT_SHDHD)
STRAIGHT.extend(STRAIGHT_SHDDS)
STRAIGHT.extend(STRAIGHT_SHDDC)
STRAIGHT.extend(STRAIGHT_SHDDH)
STRAIGHT.extend(STRAIGHT_SHDDD)
STRAIGHT.extend(STRAIGHT_SDSSS)
STRAIGHT.extend(STRAIGHT_SDSSC)
STRAIGHT.extend(STRAIGHT_SDSSH)
STRAIGHT.extend(STRAIGHT_SDSSD)
STRAIGHT.extend(STRAIGHT_SDSCS)
STRAIGHT.extend(STRAIGHT_SDSCC)
STRAIGHT.extend(STRAIGHT_SDSCH)
STRAIGHT.extend(STRAIGHT_SDSCD)
STRAIGHT.extend(STRAIGHT_SDSHS)
STRAIGHT.extend(STRAIGHT_SDSHC)
STRAIGHT.extend(STRAIGHT_SDSHH)
STRAIGHT.extend(STRAIGHT_SDSHD)
STRAIGHT.extend(STRAIGHT_SDSDS)
STRAIGHT.extend(STRAIGHT_SDSDC)
STRAIGHT.extend(STRAIGHT_SDSDH)
STRAIGHT.extend(STRAIGHT_SDSDD)
STRAIGHT.extend(STRAIGHT_SDCSS)
STRAIGHT.extend(STRAIGHT_SDCSC)
STRAIGHT.extend(STRAIGHT_SDCSH)
STRAIGHT.extend(STRAIGHT_SDCSD)
STRAIGHT.extend(STRAIGHT_SDCCS)
STRAIGHT.extend(STRAIGHT_SDCCC)
STRAIGHT.extend(STRAIGHT_SDCCH)
STRAIGHT.extend(STRAIGHT_SDCCD)
STRAIGHT.extend(STRAIGHT_SDCHS)
STRAIGHT.extend(STRAIGHT_SDCHC)
STRAIGHT.extend(STRAIGHT_SDCHH)
STRAIGHT.extend(STRAIGHT_SDCHD)
STRAIGHT.extend(STRAIGHT_SDCDS)
STRAIGHT.extend(STRAIGHT_SDCDC)
STRAIGHT.extend(STRAIGHT_SDCDH)
STRAIGHT.extend(STRAIGHT_SDCDD)
STRAIGHT.extend(STRAIGHT_SDHSS)
STRAIGHT.extend(STRAIGHT_SDHSC)
STRAIGHT.extend(STRAIGHT_SDHSH)
STRAIGHT.extend(STRAIGHT_SDHSD)
STRAIGHT.extend(STRAIGHT_SDHCS)
STRAIGHT.extend(STRAIGHT_SDHCC)
STRAIGHT.extend(STRAIGHT_SDHCH)
STRAIGHT.extend(STRAIGHT_SDHCD)
STRAIGHT.extend(STRAIGHT_SDHHS)
STRAIGHT.extend(STRAIGHT_SDHHC)
STRAIGHT.extend(STRAIGHT_SDHHH)
STRAIGHT.extend(STRAIGHT_SDHHD)
STRAIGHT.extend(STRAIGHT_SDHDS)
STRAIGHT.extend(STRAIGHT_SDHDC)
STRAIGHT.extend(STRAIGHT_SDHDH)
STRAIGHT.extend(STRAIGHT_SDHDD)
STRAIGHT.extend(STRAIGHT_SDDSS)
STRAIGHT.extend(STRAIGHT_SDDSC)
STRAIGHT.extend(STRAIGHT_SDDSH)
STRAIGHT.extend(STRAIGHT_SDDSD)
STRAIGHT.extend(STRAIGHT_SDDCS)
STRAIGHT.extend(STRAIGHT_SDDCC)
STRAIGHT.extend(STRAIGHT_SDDCH)
STRAIGHT.extend(STRAIGHT_SDDCD)
STRAIGHT.extend(STRAIGHT_SDDHS)
STRAIGHT.extend(STRAIGHT_SDDHC)
STRAIGHT.extend(STRAIGHT_SDDHH)
STRAIGHT.extend(STRAIGHT_SDDHD)
STRAIGHT.extend(STRAIGHT_SDDDS)
STRAIGHT.extend(STRAIGHT_SDDDC)
STRAIGHT.extend(STRAIGHT_SDDDH)
STRAIGHT.extend(STRAIGHT_SDDDD)
STRAIGHT.extend(STRAIGHT_CSSSS)
STRAIGHT.extend(STRAIGHT_CSSSC)
STRAIGHT.extend(STRAIGHT_CSSSH)
STRAIGHT.extend(STRAIGHT_CSSSD)
STRAIGHT.extend(STRAIGHT_CSSCS)
STRAIGHT.extend(STRAIGHT_CSSCC)
STRAIGHT.extend(STRAIGHT_CSSCH)
STRAIGHT.extend(STRAIGHT_CSSCD)
STRAIGHT.extend(STRAIGHT_CSSHS)
STRAIGHT.extend(STRAIGHT_CSSHC)
STRAIGHT.extend(STRAIGHT_CSSHH)
STRAIGHT.extend(STRAIGHT_CSSHD)
STRAIGHT.extend(STRAIGHT_CSSDS)
STRAIGHT.extend(STRAIGHT_CSSDC)
STRAIGHT.extend(STRAIGHT_CSSDH)
STRAIGHT.extend(STRAIGHT_CSSDD)
STRAIGHT.extend(STRAIGHT_CSCSS)
STRAIGHT.extend(STRAIGHT_CSCSC)
STRAIGHT.extend(STRAIGHT_CSCSH)
STRAIGHT.extend(STRAIGHT_CSCSD)
STRAIGHT.extend(STRAIGHT_CSCCS)
STRAIGHT.extend(STRAIGHT_CSCCC)
STRAIGHT.extend(STRAIGHT_CSCCH)
STRAIGHT.extend(STRAIGHT_CSCCD)
STRAIGHT.extend(STRAIGHT_CSCHS)
STRAIGHT.extend(STRAIGHT_CSCHC)
STRAIGHT.extend(STRAIGHT_CSCHH)
STRAIGHT.extend(STRAIGHT_CSCHD)
STRAIGHT.extend(STRAIGHT_CSCDS)
STRAIGHT.extend(STRAIGHT_CSCDC)
STRAIGHT.extend(STRAIGHT_CSCDH)
STRAIGHT.extend(STRAIGHT_CSCDD)
STRAIGHT.extend(STRAIGHT_CSHSS)
STRAIGHT.extend(STRAIGHT_CSHSC)
STRAIGHT.extend(STRAIGHT_CSHSH)
STRAIGHT.extend(STRAIGHT_CSHSD)
STRAIGHT.extend(STRAIGHT_CSHCS)
STRAIGHT.extend(STRAIGHT_CSHCC)
STRAIGHT.extend(STRAIGHT_CSHCH)
STRAIGHT.extend(STRAIGHT_CSHCD)
STRAIGHT.extend(STRAIGHT_CSHHS)
STRAIGHT.extend(STRAIGHT_CSHHC)
STRAIGHT.extend(STRAIGHT_CSHHH)
STRAIGHT.extend(STRAIGHT_CSHHD)
STRAIGHT.extend(STRAIGHT_CSHDS)
STRAIGHT.extend(STRAIGHT_CSHDC)
STRAIGHT.extend(STRAIGHT_CSHDH)
STRAIGHT.extend(STRAIGHT_CSHDD)
STRAIGHT.extend(STRAIGHT_CSDSS)
STRAIGHT.extend(STRAIGHT_CSDSC)
STRAIGHT.extend(STRAIGHT_CSDSH)
STRAIGHT.extend(STRAIGHT_CSDSD)
STRAIGHT.extend(STRAIGHT_CSDCS)
STRAIGHT.extend(STRAIGHT_CSDCC)
STRAIGHT.extend(STRAIGHT_CSDCH)
STRAIGHT.extend(STRAIGHT_CSDCD)
STRAIGHT.extend(STRAIGHT_CSDHS)
STRAIGHT.extend(STRAIGHT_CSDHC)
STRAIGHT.extend(STRAIGHT_CSDHH)
STRAIGHT.extend(STRAIGHT_CSDHD)
STRAIGHT.extend(STRAIGHT_CSDDS)
STRAIGHT.extend(STRAIGHT_CSDDC)
STRAIGHT.extend(STRAIGHT_CSDDH)
STRAIGHT.extend(STRAIGHT_CSDDD)
STRAIGHT.extend(STRAIGHT_CCSSS)
STRAIGHT.extend(STRAIGHT_CCSSC)
STRAIGHT.extend(STRAIGHT_CCSSH)
STRAIGHT.extend(STRAIGHT_CCSSD)
STRAIGHT.extend(STRAIGHT_CCSCS)
STRAIGHT.extend(STRAIGHT_CCSCC)
STRAIGHT.extend(STRAIGHT_CCSCH)
STRAIGHT.extend(STRAIGHT_CCSCD)
STRAIGHT.extend(STRAIGHT_CCSHS)
STRAIGHT.extend(STRAIGHT_CCSHC)
STRAIGHT.extend(STRAIGHT_CCSHH)
STRAIGHT.extend(STRAIGHT_CCSHD)
STRAIGHT.extend(STRAIGHT_CCSDS)
STRAIGHT.extend(STRAIGHT_CCSDC)
STRAIGHT.extend(STRAIGHT_CCSDH)
STRAIGHT.extend(STRAIGHT_CCSDD)
STRAIGHT.extend(STRAIGHT_CCCSS)
STRAIGHT.extend(STRAIGHT_CCCSC)
STRAIGHT.extend(STRAIGHT_CCCSH)
STRAIGHT.extend(STRAIGHT_CCCSD)
STRAIGHT.extend(STRAIGHT_CCCCS)
STRAIGHT.extend(STRAIGHT_CCCCH)
STRAIGHT.extend(STRAIGHT_CCCCD)
STRAIGHT.extend(STRAIGHT_CCCHS)
STRAIGHT.extend(STRAIGHT_CCCHC)
STRAIGHT.extend(STRAIGHT_CCCHH)
STRAIGHT.extend(STRAIGHT_CCCHD)
STRAIGHT.extend(STRAIGHT_CCCDS)
STRAIGHT.extend(STRAIGHT_CCCDC)
STRAIGHT.extend(STRAIGHT_CCCDH)
STRAIGHT.extend(STRAIGHT_CCCDD)
STRAIGHT.extend(STRAIGHT_CCHSS)
STRAIGHT.extend(STRAIGHT_CCHSC)
STRAIGHT.extend(STRAIGHT_CCHSH)
STRAIGHT.extend(STRAIGHT_CCHSD)
STRAIGHT.extend(STRAIGHT_CCHCS)
STRAIGHT.extend(STRAIGHT_CCHCC)
STRAIGHT.extend(STRAIGHT_CCHCH)
STRAIGHT.extend(STRAIGHT_CCHCD)
STRAIGHT.extend(STRAIGHT_CCHHS)
STRAIGHT.extend(STRAIGHT_CCHHC)
STRAIGHT.extend(STRAIGHT_CCHHH)
STRAIGHT.extend(STRAIGHT_CCHHD)
STRAIGHT.extend(STRAIGHT_CCHDS)
STRAIGHT.extend(STRAIGHT_CCHDC)
STRAIGHT.extend(STRAIGHT_CCHDH)
STRAIGHT.extend(STRAIGHT_CCHDD)
STRAIGHT.extend(STRAIGHT_CCDSS)
STRAIGHT.extend(STRAIGHT_CCDSC)
STRAIGHT.extend(STRAIGHT_CCDSH)
STRAIGHT.extend(STRAIGHT_CCDSD)
STRAIGHT.extend(STRAIGHT_CCDCS)
STRAIGHT.extend(STRAIGHT_CCDCC)
STRAIGHT.extend(STRAIGHT_CCDCH)
STRAIGHT.extend(STRAIGHT_CCDCD)
STRAIGHT.extend(STRAIGHT_CCDHS)
STRAIGHT.extend(STRAIGHT_CCDHC)
STRAIGHT.extend(STRAIGHT_CCDHH)
STRAIGHT.extend(STRAIGHT_CCDHD)
STRAIGHT.extend(STRAIGHT_CCDDS)
STRAIGHT.extend(STRAIGHT_CCDDC)
STRAIGHT.extend(STRAIGHT_CCDDH)
STRAIGHT.extend(STRAIGHT_CCDDD)
STRAIGHT.extend(STRAIGHT_CHSSS)
STRAIGHT.extend(STRAIGHT_CHSSC)
STRAIGHT.extend(STRAIGHT_CHSSH)
STRAIGHT.extend(STRAIGHT_CHSSD)
STRAIGHT.extend(STRAIGHT_CHSCS)
STRAIGHT.extend(STRAIGHT_CHSCC)
STRAIGHT.extend(STRAIGHT_CHSCH)
STRAIGHT.extend(STRAIGHT_CHSCD)
STRAIGHT.extend(STRAIGHT_CHSHS)
STRAIGHT.extend(STRAIGHT_CHSHC)
STRAIGHT.extend(STRAIGHT_CHSHH)
STRAIGHT.extend(STRAIGHT_CHSHD)
STRAIGHT.extend(STRAIGHT_CHSDS)
STRAIGHT.extend(STRAIGHT_CHSDC)
STRAIGHT.extend(STRAIGHT_CHSDH)
STRAIGHT.extend(STRAIGHT_CHSDD)
STRAIGHT.extend(STRAIGHT_CHCSS)
STRAIGHT.extend(STRAIGHT_CHCSC)
STRAIGHT.extend(STRAIGHT_CHCSH)
STRAIGHT.extend(STRAIGHT_CHCSD)
STRAIGHT.extend(STRAIGHT_CHCCS)
STRAIGHT.extend(STRAIGHT_CHCCC)
STRAIGHT.extend(STRAIGHT_CHCCH)
STRAIGHT.extend(STRAIGHT_CHCCD)
STRAIGHT.extend(STRAIGHT_CHCHS)
STRAIGHT.extend(STRAIGHT_CHCHC)
STRAIGHT.extend(STRAIGHT_CHCHH)
STRAIGHT.extend(STRAIGHT_CHCHD)
STRAIGHT.extend(STRAIGHT_CHCDS)
STRAIGHT.extend(STRAIGHT_CHCDC)
STRAIGHT.extend(STRAIGHT_CHCDH)
STRAIGHT.extend(STRAIGHT_CHCDD)
STRAIGHT.extend(STRAIGHT_CHHSS)
STRAIGHT.extend(STRAIGHT_CHHSC)
STRAIGHT.extend(STRAIGHT_CHHSH)
STRAIGHT.extend(STRAIGHT_CHHSD)
STRAIGHT.extend(STRAIGHT_CHHCS)
STRAIGHT.extend(STRAIGHT_CHHCC)
STRAIGHT.extend(STRAIGHT_CHHCH)
STRAIGHT.extend(STRAIGHT_CHHCD)
STRAIGHT.extend(STRAIGHT_CHHHS)
STRAIGHT.extend(STRAIGHT_CHHHC)
STRAIGHT.extend(STRAIGHT_CHHHH)
STRAIGHT.extend(STRAIGHT_CHHHD)
STRAIGHT.extend(STRAIGHT_CHHDS)
STRAIGHT.extend(STRAIGHT_CHHDC)
STRAIGHT.extend(STRAIGHT_CHHDH)
STRAIGHT.extend(STRAIGHT_CHHDD)
STRAIGHT.extend(STRAIGHT_CHDSS)
STRAIGHT.extend(STRAIGHT_CHDSC)
STRAIGHT.extend(STRAIGHT_CHDSH)
STRAIGHT.extend(STRAIGHT_CHDSD)
STRAIGHT.extend(STRAIGHT_CHDCS)
STRAIGHT.extend(STRAIGHT_CHDCC)
STRAIGHT.extend(STRAIGHT_CHDCH)
STRAIGHT.extend(STRAIGHT_CHDCD)
STRAIGHT.extend(STRAIGHT_CHDHS)
STRAIGHT.extend(STRAIGHT_CHDHC)
STRAIGHT.extend(STRAIGHT_CHDHH)
STRAIGHT.extend(STRAIGHT_CHDHD)
STRAIGHT.extend(STRAIGHT_CHDDS)
STRAIGHT.extend(STRAIGHT_CHDDC)
STRAIGHT.extend(STRAIGHT_CHDDH)
STRAIGHT.extend(STRAIGHT_CHDDD)
STRAIGHT.extend(STRAIGHT_CDSSS)
STRAIGHT.extend(STRAIGHT_CDSSC)
STRAIGHT.extend(STRAIGHT_CDSSH)
STRAIGHT.extend(STRAIGHT_CDSSD)
STRAIGHT.extend(STRAIGHT_CDSCS)
STRAIGHT.extend(STRAIGHT_CDSCC)
STRAIGHT.extend(STRAIGHT_CDSCH)
STRAIGHT.extend(STRAIGHT_CDSCD)
STRAIGHT.extend(STRAIGHT_CDSHS)
STRAIGHT.extend(STRAIGHT_CDSHC)
STRAIGHT.extend(STRAIGHT_CDSHH)
STRAIGHT.extend(STRAIGHT_CDSHD)
STRAIGHT.extend(STRAIGHT_CDSDS)
STRAIGHT.extend(STRAIGHT_CDSDC)
STRAIGHT.extend(STRAIGHT_CDSDH)
STRAIGHT.extend(STRAIGHT_CDSDD)
STRAIGHT.extend(STRAIGHT_CDCSS)
STRAIGHT.extend(STRAIGHT_CDCSC)
STRAIGHT.extend(STRAIGHT_CDCSH)
STRAIGHT.extend(STRAIGHT_CDCSD)
STRAIGHT.extend(STRAIGHT_CDCCS)
STRAIGHT.extend(STRAIGHT_CDCCC)
STRAIGHT.extend(STRAIGHT_CDCCH)
STRAIGHT.extend(STRAIGHT_CDCCD)
STRAIGHT.extend(STRAIGHT_CDCHS)
STRAIGHT.extend(STRAIGHT_CDCHC)
STRAIGHT.extend(STRAIGHT_CDCHH)
STRAIGHT.extend(STRAIGHT_CDCHD)
STRAIGHT.extend(STRAIGHT_CDCDS)
STRAIGHT.extend(STRAIGHT_CDCDC)
STRAIGHT.extend(STRAIGHT_CDCDH)
STRAIGHT.extend(STRAIGHT_CDCDD)
STRAIGHT.extend(STRAIGHT_CDHSS)
STRAIGHT.extend(STRAIGHT_CDHSC)
STRAIGHT.extend(STRAIGHT_CDHSH)
STRAIGHT.extend(STRAIGHT_CDHSD)
STRAIGHT.extend(STRAIGHT_CDHCS)
STRAIGHT.extend(STRAIGHT_CDHCC)
STRAIGHT.extend(STRAIGHT_CDHCH)
STRAIGHT.extend(STRAIGHT_CDHCD)
STRAIGHT.extend(STRAIGHT_CDHHS)
STRAIGHT.extend(STRAIGHT_CDHHC)
STRAIGHT.extend(STRAIGHT_CDHHH)
STRAIGHT.extend(STRAIGHT_CDHHD)
STRAIGHT.extend(STRAIGHT_CDHDS)
STRAIGHT.extend(STRAIGHT_CDHDC)
STRAIGHT.extend(STRAIGHT_CDHDH)
STRAIGHT.extend(STRAIGHT_CDHDD)
STRAIGHT.extend(STRAIGHT_CDDSS)
STRAIGHT.extend(STRAIGHT_CDDSC)
STRAIGHT.extend(STRAIGHT_CDDSH)
STRAIGHT.extend(STRAIGHT_CDDSD)
STRAIGHT.extend(STRAIGHT_CDDCS)
STRAIGHT.extend(STRAIGHT_CDDCC)
STRAIGHT.extend(STRAIGHT_CDDCH)
STRAIGHT.extend(STRAIGHT_CDDCD)
STRAIGHT.extend(STRAIGHT_CDDHS)
STRAIGHT.extend(STRAIGHT_CDDHC)
STRAIGHT.extend(STRAIGHT_CDDHH)
STRAIGHT.extend(STRAIGHT_CDDHD)
STRAIGHT.extend(STRAIGHT_CDDDS)
STRAIGHT.extend(STRAIGHT_CDDDC)
STRAIGHT.extend(STRAIGHT_CDDDH)
STRAIGHT.extend(STRAIGHT_CDDDD)
STRAIGHT.extend(STRAIGHT_HSSSS)
STRAIGHT.extend(STRAIGHT_HSSSC)
STRAIGHT.extend(STRAIGHT_HSSSH)
STRAIGHT.extend(STRAIGHT_HSSSD)
STRAIGHT.extend(STRAIGHT_HSSCS)
STRAIGHT.extend(STRAIGHT_HSSCC)
STRAIGHT.extend(STRAIGHT_HSSCH)
STRAIGHT.extend(STRAIGHT_HSSCD)
STRAIGHT.extend(STRAIGHT_HSSHS)
STRAIGHT.extend(STRAIGHT_HSSHC)
STRAIGHT.extend(STRAIGHT_HSSHH)
STRAIGHT.extend(STRAIGHT_HSSHD)
STRAIGHT.extend(STRAIGHT_HSSDS)
STRAIGHT.extend(STRAIGHT_HSSDC)
STRAIGHT.extend(STRAIGHT_HSSDH)
STRAIGHT.extend(STRAIGHT_HSSDD)
STRAIGHT.extend(STRAIGHT_HSCSS)
STRAIGHT.extend(STRAIGHT_HSCSC)
STRAIGHT.extend(STRAIGHT_HSCSH)
STRAIGHT.extend(STRAIGHT_HSCSD)
STRAIGHT.extend(STRAIGHT_HSCCS)
STRAIGHT.extend(STRAIGHT_HSCCC)
STRAIGHT.extend(STRAIGHT_HSCCH)
STRAIGHT.extend(STRAIGHT_HSCCD)
STRAIGHT.extend(STRAIGHT_HSCHS)
STRAIGHT.extend(STRAIGHT_HSCHC)
STRAIGHT.extend(STRAIGHT_HSCHH)
STRAIGHT.extend(STRAIGHT_HSCHD)
STRAIGHT.extend(STRAIGHT_HSCDS)
STRAIGHT.extend(STRAIGHT_HSCDC)
STRAIGHT.extend(STRAIGHT_HSCDH)
STRAIGHT.extend(STRAIGHT_HSCDD)
STRAIGHT.extend(STRAIGHT_HSHSS)
STRAIGHT.extend(STRAIGHT_HSHSC)
STRAIGHT.extend(STRAIGHT_HSHSH)
STRAIGHT.extend(STRAIGHT_HSHSD)
STRAIGHT.extend(STRAIGHT_HSHCS)
STRAIGHT.extend(STRAIGHT_HSHCC)
STRAIGHT.extend(STRAIGHT_HSHCH)
STRAIGHT.extend(STRAIGHT_HSHCD)
STRAIGHT.extend(STRAIGHT_HSHHS)
STRAIGHT.extend(STRAIGHT_HSHHC)
STRAIGHT.extend(STRAIGHT_HSHHH)
STRAIGHT.extend(STRAIGHT_HSHHD)
STRAIGHT.extend(STRAIGHT_HSHDS)
STRAIGHT.extend(STRAIGHT_HSHDC)
STRAIGHT.extend(STRAIGHT_HSHDH)
STRAIGHT.extend(STRAIGHT_HSHDD)
STRAIGHT.extend(STRAIGHT_HSDSS)
STRAIGHT.extend(STRAIGHT_HSDSC)
STRAIGHT.extend(STRAIGHT_HSDSH)
STRAIGHT.extend(STRAIGHT_HSDSD)
STRAIGHT.extend(STRAIGHT_HSDCS)
STRAIGHT.extend(STRAIGHT_HSDCC)
STRAIGHT.extend(STRAIGHT_HSDCH)
STRAIGHT.extend(STRAIGHT_HSDCD)
STRAIGHT.extend(STRAIGHT_HSDHS)
STRAIGHT.extend(STRAIGHT_HSDHC)
STRAIGHT.extend(STRAIGHT_HSDHH)
STRAIGHT.extend(STRAIGHT_HSDHD)
STRAIGHT.extend(STRAIGHT_HSDDS)
STRAIGHT.extend(STRAIGHT_HSDDC)
STRAIGHT.extend(STRAIGHT_HSDDH)
STRAIGHT.extend(STRAIGHT_HSDDD)
STRAIGHT.extend(STRAIGHT_HCSSS)
STRAIGHT.extend(STRAIGHT_HCSSC)
STRAIGHT.extend(STRAIGHT_HCSSH)
STRAIGHT.extend(STRAIGHT_HCSSD)
STRAIGHT.extend(STRAIGHT_HCSCS)
STRAIGHT.extend(STRAIGHT_HCSCC)
STRAIGHT.extend(STRAIGHT_HCSCH)
STRAIGHT.extend(STRAIGHT_HCSCD)
STRAIGHT.extend(STRAIGHT_HCSHS)
STRAIGHT.extend(STRAIGHT_HCSHC)
STRAIGHT.extend(STRAIGHT_HCSHH)
STRAIGHT.extend(STRAIGHT_HCSHD)
STRAIGHT.extend(STRAIGHT_HCSDS)
STRAIGHT.extend(STRAIGHT_HCSDC)
STRAIGHT.extend(STRAIGHT_HCSDH)
STRAIGHT.extend(STRAIGHT_HCSDD)
STRAIGHT.extend(STRAIGHT_HCCSS)
STRAIGHT.extend(STRAIGHT_HCCSC)
STRAIGHT.extend(STRAIGHT_HCCSH)
STRAIGHT.extend(STRAIGHT_HCCSD)
STRAIGHT.extend(STRAIGHT_HCCCS)
STRAIGHT.extend(STRAIGHT_HCCCC)
STRAIGHT.extend(STRAIGHT_HCCCH)
STRAIGHT.extend(STRAIGHT_HCCCD)
STRAIGHT.extend(STRAIGHT_HCCHS)
STRAIGHT.extend(STRAIGHT_HCCHC)
STRAIGHT.extend(STRAIGHT_HCCHH)
STRAIGHT.extend(STRAIGHT_HCCHD)
STRAIGHT.extend(STRAIGHT_HCCDS)
STRAIGHT.extend(STRAIGHT_HCCDC)
STRAIGHT.extend(STRAIGHT_HCCDH)
STRAIGHT.extend(STRAIGHT_HCCDD)
STRAIGHT.extend(STRAIGHT_HCHSS)
STRAIGHT.extend(STRAIGHT_HCHSC)
STRAIGHT.extend(STRAIGHT_HCHSH)
STRAIGHT.extend(STRAIGHT_HCHSD)
STRAIGHT.extend(STRAIGHT_HCHCS)
STRAIGHT.extend(STRAIGHT_HCHCC)
STRAIGHT.extend(STRAIGHT_HCHCH)
STRAIGHT.extend(STRAIGHT_HCHCD)
STRAIGHT.extend(STRAIGHT_HCHHS)
STRAIGHT.extend(STRAIGHT_HCHHC)
STRAIGHT.extend(STRAIGHT_HCHHH)
STRAIGHT.extend(STRAIGHT_HCHHD)
STRAIGHT.extend(STRAIGHT_HCHDS)
STRAIGHT.extend(STRAIGHT_HCHDC)
STRAIGHT.extend(STRAIGHT_HCHDH)
STRAIGHT.extend(STRAIGHT_HCHDD)
STRAIGHT.extend(STRAIGHT_HCDSS)
STRAIGHT.extend(STRAIGHT_HCDSC)
STRAIGHT.extend(STRAIGHT_HCDSH)
STRAIGHT.extend(STRAIGHT_HCDSD)
STRAIGHT.extend(STRAIGHT_HCDCS)
STRAIGHT.extend(STRAIGHT_HCDCC)
STRAIGHT.extend(STRAIGHT_HCDCH)
STRAIGHT.extend(STRAIGHT_HCDCD)
STRAIGHT.extend(STRAIGHT_HCDHS)
STRAIGHT.extend(STRAIGHT_HCDHC)
STRAIGHT.extend(STRAIGHT_HCDHH)
STRAIGHT.extend(STRAIGHT_HCDHD)
STRAIGHT.extend(STRAIGHT_HCDDS)
STRAIGHT.extend(STRAIGHT_HCDDC)
STRAIGHT.extend(STRAIGHT_HCDDH)
STRAIGHT.extend(STRAIGHT_HCDDD)
STRAIGHT.extend(STRAIGHT_HHSSS)
STRAIGHT.extend(STRAIGHT_HHSSC)
STRAIGHT.extend(STRAIGHT_HHSSH)
STRAIGHT.extend(STRAIGHT_HHSSD)
STRAIGHT.extend(STRAIGHT_HHSCS)
STRAIGHT.extend(STRAIGHT_HHSCC)
STRAIGHT.extend(STRAIGHT_HHSCH)
STRAIGHT.extend(STRAIGHT_HHSCD)
STRAIGHT.extend(STRAIGHT_HHSHS)
STRAIGHT.extend(STRAIGHT_HHSHC)
STRAIGHT.extend(STRAIGHT_HHSHH)
STRAIGHT.extend(STRAIGHT_HHSHD)
STRAIGHT.extend(STRAIGHT_HHSDS)
STRAIGHT.extend(STRAIGHT_HHSDC)
STRAIGHT.extend(STRAIGHT_HHSDH)
STRAIGHT.extend(STRAIGHT_HHSDD)
STRAIGHT.extend(STRAIGHT_HHCSS)
STRAIGHT.extend(STRAIGHT_HHCSC)
STRAIGHT.extend(STRAIGHT_HHCSH)
STRAIGHT.extend(STRAIGHT_HHCSD)
STRAIGHT.extend(STRAIGHT_HHCCS)
STRAIGHT.extend(STRAIGHT_HHCCC)
STRAIGHT.extend(STRAIGHT_HHCCH)
STRAIGHT.extend(STRAIGHT_HHCCD)
STRAIGHT.extend(STRAIGHT_HHCHS)
STRAIGHT.extend(STRAIGHT_HHCHC)
STRAIGHT.extend(STRAIGHT_HHCHH)
STRAIGHT.extend(STRAIGHT_HHCHD)
STRAIGHT.extend(STRAIGHT_HHCDS)
STRAIGHT.extend(STRAIGHT_HHCDC)
STRAIGHT.extend(STRAIGHT_HHCDH)
STRAIGHT.extend(STRAIGHT_HHCDD)
STRAIGHT.extend(STRAIGHT_HHHSS)
STRAIGHT.extend(STRAIGHT_HHHSC)
STRAIGHT.extend(STRAIGHT_HHHSH)
STRAIGHT.extend(STRAIGHT_HHHSD)
STRAIGHT.extend(STRAIGHT_HHHCS)
STRAIGHT.extend(STRAIGHT_HHHCC)
STRAIGHT.extend(STRAIGHT_HHHCH)
STRAIGHT.extend(STRAIGHT_HHHCD)
STRAIGHT.extend(STRAIGHT_HHHHS)
STRAIGHT.extend(STRAIGHT_HHHHC)
STRAIGHT.extend(STRAIGHT_HHHHD)
STRAIGHT.extend(STRAIGHT_HHHDS)
STRAIGHT.extend(STRAIGHT_HHHDC)
STRAIGHT.extend(STRAIGHT_HHHDH)
STRAIGHT.extend(STRAIGHT_HHHDD)
STRAIGHT.extend(STRAIGHT_HHDSS)
STRAIGHT.extend(STRAIGHT_HHDSC)
STRAIGHT.extend(STRAIGHT_HHDSH)
STRAIGHT.extend(STRAIGHT_HHDSD)
STRAIGHT.extend(STRAIGHT_HHDCS)
STRAIGHT.extend(STRAIGHT_HHDCC)
STRAIGHT.extend(STRAIGHT_HHDCH)
STRAIGHT.extend(STRAIGHT_HHDCD)
STRAIGHT.extend(STRAIGHT_HHDHS)
STRAIGHT.extend(STRAIGHT_HHDHC)
STRAIGHT.extend(STRAIGHT_HHDHH)
STRAIGHT.extend(STRAIGHT_HHDHD)
STRAIGHT.extend(STRAIGHT_HHDDS)
STRAIGHT.extend(STRAIGHT_HHDDC)
STRAIGHT.extend(STRAIGHT_HHDDH)
STRAIGHT.extend(STRAIGHT_HHDDD)
STRAIGHT.extend(STRAIGHT_HDSSS)
STRAIGHT.extend(STRAIGHT_HDSSC)
STRAIGHT.extend(STRAIGHT_HDSSH)
STRAIGHT.extend(STRAIGHT_HDSSD)
STRAIGHT.extend(STRAIGHT_HDSCS)
STRAIGHT.extend(STRAIGHT_HDSCC)
STRAIGHT.extend(STRAIGHT_HDSCH)
STRAIGHT.extend(STRAIGHT_HDSCD)
STRAIGHT.extend(STRAIGHT_HDSHS)
STRAIGHT.extend(STRAIGHT_HDSHC)
STRAIGHT.extend(STRAIGHT_HDSHH)
STRAIGHT.extend(STRAIGHT_HDSHD)
STRAIGHT.extend(STRAIGHT_HDSDS)
STRAIGHT.extend(STRAIGHT_HDSDC)
STRAIGHT.extend(STRAIGHT_HDSDH)
STRAIGHT.extend(STRAIGHT_HDSDD)
STRAIGHT.extend(STRAIGHT_HDCSS)
STRAIGHT.extend(STRAIGHT_HDCSC)
STRAIGHT.extend(STRAIGHT_HDCSH)
STRAIGHT.extend(STRAIGHT_HDCSD)
STRAIGHT.extend(STRAIGHT_HDCCS)
STRAIGHT.extend(STRAIGHT_HDCCC)
STRAIGHT.extend(STRAIGHT_HDCCH)
STRAIGHT.extend(STRAIGHT_HDCCD)
STRAIGHT.extend(STRAIGHT_HDCHS)
STRAIGHT.extend(STRAIGHT_HDCHC)
STRAIGHT.extend(STRAIGHT_HDCHH)
STRAIGHT.extend(STRAIGHT_HDCHD)
STRAIGHT.extend(STRAIGHT_HDCDS)
STRAIGHT.extend(STRAIGHT_HDCDC)
STRAIGHT.extend(STRAIGHT_HDCDH)
STRAIGHT.extend(STRAIGHT_HDCDD)
STRAIGHT.extend(STRAIGHT_HDHSS)
STRAIGHT.extend(STRAIGHT_HDHSC)
STRAIGHT.extend(STRAIGHT_HDHSH)
STRAIGHT.extend(STRAIGHT_HDHSD)
STRAIGHT.extend(STRAIGHT_HDHCS)
STRAIGHT.extend(STRAIGHT_HDHCC)
STRAIGHT.extend(STRAIGHT_HDHCH)
STRAIGHT.extend(STRAIGHT_HDHCD)
STRAIGHT.extend(STRAIGHT_HDHHS)
STRAIGHT.extend(STRAIGHT_HDHHC)
STRAIGHT.extend(STRAIGHT_HDHHH)
STRAIGHT.extend(STRAIGHT_HDHHD)
STRAIGHT.extend(STRAIGHT_HDHDS)
STRAIGHT.extend(STRAIGHT_HDHDC)
STRAIGHT.extend(STRAIGHT_HDHDH)
STRAIGHT.extend(STRAIGHT_HDHDD)
STRAIGHT.extend(STRAIGHT_HDDSS)
STRAIGHT.extend(STRAIGHT_HDDSC)
STRAIGHT.extend(STRAIGHT_HDDSH)
STRAIGHT.extend(STRAIGHT_HDDSD)
STRAIGHT.extend(STRAIGHT_HDDCS)
STRAIGHT.extend(STRAIGHT_HDDCC)
STRAIGHT.extend(STRAIGHT_HDDCH)
STRAIGHT.extend(STRAIGHT_HDDCD)
STRAIGHT.extend(STRAIGHT_HDDHS)
STRAIGHT.extend(STRAIGHT_HDDHC)
STRAIGHT.extend(STRAIGHT_HDDHH)
STRAIGHT.extend(STRAIGHT_HDDHD)
STRAIGHT.extend(STRAIGHT_HDDDS)
STRAIGHT.extend(STRAIGHT_HDDDC)
STRAIGHT.extend(STRAIGHT_HDDDH)
STRAIGHT.extend(STRAIGHT_HDDDD)
STRAIGHT.extend(STRAIGHT_DSSSS)
STRAIGHT.extend(STRAIGHT_DSSSC)
STRAIGHT.extend(STRAIGHT_DSSSH)
STRAIGHT.extend(STRAIGHT_DSSSD)
STRAIGHT.extend(STRAIGHT_DSSCS)
STRAIGHT.extend(STRAIGHT_DSSCC)
STRAIGHT.extend(STRAIGHT_DSSCH)
STRAIGHT.extend(STRAIGHT_DSSCD)
STRAIGHT.extend(STRAIGHT_DSSHS)
STRAIGHT.extend(STRAIGHT_DSSHC)
STRAIGHT.extend(STRAIGHT_DSSHH)
STRAIGHT.extend(STRAIGHT_DSSHD)
STRAIGHT.extend(STRAIGHT_DSSDS)
STRAIGHT.extend(STRAIGHT_DSSDC)
STRAIGHT.extend(STRAIGHT_DSSDH)
STRAIGHT.extend(STRAIGHT_DSSDD)
STRAIGHT.extend(STRAIGHT_DSCSS)
STRAIGHT.extend(STRAIGHT_DSCSC)
STRAIGHT.extend(STRAIGHT_DSCSH)
STRAIGHT.extend(STRAIGHT_DSCSD)
STRAIGHT.extend(STRAIGHT_DSCCS)
STRAIGHT.extend(STRAIGHT_DSCCC)
STRAIGHT.extend(STRAIGHT_DSCCH)
STRAIGHT.extend(STRAIGHT_DSCCD)
STRAIGHT.extend(STRAIGHT_DSCHS)
STRAIGHT.extend(STRAIGHT_DSCHC)
STRAIGHT.extend(STRAIGHT_DSCHH)
STRAIGHT.extend(STRAIGHT_DSCHD)
STRAIGHT.extend(STRAIGHT_DSCDS)
STRAIGHT.extend(STRAIGHT_DSCDC)
STRAIGHT.extend(STRAIGHT_DSCDH)
STRAIGHT.extend(STRAIGHT_DSCDD)
STRAIGHT.extend(STRAIGHT_DSHSS)
STRAIGHT.extend(STRAIGHT_DSHSC)
STRAIGHT.extend(STRAIGHT_DSHSH)
STRAIGHT.extend(STRAIGHT_DSHSD)
STRAIGHT.extend(STRAIGHT_DSHCS)
STRAIGHT.extend(STRAIGHT_DSHCC)
STRAIGHT.extend(STRAIGHT_DSHCH)
STRAIGHT.extend(STRAIGHT_DSHCD)
STRAIGHT.extend(STRAIGHT_DSHHS)
STRAIGHT.extend(STRAIGHT_DSHHC)
STRAIGHT.extend(STRAIGHT_DSHHH)
STRAIGHT.extend(STRAIGHT_DSHHD)
STRAIGHT.extend(STRAIGHT_DSHDS)
STRAIGHT.extend(STRAIGHT_DSHDC)
STRAIGHT.extend(STRAIGHT_DSHDH)
STRAIGHT.extend(STRAIGHT_DSHDD)
STRAIGHT.extend(STRAIGHT_DSDSS)
STRAIGHT.extend(STRAIGHT_DSDSC)
STRAIGHT.extend(STRAIGHT_DSDSH)
STRAIGHT.extend(STRAIGHT_DSDSD)
STRAIGHT.extend(STRAIGHT_DSDCS)
STRAIGHT.extend(STRAIGHT_DSDCC)
STRAIGHT.extend(STRAIGHT_DSDCH)
STRAIGHT.extend(STRAIGHT_DSDCD)
STRAIGHT.extend(STRAIGHT_DSDHS)
STRAIGHT.extend(STRAIGHT_DSDHC)
STRAIGHT.extend(STRAIGHT_DSDHH)
STRAIGHT.extend(STRAIGHT_DSDHD)
STRAIGHT.extend(STRAIGHT_DSDDS)
STRAIGHT.extend(STRAIGHT_DSDDC)
STRAIGHT.extend(STRAIGHT_DSDDH)
STRAIGHT.extend(STRAIGHT_DSDDD)
STRAIGHT.extend(STRAIGHT_DCSSS)
STRAIGHT.extend(STRAIGHT_DCSSC)
STRAIGHT.extend(STRAIGHT_DCSSH)
STRAIGHT.extend(STRAIGHT_DCSSD)
STRAIGHT.extend(STRAIGHT_DCSCS)
STRAIGHT.extend(STRAIGHT_DCSCC)
STRAIGHT.extend(STRAIGHT_DCSCH)
STRAIGHT.extend(STRAIGHT_DCSCD)
STRAIGHT.extend(STRAIGHT_DCSHS)
STRAIGHT.extend(STRAIGHT_DCSHC)
STRAIGHT.extend(STRAIGHT_DCSHH)
STRAIGHT.extend(STRAIGHT_DCSHD)
STRAIGHT.extend(STRAIGHT_DCSDS)
STRAIGHT.extend(STRAIGHT_DCSDC)
STRAIGHT.extend(STRAIGHT_DCSDH)
STRAIGHT.extend(STRAIGHT_DCSDD)
STRAIGHT.extend(STRAIGHT_DCCSS)
STRAIGHT.extend(STRAIGHT_DCCSC)
STRAIGHT.extend(STRAIGHT_DCCSH)
STRAIGHT.extend(STRAIGHT_DCCSD)
STRAIGHT.extend(STRAIGHT_DCCCS)
STRAIGHT.extend(STRAIGHT_DCCCC)
STRAIGHT.extend(STRAIGHT_DCCCH)
STRAIGHT.extend(STRAIGHT_DCCCD)
STRAIGHT.extend(STRAIGHT_DCCHS)
STRAIGHT.extend(STRAIGHT_DCCHC)
STRAIGHT.extend(STRAIGHT_DCCHH)
STRAIGHT.extend(STRAIGHT_DCCHD)
STRAIGHT.extend(STRAIGHT_DCCDS)
STRAIGHT.extend(STRAIGHT_DCCDC)
STRAIGHT.extend(STRAIGHT_DCCDH)
STRAIGHT.extend(STRAIGHT_DCCDD)
STRAIGHT.extend(STRAIGHT_DCHSS)
STRAIGHT.extend(STRAIGHT_DCHSC)
STRAIGHT.extend(STRAIGHT_DCHSH)
STRAIGHT.extend(STRAIGHT_DCHSD)
STRAIGHT.extend(STRAIGHT_DCHCS)
STRAIGHT.extend(STRAIGHT_DCHCC)
STRAIGHT.extend(STRAIGHT_DCHCH)
STRAIGHT.extend(STRAIGHT_DCHCD)
STRAIGHT.extend(STRAIGHT_DCHHS)
STRAIGHT.extend(STRAIGHT_DCHHC)
STRAIGHT.extend(STRAIGHT_DCHHH)
STRAIGHT.extend(STRAIGHT_DCHHD)
STRAIGHT.extend(STRAIGHT_DCHDS)
STRAIGHT.extend(STRAIGHT_DCHDC)
STRAIGHT.extend(STRAIGHT_DCHDH)
STRAIGHT.extend(STRAIGHT_DCHDD)
STRAIGHT.extend(STRAIGHT_DCDSS)
STRAIGHT.extend(STRAIGHT_DCDSC)
STRAIGHT.extend(STRAIGHT_DCDSH)
STRAIGHT.extend(STRAIGHT_DCDSD)
STRAIGHT.extend(STRAIGHT_DCDCS)
STRAIGHT.extend(STRAIGHT_DCDCC)
STRAIGHT.extend(STRAIGHT_DCDCH)
STRAIGHT.extend(STRAIGHT_DCDCD)
STRAIGHT.extend(STRAIGHT_DCDHS)
STRAIGHT.extend(STRAIGHT_DCDHC)
STRAIGHT.extend(STRAIGHT_DCDHH)
STRAIGHT.extend(STRAIGHT_DCDHD)
STRAIGHT.extend(STRAIGHT_DCDDS)
STRAIGHT.extend(STRAIGHT_DCDDC)
STRAIGHT.extend(STRAIGHT_DCDDH)
STRAIGHT.extend(STRAIGHT_DCDDD)
STRAIGHT.extend(STRAIGHT_DHSSS)
STRAIGHT.extend(STRAIGHT_DHSSC)
STRAIGHT.extend(STRAIGHT_DHSSH)
STRAIGHT.extend(STRAIGHT_DHSSD)
STRAIGHT.extend(STRAIGHT_DHSCS)
STRAIGHT.extend(STRAIGHT_DHSCC)
STRAIGHT.extend(STRAIGHT_DHSCH)
STRAIGHT.extend(STRAIGHT_DHSCD)
STRAIGHT.extend(STRAIGHT_DHSHS)
STRAIGHT.extend(STRAIGHT_DHSHC)
STRAIGHT.extend(STRAIGHT_DHSHH)
STRAIGHT.extend(STRAIGHT_DHSHD)
STRAIGHT.extend(STRAIGHT_DHSDS)
STRAIGHT.extend(STRAIGHT_DHSDC)
STRAIGHT.extend(STRAIGHT_DHSDH)
STRAIGHT.extend(STRAIGHT_DHSDD)
STRAIGHT.extend(STRAIGHT_DHCSS)
STRAIGHT.extend(STRAIGHT_DHCSC)
STRAIGHT.extend(STRAIGHT_DHCSH)
STRAIGHT.extend(STRAIGHT_DHCSD)
STRAIGHT.extend(STRAIGHT_DHCCS)
STRAIGHT.extend(STRAIGHT_DHCCC)
STRAIGHT.extend(STRAIGHT_DHCCH)
STRAIGHT.extend(STRAIGHT_DHCCD)
STRAIGHT.extend(STRAIGHT_DHCHS)
STRAIGHT.extend(STRAIGHT_DHCHC)
STRAIGHT.extend(STRAIGHT_DHCHH)
STRAIGHT.extend(STRAIGHT_DHCHD)
STRAIGHT.extend(STRAIGHT_DHCDS)
STRAIGHT.extend(STRAIGHT_DHCDC)
STRAIGHT.extend(STRAIGHT_DHCDH)
STRAIGHT.extend(STRAIGHT_DHCDD)
STRAIGHT.extend(STRAIGHT_DHHSS)
STRAIGHT.extend(STRAIGHT_DHHSC)
STRAIGHT.extend(STRAIGHT_DHHSH)
STRAIGHT.extend(STRAIGHT_DHHSD)
STRAIGHT.extend(STRAIGHT_DHHCS)
STRAIGHT.extend(STRAIGHT_DHHCC)
STRAIGHT.extend(STRAIGHT_DHHCH)
STRAIGHT.extend(STRAIGHT_DHHCD)
STRAIGHT.extend(STRAIGHT_DHHHS)
STRAIGHT.extend(STRAIGHT_DHHHC)
STRAIGHT.extend(STRAIGHT_DHHHH)
STRAIGHT.extend(STRAIGHT_DHHHD)
STRAIGHT.extend(STRAIGHT_DHHDS)
STRAIGHT.extend(STRAIGHT_DHHDC)
STRAIGHT.extend(STRAIGHT_DHHDH)
STRAIGHT.extend(STRAIGHT_DHHDD)
STRAIGHT.extend(STRAIGHT_DHDSS)
STRAIGHT.extend(STRAIGHT_DHDSC)
STRAIGHT.extend(STRAIGHT_DHDSH)
STRAIGHT.extend(STRAIGHT_DHDSD)
STRAIGHT.extend(STRAIGHT_DHDCS)
STRAIGHT.extend(STRAIGHT_DHDCC)
STRAIGHT.extend(STRAIGHT_DHDCH)
STRAIGHT.extend(STRAIGHT_DHDCD)
STRAIGHT.extend(STRAIGHT_DHDHS)
STRAIGHT.extend(STRAIGHT_DHDHC)
STRAIGHT.extend(STRAIGHT_DHDHH)
STRAIGHT.extend(STRAIGHT_DHDHD)
STRAIGHT.extend(STRAIGHT_DHDDS)
STRAIGHT.extend(STRAIGHT_DHDDC)
STRAIGHT.extend(STRAIGHT_DHDDH)
STRAIGHT.extend(STRAIGHT_DHDDD)
STRAIGHT.extend(STRAIGHT_DDSSS)
STRAIGHT.extend(STRAIGHT_DDSSC)
STRAIGHT.extend(STRAIGHT_DDSSH)
STRAIGHT.extend(STRAIGHT_DDSSD)
STRAIGHT.extend(STRAIGHT_DDSCS)
STRAIGHT.extend(STRAIGHT_DDSCC)
STRAIGHT.extend(STRAIGHT_DDSCH)
STRAIGHT.extend(STRAIGHT_DDSCD)
STRAIGHT.extend(STRAIGHT_DDSHS)
STRAIGHT.extend(STRAIGHT_DDSHC)
STRAIGHT.extend(STRAIGHT_DDSHH)
STRAIGHT.extend(STRAIGHT_DDSHD)
STRAIGHT.extend(STRAIGHT_DDSDS)
STRAIGHT.extend(STRAIGHT_DDSDC)
STRAIGHT.extend(STRAIGHT_DDSDH)
STRAIGHT.extend(STRAIGHT_DDSDD)
STRAIGHT.extend(STRAIGHT_DDCSS)
STRAIGHT.extend(STRAIGHT_DDCSC)
STRAIGHT.extend(STRAIGHT_DDCSH)
STRAIGHT.extend(STRAIGHT_DDCSD)
STRAIGHT.extend(STRAIGHT_DDCCS)
STRAIGHT.extend(STRAIGHT_DDCCC)
STRAIGHT.extend(STRAIGHT_DDCCH)
STRAIGHT.extend(STRAIGHT_DDCCD)
STRAIGHT.extend(STRAIGHT_DDCHS)
STRAIGHT.extend(STRAIGHT_DDCHC)
STRAIGHT.extend(STRAIGHT_DDCHH)
STRAIGHT.extend(STRAIGHT_DDCHD)
STRAIGHT.extend(STRAIGHT_DDCDS)
STRAIGHT.extend(STRAIGHT_DDCDC)
STRAIGHT.extend(STRAIGHT_DDCDH)
STRAIGHT.extend(STRAIGHT_DDCDD)
STRAIGHT.extend(STRAIGHT_DDHSS)
STRAIGHT.extend(STRAIGHT_DDHSC)
STRAIGHT.extend(STRAIGHT_DDHSH)
STRAIGHT.extend(STRAIGHT_DDHSD)
STRAIGHT.extend(STRAIGHT_DDHCS)
STRAIGHT.extend(STRAIGHT_DDHCC)
STRAIGHT.extend(STRAIGHT_DDHCH)
STRAIGHT.extend(STRAIGHT_DDHCD)
STRAIGHT.extend(STRAIGHT_DDHHS)
STRAIGHT.extend(STRAIGHT_DDHHC)
STRAIGHT.extend(STRAIGHT_DDHHH)
STRAIGHT.extend(STRAIGHT_DDHHD)
STRAIGHT.extend(STRAIGHT_DDHDS)
STRAIGHT.extend(STRAIGHT_DDHDC)
STRAIGHT.extend(STRAIGHT_DDHDH)
STRAIGHT.extend(STRAIGHT_DDHDD)
STRAIGHT.extend(STRAIGHT_DDDSS)
STRAIGHT.extend(STRAIGHT_DDDSC)
STRAIGHT.extend(STRAIGHT_DDDSH)
STRAIGHT.extend(STRAIGHT_DDDSD)
STRAIGHT.extend(STRAIGHT_DDDCS)
STRAIGHT.extend(STRAIGHT_DDDCC)
STRAIGHT.extend(STRAIGHT_DDDCH)
STRAIGHT.extend(STRAIGHT_DDDCD)
STRAIGHT.extend(STRAIGHT_DDDHS)
STRAIGHT.extend(STRAIGHT_DDDHC)
STRAIGHT.extend(STRAIGHT_DDDHH)
STRAIGHT.extend(STRAIGHT_DDDHD)
STRAIGHT.extend(STRAIGHT_DDDDS)
STRAIGHT.extend(STRAIGHT_DDDDC)
STRAIGHT.extend(STRAIGHT_DDDDH)
