from tqdm import tqdm 
def parse(fname):
    with open(fname, "r") as f:
        data = f.read().split("\n")
    ndata = []
    for line in data:
        split = line.split(" ")
        sx = int(split[2][2:-1])
        sy = int(split[3][2:-1])
        bx = int(split[8][2:-1])
        by = int(split[9][2:])
        ndata.append(((sx,sy),(bx,by),calcDist((sx,sy),(bx,by))))
    return ndata
def calcDist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
def merge(a,b):
    if a[1]>=b[0]:
        if b[1]>a[1]:
            return [[a[0],b[1]]]
        else:
            return [[a[0],a[1]]]
    return [a,b]
def checkSet(set):
    last = set[0][1]
    for i in set[1:]:
        if i[0]>=last:
            return False
        last = i[1]
    return True
def combine(maped):
    maped.sort()
    count = 1
    while count<len(maped):
        merds = merge(maped[count-1],maped[count])
        if len(merds)==1:
            maped.pop(count-1)
            maped.pop(count-1)
            maped.insert(count-1,merds[0])
        else:
            count+=1
    return maped
def countDif(listed):
    sum = 0
    for range in listed:
        sum+=range[1]-range[0]
    return sum
def locateGaps(listed):
    count = 0
    gaps = []
    while count+1<len(listed):
        if listed[count+1][0]-listed[count][1]==2:
            gaps.append(listed[count][1]+1)
        count+=1
    return gaps
def findHoles(parsed,row):
    maped = []
    for scanner in parsed:
        dist = abs(scanner[0][1]-row)
        xoffset = scanner[2]-dist
        if xoffset>0:
            maped.append([scanner[0][0]-xoffset,scanner[0][0]+xoffset])
    # print(maped)
    rslt = combine(maped)
    # print(rslt)
    gaps = locateGaps(rslt)
    # print(gaps)
    return gaps
def findDistress(parsed, rangeCheck):
    for i in tqdm(range(rangeCheck)):
        gaps = findHoles(parsed,i)
        for gap in gaps:
            if 0 <= gap <= 4000000:
                return gap, i, gap*4000000+i
parsed = parse("input.txt")
x, y, score = findDistress(parsed, 4000000)
print("x={}".format(x))
print("y={}".format(y))
print("Answer: {}".format(score))