directionMap = [(0,1),(1,0),(0,-1),(-1,0)]
name = "input.txt"
blockScale = 50
blockHeight = 4
blockWidth = 3
# name = "test.txt"
# blockScale = 4
# blockHeight = 3
# blockWidth = 4
def parse(fname):
    with open(fname, "r") as f:
        data = f.read().split("\n\n")
    return pad(data[0].split("\n")) , fix(data[1][:-1])
def pad(splitData):
    ndata = []
    for i in splitData:
        string = i
        for c in range((blockWidth*blockScale)-len(i)):
            string+=" "
        ndata.append(string)
    return ndata
def fix(input):
    rslt = []
    for rblock in input.split("R"):
        for lblock in rblock.split("L"):
            rslt.append(int(lblock))
            rslt.append("L")
        rslt.pop(-1)
        rslt.append("R")
    rslt.pop(-1)
    print(rslt)
    return rslt
def score(direction, position):
    return (position[0]+1)*1000 + 4*(position[1]+1) + direction
block, code = parse(name)
linelen = len(block[0])
for line in block:
    if len(line)!=linelen:
        print("LINE ERROR")
# print(block)
print(code)
direction = 0
position = [0,1]
for instruction in code:
    if instruction=="L":
        direction = (direction-1)%4
    elif instruction=="R":
        direction = (direction+1)%4
    else:
        for i in range(instruction):
            newPos = position.copy()
            while True:
                newPos[0]+=directionMap[direction][0]
                newPos[1]+=directionMap[direction][1]
                if newPos[0]<0:
                    newPos[0] = len(block)-1
                elif newPos[1]<0:
                    newPos[1] = len(block[0])-1
                elif newPos[0]==len(block):
                    newPos[0] = 0
                elif newPos[1]==len(block[newPos[0]]):
                    newPos[1] = 0
                if block[newPos[0]][newPos[1]]!=" ":
                    break
                # print("-"+str(newPos))
            if block[newPos[0]][newPos[1]]==".":
                position = newPos
            else:
                break
            # print(position)
    if block[position[0]][position[1]]!=".":
        print("ERROR")
    # print(instruction)
    # print(direction)
    # print(position)
    # print("----------------")
print(score(direction, position))
