from heapq import heappush, heappop
def parse(file="input.txt"):
    with open(file,"r") as f:
        data = f.read().split('\n')[:-1]
    newdata = []
    start = []
    for i,line in enumerate(data):
        newdata.append(list(line))
        if 'S' in newdata[-1]:
            start = [i,newdata[-1].index('S')]
        
    return data, start
class Heap:
    def __init__(self):
        self.h = []
        self.lookup = []
    def push(self,weight,d,p,exp):
        heappush(self.h, (weight,d,tuple(p),len(self.lookup)))
        self.lookup.append((weight, d, p, exp))
    def pop(self):
        index = heappop(self.h)[-1]
        return self.lookup[index]
    def peek(self):
        if len(self.h) == 0:
            return (None, None, None, None)
        index = self.h[0][-1]
        return self.lookup[index]
    def showTop(self,amnt=3):
        for tpl in self.h[:amnt]:
            try:
                print(self.lookup[tpl[-1]][:3])
            except:
                pass
        print("")
def findNewPoints(data,cpoint):
    newp = []
    for did, offset in enumerate([[0,1],[1,0],[0,-1],[-1,0]]):
        potential = cpoint.copy()
        potential[0] += offset[0]
        potential[1] += offset[1]
        if potential[0] >= 0 and potential[0] < len(data) and potential[1] >= 0 and potential[1] < len(data[0]):
            newp.append((did,potential))
    return newp
# def find_min(map, start):
#     directions = [[0,1],[1,0],[0,-1],[-1,0]]
#     toExplore = Heap()
#     explored = set()
#     explored.add(tuple(start))
#     toExplore.push(0,0,start.copy(),[tuple(start)])
#     while True:
#         dist, d, p, prev = toExplore.pop()
#         mergeCnt = 0
#         nextPeek = toExplore.peek()
#         while nextPeek[0] == dist and nextPeek[1] == d and nextPeek[2] == p:
#             mergeCnt += 1
#         for i in range(mergeCnt):
#             nprev = toExplore.pop()[3]
#             prev = prev
#         print(dist)
#         for did, pos in findNewPoints(map,p):
#             if tuple(pos) not in explored:
#                 if did == d:
#                     if map[pos[0]][pos[1]] == '.':
#                         toExplore.push(1+dist,d,pos,None)
#                     elif map[pos[0]][pos[1]] == 'E':
#                         return dist + 1
#                 else:
#                     if map[pos[0]][pos[1]] in ['.','E']:
#                         toExplore.push(dist + 1000*min(((did-d) % 4),((d-did) % 4)),did,p,prev)
def find_min_old(map, start):
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    toExplore = Heap()
    explored = set()
    # explored.add(tuple(start))
    toExplore.push(0,0,start.copy(),set([tuple(start)]))
    print(toExplore.lookup)
    minCost = 100000000000000000000000000
    neededSet = set()
    while True:
        # toExplore.showTop()
        # print(len(toExplore.h))
        dist, d, p, prev = toExplore.pop()
        nextPeek = toExplore.peek()
        popped = []
        while nextPeek[0] == dist and nextPeek[1] == d and tuple(nextPeek[2]) == tuple(p):
            popped.append(toExplore.pop())
            nextPeek = toExplore.peek()
        for pop in popped:
            # print(pop[2])
            # print("merging")
            # toExplore.showTop()
            oldlen = len(prev)
            # print(prev)
            # print(pop[3])
            # print("---")
            prev = prev | pop[3]
            if oldlen > len(prev):
                print('addmore')
        # print(p)
        if tuple(p + [d]) not in explored:
            explored.add(tuple(p + [d]))
            for did, pos in findNewPoints(map,p):
                if did == d:
                    if map[pos[0]][pos[1]] == '.':
                        toExplore.push(1+dist,d,pos,prev | set([tuple(pos)]))
                    elif map[pos[0]][pos[1]] == 'E':
                        if dist <= minCost:
                            minCost = dist
                            neededSet.update(prev)
                        else:
                            # print(neededSet)
                            return neededSet
                    # print(toExplore.h)
                    # print(pos)
                    # return dist + 1
                else:
                    if map[pos[0]][pos[1]] in ['.','E']:
                        toExplore.push(dist + 1000*min(((did-d) % 4),((d-did) % 4)),did,p,prev)
    # print(toExplore.h)
map, start = parse()
ns = find_min_old(map, start)
for i,line in enumerate(map):
    for ii,c in enumerate(line):
        if (i,ii) in ns:
            print("O",end="")
        else:
            print(c,end="")
    print('')
print(len(ns)+1)