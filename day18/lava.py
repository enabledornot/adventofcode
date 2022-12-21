from operator import itemgetter
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
    return 2*len(points)-cnt
parsed = parse("input.txt")
sum = 0
for i in range(3):
    sum+=findSA(parsed, i)
print(sum)