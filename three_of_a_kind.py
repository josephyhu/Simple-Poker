import deck
import copy

S = copy.deepcopy(deck.SPADES)
C = copy.deepcopy(deck.CLUBS)
H = copy.deepcopy(deck.HEARTS)
D = copy.deepcopy(deck.DIAMONDS)

THREE_OF_A_KIND_SCHSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHSS.append({S[i], C[i], H[i], S[j], S[k]})

THREE_OF_A_KIND_SCHSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHSC.append({S[i], C[i], H[i], S[j], C[k]})

THREE_OF_A_KIND_SCHSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHSH.append({S[i], C[i], H[i], S[j], H[k]})

THREE_OF_A_KIND_SCHSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHSD.append({S[i], C[i], H[i], S[j], D[k]})

THREE_OF_A_KIND_SCHCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHCS.append({S[i], C[i], H[i], C[j], S[k]})

THREE_OF_A_KIND_SCHCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHCC.append({S[i], C[i], H[i], C[j], C[k]})

THREE_OF_A_KIND_SCHCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHCH.append({S[i], C[i], H[i], C[j], H[k]})

THREE_OF_A_KIND_SCHCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHCD.append({S[i], C[i], H[i], C[j], D[k]})

THREE_OF_A_KIND_SCHHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHHS.append({S[i], C[i], H[i], H[j], S[k]})

THREE_OF_A_KIND_SCHHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHHC.append({S[i], C[i], H[i], H[j], C[k]})

THREE_OF_A_KIND_SCHHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHHH.append({S[i], C[i], H[i], H[j], H[k]})

THREE_OF_A_KIND_SCHHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHHD.append({S[i], C[i], H[i], H[j], D[k]})

THREE_OF_A_KIND_SCHDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHDS.append({S[i], C[i], H[i], D[j], S[k]})

THREE_OF_A_KIND_SCHDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHDC.append({S[i], C[i], H[i], D[j], C[k]})

THREE_OF_A_KIND_SCHDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHDH.append({S[i], C[i], H[i], D[j], H[k]})

THREE_OF_A_KIND_SCHDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCHDD.append({S[i], C[i], H[i], D[j], D[k]})

THREE_OF_A_KIND_SCDSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDSS.append({S[i], C[i], D[i], S[j], S[k]})

THREE_OF_A_KIND_SCDSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDSC.append({S[i], C[i], D[i], S[j], C[k]})

THREE_OF_A_KIND_SCDSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDSH.append({S[i], C[i], D[i], S[j], H[k]})

THREE_OF_A_KIND_SCDSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDSD.append({S[i], C[i], D[i], S[j], D[k]})

THREE_OF_A_KIND_SCDCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDCS.append({S[i], C[i], D[i], C[j], S[k]})

THREE_OF_A_KIND_SCDCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDCC.append({S[i], C[i], D[i], C[j], C[k]})

THREE_OF_A_KIND_SCDCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDCH.append({S[i], C[i], D[i], C[j], H[k]})

THREE_OF_A_KIND_SCDCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDCD.append({S[i], C[i], D[i], C[j], D[k]})

THREE_OF_A_KIND_SCDHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDHS.append({S[i], C[i], D[i], H[j], S[k]})

THREE_OF_A_KIND_SCDHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDHC.append({S[i], C[i], D[i], H[j], C[k]})

THREE_OF_A_KIND_SCDHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDHH.append({S[i], C[i], D[i], H[j], H[k]})

THREE_OF_A_KIND_SCDHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDHD.append({S[i], C[i], D[i], H[j], D[k]})

THREE_OF_A_KIND_SCDDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDDS.append({S[i], C[i], D[i], D[j], S[k]})

THREE_OF_A_KIND_SCDDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDDC.append({S[i], C[i], D[i], D[j], C[k]})

THREE_OF_A_KIND_SCDDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDDH.append({S[i], C[i], D[i], D[j], H[k]})

THREE_OF_A_KIND_SCDDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SCDDD.append({S[i], C[i], D[i], D[j], D[k]})

THREE_OF_A_KIND_SHDSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDSS.append({S[i], H[i], D[i], S[j], S[k]})

THREE_OF_A_KIND_SHDSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDSC.append({S[i], H[i], D[i], S[j], C[k]})

THREE_OF_A_KIND_SHDSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDSH.append({S[i], H[i], D[i], S[j], H[k]})

THREE_OF_A_KIND_SHDSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDSD.append({S[i], H[i], D[i], S[j], D[k]})

THREE_OF_A_KIND_SHDCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDCS.append({S[i], H[i], D[i], C[j], S[k]})

THREE_OF_A_KIND_SHDCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDCC.append({S[i], H[i], D[i], C[j], C[k]})

THREE_OF_A_KIND_SHDCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDCH.append({S[i], H[i], D[i], C[j], H[k]})

THREE_OF_A_KIND_SHDCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDCD.append({S[i], H[i], D[i], C[j], D[k]})

THREE_OF_A_KIND_SHDHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDHS.append({S[i], H[i], D[i], H[j], S[k]})

THREE_OF_A_KIND_SHDHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDHC.append({S[i], H[i], D[i], H[j], C[k]})

THREE_OF_A_KIND_SHDHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDHH.append({S[i], H[i], D[i], H[j], H[k]})

THREE_OF_A_KIND_SHDHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDHD.append({S[i], H[i], D[i], H[j], D[k]})

THREE_OF_A_KIND_SHDDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDDS.append({S[i], H[i], D[i], D[j], S[k]})

THREE_OF_A_KIND_SHDDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDDC.append({S[i], H[i], D[i], D[j], C[k]})

THREE_OF_A_KIND_SHDDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDDH.append({S[i], H[i], D[i], D[j], H[k]})

THREE_OF_A_KIND_SHDDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_SHDDD.append({S[i], H[i], D[i], D[j], D[k]})

THREE_OF_A_KIND_CHDSS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDSS.append({C[i], H[i], D[i], S[j], S[k]})

THREE_OF_A_KIND_CHDSC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDSC.append({C[i], H[i], D[i], S[j], C[k]})

THREE_OF_A_KIND_CHDSH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDSH.append({C[i], H[i], D[i], S[j], H[k]})

THREE_OF_A_KIND_CHDSD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDSD.append({C[i], H[i], D[i], S[j], D[k]})

THREE_OF_A_KIND_CHDCS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDCS.append({C[i], H[i], D[i], C[j], S[k]})

THREE_OF_A_KIND_CHDCC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDCC.append({C[i], H[i], D[i], C[j], C[k]})

THREE_OF_A_KIND_CHDCH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDCH.append({C[i], H[i], D[i], C[j], H[k]})

THREE_OF_A_KIND_CHDCD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDCD.append({C[i], H[i], D[i], C[j], D[k]})

THREE_OF_A_KIND_CHDHS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDHS.append({C[i], H[i], D[i], H[j], S[k]})

THREE_OF_A_KIND_CHDHC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDHC.append({C[i], H[i], D[i], H[j], C[k]})

THREE_OF_A_KIND_CHDHH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDHH.append({C[i], H[i], D[i], H[j], H[k]})

THREE_OF_A_KIND_CHDHD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDHD.append({C[i], H[i], D[i], H[j], D[k]})

THREE_OF_A_KIND_CHDDS = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDDS.append({C[i], H[i], D[i], D[j], S[k]})

THREE_OF_A_KIND_CHDDC = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDDC.append({C[i], H[i], D[i], D[j], C[k]})

THREE_OF_A_KIND_CHDDH = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDDH.append({C[i], H[i], D[i], D[j], H[k]})

THREE_OF_A_KIND_CHDDD = []
for i in range(13):
    for j in range(13):
        for k in range(13):
            if i != j and i != k and j != k:
                THREE_OF_A_KIND_CHDDD.append({C[i], H[i], D[i], D[j], D[k]})

THREE_OF_A_KIND = []
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHSS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHSC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHSH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHSD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHCS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHCC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHCH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHCD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHHS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHHC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHHH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHHD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHDS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHDC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHDH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCHDD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDSS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDSC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDSH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDSD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDCS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDCC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDCH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDCD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDHS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDHC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDHH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDHD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDDS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDDC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDDH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SCDDD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDSS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDSC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDSH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDSD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDCS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDCC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDCH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDCD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDHS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDHC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDHH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDHD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDDS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDDC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDDH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_SHDDD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDSS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDSC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDSH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDSD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDCS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDCC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDCH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDCD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDHS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDHC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDHH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDHD)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDDS)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDDC)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDDH)
THREE_OF_A_KIND.extend(THREE_OF_A_KIND_CHDDD)

lst = []
for i in THREE_OF_A_KIND:
    lst.append(list(i))
THREE_OF_A_KIND.clear()

for i in lst:
    i.sort()

lst2 = []
for i in lst:
    lst2.append(tuple(i))

lst2 = list(set(lst2))

for i in lst2:
    THREE_OF_A_KIND.append(set(i))

print(len(THREE_OF_A_KIND))
