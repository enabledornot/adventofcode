import sys
def parse(fname):
    with open(fname,"r") as f:
        data = f.read().split("\n")
    ndata = []
    for line in data:
        ndata.append(numerise(line.split(",")))
    return ndata
def numerise(split):
    ntuple = []
    for num in split:
        ntuple.append(int(num))
    return tuple(ntuple)
def getRange(posSet):
    min = [500,500,500]
    max = [0,0,0]
    for point in posSet:
        for direction in range(3):
            if point[direction]<min[direction]:
                min[direction] = point[direction]
            if point[direction]>max[direction]:
                max[direction] = point[direction]
    return min,max
def findSA(points, axis):
    spoints = sorted(points, key = lambda x: (x[(axis+1)%3],x[(axis+2)%3],x[axis]))
    last = spoints[0][axis]
    currentColumn = (spoints[0][(axis+1)%3],spoints[0][(axis+2)%3])
    cnt = 0
    for point in spoints[1:]:
        if point[(axis+1)%3]==currentColumn[0] and point[(axis+2)%3]==currentColumn[1]:
            diff = point[axis]-last
            if diff==1:
                cnt+=2
        last = point[axis]
        currentColumn = (point[(axis+1)%3],point[(axis+2)%3])
    # cnt+=2
    return 2*len(points)-cnt
# def findSA(points, axis):
#     maped = {}
#     for point in points:
#         key = str([point[(axis+1)%3],point[(axis+2)%3]])
#         if key not in maped:
#             maped[key] = []
#         maped[key].append(point[axis])
#     sum = 0
#     for row in maped:
#         sort = sorted(maped[row])
#         print(sort)
#         cnt = 0
#         while (cnt+1)<len(sort):
#             diff = maped[row][cnt+1]-maped[row][cnt]
#             print(diff)
#             if diff==1:
#                 sum+=1
#             cnt+=1
#     return 2*(len(points)-cnt)
def findFullSA(points):
    sum = 0
    for i in range(3):
        sum+=findSA(points, i)
    return sum
def crossMultiply(min, max, factor):
    nmax = [2*factor + max[0]-min[0], 2*factor + max[1]-min[1], 2*factor + max[2]-min[2]]
    return nmax[0]*nmax[1] + nmax[1]*nmax[2] + nmax[2]*nmax[0]
def buildArray(data):
    min, max = getRange(data)
    new = []
    for i in range(min[0]-1,max[0]+2):
        new.append([])
        for ii in range(min[1]-1,max[1]+2):
            new[-1].append([])
            for iii in range(min[2]-1,max[2]+2):
                if (i,ii,iii) in data:
                    new[-1][-1].append(1)
                elif i==min[0]-1 or ii==min[1]-1 or iii==min[2]-1 or i==max[0]+1 or ii==max[1]+1 or iii==max[2]+1:
                    new[-1][-1].append(2)
                else:
                    new[-1][-1].append(0)
    return new
class escapeCached:
    def __init__(self, map):
        self.points = map
        self.cache = {}
        self.min, self.max = getRange(map)
    def canEscape(self, pos, prev):
        # print(pos)
        # print(prev)
        key = str(pos)
        if not key in self.cache:
            self.cache[key] = self.canEscapeU(pos, prev)
        return self.cache[key]
    def canEscapeU(self, pos, prev):
        if pos in prev:
            return False
        if pos in self.points:
            return False
        for dir in range(3):
            if pos[dir]<self.min[dir] or pos[dir]>self.max[dir]:
                return True
        newPrev = prev.copy()
        newPrev.append(pos)
        for move in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
            if self.canEscape((pos[0]+move[0],pos[1]+move[1],pos[2]+move[2]),newPrev):
                return True
        return False
moves = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
def floodFill(arrayMap):
    count = 1
    while count!=0:
        count = 0
        for i in range(len(arrayMap)):
            for ii in range(len(arrayMap[0])):
                for iii in range(len(arrayMap[0][0])):
                    if arrayMap[i][ii][iii]==2:
                        for move in moves:
                            ni = i + move[0]
                            nii = ii + move[1]
                            niii = iii + move[2]
                            if 0<=ni<len(arrayMap) and 0<=nii<len(arrayMap[0]) and 0<=niii<len(arrayMap[0][0]) and arrayMap[ni][nii][niii]==0:
                                arrayMap[ni][nii][niii] = 2
                                count+=1
def findPoints(arrayMap):
    points = []
    for i in range(len(arrayMap)):
        for ii in range(len(arrayMap[0])):
            for iii in range(len(arrayMap[0][0])):
                if arrayMap[i][ii][iii]<2:
                    points.append((i,ii,iii))
    return points

parsed = parse("input.txt")
arrayMap = buildArray(parsed)
for i in arrayMap:
    for ii in i:
        for iii in ii:
            print(iii,end="")
        print("")
    print("")
floodFill(arrayMap)
print("----------------------------")
for i in arrayMap:
    for ii in i:
        for iii in ii:
            print(iii,end="")
        print("")
    print("")
points = findPoints(arrayMap)
print(findFullSA(points))
