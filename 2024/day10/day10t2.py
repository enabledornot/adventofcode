def parse(filename='input.txt'):
    with open(filename,"r") as f:
        data = f.read().split('\n')[:-1]
    newdata = []
    headmap = []
    headmap2 = []
    trailmask = []
    for line in data:
        newdata.append([])
        headmap.append([])
        headmap2.append([])
        trailmask.append([])
        for c in line:
            headmap[-1].append(set())
            headmap2[-1].append(set())
            trailmask[-1].append(False)
            try:
                newdata[-1].append(int(c))
            except:
                newdata[-1].append(-2)
    return newdata, headmap, headmap2, trailmask
def maskTrails(p,data,tmask):
    pval = data[p[0]][p[1]]
    if pval == 9:
        tmask[p[0]][p[1]] = True
        return True
    currentState = False
    for _, pos in findNewPoints(data,p):
        newval = data[pos[0]][pos[1]]
        if newval == pval + 1:
            if maskTrails(pos,data,tmask):
                currentState = True
    if currentState:
        tmask[p[0]][p[1]] = True
    return currentState
def findNewPoints(data,cpoint):
    newp = []
    for did, offset in enumerate([[0,1],[1,0],[0,-1],[-1,0]]):
        potential = list(cpoint)
        potential[0] += offset[0]
        potential[1] += offset[1]
        if potential[0] >= 0 and potential[0] < len(data) and potential[1] >= 0 and potential[1] < len(data[0]):
            newp.append((did,potential))
    return newp
def isTrailhead(allSets):
    for s0 in allSets:
        for s1 in allSets:
            if s0 != s1:
                return True
    return False
def findTrailCount(p,data,hmap,hmap2,startp):
    # if tuple(p) == (1,6):
    #     import ipdb; ipdb.set_trace()
    nines = set()
    upcnt = 0
    dncnt = 0
    pvalue = data[p[0]][p[1]]
    if pvalue == 9:
        hmap[p[0]][p[1]] = hmap[p[0]][p[1]].union({tuple(p)})
        return set([tuple(p)])
    for _, pos in findNewPoints(data,p):
        newval = data[pos[0]][pos[1]]
        if newval == pvalue + 1:
            upcnt += 1
            nnines = findTrailCount(pos,data,hmap,hmap2,startp)
            nines = nines.union(nnines)
    hmap[p[0]][p[1]] = hmap[p[0]][p[1]].union(nines)
    hmap2[p[0]][p[1]] = hmap2[p[0]][p[1]].union({startp})
    return nines
def flipMap(map):
    newmap = []
    for line in map:
        newmap.append([])
        for c in line:
            if c >= 0:
                newmap[-1].append(abs(c-9))
            else:
                newmap[-1].append(c)
    return newmap
def printGrid(grid,min=0):
    for line in grid:
        print('')
        for c in line:
            if isinstance(c,int):
                if c >= min:
                    print(c,end='')
                else:
                    print('-',end='')
            else:
                print(len(c),end='')
    print('')
map,hmap,hmap2,tmask = parse(filename='input.txt')
for line in map:
    print(line)
for i, line in enumerate(map):
    for ii, c in enumerate(line):
        if c == 0:
            maskTrails((i,ii),map,tmask)
for i, line in enumerate(tmask):
    for ii, c in enumerate(line):
        if not c:
            map[i][ii] = -3
printGrid(map)
# for line in map:
#     print(line)
# print(findTrailCount((1,6),map,hmap,hmap2,(0,0)))
# print(hmap[1][6])
# asdf
sum = 0
allsum = []
mapinv = flipMap(map)
printGrid(mapinv)
for i, line in enumerate(map):
    for ii, c in enumerate(line):
        if c == 0:
            s = findTrailCount((i,ii),map,hmap,hmap2,(i,ii))
for i, line in enumerate(map):
    for ii, pval in enumerate(line):
        ups = []
        dons = []
        for _, pos in findNewPoints(map,(i,ii)):
            posval = map[pos[0]][pos[1]]
            if pval + 1 == posval:
                ups.append(hmap[pos[0]][pos[1]])
            elif pval - 1 == posval:
                dons.append(hmap2[pos[0]][pos[1]])
        if len(ups) >= 2 or len(dons) >= 2:
            if isTrailhead(ups) or isTrailhead(dons):
                # print(len(hmap[i][ii]))
                print((i,ii))
                newsum = len(hmap[i][ii])
                print(newsum)
                # print(hmap[p[0]][p[1]])
                # allsum.append(len(hmap[p[0]][p[1]]))
                sum += newsum
# for line in hmap:
#     for c in line:
#         # if c != 0:
#         #     print(c)
#         sum += c
# printGrid(map)
# printGrid(hmap,min=1)
# print(hmap[1][6])
# for line in hmap:
#     print('')
#     for c in line:
#         print(c,end='')
sum = 0
for l1,l2 in zip(map,hmap):
    for mv, hv in zip(l1,l2):
        if mv == 0:
            sum += len(hv)
# print('')
print(sum)
# print(sorted(allsum))
