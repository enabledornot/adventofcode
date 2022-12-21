from tqdm import tqdm 
import math
shapeList = [
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,1),(1,0),(1,1),(1,2),(2,1)],
    [(0,0),(0,1),(0,2),(1,2),(2,2)],
    [(0,0),(1,0),(2,0),(3,0)],
    [(0,0),(0,1),(1,0),(1,1)]
]
def parse(fname):
    with open(fname,"r") as f:
        return f.read()
class cycler:
    def __init__(self, toCycle):
        self.cycle = toCycle
        self.current = 0
    def get(self):
        rslt = self.cycle[self.current]
        self.current = (self.current+1)%len(self.cycle)
        return rslt
class cachedEscape:
    def __init__(self, bord):
        self.board = bord
        self.cache = {}
    def canEscape(self, pos, prev):
        key = str(pos)
        if not key in self.cache:
            self.cache[key] = self.canEscapeU(pos,prev)
        return self.cache[key]
    def canEscapeU(self, pos, prev):
        if pos[0]==len(self.board):
            return True
        if pos[1]<0 or pos[1]>6:
            return False
        if self.board[pos[0]][pos[1]] > 0:
            return False
        if pos in prev:
            return False
        nprev = prev.copy()
        nprev.append(pos)
        for move in [(1,0),(0,-1),(0,1),(-1,0)]:
            if self.canEscape((pos[0]+move[0],pos[1]+move[1]),nprev):
                return True
        return False
class game:
    def __init__(self,moveList):
        self.buildMoveList(moveList)
        self.shape = cycler(shapeList)
        self.maxHeight = 0
        self.board = []
        self.last = -1
        self.prunedHeight = 0
        self.pruneCycle = len(moveList)*len(shapeList)
        self.moveCount = 0
    def buildMoveList(self, moveList):
        moves2 = []
        for char in moveList:
            if char=='<':
                moves2.append([0,-1])
            if char==">":
                moves2.append([0,1])
        self.moves = cycler(moves2)
    def getPruneHeight(self):
        ce = cachedEscape(self.board)
        cnt = len(self.board)
        for i in reversed(self.board):
            rslt = True
            cnt2 = 0
            for row in i:
                if row<=0:
                    if ce.canEscape((cnt,cnt2),[]):
                        rslt = False
                cnt2+=1
            if(rslt):
                return cnt
            cnt-=1
        return 0
    def fillBoard(self, amnt):
        while len(self.board)<=amnt:
            self.board.append([0]*7)
    def pruneBoard(self):
        phight = self.getPruneHeight()
        if phight!=0:
            # print(phight)
            # self.print()
            for i in range(phight):
                self.board.pop(0)
            self.maxHeight-=phight
            self.prunedHeight+=phight
    def print(self):
        for line in reversed(self.board):
            for char in line:
                if char==0:
                    print(".",end="")
                if char==1:
                    print("#",end="")
            print("")
    def tryMove(self, shape, current, move):
        new = [current[0]+move[0],current[1]+move[1]]
        for point in shape:
            shapeset = [new[0]+point[0],new[1]+point[1]]
            if shapeset[1]<0 or shapeset[1]==7:
                return False
            if shapeset[0]<0:
                return False
            if self.board[shapeset[0]][shapeset[1]]>0:
                return False
        return True
    def move(self):
        newShape = self.shape.get()
        self.fillBoard(newShape[-1][0]+3+self.maxHeight)
        location = [3+self.maxHeight,2]
        while(True):
            newMove = self.moves.get()
            rslt = self.tryMove(newShape, location, newMove)
            if rslt:
                location[0]+= newMove[0]
                location[1]+= newMove[1]
            rslt = self.tryMove(newShape, location, [-1,0])
            if not rslt:
                break
            location[0]+= -1
            location[1]+= 0
        for point in newShape:
            self.board[point[0]+location[0]][point[1]+location[1]] = 1
        pmaxh = newShape[-1][0] + location[0]+1
        if pmaxh>self.maxHeight:
            self.maxHeight = pmaxh
        self.moveCount+=1
        # print(self.maxHeight)
    def getHash(self):
        toHash = []
        for row in self.board:
            toHash.append(tuple(row))
        return hash(tuple(toHash))
    def moveMulti(self, cnt):
        cacheList = {}
        cycleCount = 0
        while cnt>0:
            self.pruneBoard()
            hash = str([self.getHash(),self.shape.current,self.moves.current])
            if hash in cacheList:
                cycleLength = (cycleCount-cacheList[hash][0])
                newRows = (self.maxHeight + self.prunedHeight) - cacheList[hash][1]
                cyclesToSkip = math.floor(cnt/cycleLength)
                cnt-=cyclesToSkip*cycleLength
                self.prunedHeight+= newRows*cyclesToSkip
                break
            cacheList[hash] = (cycleCount, self.maxHeight + self.prunedHeight)
            cycleCount+=1
            self.move()
            cnt-=1
        while cnt>0:
            self.move()
            cnt-=1
        return self.maxHeight + self.prunedHeight


moveList = parse("input.txt")
gam = game(moveList)
rslt = gam.moveMulti(1000000000000)
print(rslt)