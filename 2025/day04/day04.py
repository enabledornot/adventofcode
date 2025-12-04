def parse():
    with open("input.txt","r") as f:
        return f.read().split('\n')[:-1]
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
class map:
    def __init__(self, grid):
        self.grid = grid
    def checkPos(self,x, y):
        if x >= 0 and x < len(self.grid) and y >= 0 and y < len(self.grid[0]):
            return self.grid[x][y]
        else:
            return '.'
    def countAdj(self,x,y):
        cnt = 0
        for d in directions:
            if self.checkPos(x+d[0],y+d[1]) == "@":
                cnt += 1
        return cnt
m = map(parse())
tot = 0
for i in range(len(m.grid)):
    for ii in range(len(m.grid[0])):
        if m.checkPos(i,ii) == '@' and m.countAdj(i,ii) < 4:
            # print(f"{i} {ii}")
            print('x',end="")
            tot += 1
        else:
            print(m.checkPos(i,ii), end="")
    print("")
print(tot)