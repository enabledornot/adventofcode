import time

class strToInt:
    def __init__(self):
        self.starting = 0
        self.mapp = {}
    def map(self, toMap):
        if toMap not in self.mapp:
            self.mapp[toMap] = self.starting
            self.starting+=1
        return self.mapp[toMap]
def parse(fname):
    with open(fname,"r") as f:
        data = f.read().split("\n")
    ndata = []
    sti = strToInt()
    for line in data:
        split = line.split(" ")
        tunnelID = sti.map(split[1])
        flowRate = int(split[4][5:-1])
        pointsTo = []
        for line in split[9:]:
            if line[-1]==',':
                pointsTo.append(sti.map(line[:-1]))
            else:
                pointsTo.append(sti.map(line))
        while len(ndata) <= tunnelID:
            ndata.append(())
        ndata[tunnelID] = (flowRate,tuple(pointsTo))
    print(sti.mapp["AA"])
    return ndata, sti.mapp["AA"]
def locateSpecials(tlist):
    worthwhile = []
    cnt = 0
    for line in tlist:
        if line[0] != 0:
            worthwhile.append(cnt)
        cnt+=1
    return worthwhile
def getMinSteps(map, start, end, max):
    if max == 0:
        return 5000
    if start == end:
        return 0
    min = max-1
    for loc in map[start][1]:
        current = getMinSteps(map, loc, end, min)
        if current < min:
            min = current
    return min+1
def getMap(fname):
    tl,aloc = parse(fname)
    # print(tl)
    # print(max)
    specials = locateSpecials(tl)
    specials.insert(0,aloc)
    print(specials)
    maped = []
    i = 0
    for special in specials:
        maped.append((tl[special][0],[]))
        ii = 0
        for special2 in specials:
            maped[-1][1].append(getMinSteps(tl, special, special2, 50))
            ii+=1
        i+=1
    return maped
class maxValueCached:
    def __init__(self, ma):
        self.map = ma
        self.cache = {}
    def maxValue(self, opened, current, timeLeft):
        if timeLeft<2:
            return 0
        if current in opened:
            return 0
        listOpened = list(opened)
        currentItem = self.map[current]
        score = currentItem[0]*timeLeft
        timeLeft-=1
        listOpened.append(current)
        max = 0
        listTupld = tuple(sorted(listOpened))
        for dest in range(len(currentItem[1])):
            new = self.maxValueCached(listTupld, dest, timeLeft-currentItem[1][dest])
            if new > max:
                max = new
        return max + score
    def maxValueCached(self, opened, current, timeLeft):
        # print(opened)
        cacheKey = str([opened, current, timeLeft])
        if cacheKey not in self.cache:
            self.cache[cacheKey] = self.maxValue(opened,current, timeLeft)
        if len(self.cache)%1000 == 0:
            print(len(self.cache))
        return self.cache[cacheKey]


mapped = getMap("input.txt")
mvc = maxValueCached(mapped)
print(mapped)
rslt = mvc.maxValue((), 0, 30)
print(rslt)