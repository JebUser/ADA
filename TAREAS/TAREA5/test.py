ANS = []

def subsetsum(X, i, T, SB:set):
    if T == 0:
        ANS.append(SB.copy())
    elif T > 0 and i != -1:
        SB.add(X[i])
        subsetsum(X, i-1, T-X[i], SB)
        SB.remove(X[i])
        subsetsum(X, i-1, T, SB)

X = [1, 2, 3]
SB = set()
subsetsum(X, len(X)-1, 5, SB)
print(ANS, len(ANS))

ANS = []

def subsetsumW(X, i, T, SB:set, P):
    if T == 0:
        ANS.append((SB.copy(), P))
    elif T > 0 and i != -1:
        SB.add(X[i])
        subsetsumW(X, i-1, T-X[i], SB, P+W[i])
        SB.remove(X[i])
        subsetsumW(X, i-1, T, SB, P)

X = [1, 2, 3, 4]
W = [5, 3, 1, 2]
SB = set()
subsetsumW(X, len(X)-1, 5, SB, 0)

if len(ANS) == 0:
    print(float('inf'))
elif len(ANS) == 1:
    print(ANS)
else:
    ANS.sort(key = lambda x: x[1])
    print(ANS[len(ANS)-1], len(ANS))