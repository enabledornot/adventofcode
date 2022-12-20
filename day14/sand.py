def parse(fname):
    with open(fname,"r") as f:
        data = f.read().split("\n")
    ndata = []
    for line in data:
        ndata.append([])
        for cord in line.split(" -> "):
            ndata[-1].append(splitToInt(cord))
    return ndata
def splitToInt(toSplit):
    newt = []
    for new in toSplit.split(","):
        newt.append(int(new))
    newt.reverse()
    return tuple(newt)
def getRange(input):
    minX = 5000
    minY = 5000
    maxX = 0
    maxY = 0
    for block in input:
        for point in block:
            if point[0]<minX:
                minX = point[0]
            if point[1]<minY:
                minY = point[1]
            if point[0]>maxX:
                maxX=point[0]
            if point[1]>maxY:
                maxY = point[1]
    return tuple([minX,minY]),tuple([maxX,maxY])
def printAry(ary):
    for line in ary:
        for char in line:
            if char==0:
                print(".",end="")
            if char==1:
                print("#",end="")
            if char==2:
                print("o",end="")
        print("")
def smartRange(a,b):
    if a>b:
        return range(b,a+1)
    elif b>a:
        return range(a,b+1)
    else:
        return []
def pointsToMorePoints(block, fill, min):
    points = []
    last = block[0]
    for point in block[1:]:
        for lineX in smartRange(last[0],point[0]):
            fill[lineX][last[1]-min[1]] = 1
        for lineY in smartRange(last[1],point[1]):
            fill[last[0]][lineY-min[1]] = 1
        last = point
def buildArray(parsed):
    min,max = getRange(parsed)
    print(min)
    print(max)
    ary = []
    for i in range(max[0]+1):
        ary.append([0]*(max[1]-min[1]+1))
    for block in parsed:
        print(block)
        pointsToMorePoints(block, ary,min)
    return ary,min
def tryMove(sand,move,ary):
    nsand = [sand[0]+move[0],sand[1]+move[1]]
    if nsand[0]<0:
        return 1
    if nsand[1]<0:
        return 1
    if nsand[0]==len(ary):
        return 1
    if nsand[1]==len(ary[0]):
        return 1
    if ary[nsand[0]][nsand[1]]==0:
        return -1
    return 0
def dropSand(ary,min):
    sand = [0,500-min[1]]
    if ary[sand[0]][sand[1]]==2:
        return -2
    # print(sand)
    rslt = -1
    while(rslt==-1):
        for move in [(1,0),(1,-1),(1,1)]:
            rslt = tryMove(sand,move,ary)
            # print(rslt)
            if rslt==1:
                return 1
            if rslt!=0:
                sand[0] = sand[0] + move[0]
                sand[1] = sand[1] + move[1]
                break
    ary[sand[0]][sand[1]] = 2
    return -1
parsed = parse("input.txt")
ary,min = buildArray(parsed)
printAry(ary)
cnt = 0
while dropSand(ary,min)==-1:
    if cnt%100==0:
        printAry(ary)
        print("")
    cnt+=1
printAry(ary)
print(cnt)