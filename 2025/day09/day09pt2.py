from tqdm import tqdm
def parse():
    output = []
    with open('input.txt','r') as f:
        for line in f.read().split('\n')[:-1]:
            x, y = line.split(',')
            output.append((int(x),int(y)))
            # output.append((x,y))
    return output
def labeledLookup(values):
    print(values)
    lookup = {}
    last = ''
    i = 0
    for v in values:
        if str(v) != last:
            last = str(v)
            lookup[last] = i
            i += 1
    return lookup
def generateCoordTables(coordinates):
    tmpCords = coordinates.copy()
    tmpCords.append((0,0))
    tmpCords.append((100000,100000))
    valuesA = sorted(set([x[0] for x in tmpCords]))
    valuesB = sorted(set([x[1] for x in tmpCords]))
    lookupA = labeledLookup(valuesA)
    lookupB = labeledLookup(valuesB)
    return (lookupA, lookupB, valuesA, valuesB)
def convertCoordinates(tables, coordinates):
    newCoordinates = []
    for coordinate in coordinates:
        newCoordinates.append((tables[0][str(coordinate[0])], tables[1][str(coordinate[1])]))
    return newCoordinates
def unconvertCoordinate(tables, tcord):
    return (tables[2][tcord[0]],tables[3][tcord[1]])
def buildMask(tcords, maxX, maxY):
    # maxX = len(tables[2])
    # maxY = len(tables[3])
    mask = []
    for i in range(maxX):
        mask.append([1]*maxY)
    for cordA in tcords:
        for cordB in tcords:
            if cordA[0] == cordB[0]:
                if cordA[1] != cordB[1]:
                    for i in range(min(cordA[1],cordB[1]),max(cordA[1],cordB[1])+1):
                        mask[cordA[0]][i] = 2
            else:
                if cordA[1] == cordB[1]:
                    for i in range(min(cordA[0],cordB[0]),max(cordA[0],cordB[0]+1)):
                        mask[i][cordA[1]] = 2
    floodFill(mask)
    return mask
def floodFill(mask):
    toDo = [(0,0)]
    adj = [(0,1),(0,-1),(1,0),(-1,0)]
    while len(toDo) != 0:
        cur = toDo.pop(0)
        if mask[cur[0]][cur[1]] == 1:
            mask[cur[0]][cur[1]] = 0
            for m in adj:
                pcord = (cur[0]+m[0],cur[1]+m[1])
                if pcord[0] >= 0 and pcord[0] < len(mask) and pcord[1] >= 0 and pcord[1] < len(mask[0]):
                    toDo.append(pcord)
def printMask(mask):
    for i in range(len(mask)):
        for j in range(len(mask[0])):
            print(mask[j][i],end='')
        print("")
def validateCoordinates(mask, coordA, coordB):
    minCorner = (min(coordA[0],coordB[0]),min(coordA[1],coordB[1]))
    maxCorner = (max(coordA[0],coordB[0]),max(coordA[1],coordB[1]))
    for i in range(minCorner[0],maxCorner[0]+1):
        if mask[i][minCorner[1]] == 0 or mask[i][maxCorner[1]] == 0:
            return False
    for i in range(minCorner[1],maxCorner[1]+1):
        if mask[minCorner[0]][i] == 0 or mask[maxCorner[0]][i] == 0:
            return False
    return True
    
coordinates = parse()
tables = generateCoordTables(coordinates)
tcords = convertCoordinates(tables, coordinates)
# print(tcords)
mask = buildMask(tcords, len(tables[2]),len(tables[3]))
# printMask(mask)
# print(coordinates)
# print(len(coordinates))
maxArea = 0
for tcoordA in tqdm(tcords):
    coordA = unconvertCoordinate(tables,tcoordA)
    for tcoordB in tcords:
        coordB = unconvertCoordinate(tables,tcoordB)
        # print(coordB)
        deltaX, deltaY = abs(coordA[0]-coordB[0]), abs(coordA[1]-coordB[1])
        newArea = (deltaX+1) * (deltaY+1)
        if newArea > maxArea and validateCoordinates(mask, tcoordA, tcoordB):
            maxArea = newArea
print(maxArea)