def parse(filename='input.txt'):
    with open(filename,"r") as f:
        data = f.read().split('\n')[:-1]
    newdata = []
    headmap = []
    headmap2 = []
    trailmask = []
    for line in data:
        newdata.append([])
        headmap.append([])
        headmap2.append([])
        trailmask.append([])
        for c in line:
            headmap[-1].append(set())
            headmap2[-1].append(set())
            trailmask[-1].append(False)
            try:
                newdata[-1].append(int(c))
            except:
                newdata[-1].append(-2)
    return newdata
def findNewPoints(data,cpoint):
    newp = []
    for did, offset in enumerate([[0,1],[1,0],[0,-1],[-1,0]]):
        potential = list(cpoint)
        potential[0] += offset[0]
        potential[1] += offset[1]
        if potential[0] >= 0 and potential[0] < len(data) and potential[1] >= 0 and potential[1] < len(data[0]):
            newp.append((did,potential))
    return newp
def countChanges(p,map):
    # if tuple(p) == (1,6):
    #     import ipdb; ipdb.set_trace()
    pvalue = map[p[0]][p[1]]
    if pvalue == 9:
        return 1
    sum = 0
    for _, pos in findNewPoints(map,p):
        newval = map[pos[0]][pos[1]]
        if newval == pvalue + 1:
            sum += countChanges(pos,map)
    return sum
map = parse(filename='input.txt')
sum = 0
for i, line in enumerate(map):
    for ii, c in enumerate(line):
        if map[i][ii] == 0:
            thed = countChanges((i,ii),map)
            sum += thed
print(sum)