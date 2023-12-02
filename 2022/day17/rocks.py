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
class game:
    def __init__(self,moveList):
        self.buildMoveList(moveList)
        self.shape = cycler(shapeList)
        self.maxHight = 0
        self.board = []
    def buildMoveList(self, moveList):
        moves2 = []
        for char in moveList:
            if char=='<':
                moves2.append([0,-1])
            if char==">":
                moves2.append([0,1])
        self.moves = cycler(moves2)
    def fillBoard(self, amnt):
        while len(self.board)<=amnt:
            self.board.append([0]*7)
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
            if self.board[shapeset[0]][shapeset[1]]!=0:
                return False
        return True
    def move(self):
        newShape = self.shape.get()
        location = [3+self.maxHight,2]
        self.fillBoard(newShape[-1][0]+3+self.maxHight)
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
        if pmaxh>self.maxHight:
            self.maxHight = pmaxh
        # print(self.maxHight)


moveList = parse("input.txt")
gam = game(moveList)
for i in range(2022):
    gam.move()
    # gam.print()
    # print("")
print(gam.maxHight)