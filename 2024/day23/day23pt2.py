from tqdm import tqdm
def parse(filename='input.txt'):
    with open(filename, "r") as f:
        data = f.read().split('\n')[:-1]
    newdata = []
    for line in data:
        newdata.append(tuple(line.split('-')))
    return newdata
def buildConnectionDict(connections):
    connectDict = {}
    for c1, c2 in connections:
        if c1 not in connectDict:
            connectDict[c1] = set()
        connectDict[c1].add(c2)
        if c2 not in connectDict:
            connectDict[c2] = set()
        connectDict[c2].add(c1)
    return connectDict
def findRings(cdict):
    rings = set()
    for cmp1 in cdict:
        for cmp2 in cdict[cmp1]:
            for cmp3 in cdict[cmp2]:
                if cmp1 in cdict[cmp3]:
                    rings.add(tuple(sorted([cmp1,cmp2,cmp3])))
    return rings
def findSets(cdict):
    sets = set()
    for cmp1 in cdict:
        for cmp2 in cdict:
            if cmp1 != cmp2:
                newset = tuple(sorted(list(cdict[cmp1].intersection(cdict[cmp2]))))
                sets.add(newset)
    return sets
def tupleize(seat):
    return tuple(sorted(list(seat)))
def tupleadd(tupl,new):
    liste = list(tupl)
    liste.append(new)
    return tuple(sorted(liste))
connections = parse(filename='input.txt')
cdict = buildConnectionDict(connections)
intersects = {}
maxIntersect = 0
for cmp1 in cdict:
    for cmp2 in cdict:
        if cmp1 != cmp2 and cmp2 in cdict[cmp1] and cmp1 in cdict[cmp2]:
            interx = cdict[cmp1].intersection(cdict[cmp2])
            if len(interx) > maxIntersect:
                maxIntersect = len(interx)
            if len(interx) == maxIntersect:
                intersects[(cmp1,cmp2)] = interx

newInt = intersects
i = 0
while len(newInt) > 0:
    print(i)
    intersects = newInt
    newInt = {}
    maxIntersect = 0
    for cmps in tqdm(intersects):
        for cmp2 in cdict:
            if cmp2 not in cmps:
                for cmp in cmps:
                    if cmp not in cdict[cmp2]:
                        break
                else:
                    keytup = tupleadd(cmps,cmp2)
                    if keytup not in newInt:
                        interx = intersects[cmps].intersection(cdict[cmp2])
                        if len(interx) > maxIntersect:
                            maxIntersect = len(interx)
                        if len(interx) == maxIntersect:
                            newInt[keytup] = interx
    i = i + 1
print(len(intersects))
print(','.join(list(intersects.keys())[0]))
# print(len(cdict))