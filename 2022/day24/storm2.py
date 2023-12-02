from tqdm import tqdm
class storm:
    def __init__(self, fname, initCnt=0):
        with open(fname, "r") as f:
            data = f.read().split("\n")
        self.sup = []
        self.sdown = []
        self.sright = []
        self.sleft = []
        for line in data[1:-1]:
            self.sup.append([])
            self.sdown.append([])
            self.sright.append([])
            self.sleft.append([])
            for char in line[1:-1]:
                if char=="^":
                    self.sup[-1].append(1)
                else:
                    self.sup[-1].append(0)
                if char=="v":
                    self.sdown[-1].append(1)
                else:
                    self.sdown[-1].append(0)
                if char=="<":
                    self.sleft[-1].append(1)
                else:
                    self.sleft[-1].append(0)
                if char==">":
                    self.sright[-1].append(1)
                else:
                    self.sright[-1].append(0)
        for i in range(initCnt):
            self.cycle()
    def print(self, plist):
        for i in range(len(self.sup)):
            for ii in range(len(self.sup[0])):
                possible = []
                if (i,ii) in plist:
                    possible.append("E")
                else:
                    if self.sup[i][ii]==1:
                        possible.append("^")
                    if self.sdown[i][ii]==1:
                        possible.append("v")
                    if self.sleft[i][ii]==1:
                        possible.append("<")
                    if self.sright[i][ii]==1:
                        possible.append(">")
                if len(possible)==0:
                    print(".",end="")
                elif len(possible)==1:
                    print(possible[0],end="")
                else:
                    print(len(possible),end="")
            print("")
        print("")
    def cycle(self):
        tup = self.sup.pop(0)
        self.sup.append(tup)
        tdown = self.sdown.pop(-1)
        self.sdown.insert(0,tdown)
        for left in self.sleft:
            tmp = left.pop(0)
            left.append(tmp)
        for right in self.sright:
            tmp = right.pop(-1)
            right.insert(0,tmp)
    def isStorm(self, p0,p1):
        if p0<0 or p1<0 or p0==len(self.sup) or p1==len(self.sup[0]):
            return False
        if self.sup[p0][p1]==1:
            return True
        if self.sdown[p0][p1]==1:
            return True
        if self.sright[p0][p1]==1:
            return True
        if self.sleft[p0][p1]==1:
            return True
        return False
def pointsIncluded(newpos, ncpos):
    for i in newpos:
        if i[0][0]==ncpos[0] and i[0][1]==ncpos[1]:
            return True
    return False
directions = [(0,0),(0,1),(0,-1),(1,0),(-1,0)]
def calculateCyclesTo(st, startPos, endPos):
    st.cycle()
    positions = [(startPos,[])]
    newPositions = []
    cyclesMadeIt = []
    cnt = 0
    keepGoing = True
    while(keepGoing):
        if len(positions)==0:
            positions = []
            st.cycle()
            cnt+=1
            if cnt==2000:
                print("Cycle too long breaking")
                break
            # print(cnt)
            # print(len(newPositions))
            if len(newPositions)==0:
                print("out of positions")
                keepGoing = False
            for position in newPositions:
                if not st.isStorm(position[0][0],position[0][1]):
                    positions.append(position)
            newPositions = []
        else:
            cpos = positions.pop(0)
            newPrev = cpos[1].copy()
            newPrev.append(tuple(cpos[0]))
            for dir in directions:
                ncpos = cpos[0].copy()
                ncpos[0]+=dir[0]
                ncpos[1]+=dir[1]
                if ncpos[0]==endPos[0] and ncpos[1]==endPos[1]:
                    # print("FOUND IT")
                    if cnt+2 not in cyclesMadeIt:
                        cyclesMadeIt.append(cnt+2)
                    if len(cyclesMadeIt)>20:
                        keepGoing = False
                # print(ncpos)
                if ((0<=ncpos[0]<len(st.sup) and 0<=ncpos[1]<len(st.sup[0])) or ((ncpos[0]==-1 and ncpos[1]==0) or (ncpos[0]==len(st.sup) and ncpos[1]==len(st.sup[0])-1))) and (not pointsIncluded(newPositions,ncpos)):# and not st.isStorm(ncpos[0],ncpos[1]):
                    newPositions.append((ncpos,newPrev))
    return cyclesMadeIt
fileName = "input.txt"
st = storm(fileName)
cyclesToFirst = calculateCyclesTo(st,[-1,0],[len(st.sup),len(st.sup[0])-1])
cyclesNew = []
for cycle in tqdm(cyclesToFirst):
    st = storm(fileName,cycle)
    cyclesAfter = calculateCyclesTo(st, [len(st.sup),len(st.sup[0])-1], [-1,0])
    for cy in cyclesAfter:
        newCycle = cy+cycle
        if newCycle not in cyclesNew:
            cyclesNew.append(newCycle)
cyclesNewer = []
for cycle in tqdm(cyclesNew):
    st = storm(fileName,cycle)
    cyclesAfter = calculateCyclesTo(st, [-1,0], [len(st.sup),len(st.sup[0])-1])
    for cy in cyclesAfter:
        newCycle = cy+cycle
        if newCycle not in cyclesNewer:
            cyclesNewer.append(newCycle)
print(sorted(cyclesNewer)[0])