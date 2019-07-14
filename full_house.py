import deck
import copy

S = copy.deepcopy(deck.SPADES)
C = copy.deepcopy(deck.CLUBS)
H = copy.deepcopy(deck.HEARTS)
D = copy.deepcopy(deck.DIAMONDS)

FULL_HOUSE_SCHSC = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCHSC.append({S[i], C[i], H[i], S[j], C[j]})
FULL_HOUSE_SCHSH = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCHSH.append({S[i], C[i], H[i], S[j], H[j]})
FULL_HOUSE_SCHSD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCHSD.append({S[i], C[i], H[i], S[j], D[j]})
FULL_HOUSE_SCHCH = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCHCH.append({S[i], C[i], H[i], C[j], H[j]})
FULL_HOUSE_SCHCD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCHCD.append({S[i], C[i], H[i], C[j], D[j]})
FULL_HOUSE_SCHHD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCHHD.append({S[i], C[i], H[i], H[j], D[j]})

FULL_HOUSE_SCDSC = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCDSC.append({S[i], C[i], D[i], S[j], C[j]})
FULL_HOUSE_SCDSH = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCDSH.append({S[i], C[i], D[i], S[j], H[j]})
FULL_HOUSE_SCDSD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCDSD.append({S[i], C[i], D[i], S[j], D[j]})
FULL_HOUSE_SCDCH = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCDCH.append({S[i], C[i], D[i], C[j], H[j]})
FULL_HOUSE_SCDCD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCDCD.append({S[i], C[i], D[i], C[j], D[j]})
FULL_HOUSE_SCDHD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SCDHD.append({S[i], C[i], D[i], H[j], D[j]})

FULL_HOUSE_SHDSC = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SHDSC.append({S[i], H[i], D[i], S[j], C[j]})
FULL_HOUSE_SHDSH = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SHDSH.append({S[i], H[i], D[i], S[j], H[j]})
FULL_HOUSE_SHDSD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SHDSD.append({S[i], H[i], D[i], S[j], D[j]})
FULL_HOUSE_SHDCH = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SHDCH.append({S[i], H[i], D[i], C[j], H[j]})
FULL_HOUSE_SHDCD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SHDCD.append({S[i], H[i], D[i], C[j], D[j]})
FULL_HOUSE_SHDHD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_SHDHD.append({S[i], H[i], D[i], H[j], D[j]})

FULL_HOUSE_CHDSC = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_CHDSC.append({C[i], H[i], D[i], S[j], C[j]})
FULL_HOUSE_CHDSH = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_CHDSH.append({C[i], H[i], D[i], S[j], H[j]})
FULL_HOUSE_CHDSD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_CHDSD.append({C[i], H[i], D[i], S[j], D[j]})
FULL_HOUSE_CHDCH = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_CHDCH.append({C[i], H[i], D[i], C[j], H[j]})
FULL_HOUSE_CHDCD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_CHDCD.append({C[i], H[i], D[i], C[j], D[j]})
FULL_HOUSE_CHDHD = []
for i in range(13):
    for j in range(13):
        if i != j:
            FULL_HOUSE_CHDHD.append({C[i], H[i], D[i], H[j], D[j]})

FULL_HOUSE_SCH = []
FULL_HOUSE_SCH.extend(FULL_HOUSE_SCHSC)
FULL_HOUSE_SCH.extend(FULL_HOUSE_SCHSH)
FULL_HOUSE_SCH.extend(FULL_HOUSE_SCHSD)
FULL_HOUSE_SCH.extend(FULL_HOUSE_SCHCH)
FULL_HOUSE_SCH.extend(FULL_HOUSE_SCHCD)
FULL_HOUSE_SCH.extend(FULL_HOUSE_SCHHD)

FULL_HOUSE_SCD = []
FULL_HOUSE_SCD.extend(FULL_HOUSE_SCDSC)
FULL_HOUSE_SCD.extend(FULL_HOUSE_SCDSH)
FULL_HOUSE_SCD.extend(FULL_HOUSE_SCDSD)
FULL_HOUSE_SCD.extend(FULL_HOUSE_SCDCH)
FULL_HOUSE_SCD.extend(FULL_HOUSE_SCDCD)
FULL_HOUSE_SCD.extend(FULL_HOUSE_SCDHD)

FULL_HOUSE_SHD = []
FULL_HOUSE_SHD.extend(FULL_HOUSE_SHDSC)
FULL_HOUSE_SHD.extend(FULL_HOUSE_SHDSH)
FULL_HOUSE_SHD.extend(FULL_HOUSE_SHDSD)
FULL_HOUSE_SHD.extend(FULL_HOUSE_SHDCH)
FULL_HOUSE_SHD.extend(FULL_HOUSE_SHDCD)
FULL_HOUSE_SHD.extend(FULL_HOUSE_SHDHD)

FULL_HOUSE_CHD = []
FULL_HOUSE_CHD.extend(FULL_HOUSE_CHDSC)
FULL_HOUSE_CHD.extend(FULL_HOUSE_CHDSH)
FULL_HOUSE_CHD.extend(FULL_HOUSE_CHDSD)
FULL_HOUSE_CHD.extend(FULL_HOUSE_CHDCH)
FULL_HOUSE_CHD.extend(FULL_HOUSE_CHDCD)
FULL_HOUSE_CHD.extend(FULL_HOUSE_CHDHD)

FULL_HOUSE = []
FULL_HOUSE.extend(FULL_HOUSE_SCH)
FULL_HOUSE.extend(FULL_HOUSE_SCD)
FULL_HOUSE.extend(FULL_HOUSE_SHD)
FULL_HOUSE.extend(FULL_HOUSE_CHD)
