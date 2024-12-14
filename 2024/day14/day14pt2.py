class Robot:
    def __init__(self,string):
        spt = string.split(" ")
        self.sp = spt[0][2:].split(",")
        self.sp[0] = int(self.sp[0])
        self.sp[1] = int(self.sp[1])
        self.cp = self.sp.copy()
        self.v = spt[1][2:].split(",")
        self.v[0] = int(self.v[0])
        self.v[1] = int(self.v[1])
    def __str__(self):
        pstr = f"{self.cp[0]},{self.cp[1]}"
        vstr = f"{self.v[0]},{self.v[1]}"
        return f"p={pstr} v={vstr}"
    def __repr__(self):
        return self.__str__()
    def move(self,amnt):
        self.cp[0] = (self.cp[0] + (self.v[0] * amnt)) % 101
        self.cp[1] = (self.cp[1] + (self.v[1] * amnt)) % 103
def parse(filename='input.txt'):
    with open(filename,"r") as f:
        splitt = f.read().split("\n")[:-1]
    positions = []
    velocities = []
    for line in splitt:
        r = Robot(line)
        positions.append(tuple(r.cp))
        velocities.append(tuple(r.v))
    return positions,velocities
def applyVelocity(p,v):
    for i in range(len(p)):
        p[i] = list(p[i])
        p[i][0] = (p[i][0] + v[i][0]) % 101
        p[i][1] = (p[i][1] + v[i][1]) % 103
        p[i] = tuple(p[i])
def findNext(point):
    directions = [[-1,0],[1,0],[0,1],[0,-1]]
    for d in directions:
        yield tuple([point[0] + d[0],point[1] + d[1]])
def longestLoop(p):
    checked = set()
    maxloop = 0
    setp = set(p)
    cloop = 0
    for newp in p:
        cloop = 0
        if newp in checked:
            continue
        toCheck = [newp]
        while len(toCheck) != 0:
            cloop += 1
            new = toCheck.pop()
            checked.add(new)
            # print(new)
            for pp in findNext(new):
                if pp in setp and pp not in checked:
                    toCheck.append(pp)
        if cloop > maxloop:
            maxloop = cloop
    return maxloop
        

def countRobots(robots):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for r in robots:
        if r.cp[0] < 50 and r.cp[1] < 51:
            q1 += 1
        if r.cp[0] > 50 and r.cp[1] < 51:
            q2 += 1
        if r.cp[0] > 50 and r.cp[1] > 51:
            q3 += 1
        if r.cp[0] < 50 and r.cp[1] > 51:
            q4 += 1
    return q1 * q2 * q3 * q4
def displayRobots(p):
    for i in range(101):
        for ii in range(103):
            if (i,ii) in p:
                print("#",end="")
            else:
                print(" ",end="")
        print("")
p,v = parse()
cnt = 0
while True:
    cnt += 1
    applyVelocity(p,v)
    ll = longestLoop(p)
    if ll > 100:
        print(f"cnt={cnt}")
        displayRobots(p)
    # print(f"ll={ll}")
    # displayRobots(p)
    # print("")
count = countRobots(robots)
print(count)