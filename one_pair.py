import deck
import copy

S = copy.deepcopy(deck.SPADES)
C = copy.deepcopy(deck.CLUBS)
H = copy.deepcopy(deck.HEARTS)
D = copy.deepcopy(deck.DIAMONDS)

ONE_PAIR_SCSSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSSS.append({S[i], C[i], S[j], S[k], S[l]})

ONE_PAIR_SCSSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSSC.append({S[i], C[i], S[j], S[k], C[l]})

ONE_PAIR_SCSSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSSH.append({S[i], C[i], S[j], S[k], H[l]})

ONE_PAIR_SCSSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSSD.append({S[i], C[i], S[j], S[k], D[l]})

ONE_PAIR_SCSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSCS.append({S[i], C[i], S[j], C[k], S[l]})

ONE_PAIR_SCSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSCC.append({S[i], C[i], S[j], C[k], C[l]})

ONE_PAIR_SCSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSCH.append({S[i], C[i], S[j], C[k], H[l]})

ONE_PAIR_SCSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSCD.append({S[i], C[i], S[j], C[k], D[l]})

ONE_PAIR_SCSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSHS.append({S[i], C[i], S[j], H[k], S[l]})

ONE_PAIR_SCSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSHC.append({S[i], C[i], S[j], H[k], C[l]})

ONE_PAIR_SCSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSHH.append({S[i], C[i], S[j], H[k], H[l]})

ONE_PAIR_SCSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSHD.append({S[i], C[i], S[j], H[k], D[l]})

ONE_PAIR_SCSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSDS.append({S[i], C[i], S[j], D[k], S[l]})

ONE_PAIR_SCSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSDC.append({S[i], C[i], S[j], D[k], C[l]})

ONE_PAIR_SCSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSDH.append({S[i], C[i], S[j], D[k], H[l]})

ONE_PAIR_SCSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCSDD.append({S[i], C[i], S[j], D[k], D[l]})
ONE_PAIR_SCCSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCSS.append({S[i], C[i], C[j], S[k], S[l]})

ONE_PAIR_SCCSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCSC.append({S[i], C[i], C[j], S[k], C[l]})

ONE_PAIR_SCCSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCSH.append({S[i], C[i], C[j], S[k], H[l]})

ONE_PAIR_SCCSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCSD.append({S[i], C[i], C[j], S[k], D[l]})

ONE_PAIR_SCCCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCCS.append({S[i], C[i], C[j], C[k], S[l]})

ONE_PAIR_SCCCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCCC.append({S[i], C[i], C[j], C[k], C[l]})

ONE_PAIR_SCCCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCCH.append({S[i], C[i], C[j], C[k], H[l]})

ONE_PAIR_SCCCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCCD.append({S[i], C[i], C[j], C[k], D[l]})

ONE_PAIR_SCCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCHS.append({S[i], C[i], C[j], H[k], S[l]})

ONE_PAIR_SCCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCHC.append({S[i], C[i], C[j], H[k], C[l]})

ONE_PAIR_SCCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCHH.append({S[i], C[i], C[j], H[k], H[l]})

ONE_PAIR_SCCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCHD.append({S[i], C[i], C[j], H[k], D[l]})

ONE_PAIR_SCCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCDS.append({S[i], C[i], C[j], D[k], S[l]})

ONE_PAIR_SCCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCDC.append({S[i], C[i], C[j], D[k], C[l]})

ONE_PAIR_SCCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCDH.append({S[i], C[i], C[j], D[k], H[l]})

ONE_PAIR_SCCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCCDD.append({S[i], C[i], C[j], D[k], D[l]})

ONE_PAIR_SCHSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHSS.append({S[i], C[i], H[j], S[k], S[l]})

ONE_PAIR_SCHSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHSC.append({S[i], C[i], H[j], S[k], C[l]})

ONE_PAIR_SCHSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHSH.append({S[i], C[i], H[j], S[k], H[l]})

ONE_PAIR_SCHSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHSD.append({S[i], C[i], H[j], S[k], D[l]})

ONE_PAIR_SCHCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHCS.append({S[i], C[i], H[j], C[k], S[l]})

ONE_PAIR_SCHCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHCC.append({S[i], C[i], H[j], C[k], C[l]})

ONE_PAIR_SCHCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHCH.append({S[i], C[i], H[j], C[k], H[l]})

ONE_PAIR_SCHCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHCD.append({S[i], C[i], H[j], C[k], D[l]})

ONE_PAIR_SCHHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHHS.append({S[i], C[i], H[j], H[k], S[l]})

ONE_PAIR_SCHHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHHC.append({S[i], C[i], H[j], H[k], C[l]})

ONE_PAIR_SCHHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHHH.append({S[i], C[i], H[j], H[k], H[l]})

ONE_PAIR_SCHHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHHD.append({S[i], C[i], H[j], H[k], D[l]})

ONE_PAIR_SCHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHDS.append({S[i], C[i], H[j], D[k], S[l]})

ONE_PAIR_SCHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHDC.append({S[i], C[i], H[j], D[k], C[l]})

ONE_PAIR_SCHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHDH.append({S[i], C[i], H[j], D[k], H[l]})

ONE_PAIR_SCHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCHDD.append({S[i], C[i], H[j], D[k], D[l]})

ONE_PAIR_SCDSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDSS.append({S[i], C[i], D[j], S[k], S[l]})

ONE_PAIR_SCDSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDSC.append({S[i], C[i], D[j], S[k], C[l]})

ONE_PAIR_SCDSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDSH.append({S[i], C[i], D[j], S[k], H[l]})

ONE_PAIR_SCDSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDSD.append({S[i], C[i], D[j], S[k], D[l]})

ONE_PAIR_SCDCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDCS.append({S[i], C[i], D[j], C[k], S[l]})

ONE_PAIR_SCDCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDCC.append({S[i], C[i], D[j], C[k], C[l]})

ONE_PAIR_SCDCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDCH.append({S[i], C[i], D[j], C[k], H[l]})

ONE_PAIR_SCDCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDCD.append({S[i], C[i], D[j], C[k], D[l]})

ONE_PAIR_SCDHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDHS.append({S[i], C[i], D[j], H[k], S[l]})

ONE_PAIR_SCDHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDHC.append({S[i], C[i], D[j], H[k], C[l]})

ONE_PAIR_SCDHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDHH.append({S[i], C[i], D[j], H[k], H[l]})

ONE_PAIR_SCDHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDHD.append({S[i], C[i], D[j], H[k], D[l]})

ONE_PAIR_SCDDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDDS.append({S[i], C[i], D[j], D[k], S[l]})

ONE_PAIR_SCDDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDDC.append({S[i], C[i], D[j], D[k], C[l]})

ONE_PAIR_SCDDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDDH.append({S[i], C[i], D[j], D[k], H[l]})

ONE_PAIR_SCDDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SCDDD.append({S[i], C[i], D[j], D[k], D[l]})

ONE_PAIR_SHSSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSSS.append({S[i], H[i], S[j], S[k], S[l]})

ONE_PAIR_SHSSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSSC.append({S[i], H[i], S[j], S[k], C[l]})

ONE_PAIR_SHSSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSSH.append({S[i], H[i], S[j], S[k], H[l]})

ONE_PAIR_SHSSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSSD.append({S[i], H[i], S[j], S[k], D[l]})

ONE_PAIR_SHSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSCS.append({S[i], H[i], S[j], C[k], S[l]})

ONE_PAIR_SHSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSCC.append({S[i], H[i], S[j], C[k], C[l]})

ONE_PAIR_SHSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSCH.append({S[i], H[i], S[j], C[k], H[l]})

ONE_PAIR_SHSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSCD.append({S[i], H[i], S[j], C[k], D[l]})

ONE_PAIR_SHSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSHS.append({S[i], H[i], S[j], H[k], S[l]})

ONE_PAIR_SHSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSHC.append({S[i], H[i], S[j], H[k], C[l]})

ONE_PAIR_SHSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSHH.append({S[i], H[i], S[j], H[k], H[l]})

ONE_PAIR_SHSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSHD.append({S[i], H[i], S[j], H[k], D[l]})

ONE_PAIR_SHSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSDS.append({S[i], H[i], S[j], D[k], S[l]})

ONE_PAIR_SHSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSDC.append({S[i], H[i], S[j], D[k], C[l]})

ONE_PAIR_SHSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSDH.append({S[i], H[i], S[j], D[k], H[l]})

ONE_PAIR_SHSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHSDD.append({S[i], H[i], S[j], D[k], D[l]})
ONE_PAIR_SHCSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCSS.append({S[i], H[i], C[j], S[k], S[l]})

ONE_PAIR_SHCSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCSC.append({S[i], H[i], C[j], S[k], C[l]})

ONE_PAIR_SHCSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCSH.append({S[i], H[i], C[j], S[k], H[l]})

ONE_PAIR_SHCSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCSD.append({S[i], H[i], C[j], S[k], D[l]})

ONE_PAIR_SHCCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCCS.append({S[i], H[i], C[j], C[k], S[l]})

ONE_PAIR_SHCCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCCC.append({S[i], H[i], C[j], C[k], C[l]})

ONE_PAIR_SHCCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCCH.append({S[i], H[i], C[j], C[k], H[l]})

ONE_PAIR_SHCCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCCD.append({S[i], H[i], C[j], C[k], D[l]})

ONE_PAIR_SHCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCHS.append({S[i], H[i], C[j], H[k], S[l]})

ONE_PAIR_SHCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCHC.append({S[i], H[i], C[j], H[k], C[l]})

ONE_PAIR_SHCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCHH.append({S[i], H[i], C[j], H[k], H[l]})

ONE_PAIR_SHCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCHD.append({S[i], H[i], C[j], H[k], D[l]})

ONE_PAIR_SHCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCDS.append({S[i], H[i], C[j], D[k], S[l]})

ONE_PAIR_SHCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCDC.append({S[i], H[i], C[j], D[k], C[l]})

ONE_PAIR_SHCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCDH.append({S[i], H[i], C[j], D[k], H[l]})

ONE_PAIR_SHCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHCDD.append({S[i], H[i], C[j], D[k], D[l]})

ONE_PAIR_SHHSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHSS.append({S[i], H[i], H[j], S[k], S[l]})

ONE_PAIR_SHHSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHSC.append({S[i], H[i], H[j], S[k], C[l]})

ONE_PAIR_SHHSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHSH.append({S[i], H[i], H[j], S[k], H[l]})

ONE_PAIR_SHHSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHSD.append({S[i], H[i], H[j], S[k], D[l]})

ONE_PAIR_SHHCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHCS.append({S[i], H[i], H[j], C[k], S[l]})

ONE_PAIR_SHHCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHCC.append({S[i], H[i], H[j], C[k], C[l]})

ONE_PAIR_SHHCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHCH.append({S[i], H[i], H[j], C[k], H[l]})

ONE_PAIR_SHHCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHCD.append({S[i], H[i], H[j], C[k], D[l]})

ONE_PAIR_SHHHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHHS.append({S[i], H[i], H[j], H[k], S[l]})

ONE_PAIR_SHHHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHHC.append({S[i], H[i], H[j], H[k], C[l]})

ONE_PAIR_SHHHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHHH.append({S[i], H[i], H[j], H[k], H[l]})

ONE_PAIR_SHHHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHHD.append({S[i], H[i], H[j], H[k], D[l]})

ONE_PAIR_SHHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHDS.append({S[i], H[i], H[j], D[k], S[l]})

ONE_PAIR_SHHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHDC.append({S[i], H[i], H[j], D[k], C[l]})

ONE_PAIR_SHHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHDH.append({S[i], H[i], H[j], D[k], H[l]})

ONE_PAIR_SHHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHHDD.append({S[i], H[i], H[j], D[k], D[l]})

ONE_PAIR_SHDSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDSS.append({S[i], H[i], D[j], S[k], S[l]})

ONE_PAIR_SHDSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDSC.append({S[i], H[i], D[j], S[k], C[l]})

ONE_PAIR_SHDSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDSH.append({S[i], H[i], D[j], S[k], H[l]})

ONE_PAIR_SHDSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDSD.append({S[i], H[i], D[j], S[k], D[l]})

ONE_PAIR_SHDCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDCS.append({S[i], H[i], D[j], C[k], S[l]})

ONE_PAIR_SHDCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDCC.append({S[i], H[i], D[j], C[k], C[l]})

ONE_PAIR_SHDCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDCH.append({S[i], H[i], D[j], C[k], H[l]})

ONE_PAIR_SHDCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDCD.append({S[i], H[i], D[j], C[k], D[l]})

ONE_PAIR_SHDHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDHS.append({S[i], H[i], D[j], H[k], S[l]})

ONE_PAIR_SHDHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDHC.append({S[i], H[i], D[j], H[k], C[l]})

ONE_PAIR_SHDHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDHH.append({S[i], H[i], D[j], H[k], H[l]})

ONE_PAIR_SHDHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDHD.append({S[i], H[i], D[j], H[k], D[l]})

ONE_PAIR_SHDDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDDS.append({S[i], H[i], D[j], D[k], S[l]})

ONE_PAIR_SHDDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDDC.append({S[i], H[i], D[j], D[k], C[l]})

ONE_PAIR_SHDDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDDH.append({S[i], H[i], D[j], D[k], H[l]})

ONE_PAIR_SHDDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SHDDD.append({S[i], H[i], D[j], D[k], D[l]})

ONE_PAIR_SDSSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSSS.append({S[i], D[i], S[j], S[k], S[l]})

ONE_PAIR_SDSSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSSC.append({S[i], D[i], S[j], S[k], C[l]})

ONE_PAIR_SDSSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSSH.append({S[i], D[i], S[j], S[k], H[l]})

ONE_PAIR_SDSSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSSD.append({S[i], D[i], S[j], S[k], D[l]})

ONE_PAIR_SDSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSCS.append({S[i], D[i], S[j], C[k], S[l]})

ONE_PAIR_SDSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSCC.append({S[i], D[i], S[j], C[k], C[l]})

ONE_PAIR_SDSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSCH.append({S[i], D[i], S[j], C[k], H[l]})

ONE_PAIR_SDSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSCD.append({S[i], D[i], S[j], C[k], D[l]})

ONE_PAIR_SDSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSHS.append({S[i], D[i], S[j], H[k], S[l]})

ONE_PAIR_SDSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSHC.append({S[i], D[i], S[j], H[k], C[l]})

ONE_PAIR_SDSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSHH.append({S[i], D[i], S[j], H[k], H[l]})

ONE_PAIR_SDSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSHD.append({S[i], D[i], S[j], H[k], D[l]})

ONE_PAIR_SDSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSDS.append({S[i], D[i], S[j], D[k], S[l]})

ONE_PAIR_SDSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSDC.append({S[i], D[i], S[j], D[k], C[l]})

ONE_PAIR_SDSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSDH.append({S[i], D[i], S[j], D[k], H[l]})

ONE_PAIR_SDSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDSDD.append({S[i], D[i], S[j], D[k], D[l]})
ONE_PAIR_SDCSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCSS.append({S[i], D[i], C[j], S[k], S[l]})

ONE_PAIR_SDCSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCSC.append({S[i], D[i], C[j], S[k], C[l]})

ONE_PAIR_SDCSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCSH.append({S[i], D[i], C[j], S[k], H[l]})

ONE_PAIR_SDCSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCSD.append({S[i], D[i], C[j], S[k], D[l]})

ONE_PAIR_SDCCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCCS.append({S[i], D[i], C[j], C[k], S[l]})

ONE_PAIR_SDCCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCCC.append({S[i], D[i], C[j], C[k], C[l]})

ONE_PAIR_SDCCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCCH.append({S[i], D[i], C[j], C[k], H[l]})

ONE_PAIR_SDCCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCCD.append({S[i], D[i], C[j], C[k], D[l]})

ONE_PAIR_SDCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCHS.append({S[i], D[i], C[j], H[k], S[l]})

ONE_PAIR_SDCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCHC.append({S[i], D[i], C[j], H[k], C[l]})

ONE_PAIR_SDCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCHH.append({S[i], D[i], C[j], H[k], H[l]})

ONE_PAIR_SDCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCHD.append({S[i], D[i], C[j], H[k], D[l]})

ONE_PAIR_SDCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCDS.append({S[i], D[i], C[j], D[k], S[l]})

ONE_PAIR_SDCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCDC.append({S[i], D[i], C[j], D[k], C[l]})

ONE_PAIR_SDCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCDH.append({S[i], D[i], C[j], D[k], H[l]})

ONE_PAIR_SDCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDCDD.append({S[i], D[i], C[j], D[k], D[l]})

ONE_PAIR_SDHSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHSS.append({S[i], D[i], H[j], S[k], S[l]})

ONE_PAIR_SDHSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHSC.append({S[i], D[i], H[j], S[k], C[l]})

ONE_PAIR_SDHSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHSH.append({S[i], D[i], H[j], S[k], H[l]})

ONE_PAIR_SDHSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHSD.append({S[i], D[i], H[j], S[k], D[l]})

ONE_PAIR_SDHCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHCS.append({S[i], D[i], H[j], C[k], S[l]})

ONE_PAIR_SDHCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHCC.append({S[i], D[i], H[j], C[k], C[l]})

ONE_PAIR_SDHCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHCH.append({S[i], D[i], H[j], C[k], H[l]})

ONE_PAIR_SDHCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHCD.append({S[i], D[i], H[j], C[k], D[l]})

ONE_PAIR_SDHHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHHS.append({S[i], D[i], H[j], H[k], S[l]})

ONE_PAIR_SDHHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHHC.append({S[i], D[i], H[j], H[k], C[l]})

ONE_PAIR_SDHHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHHH.append({S[i], D[i], H[j], H[k], H[l]})

ONE_PAIR_SDHHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHHD.append({S[i], D[i], H[j], H[k], D[l]})

ONE_PAIR_SDHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHDS.append({S[i], D[i], H[j], D[k], S[l]})

ONE_PAIR_SDHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHDC.append({S[i], D[i], H[j], D[k], C[l]})

ONE_PAIR_SDHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHDH.append({S[i], D[i], H[j], D[k], H[l]})

ONE_PAIR_SDHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDHDD.append({S[i], D[i], H[j], D[k], D[l]})

ONE_PAIR_SDDSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDSS.append({S[i], D[i], D[j], S[k], S[l]})

ONE_PAIR_SDDSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDSC.append({S[i], D[i], D[j], S[k], C[l]})

ONE_PAIR_SDDSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDSH.append({S[i], D[i], D[j], S[k], H[l]})

ONE_PAIR_SDDSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDSD.append({S[i], D[i], D[j], S[k], D[l]})

ONE_PAIR_SDDCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDCS.append({S[i], D[i], D[j], C[k], S[l]})

ONE_PAIR_SDDCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDCC.append({S[i], D[i], D[j], C[k], C[l]})

ONE_PAIR_SDDCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDCH.append({S[i], D[i], D[j], C[k], H[l]})

ONE_PAIR_SDDCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDCD.append({S[i], D[i], D[j], C[k], D[l]})

ONE_PAIR_SDDHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDHS.append({S[i], D[i], D[j], H[k], S[l]})

ONE_PAIR_SDDHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDHC.append({S[i], D[i], D[j], H[k], C[l]})

ONE_PAIR_SDDHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDHH.append({S[i], D[i], D[j], H[k], H[l]})

ONE_PAIR_SDDHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDHD.append({S[i], D[i], D[j], H[k], D[l]})

ONE_PAIR_SDDDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDDS.append({S[i], D[i], D[j], D[k], S[l]})

ONE_PAIR_SDDDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDDC.append({S[i], D[i], D[j], D[k], C[l]})

ONE_PAIR_SDDDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDDH.append({S[i], D[i], D[j], D[k], H[l]})

ONE_PAIR_SDDDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_SDDDD.append({S[i], D[i], D[j], D[k], D[l]})

ONE_PAIR_CHSSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSSS.append({C[i], H[i], S[j], S[k], S[l]})

ONE_PAIR_CHSSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSSC.append({C[i], H[i], S[j], S[k], C[l]})

ONE_PAIR_CHSSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSSH.append({C[i], H[i], S[j], S[k], H[l]})

ONE_PAIR_CHSSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSSD.append({C[i], H[i], S[j], S[k], D[l]})

ONE_PAIR_CHSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSCS.append({C[i], H[i], S[j], C[k], S[l]})

ONE_PAIR_CHSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSCC.append({C[i], H[i], S[j], C[k], C[l]})

ONE_PAIR_CHSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSCH.append({C[i], H[i], S[j], C[k], H[l]})

ONE_PAIR_CHSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSCD.append({C[i], H[i], S[j], C[k], D[l]})

ONE_PAIR_CHSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSHS.append({C[i], H[i], S[j], H[k], S[l]})

ONE_PAIR_CHSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSHC.append({C[i], H[i], S[j], H[k], C[l]})

ONE_PAIR_CHSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSHH.append({C[i], H[i], S[j], H[k], H[l]})

ONE_PAIR_CHSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSHD.append({C[i], H[i], S[j], H[k], D[l]})

ONE_PAIR_CHSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSDS.append({C[i], H[i], S[j], D[k], S[l]})

ONE_PAIR_CHSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSDC.append({C[i], H[i], S[j], D[k], C[l]})

ONE_PAIR_CHSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSDH.append({C[i], H[i], S[j], D[k], H[l]})

ONE_PAIR_CHSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHSDD.append({C[i], H[i], S[j], D[k], D[l]})
ONE_PAIR_CHCSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCSS.append({C[i], H[i], C[j], S[k], S[l]})

ONE_PAIR_CHCSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCSC.append({C[i], H[i], C[j], S[k], C[l]})

ONE_PAIR_CHCSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCSH.append({C[i], H[i], C[j], S[k], H[l]})

ONE_PAIR_CHCSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCSD.append({C[i], H[i], C[j], S[k], D[l]})

ONE_PAIR_CHCCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCCS.append({C[i], H[i], C[j], C[k], S[l]})

ONE_PAIR_CHCCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCCC.append({C[i], H[i], C[j], C[k], C[l]})

ONE_PAIR_CHCCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCCH.append({C[i], H[i], C[j], C[k], H[l]})

ONE_PAIR_CHCCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCCD.append({C[i], H[i], C[j], C[k], D[l]})

ONE_PAIR_CHCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCHS.append({C[i], H[i], C[j], H[k], S[l]})

ONE_PAIR_CHCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCHC.append({C[i], H[i], C[j], H[k], C[l]})

ONE_PAIR_CHCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCHH.append({C[i], H[i], C[j], H[k], H[l]})

ONE_PAIR_CHCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCHD.append({C[i], H[i], C[j], H[k], D[l]})

ONE_PAIR_CHCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCDS.append({C[i], H[i], C[j], D[k], S[l]})

ONE_PAIR_CHCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCDC.append({C[i], H[i], C[j], D[k], C[l]})

ONE_PAIR_CHCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCDH.append({C[i], H[i], C[j], D[k], H[l]})

ONE_PAIR_CHCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHCDD.append({C[i], H[i], C[j], D[k], D[l]})

ONE_PAIR_CHHSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHSS.append({C[i], H[i], H[j], S[k], S[l]})

ONE_PAIR_CHHSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHSC.append({C[i], H[i], H[j], S[k], C[l]})

ONE_PAIR_CHHSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHSH.append({C[i], H[i], H[j], S[k], H[l]})

ONE_PAIR_CHHSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHSD.append({C[i], H[i], H[j], S[k], D[l]})

ONE_PAIR_CHHCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHCS.append({C[i], H[i], H[j], C[k], S[l]})

ONE_PAIR_CHHCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHCC.append({C[i], H[i], H[j], C[k], C[l]})

ONE_PAIR_CHHCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHCH.append({C[i], H[i], H[j], C[k], H[l]})

ONE_PAIR_CHHCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHCD.append({C[i], H[i], H[j], C[k], D[l]})

ONE_PAIR_CHHHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHHS.append({C[i], H[i], H[j], H[k], S[l]})

ONE_PAIR_CHHHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHHC.append({C[i], H[i], H[j], H[k], C[l]})

ONE_PAIR_CHHHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHHH.append({C[i], H[i], H[j], H[k], H[l]})

ONE_PAIR_CHHHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHHD.append({C[i], H[i], H[j], H[k], D[l]})

ONE_PAIR_CHHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHDS.append({C[i], H[i], H[j], D[k], S[l]})

ONE_PAIR_CHHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHDC.append({C[i], H[i], H[j], D[k], C[l]})

ONE_PAIR_CHHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHDH.append({C[i], H[i], H[j], D[k], H[l]})

ONE_PAIR_CHHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHHDD.append({C[i], H[i], H[j], D[k], D[l]})

ONE_PAIR_CHDSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDSS.append({C[i], H[i], D[j], S[k], S[l]})

ONE_PAIR_CHDSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDSC.append({C[i], H[i], D[j], S[k], C[l]})

ONE_PAIR_CHDSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDSH.append({C[i], H[i], D[j], S[k], H[l]})

ONE_PAIR_CHDSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDSD.append({C[i], H[i], D[j], S[k], D[l]})

ONE_PAIR_CHDCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDCS.append({C[i], H[i], D[j], C[k], S[l]})

ONE_PAIR_CHDCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDCC.append({C[i], H[i], D[j], C[k], C[l]})

ONE_PAIR_CHDCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDCH.append({C[i], H[i], D[j], C[k], H[l]})

ONE_PAIR_CHDCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDCD.append({C[i], H[i], D[j], C[k], D[l]})

ONE_PAIR_CHDHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDHS.append({C[i], H[i], D[j], H[k], S[l]})

ONE_PAIR_CHDHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDHC.append({C[i], H[i], D[j], H[k], C[l]})

ONE_PAIR_CHDHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDHH.append({C[i], H[i], D[j], H[k], H[l]})

ONE_PAIR_CHDHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDHD.append({C[i], H[i], D[j], H[k], D[l]})

ONE_PAIR_CHDDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDDS.append({C[i], H[i], D[j], D[k], S[l]})

ONE_PAIR_CHDDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDDC.append({C[i], H[i], D[j], D[k], C[l]})

ONE_PAIR_CHDDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDDH.append({C[i], H[i], D[j], D[k], H[l]})

ONE_PAIR_CHDDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CHDDD.append({C[i], H[i], D[j], D[k], D[l]})

ONE_PAIR_CDSSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSSS.append({C[i], D[i], S[j], S[k], S[l]})

ONE_PAIR_CDSSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSSC.append({C[i], D[i], S[j], S[k], C[l]})

ONE_PAIR_CDSSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSSH.append({C[i], D[i], S[j], S[k], H[l]})

ONE_PAIR_CDSSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSSD.append({C[i], D[i], S[j], S[k], D[l]})

ONE_PAIR_CDSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSCS.append({C[i], D[i], S[j], C[k], S[l]})

ONE_PAIR_CDSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSCC.append({C[i], D[i], S[j], C[k], C[l]})

ONE_PAIR_CDSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSCH.append({C[i], D[i], S[j], C[k], H[l]})

ONE_PAIR_CDSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSCD.append({C[i], D[i], S[j], C[k], D[l]})

ONE_PAIR_CDSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSHS.append({C[i], D[i], S[j], H[k], S[l]})

ONE_PAIR_CDSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSHC.append({C[i], D[i], S[j], H[k], C[l]})

ONE_PAIR_CDSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSHH.append({C[i], D[i], S[j], H[k], H[l]})

ONE_PAIR_CDSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSHD.append({C[i], D[i], S[j], H[k], D[l]})

ONE_PAIR_CDSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSDS.append({C[i], D[i], S[j], D[k], S[l]})

ONE_PAIR_CDSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSDC.append({C[i], D[i], S[j], D[k], C[l]})

ONE_PAIR_CDSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSDH.append({C[i], D[i], S[j], D[k], H[l]})

ONE_PAIR_CDSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDSDD.append({C[i], D[i], S[j], D[k], D[l]})
ONE_PAIR_CDCSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCSS.append({C[i], D[i], C[j], S[k], S[l]})

ONE_PAIR_CDCSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCSC.append({C[i], D[i], C[j], S[k], C[l]})

ONE_PAIR_CDCSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCSH.append({C[i], D[i], C[j], S[k], H[l]})

ONE_PAIR_CDCSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCSD.append({C[i], D[i], C[j], S[k], D[l]})

ONE_PAIR_CDCCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCCS.append({C[i], D[i], C[j], C[k], S[l]})

ONE_PAIR_CDCCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCCC.append({C[i], D[i], C[j], C[k], C[l]})

ONE_PAIR_CDCCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCCH.append({C[i], D[i], C[j], C[k], H[l]})

ONE_PAIR_CDCCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCCD.append({C[i], D[i], C[j], C[k], D[l]})

ONE_PAIR_CDCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCHS.append({C[i], D[i], C[j], H[k], S[l]})

ONE_PAIR_CDCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCHC.append({C[i], D[i], C[j], H[k], C[l]})

ONE_PAIR_CDCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCHH.append({C[i], D[i], C[j], H[k], H[l]})

ONE_PAIR_CDCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCHD.append({C[i], D[i], C[j], H[k], D[l]})

ONE_PAIR_CDCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCDS.append({C[i], D[i], C[j], D[k], S[l]})

ONE_PAIR_CDCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCDC.append({C[i], D[i], C[j], D[k], C[l]})

ONE_PAIR_CDCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCDH.append({C[i], D[i], C[j], D[k], H[l]})

ONE_PAIR_CDCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDCDD.append({C[i], D[i], C[j], D[k], D[l]})

ONE_PAIR_CDHSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHSS.append({C[i], D[i], H[j], S[k], S[l]})

ONE_PAIR_CDHSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHSC.append({C[i], D[i], H[j], S[k], C[l]})

ONE_PAIR_CDHSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHSH.append({C[i], D[i], H[j], S[k], H[l]})

ONE_PAIR_CDHSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHSD.append({C[i], D[i], H[j], S[k], D[l]})

ONE_PAIR_CDHCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHCS.append({C[i], D[i], H[j], C[k], S[l]})

ONE_PAIR_CDHCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHCC.append({C[i], D[i], H[j], C[k], C[l]})

ONE_PAIR_CDHCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHCH.append({C[i], D[i], H[j], C[k], H[l]})

ONE_PAIR_CDHCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHCD.append({C[i], D[i], H[j], C[k], D[l]})

ONE_PAIR_CDHHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHHS.append({C[i], D[i], H[j], H[k], S[l]})

ONE_PAIR_CDHHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHHC.append({C[i], D[i], H[j], H[k], C[l]})

ONE_PAIR_CDHHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHHH.append({C[i], D[i], H[j], H[k], H[l]})

ONE_PAIR_CDHHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHHD.append({C[i], D[i], H[j], H[k], D[l]})

ONE_PAIR_CDHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHDS.append({C[i], D[i], H[j], D[k], S[l]})

ONE_PAIR_CDHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHDC.append({C[i], D[i], H[j], D[k], C[l]})

ONE_PAIR_CDHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHDH.append({C[i], D[i], H[j], D[k], H[l]})

ONE_PAIR_CDHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDHDD.append({C[i], D[i], H[j], D[k], D[l]})

ONE_PAIR_CDDSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDSS.append({C[i], D[i], D[j], S[k], S[l]})

ONE_PAIR_CDDSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDSC.append({C[i], D[i], D[j], S[k], C[l]})

ONE_PAIR_CDDSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDSH.append({C[i], D[i], D[j], S[k], H[l]})

ONE_PAIR_CDDSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDSD.append({C[i], D[i], D[j], S[k], D[l]})

ONE_PAIR_CDDCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDCS.append({C[i], D[i], D[j], C[k], S[l]})

ONE_PAIR_CDDCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDCC.append({C[i], D[i], D[j], C[k], C[l]})

ONE_PAIR_CDDCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDCH.append({C[i], D[i], D[j], C[k], H[l]})

ONE_PAIR_CDDCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDCD.append({C[i], D[i], D[j], C[k], D[l]})

ONE_PAIR_CDDHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDHS.append({C[i], D[i], D[j], H[k], S[l]})

ONE_PAIR_CDDHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDHC.append({C[i], D[i], D[j], H[k], C[l]})

ONE_PAIR_CDDHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDHH.append({C[i], D[i], D[j], H[k], H[l]})

ONE_PAIR_CDDHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDHD.append({C[i], D[i], D[j], H[k], D[l]})

ONE_PAIR_CDDDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDDS.append({C[i], D[i], D[j], D[k], S[l]})

ONE_PAIR_CDDDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDDC.append({C[i], D[i], D[j], D[k], C[l]})

ONE_PAIR_CDDDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDDH.append({C[i], D[i], D[j], D[k], H[l]})

ONE_PAIR_CDDDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_CDDDD.append({C[i], D[i], D[j], D[k], D[l]})

ONE_PAIR_HDSSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSSS.append({H[i], D[i], S[j], S[k], S[l]})

ONE_PAIR_HDSSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSSC.append({H[i], D[i], S[j], S[k], C[l]})

ONE_PAIR_HDSSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSSH.append({H[i], D[i], S[j], S[k], H[l]})

ONE_PAIR_HDSSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSSD.append({H[i], D[i], S[j], S[k], D[l]})

ONE_PAIR_HDSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSCS.append({H[i], D[i], S[j], C[k], S[l]})

ONE_PAIR_HDSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSCC.append({H[i], D[i], S[j], C[k], C[l]})

ONE_PAIR_HDSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSCH.append({H[i], D[i], S[j], C[k], H[l]})

ONE_PAIR_HDSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSCD.append({H[i], D[i], S[j], C[k], D[l]})

ONE_PAIR_HDSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSHS.append({H[i], D[i], S[j], H[k], S[l]})

ONE_PAIR_HDSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSHC.append({H[i], D[i], S[j], H[k], C[l]})

ONE_PAIR_HDSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSHH.append({H[i], D[i], S[j], H[k], H[l]})

ONE_PAIR_HDSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSHD.append({H[i], D[i], S[j], H[k], D[l]})

ONE_PAIR_HDSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSDS.append({H[i], D[i], S[j], D[k], S[l]})

ONE_PAIR_HDSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSDC.append({H[i], D[i], S[j], D[k], C[l]})

ONE_PAIR_HDSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSDH.append({H[i], D[i], S[j], D[k], H[l]})

ONE_PAIR_HDSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDSDD.append({H[i], D[i], S[j], D[k], D[l]})
ONE_PAIR_HDCSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCSS.append({H[i], D[i], C[j], S[k], S[l]})

ONE_PAIR_HDCSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCSC.append({H[i], D[i], C[j], S[k], C[l]})

ONE_PAIR_HDCSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCSH.append({H[i], D[i], C[j], S[k], H[l]})

ONE_PAIR_HDCSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCSD.append({H[i], D[i], C[j], S[k], D[l]})

ONE_PAIR_HDCCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCCS.append({H[i], D[i], C[j], C[k], S[l]})

ONE_PAIR_HDCCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCCC.append({H[i], D[i], C[j], C[k], C[l]})

ONE_PAIR_HDCCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCCH.append({H[i], D[i], C[j], C[k], H[l]})

ONE_PAIR_HDCCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCCD.append({H[i], D[i], C[j], C[k], D[l]})

ONE_PAIR_HDCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCHS.append({H[i], D[i], C[j], H[k], S[l]})

ONE_PAIR_HDCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCHC.append({H[i], D[i], C[j], H[k], C[l]})

ONE_PAIR_HDCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCHH.append({H[i], D[i], C[j], H[k], H[l]})

ONE_PAIR_HDCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCHD.append({H[i], D[i], C[j], H[k], D[l]})

ONE_PAIR_HDCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCDS.append({H[i], D[i], C[j], D[k], S[l]})

ONE_PAIR_HDCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCDC.append({H[i], D[i], C[j], D[k], C[l]})

ONE_PAIR_HDCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCDH.append({H[i], D[i], C[j], D[k], H[l]})

ONE_PAIR_HDCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDCDD.append({H[i], D[i], C[j], D[k], D[l]})

ONE_PAIR_HDHSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHSS.append({H[i], D[i], H[j], S[k], S[l]})

ONE_PAIR_HDHSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHSC.append({H[i], D[i], H[j], S[k], C[l]})

ONE_PAIR_HDHSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHSH.append({H[i], D[i], H[j], S[k], H[l]})

ONE_PAIR_HDHSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHSD.append({H[i], D[i], H[j], S[k], D[l]})

ONE_PAIR_HDHCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHCS.append({H[i], D[i], H[j], C[k], S[l]})

ONE_PAIR_HDHCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHCC.append({H[i], D[i], H[j], C[k], C[l]})

ONE_PAIR_HDHCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHCH.append({H[i], D[i], H[j], C[k], H[l]})

ONE_PAIR_HDHCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHCD.append({H[i], D[i], H[j], C[k], D[l]})

ONE_PAIR_HDHHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHHS.append({H[i], D[i], H[j], H[k], S[l]})

ONE_PAIR_HDHHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHHC.append({H[i], D[i], H[j], H[k], C[l]})

ONE_PAIR_HDHHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHHH.append({H[i], D[i], H[j], H[k], H[l]})

ONE_PAIR_HDHHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHHD.append({H[i], D[i], H[j], H[k], D[l]})

ONE_PAIR_HDHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHDS.append({H[i], D[i], H[j], D[k], S[l]})

ONE_PAIR_HDHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHDC.append({H[i], D[i], H[j], D[k], C[l]})

ONE_PAIR_HDHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHDH.append({H[i], D[i], H[j], D[k], H[l]})

ONE_PAIR_HDHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDHDD.append({H[i], D[i], H[j], D[k], D[l]})

ONE_PAIR_HDDSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDSS.append({H[i], D[i], D[j], S[k], S[l]})

ONE_PAIR_HDDSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDSC.append({H[i], D[i], D[j], S[k], C[l]})

ONE_PAIR_HDDSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDSH.append({H[i], D[i], D[j], S[k], H[l]})

ONE_PAIR_HDDSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDSD.append({H[i], D[i], D[j], S[k], D[l]})

ONE_PAIR_HDDCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDCS.append({H[i], D[i], D[j], C[k], S[l]})

ONE_PAIR_HDDCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDCC.append({H[i], D[i], D[j], C[k], C[l]})

ONE_PAIR_HDDCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDCH.append({H[i], D[i], D[j], C[k], H[l]})

ONE_PAIR_HDDCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDCD.append({H[i], D[i], D[j], C[k], D[l]})

ONE_PAIR_HDDHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDHS.append({H[i], D[i], D[j], H[k], S[l]})

ONE_PAIR_HDDHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDHC.append({H[i], D[i], D[j], H[k], C[l]})

ONE_PAIR_HDDHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDHH.append({H[i], D[i], D[j], H[k], H[l]})

ONE_PAIR_HDDHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDHD.append({H[i], D[i], D[j], H[k], D[l]})

ONE_PAIR_HDDDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDDS.append({H[i], D[i], D[j], D[k], S[l]})

ONE_PAIR_HDDDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDDC.append({H[i], D[i], D[j], D[k], C[l]})

ONE_PAIR_HDDDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDDH.append({H[i], D[i], D[j], D[k], H[l]})

ONE_PAIR_HDDDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            for l in range(13):
                if i != j and i != k and i != l:
                    if j != k and j != l and k != l:
                        ONE_PAIR_HDDDD.append({H[i], D[i], D[j], D[k], D[l]})

ONE_PAIR = []
ONE_PAIR.extend(ONE_PAIR_SCSSS)
ONE_PAIR.extend(ONE_PAIR_SCSSC)
ONE_PAIR.extend(ONE_PAIR_SCSSH)
ONE_PAIR.extend(ONE_PAIR_SCSSD)
ONE_PAIR.extend(ONE_PAIR_SCSCS)
ONE_PAIR.extend(ONE_PAIR_SCSCC)
ONE_PAIR.extend(ONE_PAIR_SCSCH)
ONE_PAIR.extend(ONE_PAIR_SCSCD)
ONE_PAIR.extend(ONE_PAIR_SCSHS)
ONE_PAIR.extend(ONE_PAIR_SCSHC)
ONE_PAIR.extend(ONE_PAIR_SCSHH)
ONE_PAIR.extend(ONE_PAIR_SCSHD)
ONE_PAIR.extend(ONE_PAIR_SCSDS)
ONE_PAIR.extend(ONE_PAIR_SCSDC)
ONE_PAIR.extend(ONE_PAIR_SCSDH)
ONE_PAIR.extend(ONE_PAIR_SCSDD)
ONE_PAIR.extend(ONE_PAIR_SCCSS)
ONE_PAIR.extend(ONE_PAIR_SCCSC)
ONE_PAIR.extend(ONE_PAIR_SCCSH)
ONE_PAIR.extend(ONE_PAIR_SCCSD)
ONE_PAIR.extend(ONE_PAIR_SCCCS)
ONE_PAIR.extend(ONE_PAIR_SCCCC)
ONE_PAIR.extend(ONE_PAIR_SCCCH)
ONE_PAIR.extend(ONE_PAIR_SCCCD)
ONE_PAIR.extend(ONE_PAIR_SCCHS)
ONE_PAIR.extend(ONE_PAIR_SCCHC)
ONE_PAIR.extend(ONE_PAIR_SCCHH)
ONE_PAIR.extend(ONE_PAIR_SCCHD)
ONE_PAIR.extend(ONE_PAIR_SCCDS)
ONE_PAIR.extend(ONE_PAIR_SCCDC)
ONE_PAIR.extend(ONE_PAIR_SCCDH)
ONE_PAIR.extend(ONE_PAIR_SCCDD)
ONE_PAIR.extend(ONE_PAIR_SCHSS)
ONE_PAIR.extend(ONE_PAIR_SCHSC)
ONE_PAIR.extend(ONE_PAIR_SCHSH)
ONE_PAIR.extend(ONE_PAIR_SCHSD)
ONE_PAIR.extend(ONE_PAIR_SCHCS)
ONE_PAIR.extend(ONE_PAIR_SCHCC)
ONE_PAIR.extend(ONE_PAIR_SCHCH)
ONE_PAIR.extend(ONE_PAIR_SCHCD)
ONE_PAIR.extend(ONE_PAIR_SCHHS)
ONE_PAIR.extend(ONE_PAIR_SCHHC)
ONE_PAIR.extend(ONE_PAIR_SCHHH)
ONE_PAIR.extend(ONE_PAIR_SCHHD)
ONE_PAIR.extend(ONE_PAIR_SCHDS)
ONE_PAIR.extend(ONE_PAIR_SCHDC)
ONE_PAIR.extend(ONE_PAIR_SCHDH)
ONE_PAIR.extend(ONE_PAIR_SCHDD)
ONE_PAIR.extend(ONE_PAIR_SCDSS)
ONE_PAIR.extend(ONE_PAIR_SCDSC)
ONE_PAIR.extend(ONE_PAIR_SCDSH)
ONE_PAIR.extend(ONE_PAIR_SCDSD)
ONE_PAIR.extend(ONE_PAIR_SCDCS)
ONE_PAIR.extend(ONE_PAIR_SCDCC)
ONE_PAIR.extend(ONE_PAIR_SCDCH)
ONE_PAIR.extend(ONE_PAIR_SCDCD)
ONE_PAIR.extend(ONE_PAIR_SCDHS)
ONE_PAIR.extend(ONE_PAIR_SCDHC)
ONE_PAIR.extend(ONE_PAIR_SCDHH)
ONE_PAIR.extend(ONE_PAIR_SCDHD)
ONE_PAIR.extend(ONE_PAIR_SCDDS)
ONE_PAIR.extend(ONE_PAIR_SCDDC)
ONE_PAIR.extend(ONE_PAIR_SCDDH)
ONE_PAIR.extend(ONE_PAIR_SCDDD)
ONE_PAIR.extend(ONE_PAIR_SHSSS)
ONE_PAIR.extend(ONE_PAIR_SHSSC)
ONE_PAIR.extend(ONE_PAIR_SHSSH)
ONE_PAIR.extend(ONE_PAIR_SHSSD)
ONE_PAIR.extend(ONE_PAIR_SHSCS)
ONE_PAIR.extend(ONE_PAIR_SHSCC)
ONE_PAIR.extend(ONE_PAIR_SHSCH)
ONE_PAIR.extend(ONE_PAIR_SHSCD)
ONE_PAIR.extend(ONE_PAIR_SHSHS)
ONE_PAIR.extend(ONE_PAIR_SHSHC)
ONE_PAIR.extend(ONE_PAIR_SHSHH)
ONE_PAIR.extend(ONE_PAIR_SHSHD)
ONE_PAIR.extend(ONE_PAIR_SHSDS)
ONE_PAIR.extend(ONE_PAIR_SHSDC)
ONE_PAIR.extend(ONE_PAIR_SHSDH)
ONE_PAIR.extend(ONE_PAIR_SHSDD)
ONE_PAIR.extend(ONE_PAIR_SHCSS)
ONE_PAIR.extend(ONE_PAIR_SHCSC)
ONE_PAIR.extend(ONE_PAIR_SHCSH)
ONE_PAIR.extend(ONE_PAIR_SHCSD)
ONE_PAIR.extend(ONE_PAIR_SHCCS)
ONE_PAIR.extend(ONE_PAIR_SHCCC)
ONE_PAIR.extend(ONE_PAIR_SHCCH)
ONE_PAIR.extend(ONE_PAIR_SHCCD)
ONE_PAIR.extend(ONE_PAIR_SHCHS)
ONE_PAIR.extend(ONE_PAIR_SHCHC)
ONE_PAIR.extend(ONE_PAIR_SHCHH)
ONE_PAIR.extend(ONE_PAIR_SHCHD)
ONE_PAIR.extend(ONE_PAIR_SHCDS)
ONE_PAIR.extend(ONE_PAIR_SHCDC)
ONE_PAIR.extend(ONE_PAIR_SHCDH)
ONE_PAIR.extend(ONE_PAIR_SHCDD)
ONE_PAIR.extend(ONE_PAIR_SHHSS)
ONE_PAIR.extend(ONE_PAIR_SHHSC)
ONE_PAIR.extend(ONE_PAIR_SHHSH)
ONE_PAIR.extend(ONE_PAIR_SHHSD)
ONE_PAIR.extend(ONE_PAIR_SHHCS)
ONE_PAIR.extend(ONE_PAIR_SHHCC)
ONE_PAIR.extend(ONE_PAIR_SHHCH)
ONE_PAIR.extend(ONE_PAIR_SHHCD)
ONE_PAIR.extend(ONE_PAIR_SHHHS)
ONE_PAIR.extend(ONE_PAIR_SHHHC)
ONE_PAIR.extend(ONE_PAIR_SHHHH)
ONE_PAIR.extend(ONE_PAIR_SHHHD)
ONE_PAIR.extend(ONE_PAIR_SHHDS)
ONE_PAIR.extend(ONE_PAIR_SHHDC)
ONE_PAIR.extend(ONE_PAIR_SHHDH)
ONE_PAIR.extend(ONE_PAIR_SHHDD)
ONE_PAIR.extend(ONE_PAIR_SHDSS)
ONE_PAIR.extend(ONE_PAIR_SHDSC)
ONE_PAIR.extend(ONE_PAIR_SHDSH)
ONE_PAIR.extend(ONE_PAIR_SHDSD)
ONE_PAIR.extend(ONE_PAIR_SHDCS)
ONE_PAIR.extend(ONE_PAIR_SHDCC)
ONE_PAIR.extend(ONE_PAIR_SHDCH)
ONE_PAIR.extend(ONE_PAIR_SHDCD)
ONE_PAIR.extend(ONE_PAIR_SHDHS)
ONE_PAIR.extend(ONE_PAIR_SHDHC)
ONE_PAIR.extend(ONE_PAIR_SHDHH)
ONE_PAIR.extend(ONE_PAIR_SHDHD)
ONE_PAIR.extend(ONE_PAIR_SHDDS)
ONE_PAIR.extend(ONE_PAIR_SHDDC)
ONE_PAIR.extend(ONE_PAIR_SHDDH)
ONE_PAIR.extend(ONE_PAIR_SHDDD)
ONE_PAIR.extend(ONE_PAIR_SDSSS)
ONE_PAIR.extend(ONE_PAIR_SDSSC)
ONE_PAIR.extend(ONE_PAIR_SDSSH)
ONE_PAIR.extend(ONE_PAIR_SDSSD)
ONE_PAIR.extend(ONE_PAIR_SDSCS)
ONE_PAIR.extend(ONE_PAIR_SDSCC)
ONE_PAIR.extend(ONE_PAIR_SDSCH)
ONE_PAIR.extend(ONE_PAIR_SDSCD)
ONE_PAIR.extend(ONE_PAIR_SDSHS)
ONE_PAIR.extend(ONE_PAIR_SDSHC)
ONE_PAIR.extend(ONE_PAIR_SDSHH)
ONE_PAIR.extend(ONE_PAIR_SDSHD)
ONE_PAIR.extend(ONE_PAIR_SDSDS)
ONE_PAIR.extend(ONE_PAIR_SDSDC)
ONE_PAIR.extend(ONE_PAIR_SDSDH)
ONE_PAIR.extend(ONE_PAIR_SDSDD)
ONE_PAIR.extend(ONE_PAIR_SDCSS)
ONE_PAIR.extend(ONE_PAIR_SDCSC)
ONE_PAIR.extend(ONE_PAIR_SDCSH)
ONE_PAIR.extend(ONE_PAIR_SDCSD)
ONE_PAIR.extend(ONE_PAIR_SDCCS)
ONE_PAIR.extend(ONE_PAIR_SDCCC)
ONE_PAIR.extend(ONE_PAIR_SDCCH)
ONE_PAIR.extend(ONE_PAIR_SDCCD)
ONE_PAIR.extend(ONE_PAIR_SDCHS)
ONE_PAIR.extend(ONE_PAIR_SDCHC)
ONE_PAIR.extend(ONE_PAIR_SDCHH)
ONE_PAIR.extend(ONE_PAIR_SDCHD)
ONE_PAIR.extend(ONE_PAIR_SDCDS)
ONE_PAIR.extend(ONE_PAIR_SDCDC)
ONE_PAIR.extend(ONE_PAIR_SDCDH)
ONE_PAIR.extend(ONE_PAIR_SDCDD)
ONE_PAIR.extend(ONE_PAIR_SDHSS)
ONE_PAIR.extend(ONE_PAIR_SDHSC)
ONE_PAIR.extend(ONE_PAIR_SDHSH)
ONE_PAIR.extend(ONE_PAIR_SDHSD)
ONE_PAIR.extend(ONE_PAIR_SDHCS)
ONE_PAIR.extend(ONE_PAIR_SDHCC)
ONE_PAIR.extend(ONE_PAIR_SDHCH)
ONE_PAIR.extend(ONE_PAIR_SDHCD)
ONE_PAIR.extend(ONE_PAIR_SDHHS)
ONE_PAIR.extend(ONE_PAIR_SDHHC)
ONE_PAIR.extend(ONE_PAIR_SDHHH)
ONE_PAIR.extend(ONE_PAIR_SDHHD)
ONE_PAIR.extend(ONE_PAIR_SDHDS)
ONE_PAIR.extend(ONE_PAIR_SDHDC)
ONE_PAIR.extend(ONE_PAIR_SDHDH)
ONE_PAIR.extend(ONE_PAIR_SDHDD)
ONE_PAIR.extend(ONE_PAIR_SDDSS)
ONE_PAIR.extend(ONE_PAIR_SDDSC)
ONE_PAIR.extend(ONE_PAIR_SDDSH)
ONE_PAIR.extend(ONE_PAIR_SDDSD)
ONE_PAIR.extend(ONE_PAIR_SDDCS)
ONE_PAIR.extend(ONE_PAIR_SDDCC)
ONE_PAIR.extend(ONE_PAIR_SDDCH)
ONE_PAIR.extend(ONE_PAIR_SDDCD)
ONE_PAIR.extend(ONE_PAIR_SDDHS)
ONE_PAIR.extend(ONE_PAIR_SDDHC)
ONE_PAIR.extend(ONE_PAIR_SDDHH)
ONE_PAIR.extend(ONE_PAIR_SDDHD)
ONE_PAIR.extend(ONE_PAIR_SDDDS)
ONE_PAIR.extend(ONE_PAIR_SDDDC)
ONE_PAIR.extend(ONE_PAIR_SDDDH)
ONE_PAIR.extend(ONE_PAIR_SDDDD)
ONE_PAIR.extend(ONE_PAIR_CHSSS)
ONE_PAIR.extend(ONE_PAIR_CHSSC)
ONE_PAIR.extend(ONE_PAIR_CHSSH)
ONE_PAIR.extend(ONE_PAIR_CHSSD)
ONE_PAIR.extend(ONE_PAIR_CHSCS)
ONE_PAIR.extend(ONE_PAIR_CHSCC)
ONE_PAIR.extend(ONE_PAIR_CHSCH)
ONE_PAIR.extend(ONE_PAIR_CHSCD)
ONE_PAIR.extend(ONE_PAIR_CHSHS)
ONE_PAIR.extend(ONE_PAIR_CHSHC)
ONE_PAIR.extend(ONE_PAIR_CHSHH)
ONE_PAIR.extend(ONE_PAIR_CHSHD)
ONE_PAIR.extend(ONE_PAIR_CHSDS)
ONE_PAIR.extend(ONE_PAIR_CHSDC)
ONE_PAIR.extend(ONE_PAIR_CHSDH)
ONE_PAIR.extend(ONE_PAIR_CHSDD)
ONE_PAIR.extend(ONE_PAIR_CHCSS)
ONE_PAIR.extend(ONE_PAIR_CHCSC)
ONE_PAIR.extend(ONE_PAIR_CHCSH)
ONE_PAIR.extend(ONE_PAIR_CHCSD)
ONE_PAIR.extend(ONE_PAIR_CHCCS)
ONE_PAIR.extend(ONE_PAIR_CHCCC)
ONE_PAIR.extend(ONE_PAIR_CHCCH)
ONE_PAIR.extend(ONE_PAIR_CHCCD)
ONE_PAIR.extend(ONE_PAIR_CHCHS)
ONE_PAIR.extend(ONE_PAIR_CHCHC)
ONE_PAIR.extend(ONE_PAIR_CHCHH)
ONE_PAIR.extend(ONE_PAIR_CHCHD)
ONE_PAIR.extend(ONE_PAIR_CHCDS)
ONE_PAIR.extend(ONE_PAIR_CHCDC)
ONE_PAIR.extend(ONE_PAIR_CHCDH)
ONE_PAIR.extend(ONE_PAIR_CHCDD)
ONE_PAIR.extend(ONE_PAIR_CHHSS)
ONE_PAIR.extend(ONE_PAIR_CHHSC)
ONE_PAIR.extend(ONE_PAIR_CHHSH)
ONE_PAIR.extend(ONE_PAIR_CHHSD)
ONE_PAIR.extend(ONE_PAIR_CHHCS)
ONE_PAIR.extend(ONE_PAIR_CHHCC)
ONE_PAIR.extend(ONE_PAIR_CHHCH)
ONE_PAIR.extend(ONE_PAIR_CHHCD)
ONE_PAIR.extend(ONE_PAIR_CHHHS)
ONE_PAIR.extend(ONE_PAIR_CHHHC)
ONE_PAIR.extend(ONE_PAIR_CHHHH)
ONE_PAIR.extend(ONE_PAIR_CHHHD)
ONE_PAIR.extend(ONE_PAIR_CHHDS)
ONE_PAIR.extend(ONE_PAIR_CHHDC)
ONE_PAIR.extend(ONE_PAIR_CHHDH)
ONE_PAIR.extend(ONE_PAIR_CHHDD)
ONE_PAIR.extend(ONE_PAIR_CHDSS)
ONE_PAIR.extend(ONE_PAIR_CHDSC)
ONE_PAIR.extend(ONE_PAIR_CHDSH)
ONE_PAIR.extend(ONE_PAIR_CHDSD)
ONE_PAIR.extend(ONE_PAIR_CHDCS)
ONE_PAIR.extend(ONE_PAIR_CHDCC)
ONE_PAIR.extend(ONE_PAIR_CHDCH)
ONE_PAIR.extend(ONE_PAIR_CHDCD)
ONE_PAIR.extend(ONE_PAIR_CHDHS)
ONE_PAIR.extend(ONE_PAIR_CHDHC)
ONE_PAIR.extend(ONE_PAIR_CHDHH)
ONE_PAIR.extend(ONE_PAIR_CHDHD)
ONE_PAIR.extend(ONE_PAIR_CHDDS)
ONE_PAIR.extend(ONE_PAIR_CHDDC)
ONE_PAIR.extend(ONE_PAIR_CHDDH)
ONE_PAIR.extend(ONE_PAIR_CHDDD)
ONE_PAIR.extend(ONE_PAIR_CDSSS)
ONE_PAIR.extend(ONE_PAIR_CDSSC)
ONE_PAIR.extend(ONE_PAIR_CDSSH)
ONE_PAIR.extend(ONE_PAIR_CDSSD)
ONE_PAIR.extend(ONE_PAIR_CDSCS)
ONE_PAIR.extend(ONE_PAIR_CDSCC)
ONE_PAIR.extend(ONE_PAIR_CDSCH)
ONE_PAIR.extend(ONE_PAIR_CDSCD)
ONE_PAIR.extend(ONE_PAIR_CDSHS)
ONE_PAIR.extend(ONE_PAIR_CDSHC)
ONE_PAIR.extend(ONE_PAIR_CDSHH)
ONE_PAIR.extend(ONE_PAIR_CDSHD)
ONE_PAIR.extend(ONE_PAIR_CDSDS)
ONE_PAIR.extend(ONE_PAIR_CDSDC)
ONE_PAIR.extend(ONE_PAIR_CDSDH)
ONE_PAIR.extend(ONE_PAIR_CDSDD)
ONE_PAIR.extend(ONE_PAIR_CDCSS)
ONE_PAIR.extend(ONE_PAIR_CDCSC)
ONE_PAIR.extend(ONE_PAIR_CDCSH)
ONE_PAIR.extend(ONE_PAIR_CDCSD)
ONE_PAIR.extend(ONE_PAIR_CDCCS)
ONE_PAIR.extend(ONE_PAIR_CDCCC)
ONE_PAIR.extend(ONE_PAIR_CDCCH)
ONE_PAIR.extend(ONE_PAIR_CDCCD)
ONE_PAIR.extend(ONE_PAIR_CDCHS)
ONE_PAIR.extend(ONE_PAIR_CDCHC)
ONE_PAIR.extend(ONE_PAIR_CDCHH)
ONE_PAIR.extend(ONE_PAIR_CDCHD)
ONE_PAIR.extend(ONE_PAIR_CDCDS)
ONE_PAIR.extend(ONE_PAIR_CDCDC)
ONE_PAIR.extend(ONE_PAIR_CDCDH)
ONE_PAIR.extend(ONE_PAIR_CDCDD)
ONE_PAIR.extend(ONE_PAIR_CDHSS)
ONE_PAIR.extend(ONE_PAIR_CDHSC)
ONE_PAIR.extend(ONE_PAIR_CDHSH)
ONE_PAIR.extend(ONE_PAIR_CDHSD)
ONE_PAIR.extend(ONE_PAIR_CDHCS)
ONE_PAIR.extend(ONE_PAIR_CDHCC)
ONE_PAIR.extend(ONE_PAIR_CDHCH)
ONE_PAIR.extend(ONE_PAIR_CDHCD)
ONE_PAIR.extend(ONE_PAIR_CDHHS)
ONE_PAIR.extend(ONE_PAIR_CDHHC)
ONE_PAIR.extend(ONE_PAIR_CDHHH)
ONE_PAIR.extend(ONE_PAIR_CDHHD)
ONE_PAIR.extend(ONE_PAIR_CDHDS)
ONE_PAIR.extend(ONE_PAIR_CDHDC)
ONE_PAIR.extend(ONE_PAIR_CDHDH)
ONE_PAIR.extend(ONE_PAIR_CDHDD)
ONE_PAIR.extend(ONE_PAIR_CDDSS)
ONE_PAIR.extend(ONE_PAIR_CDDSC)
ONE_PAIR.extend(ONE_PAIR_CDDSH)
ONE_PAIR.extend(ONE_PAIR_CDDSD)
ONE_PAIR.extend(ONE_PAIR_CDDCS)
ONE_PAIR.extend(ONE_PAIR_CDDCC)
ONE_PAIR.extend(ONE_PAIR_CDDCH)
ONE_PAIR.extend(ONE_PAIR_CDDCD)
ONE_PAIR.extend(ONE_PAIR_CDDHS)
ONE_PAIR.extend(ONE_PAIR_CDDHC)
ONE_PAIR.extend(ONE_PAIR_CDDHH)
ONE_PAIR.extend(ONE_PAIR_CDDHD)
ONE_PAIR.extend(ONE_PAIR_CDDDS)
ONE_PAIR.extend(ONE_PAIR_CDDDC)
ONE_PAIR.extend(ONE_PAIR_CDDDH)
ONE_PAIR.extend(ONE_PAIR_CDDDD)
ONE_PAIR.extend(ONE_PAIR_HDSSS)
ONE_PAIR.extend(ONE_PAIR_HDSSC)
ONE_PAIR.extend(ONE_PAIR_HDSSH)
ONE_PAIR.extend(ONE_PAIR_HDSSD)
ONE_PAIR.extend(ONE_PAIR_HDSCS)
ONE_PAIR.extend(ONE_PAIR_HDSCC)
ONE_PAIR.extend(ONE_PAIR_HDSCH)
ONE_PAIR.extend(ONE_PAIR_HDSCD)
ONE_PAIR.extend(ONE_PAIR_HDSHS)
ONE_PAIR.extend(ONE_PAIR_HDSHC)
ONE_PAIR.extend(ONE_PAIR_HDSHH)
ONE_PAIR.extend(ONE_PAIR_HDSHD)
ONE_PAIR.extend(ONE_PAIR_HDSDS)
ONE_PAIR.extend(ONE_PAIR_HDSDC)
ONE_PAIR.extend(ONE_PAIR_HDSDH)
ONE_PAIR.extend(ONE_PAIR_HDSDD)
ONE_PAIR.extend(ONE_PAIR_HDCSS)
ONE_PAIR.extend(ONE_PAIR_HDCSC)
ONE_PAIR.extend(ONE_PAIR_HDCSH)
ONE_PAIR.extend(ONE_PAIR_HDCSD)
ONE_PAIR.extend(ONE_PAIR_HDCCS)
ONE_PAIR.extend(ONE_PAIR_HDCCC)
ONE_PAIR.extend(ONE_PAIR_HDCCH)
ONE_PAIR.extend(ONE_PAIR_HDCCD)
ONE_PAIR.extend(ONE_PAIR_HDCHS)
ONE_PAIR.extend(ONE_PAIR_HDCHC)
ONE_PAIR.extend(ONE_PAIR_HDCHH)
ONE_PAIR.extend(ONE_PAIR_HDCHD)
ONE_PAIR.extend(ONE_PAIR_HDCDS)
ONE_PAIR.extend(ONE_PAIR_HDCDC)
ONE_PAIR.extend(ONE_PAIR_HDCDH)
ONE_PAIR.extend(ONE_PAIR_HDCDD)
ONE_PAIR.extend(ONE_PAIR_HDHSS)
ONE_PAIR.extend(ONE_PAIR_HDHSC)
ONE_PAIR.extend(ONE_PAIR_HDHSH)
ONE_PAIR.extend(ONE_PAIR_HDHSD)
ONE_PAIR.extend(ONE_PAIR_HDHCS)
ONE_PAIR.extend(ONE_PAIR_HDHCC)
ONE_PAIR.extend(ONE_PAIR_HDHCH)
ONE_PAIR.extend(ONE_PAIR_HDHCD)
ONE_PAIR.extend(ONE_PAIR_HDHHS)
ONE_PAIR.extend(ONE_PAIR_HDHHC)
ONE_PAIR.extend(ONE_PAIR_HDHHH)
ONE_PAIR.extend(ONE_PAIR_HDHHD)
ONE_PAIR.extend(ONE_PAIR_HDHDS)
ONE_PAIR.extend(ONE_PAIR_HDHDC)
ONE_PAIR.extend(ONE_PAIR_HDHDH)
ONE_PAIR.extend(ONE_PAIR_HDHDD)
ONE_PAIR.extend(ONE_PAIR_HDDSS)
ONE_PAIR.extend(ONE_PAIR_HDDSC)
ONE_PAIR.extend(ONE_PAIR_HDDSH)
ONE_PAIR.extend(ONE_PAIR_HDDSD)
ONE_PAIR.extend(ONE_PAIR_HDDCS)
ONE_PAIR.extend(ONE_PAIR_HDDCC)
ONE_PAIR.extend(ONE_PAIR_HDDCH)
ONE_PAIR.extend(ONE_PAIR_HDDCD)
ONE_PAIR.extend(ONE_PAIR_HDDHS)
ONE_PAIR.extend(ONE_PAIR_HDDHC)
ONE_PAIR.extend(ONE_PAIR_HDDHH)
ONE_PAIR.extend(ONE_PAIR_HDDHD)
ONE_PAIR.extend(ONE_PAIR_HDDDS)
ONE_PAIR.extend(ONE_PAIR_HDDDC)
ONE_PAIR.extend(ONE_PAIR_HDDDH)
ONE_PAIR.extend(ONE_PAIR_HDDDD)

lst = []
for i in ONE_PAIR:
    lst.append(list(i))
ONE_PAIR.clear()

for i in lst:
    i.sort()

lst2 = []
for i in lst:
    lst2.append(tuple(i))

lst2 = list(set(lst2))

for i in lst2:
    ONE_PAIR.append(set(i))
