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
connections = parse(filename='input.txt')
cdict = buildConnectionDict(connections)
rings = findRings(cdict)
cnt = 0
for ring in rings:
    for e in ring:
        if e[0] == 't':
            cnt += 1
            break
print(cnt)