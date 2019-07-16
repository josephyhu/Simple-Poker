import deck
import copy

S = copy.deepcopy(deck.SPADES)
C = copy.deepcopy(deck.CLUBS)
H = copy.deepcopy(deck.HEARTS)
D = copy.deepcopy(deck.DIAMONDS)

TWO_PAIR_SCSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSCS.append({S[i], C[i], S[j], C[j], S[k]})

TWO_PAIR_SCSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSCC.append({S[i], C[i], S[j], C[j], C[k]})

TWO_PAIR_SCSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSCH.append({S[i], C[i], S[j], C[j], H[k]})

TWO_PAIR_SCSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSCD.append({S[i], C[i], S[j], C[j], D[k]})

TWO_PAIR_SCSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSHS.append({S[i], C[i], S[j], H[j], S[k]})

TWO_PAIR_SCSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSHC.append({S[i], C[i], S[j], H[j], C[k]})

TWO_PAIR_SCSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSHH.append({S[i], C[i], S[j], H[j], H[k]})

TWO_PAIR_SCSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSHD.append({S[i], C[i], S[j], H[j], D[k]})

TWO_PAIR_SCSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSDS.append({S[i], C[i], S[j], D[j], S[k]})

TWO_PAIR_SCSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSDC.append({S[i], C[i], S[j], D[j], C[k]})

TWO_PAIR_SCSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSDH.append({S[i], C[i], S[j], D[j], H[k]})

TWO_PAIR_SCSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCSDD.append({S[i], C[i], S[j], D[j], D[k]})

TWO_PAIR_SCCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCCHS.append({S[i], C[i], C[j], H[j], S[k]})

TWO_PAIR_SCCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCCHC.append({S[i], C[i], C[j], H[j], C[k]})

TWO_PAIR_SCCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCCHH.append({S[i], C[i], C[j], H[j], H[k]})

TWO_PAIR_SCCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCCHD.append({S[i], C[i], C[j], H[j], D[k]})

TWO_PAIR_SCCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCCDS.append({S[i], C[i], C[j], D[j], S[k]})

TWO_PAIR_SCCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCCDC.append({S[i], C[i], C[j], D[j], C[k]})

TWO_PAIR_SCCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCCDH.append({S[i], C[i], C[j], D[j], H[k]})

TWO_PAIR_SCCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCCDD.append({S[i], C[i], C[j], D[j], D[k]})

TWO_PAIR_SCHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCHDS.append({S[i], C[i], H[j], D[j], S[k]})

TWO_PAIR_SCHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCHDC.append({S[i], C[i], H[j], D[j], C[k]})

TWO_PAIR_SCHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCHDH.append({S[i], C[i], H[j], D[j], H[k]})

TWO_PAIR_SCHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SCHDD.append({S[i], C[i], H[j], D[j], D[k]})

TWO_PAIR_SHSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSCS.append({S[i], H[i], S[j], C[j], S[k]})

TWO_PAIR_SHSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSCC.append({S[i], H[i], S[j], C[j], C[k]})

TWO_PAIR_SHSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSCH.append({S[i], H[i], S[j], C[j], H[k]})

TWO_PAIR_SHSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSCD.append({S[i], H[i], S[j], C[j], D[k]})

TWO_PAIR_SHSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSHS.append({S[i], H[i], S[j], H[j], S[k]})

TWO_PAIR_SHSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSHC.append({S[i], H[i], S[j], H[j], C[k]})

TWO_PAIR_SHSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSHH.append({S[i], H[i], S[j], H[j], H[k]})

TWO_PAIR_SHSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSHD.append({S[i], H[i], S[j], H[j], D[k]})

TWO_PAIR_SHSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSDS.append({S[i], H[i], S[j], D[j], S[k]})

TWO_PAIR_SHSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSDC.append({S[i], H[i], S[j], D[j], C[k]})

TWO_PAIR_SHSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSDH.append({S[i], H[i], S[j], D[j], H[k]})

TWO_PAIR_SHSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHSDD.append({S[i], H[i], S[j], D[j], D[k]})

TWO_PAIR_SHCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHCHS.append({S[i], H[i], C[j], H[j], S[k]})

TWO_PAIR_SHCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHCHC.append({S[i], H[i], C[j], H[j], C[k]})

TWO_PAIR_SHCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHCHH.append({S[i], H[i], C[j], H[j], H[k]})

TWO_PAIR_SHCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHCHD.append({S[i], H[i], C[j], H[j], D[k]})

TWO_PAIR_SHCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHCDS.append({S[i], H[i], C[j], D[j], S[k]})

TWO_PAIR_SHCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHCDC.append({S[i], H[i], C[j], D[j], C[k]})

TWO_PAIR_SHCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHCDH.append({S[i], H[i], C[j], D[j], H[k]})

TWO_PAIR_SHCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHCDD.append({S[i], H[i], C[j], D[j], D[k]})

TWO_PAIR_SHHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHHDS.append({S[i], H[i], H[j], D[j], S[k]})

TWO_PAIR_SHHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHHDC.append({S[i], H[i], H[j], D[j], C[k]})

TWO_PAIR_SHHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHHDH.append({S[i], H[i], H[j], D[j], H[k]})

TWO_PAIR_SHHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SHHDD.append({S[i], H[i], H[j], D[j], D[k]})

TWO_PAIR_SDSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSCS.append({S[i], D[i], S[j], C[j], S[k]})

TWO_PAIR_SDSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSCC.append({S[i], D[i], S[j], C[j], C[k]})

TWO_PAIR_SDSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSCH.append({S[i], D[i], S[j], C[j], H[k]})

TWO_PAIR_SDSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSCD.append({S[i], D[i], S[j], C[j], D[k]})

TWO_PAIR_SDSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSHS.append({S[i], D[i], S[j], H[j], S[k]})

TWO_PAIR_SDSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSHC.append({S[i], D[i], S[j], H[j], C[k]})

TWO_PAIR_SDSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSHH.append({S[i], D[i], S[j], H[j], H[k]})

TWO_PAIR_SDSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSHD.append({S[i], D[i], S[j], H[j], D[k]})

TWO_PAIR_SDSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSDS.append({S[i], D[i], S[j], D[j], S[k]})

TWO_PAIR_SDSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSDC.append({S[i], D[i], S[j], D[j], C[k]})

TWO_PAIR_SDSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSDH.append({S[i], D[i], S[j], D[j], H[k]})

TWO_PAIR_SDSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDSDD.append({S[i], D[i], S[j], D[j], D[k]})

TWO_PAIR_SDCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDCHS.append({S[i], D[i], C[j], H[j], S[k]})

TWO_PAIR_SDCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDCHC.append({S[i], D[i], C[j], H[j], C[k]})

TWO_PAIR_SDCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDCHH.append({S[i], D[i], C[j], H[j], H[k]})

TWO_PAIR_SDCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDCHD.append({S[i], D[i], C[j], H[j], D[k]})

TWO_PAIR_SDCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDCDS.append({S[i], D[i], C[j], D[j], S[k]})

TWO_PAIR_SDCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDCDC.append({S[i], D[i], C[j], D[j], C[k]})

TWO_PAIR_SDCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDCDH.append({S[i], D[i], C[j], D[j], H[k]})

TWO_PAIR_SDCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDCDD.append({S[i], D[i], C[j], D[j], D[k]})

TWO_PAIR_SDHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDHDS.append({S[i], D[i], H[j], D[j], S[k]})

TWO_PAIR_SDHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDHDC.append({S[i], D[i], H[j], D[j], C[k]})

TWO_PAIR_SDHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDHDH.append({S[i], D[i], H[j], D[j], H[k]})

TWO_PAIR_SDHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_SDHDD.append({S[i], D[i], H[j], D[j], D[k]})

TWO_PAIR_CHSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSCS.append({C[i], H[i], S[j], C[j], S[k]})

TWO_PAIR_CHSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSCC.append({C[i], H[i], S[j], C[j], C[k]})

TWO_PAIR_CHSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSCH.append({C[i], H[i], S[j], C[j], H[k]})

TWO_PAIR_CHSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSCD.append({C[i], H[i], S[j], C[j], D[k]})

TWO_PAIR_CHSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSHS.append({C[i], H[i], S[j], H[j], S[k]})

TWO_PAIR_CHSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSHC.append({C[i], H[i], S[j], H[j], C[k]})

TWO_PAIR_CHSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSHH.append({C[i], H[i], S[j], H[j], H[k]})

TWO_PAIR_CHSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSHD.append({C[i], H[i], S[j], H[j], D[k]})

TWO_PAIR_CHSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSDS.append({C[i], H[i], S[j], D[j], S[k]})

TWO_PAIR_CHSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSDC.append({C[i], H[i], S[j], D[j], C[k]})

TWO_PAIR_CHSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSDH.append({C[i], H[i], S[j], D[j], H[k]})

TWO_PAIR_CHSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHSDD.append({C[i], H[i], S[j], D[j], D[k]})

TWO_PAIR_CHCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHCHS.append({C[i], H[i], C[j], H[j], S[k]})

TWO_PAIR_CHCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHCHC.append({C[i], H[i], C[j], H[j], C[k]})

TWO_PAIR_CHCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHCHH.append({C[i], H[i], C[j], H[j], H[k]})

TWO_PAIR_CHCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHCHD.append({C[i], H[i], C[j], H[j], D[k]})

TWO_PAIR_CHCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHCDS.append({C[i], H[i], C[j], D[j], S[k]})

TWO_PAIR_CHCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHCDC.append({C[i], H[i], C[j], D[j], C[k]})

TWO_PAIR_CHCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHCDH.append({C[i], H[i], C[j], D[j], H[k]})

TWO_PAIR_CHCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHCDD.append({C[i], H[i], C[j], D[j], D[k]})

TWO_PAIR_CHHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHHDS.append({C[i], H[i], H[j], D[j], S[k]})

TWO_PAIR_CHHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHHDC.append({C[i], H[i], H[j], D[j], C[k]})

TWO_PAIR_CHHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHHDH.append({C[i], H[i], H[j], D[j], H[k]})

TWO_PAIR_CHHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CHHDD.append({C[i], H[i], H[j], D[j], D[k]})

TWO_PAIR_CDSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSCS.append({C[i], D[i], S[j], C[j], S[k]})

TWO_PAIR_CDSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSCC.append({C[i], D[i], S[j], C[j], C[k]})

TWO_PAIR_CDSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSCH.append({C[i], D[i], S[j], C[j], H[k]})

TWO_PAIR_CDSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSCD.append({C[i], D[i], S[j], C[j], D[k]})

TWO_PAIR_CDSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSHS.append({C[i], D[i], S[j], H[j], S[k]})

TWO_PAIR_CDSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSHC.append({C[i], D[i], S[j], H[j], C[k]})

TWO_PAIR_CDSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSHH.append({C[i], D[i], S[j], H[j], H[k]})

TWO_PAIR_CDSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSHD.append({C[i], D[i], S[j], H[j], D[k]})

TWO_PAIR_CDSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSDS.append({C[i], D[i], S[j], D[j], S[k]})

TWO_PAIR_CDSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSDC.append({C[i], D[i], S[j], D[j], C[k]})

TWO_PAIR_CDSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSDH.append({C[i], D[i], S[j], D[j], H[k]})

TWO_PAIR_CDSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDSDD.append({C[i], D[i], S[j], D[j], D[k]})

TWO_PAIR_CDCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDCHS.append({C[i], D[i], C[j], H[j], S[k]})

TWO_PAIR_CDCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDCHC.append({C[i], D[i], C[j], H[j], C[k]})

TWO_PAIR_CDCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDCHH.append({C[i], D[i], C[j], H[j], H[k]})

TWO_PAIR_CDCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDCHD.append({C[i], D[i], C[j], H[j], D[k]})

TWO_PAIR_CDCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDCDS.append({C[i], D[i], C[j], D[j], S[k]})

TWO_PAIR_CDCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDCDC.append({C[i], D[i], C[j], D[j], C[k]})

TWO_PAIR_CDCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDCDH.append({C[i], D[i], C[j], D[j], H[k]})

TWO_PAIR_CDCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDCDD.append({C[i], D[i], C[j], D[j], D[k]})

TWO_PAIR_CDHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDHDS.append({C[i], D[i], H[j], D[j], S[k]})

TWO_PAIR_CDHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDHDC.append({C[i], D[i], H[j], D[j], C[k]})

TWO_PAIR_CDHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDHDH.append({C[i], D[i], H[j], D[j], H[k]})

TWO_PAIR_CDHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_CDHDD.append({C[i], D[i], H[j], D[j], D[k]})

TWO_PAIR_HDSCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSCS.append({H[i], D[i], S[j], C[j], S[k]})

TWO_PAIR_HDSCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSCC.append({H[i], D[i], S[j], C[j], C[k]})

TWO_PAIR_HDSCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSCH.append({H[i], D[i], S[j], C[j], H[k]})

TWO_PAIR_HDSCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSCD.append({H[i], D[i], S[j], C[j], D[k]})

TWO_PAIR_HDSHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSHS.append({H[i], D[i], S[j], H[j], S[k]})

TWO_PAIR_HDSHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSHC.append({H[i], D[i], S[j], H[j], C[k]})

TWO_PAIR_HDSHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSHH.append({H[i], D[i], S[j], H[j], H[k]})

TWO_PAIR_HDSHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSHD.append({H[i], D[i], S[j], H[j], D[k]})

TWO_PAIR_HDSDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSDS.append({H[i], D[i], S[j], D[j], S[k]})

TWO_PAIR_HDSDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSDC.append({H[i], D[i], S[j], D[j], C[k]})

TWO_PAIR_HDSDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSDH.append({H[i], D[i], S[j], D[j], H[k]})

TWO_PAIR_HDSDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDSDD.append({H[i], D[i], S[j], D[j], D[k]})

TWO_PAIR_HDCHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDCHS.append({H[i], D[i], C[j], H[j], S[k]})

TWO_PAIR_HDCHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDCHC.append({H[i], D[i], C[j], H[j], C[k]})

TWO_PAIR_HDCHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDCHH.append({H[i], D[i], C[j], H[j], H[k]})

TWO_PAIR_HDCHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDCHD.append({H[i], D[i], C[j], H[j], D[k]})

TWO_PAIR_HDCDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDCDS.append({H[i], D[i], C[j], D[j], S[k]})

TWO_PAIR_HDCDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDCDC.append({H[i], D[i], C[j], D[j], C[k]})

TWO_PAIR_HDCDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDCDH.append({H[i], D[i], C[j], D[j], H[k]})

TWO_PAIR_HDCDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDCDD.append({H[i], D[i], C[j], D[j], D[k]})

TWO_PAIR_HDHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDHDS.append({H[i], D[i], H[j], D[j], S[k]})

TWO_PAIR_HDHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDHDC.append({H[i], D[i], H[j], D[j], C[k]})

TWO_PAIR_HDHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDHDH.append({H[i], D[i], H[j], D[j], H[k]})

TWO_PAIR_HDHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i !=k and j != k:
                TWO_PAIR_HDHDD.append({H[i], D[i], H[j], D[j], D[k]})

TWO_PAIR = []
TWO_PAIR.extend(TWO_PAIR_SCSCS)
TWO_PAIR.extend(TWO_PAIR_SCSCC)
TWO_PAIR.extend(TWO_PAIR_SCSCH)
TWO_PAIR.extend(TWO_PAIR_SCSCD)
TWO_PAIR.extend(TWO_PAIR_SCSHS)
TWO_PAIR.extend(TWO_PAIR_SCSHC)
TWO_PAIR.extend(TWO_PAIR_SCSHH)
TWO_PAIR.extend(TWO_PAIR_SCSHD)
TWO_PAIR.extend(TWO_PAIR_SCSDS)
TWO_PAIR.extend(TWO_PAIR_SCSDC)
TWO_PAIR.extend(TWO_PAIR_SCSDH)
TWO_PAIR.extend(TWO_PAIR_SCSDD)
TWO_PAIR.extend(TWO_PAIR_SCCHS)
TWO_PAIR.extend(TWO_PAIR_SCCHC)
TWO_PAIR.extend(TWO_PAIR_SCCHH)
TWO_PAIR.extend(TWO_PAIR_SCCHD)
TWO_PAIR.extend(TWO_PAIR_SCCDS)
TWO_PAIR.extend(TWO_PAIR_SCCDC)
TWO_PAIR.extend(TWO_PAIR_SCCDH)
TWO_PAIR.extend(TWO_PAIR_SCCDD)
TWO_PAIR.extend(TWO_PAIR_SCHDS)
TWO_PAIR.extend(TWO_PAIR_SCHDC)
TWO_PAIR.extend(TWO_PAIR_SCHDH)
TWO_PAIR.extend(TWO_PAIR_SCHDD)
TWO_PAIR.extend(TWO_PAIR_SHSCS)
TWO_PAIR.extend(TWO_PAIR_SHSCC)
TWO_PAIR.extend(TWO_PAIR_SHSCH)
TWO_PAIR.extend(TWO_PAIR_SHSCD)
TWO_PAIR.extend(TWO_PAIR_SHSHS)
TWO_PAIR.extend(TWO_PAIR_SHSHC)
TWO_PAIR.extend(TWO_PAIR_SHSHH)
TWO_PAIR.extend(TWO_PAIR_SHSHD)
TWO_PAIR.extend(TWO_PAIR_SHSDS)
TWO_PAIR.extend(TWO_PAIR_SHSDC)
TWO_PAIR.extend(TWO_PAIR_SHSDH)
TWO_PAIR.extend(TWO_PAIR_SHSDD)
TWO_PAIR.extend(TWO_PAIR_SHCHS)
TWO_PAIR.extend(TWO_PAIR_SHCHC)
TWO_PAIR.extend(TWO_PAIR_SHCHH)
TWO_PAIR.extend(TWO_PAIR_SHCHD)
TWO_PAIR.extend(TWO_PAIR_SHCDS)
TWO_PAIR.extend(TWO_PAIR_SHCDC)
TWO_PAIR.extend(TWO_PAIR_SHCDH)
TWO_PAIR.extend(TWO_PAIR_SHCDD)
TWO_PAIR.extend(TWO_PAIR_SHHDS)
TWO_PAIR.extend(TWO_PAIR_SHHDC)
TWO_PAIR.extend(TWO_PAIR_SHHDH)
TWO_PAIR.extend(TWO_PAIR_SHHDD)
TWO_PAIR.extend(TWO_PAIR_SDSCS)
TWO_PAIR.extend(TWO_PAIR_SDSCC)
TWO_PAIR.extend(TWO_PAIR_SDSCH)
TWO_PAIR.extend(TWO_PAIR_SDSCD)
TWO_PAIR.extend(TWO_PAIR_SDSHS)
TWO_PAIR.extend(TWO_PAIR_SDSHC)
TWO_PAIR.extend(TWO_PAIR_SDSHH)
TWO_PAIR.extend(TWO_PAIR_SDSHD)
TWO_PAIR.extend(TWO_PAIR_SDSDS)
TWO_PAIR.extend(TWO_PAIR_SDSDC)
TWO_PAIR.extend(TWO_PAIR_SDSDH)
TWO_PAIR.extend(TWO_PAIR_SDSDD)
TWO_PAIR.extend(TWO_PAIR_SDCHS)
TWO_PAIR.extend(TWO_PAIR_SDCHC)
TWO_PAIR.extend(TWO_PAIR_SDCHH)
TWO_PAIR.extend(TWO_PAIR_SDCHD)
TWO_PAIR.extend(TWO_PAIR_SDCDS)
TWO_PAIR.extend(TWO_PAIR_SDCDC)
TWO_PAIR.extend(TWO_PAIR_SDCDH)
TWO_PAIR.extend(TWO_PAIR_SDCDD)
TWO_PAIR.extend(TWO_PAIR_SDHDS)
TWO_PAIR.extend(TWO_PAIR_SDHDC)
TWO_PAIR.extend(TWO_PAIR_SDHDH)
TWO_PAIR.extend(TWO_PAIR_SDHDD)
TWO_PAIR.extend(TWO_PAIR_CHSCS)
TWO_PAIR.extend(TWO_PAIR_CHSCC)
TWO_PAIR.extend(TWO_PAIR_CHSCH)
TWO_PAIR.extend(TWO_PAIR_CHSCD)
TWO_PAIR.extend(TWO_PAIR_CHSHS)
TWO_PAIR.extend(TWO_PAIR_CHSHC)
TWO_PAIR.extend(TWO_PAIR_CHSHH)
TWO_PAIR.extend(TWO_PAIR_CHSHD)
TWO_PAIR.extend(TWO_PAIR_CHSDS)
TWO_PAIR.extend(TWO_PAIR_CHSDC)
TWO_PAIR.extend(TWO_PAIR_CHSDH)
TWO_PAIR.extend(TWO_PAIR_CHSDD)
TWO_PAIR.extend(TWO_PAIR_CHCHS)
TWO_PAIR.extend(TWO_PAIR_CHCHC)
TWO_PAIR.extend(TWO_PAIR_CHCHH)
TWO_PAIR.extend(TWO_PAIR_CHCHD)
TWO_PAIR.extend(TWO_PAIR_CHCDS)
TWO_PAIR.extend(TWO_PAIR_CHCDC)
TWO_PAIR.extend(TWO_PAIR_CHCDH)
TWO_PAIR.extend(TWO_PAIR_CHCDD)
TWO_PAIR.extend(TWO_PAIR_CHHDS)
TWO_PAIR.extend(TWO_PAIR_CHHDC)
TWO_PAIR.extend(TWO_PAIR_CHHDH)
TWO_PAIR.extend(TWO_PAIR_CHHDD)
TWO_PAIR.extend(TWO_PAIR_CDSCS)
TWO_PAIR.extend(TWO_PAIR_CDSCC)
TWO_PAIR.extend(TWO_PAIR_CDSCH)
TWO_PAIR.extend(TWO_PAIR_CDSCD)
TWO_PAIR.extend(TWO_PAIR_CDSHS)
TWO_PAIR.extend(TWO_PAIR_CDSHC)
TWO_PAIR.extend(TWO_PAIR_CDSHH)
TWO_PAIR.extend(TWO_PAIR_CDSHD)
TWO_PAIR.extend(TWO_PAIR_CDSDS)
TWO_PAIR.extend(TWO_PAIR_CDSDC)
TWO_PAIR.extend(TWO_PAIR_CDSDH)
TWO_PAIR.extend(TWO_PAIR_CDSDD)
TWO_PAIR.extend(TWO_PAIR_CDCHS)
TWO_PAIR.extend(TWO_PAIR_CDCHC)
TWO_PAIR.extend(TWO_PAIR_CDCHH)
TWO_PAIR.extend(TWO_PAIR_CDCHD)
TWO_PAIR.extend(TWO_PAIR_CDCDS)
TWO_PAIR.extend(TWO_PAIR_CDCDC)
TWO_PAIR.extend(TWO_PAIR_CDCDH)
TWO_PAIR.extend(TWO_PAIR_CDCDD)
TWO_PAIR.extend(TWO_PAIR_CDHDS)
TWO_PAIR.extend(TWO_PAIR_CDHDC)
TWO_PAIR.extend(TWO_PAIR_CDHDH)
TWO_PAIR.extend(TWO_PAIR_CDHDD)
TWO_PAIR.extend(TWO_PAIR_HDSCS)
TWO_PAIR.extend(TWO_PAIR_HDSCC)
TWO_PAIR.extend(TWO_PAIR_HDSCH)
TWO_PAIR.extend(TWO_PAIR_HDSCD)
TWO_PAIR.extend(TWO_PAIR_HDSHS)
TWO_PAIR.extend(TWO_PAIR_HDSHC)
TWO_PAIR.extend(TWO_PAIR_HDSHH)
TWO_PAIR.extend(TWO_PAIR_HDSHD)
TWO_PAIR.extend(TWO_PAIR_HDSDS)
TWO_PAIR.extend(TWO_PAIR_HDSDC)
TWO_PAIR.extend(TWO_PAIR_HDSDH)
TWO_PAIR.extend(TWO_PAIR_HDSDD)
TWO_PAIR.extend(TWO_PAIR_HDCHS)
TWO_PAIR.extend(TWO_PAIR_HDCHC)
TWO_PAIR.extend(TWO_PAIR_HDCHH)
TWO_PAIR.extend(TWO_PAIR_HDCHD)
TWO_PAIR.extend(TWO_PAIR_HDCDS)
TWO_PAIR.extend(TWO_PAIR_HDCDC)
TWO_PAIR.extend(TWO_PAIR_HDCDH)
TWO_PAIR.extend(TWO_PAIR_HDCDD)
TWO_PAIR.extend(TWO_PAIR_HDHDS)
TWO_PAIR.extend(TWO_PAIR_HDHDC)
TWO_PAIR.extend(TWO_PAIR_HDHDH)
TWO_PAIR.extend(TWO_PAIR_HDHDD)

lst = []
for i in TWO_PAIR:
    lst.append(list(i))
TWO_PAIR.clear()

for i in lst:
    i.sort()

lst2 = []
for i in lst:
    lst2.append(tuple(i))

lst2 = list(set(lst2))

for i in lst2:
    TWO_PAIR.append(set(i))
