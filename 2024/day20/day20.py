from functools import cache
from queue import PriorityQueue
def parse(filename="input.txt"):
    with open(filename,"r") as f:
        map = f.read().split('\n')[:-1]
    newmap = []
    posA = []
    for i,line in enumerate(map):
        newmap.append(list(line))
        if 'S' in newmap[-1]:
            posA = [i,newmap[-1].index('S')]
            newmap[-1][newmap[-1].index('S')] = '.'
    return newmap, posA
def findNewPoints(data,cpoint):
    newp = []
    for did, offset in enumerate([[0,1],[1,0],[0,-1],[-1,0]]):
        potential = list(cpoint)
        potential[0] += offset[0]
        potential[1] += offset[1]
        if potential[0] >= 0 and potential[0] < len(data) and potential[1] >= 0 and potential[1] < len(data[0]):
            newp.append((offset,tuple(potential)))
    return newp
def buildMap(map, sp):
    toDo = PriorityQueue()
    toDo.put((0,sp))
    while True:
        try:
            c, p = toDo.get(block=False)
        except:
            return
        if map[p[0]][p[1]] == '.':
            map[p[0]][p[1]] = c
            for _, np in findNewPoints(map,p):
                toDo.put((c+1,np))
        elif map[p[0]][p[1]] == 'E':
            map[p[0]][p[1]] = c
            return
def calculateAllSavings(map):
    savings = []
    for i, line in enumerate(map):
        for ii, c in enumerate(line):
            if isinstance(c,int):
                for d, np in findNewPoints(map,[i,ii]):
                    if map[np[0]][np[1]] == '#':
                        nnp = [np[0]+d[0],np[1]+d[1]]
                        if nnp[0] >= 0 and nnp[0] < len(map) and nnp[1] >= 0 and nnp[1] < len(map[0]):
                            nnpv = map[nnp[0]][nnp[1]]
                            if isinstance(nnpv,int):
                                savings.append(nnpv - c - 2)
    return savings
map, startP = parse(filename='input.txt')
for i in map:
    print(i)
buildMap(map,startP)
print("")
for i in map:
    print(i)
result = calculateAllSavings(map)
cnt = 0
counts = {}
for res in result:
    if res > 0:
        if res not in counts:
            counts[res] = 0
        counts[res] += 1
    if res >= 100:
        cnt += 1
        # print(res)
print("")
print(counts)
print(cnt)