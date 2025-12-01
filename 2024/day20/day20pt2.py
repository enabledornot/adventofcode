from functools import cache
from tqdm import tqdm
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
    savings = 0
    for i, line in enumerate(tqdm(map)):
        for ii, c in enumerate(line):
            if isinstance(c,int):
                p = (i,ii)
                cheats = getCheats(map,(i,ii),map[i][ii])
                savings += cheats
                # savings[p] = cheats
                # savings[p] = {}
                # for dest in cheats:
                #     if cheats[dest] > 0:
                #         savings[(p,dest)] = cheats[dest]
                        # savings[p][dest] = cheats[dest]
    return savings
                        
    return savings
def getCheats(map, p, sw):
    cheats = {}
    min0 = 0
    max0 = len(map)
    min1 = 0
    max1 = len(map[0])
    cnt = 0
    min0 = max(0,p[0]-20)
    max0 = min(len(map),p[0]+21)
    min1 = max(0,p[1]-20)
    max1 = min(len(map[0]),p[1]+21)
    for i in range(min0,max0):
        for ii in range(min1,max1):
            if abs(p[0]-i) + abs(p[1]-ii) <= 20:
                val = map[i][ii]
                if isinstance(val,int):
                    weight = val - sw - abs(p[0]-i) - abs(p[1]-ii)
                    if weight >= 100:
                        cnt += 1
                    # cheats[(i,ii)] = val - sw - abs(p[0]-i) - abs(p[1]-ii)
    return cnt
def computeDist(map,src,dest):
    src = tuple(src)
    dest = tuple(dest)
    visited = set()
    toDo = PriorityQueue()
    for _, np in findNewPoints(map, src):
        toDo.put((1,np))
    while True:
        c, p = toDo.get(block=False)
        if c > 20:
            return
        pv = map[p[0]][p[1]]
        if p == dest:
            return c
        if p not in visited and pv == '#':
            visited.add(p)
            for _, np in findNewPoints(map, p):
                toDo.put((c+1,np))
def checkCheet(map,s,d):
    if d[0] == s[0]:
        m0 = 0
    else:
        m0 = int((d[0]-s[0]) / abs(d[0]-s[0]))
    if d[1] == s[1]:
        m1 = 0
    else:
        m1 = int((d[1]-s[1]) / abs(d[1]-s[1]))
    if m0 == 0:
        return map[s[0]][s[1]+m1] == '#' and map[d[0]][d[1]-m1] == '#'
    elif m1 == 0:
        return map[s[0]+m0][s[1]] == '#' and map[d[0]+m0][d[1]] == '#'
    return map[s[0]+m0][s[1]] == '#' and map[s[0]][s[1]+m1] == '#' and map[d[0]-m0][d[1]] == '#' and map[d[0]][d[1]-m1]
    # if map[s[0]+m0][s[1]] == '#':
    #     if map[d[0]][d[1]-m1] == '#':
    #         return True
    # if map[s[0]][s[1]+m1] == '#':
    #     if map[d[0]-m0][d[1]] == '#':
    #         return True
    return False
map, startP = parse(filename='input.txt')
for i in map:
    print(i)
buildMap(map,startP)
print("")
for i in map:
    print(i)
result = calculateAllSavings(map)
print(result)
# newres = {}
# for src,dest in result:
#     # if checkCheet(map,src,dest):
#     newres[(src,dest)] = result[(src,dest)]
# print(len(result))
# print(len(newres))
# cnt = 0
# counts = {}
# for r in newres:
#     res = newres[r]
#     if res > 0:
#         if res not in counts:
#             counts[res] = 0
#         counts[res] += 1
#     if res >= 100:
#         # print(r)
#         cnt += 1
#         # print(res)
# # print("")
# # for pc in range(200):
# #     if pc in counts:
# #         print(f"counts[{pc}] = {counts[pc]}")
# print(cnt)