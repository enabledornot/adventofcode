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
    def push(self,weight,d,p):
        heappush(self.h, (weight, d, p))
    def pop(self):
        return heappop(self.h)
def findNewPoints(data,cpoint):
    newp = []
    for did, offset in enumerate([[0,1],[1,0],[0,-1],[-1,0]]):
        potential = cpoint.copy()
        potential[0] += offset[0]
        potential[1] += offset[1]
        if potential[0] >= 0 and potential[0] < len(data) and potential[1] >= 0 and potential[1] < len(data[0]):
            newp.append((did,potential))
    return newp
def find_min(map, start):
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    toExplore = Heap()
    explored = set()
    explored.add(tuple(start))
    toExplore.push(0,0,start.copy())
    while True:
        print(len(toExplore.h))
        dist, d, p = toExplore.pop()
        for did, pos in findNewPoints(map,p):
            if tuple(pos) not in explored:
                if did == d:
                    if map[pos[0]][pos[1]] == '.':
                        explored.add(tuple(pos))
                        toExplore.push(1+dist,d,pos)
                    elif map[pos[0]][pos[1]] == 'E':
                        # print(toExplore.h)
                        # print(pos)
                        return dist + 1
                else:
                    if map[pos[0]][pos[1]] in ['.','E']:
                        toExplore.push(dist + 1000*min(((did-d) % 4),((d-did) % 4)),did,p)
map, start = parse()
min = find_min(map, start)
print(min)