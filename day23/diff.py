def parse(fname):
    with open(fname, "r") as f:
        data = f.read().split("\n")
    ndata = []
    i = 0
    for line in data:
        ii = 0
        for char in line:
            if char=="#":
                ndata.append((i,ii))
            ii+=1
        i+=1
    return ndata
def getRange(data):
    min = [500,500]
    max = [0,0]
    for point in data:
        if point[0]<min[0]:
            min[0] = point[0]
        if point[1]<min[1]:
            min[1] = point[1]
        if point[0]>max[0]:
            max[0] = point[0]
        if point[1]>max[1]:
            max[1] = point[1]
    return min,max
def printData(loc, prop):
    min, max = getRange(loc)
    # print(min)
    # print(max)
    for i in range(min[0]-1,max[0]+2):
        for ii in range(min[1]-1,max[1]+2):
            if (i,ii) in loc:
                print("#",end="")
            elif (i,ii) in prop:
                print("*",end="")
            else:
                print(".",end="")
        print("")
    print("")
def removeDupes(prop):
    cnt = 0
    while cnt<len(prop):
        if prop[cnt]!=() and prop.index(prop[cnt])!=cnt:
            toRem = prop[cnt]
            while toRem in prop:
                prop[prop.index(toRem)] = ()
        cnt+=1
directions = [
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,-1),
    (0,1),
    (1,-1),
    (1,0),
    (1,1)
]
moves = [
    ([(-1,-1),(-1,0),(-1,1)],(-1,0)),
    ([(1,-1),(1,0),(1,1)],(1,0)),
    ([(-1,-1),(0,-1),(1,-1)],(0,-1)),
    ([(-1,1),(0,1),(1,1)],(0,1)),
    ([(-1,-1),(-1,0),(-1,1)],(-1,0)),
    ([(1,-1),(1,0),(1,1)],(1,0)),
    ([(-1,-1),(0,-1),(1,-1)],(0,-1)),
    ([(-1,1),(0,1),(1,1)],(0,1))
]
def isInCheck(data, point, positions):
    for pos in positions:
        if (point[0]+pos[0],point[1]+pos[1]) in data:
            return True
    return False
def getPropose(data, currentDirection):
    proposed = []
    for point in data:
        proposed.append(())
        if isInCheck(data, point, directions):
            for move in moves[currentDirection:currentDirection+4]:
                if not isInCheck(data, point, move[0]):
                    proposed[-1] = ((point[0]+move[1][0],point[1]+move[1][1]))
                    break
            
    return proposed
def moveElphs(data, moves):
    moved = False
    for i in range(len(data)):
        if moves[i]!=():
            data[i] = moves[i]
            moved = True
    return moved
def doTurn(data,cdir):
    prop = getPropose(data,cdir)
    removeDupes(prop)
    return moveElphs(data,prop)
def getFreeSpace(data):
    min, max = getRange(data)
    # print(min)
    # print(max)
    full = (max[0]-min[0]+1)*(max[1]-min[1]+1)
    # print(full)
    return full - len(data)
rslt = parse("input.txt")
for i in range(10):
    doTurn(rslt, i%4)
# mcount = 0
# while doTurn(rslt, mcount%4):
#     print(mcount)
#     mcount+=1
# printData(rslt,[])
print(getFreeSpace(rslt))