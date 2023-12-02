sides = [
    # index 0 is the new direction
    # index 1 is the side ID
    # index 2 is whether you flip cords
    # index 3 is whether you flip relevent
    # index 4 is whether you flip irrelevent
    [
        (0,1,False,False,True),
        (1,2,False,False,True),
        (0,3,False,True,False),
        (0,5,True,False,False)
    ],
    [
        (2,4,False,True,False),
        (2,2,True,False,False),
        (2,0,False,False,True),
        (3,5,False,False,True)
    ],
    [
        (3,1,True,False,False),
        (1,4,False,False,True),
        (1,3,True,False,False),
        (3,0,False,False,True)
    ],
    [
        (0,4,False,False,True),
        (1,5,False,False,True),
        (0,0,False,True,False),
        (0,2,True,False,False)
    ],
    [
        (2,1,False,True,False),
        (2,5,True,False,False),
        (2,3,False,False,True),
        (3,2,False,False,True)
    ],
    [
        (3,4,True,False,False),
        (1,1,False,False,True),
        (1,0,True,False,False),
        (3,3,False,False,True)
    ]
    # [
    #     (0,5,False,True,True),
    #     (1,3,False,False,True),
    #     (1,2,True,False,False),
    #     (1,1,False,False,False)
    # ],
    # [
    #     (0,2,False,False,True),
    #     (3,4,False,True,False),
    #     (1,5,True,True,True),
    #     (3,0,False,True,False)
    # ],
    # [
    #     (0,3,False,False,True),
    #     (0,4,False,False,True),
    #     (2,1,True,True,True),
    #     (0,0,True,False,False)
    # ],
    # [
    #     (1,5,True,True,True),
    #     (1,4,False,False,True),
    #     (2,2,False,False,True),
    #     (3,0,False,False,True)
    # ],
    # [
    #     (0,5,False,False,True),
    #     (3,1,False,True,False),
    #     (3,2,True,True,True),
    #     (3,3,False,False,True)
    # ],
    # [
    #     (2,0,False,True,False),
    #     (0,1,True,True,True),
    #     (2,4,False,False,True),
    #     (2,3,True,True,True)
    # ]
]
directionMap = [(0,1),(1,0),(0,-1),(-1,0)]
def parse(fname):
    with open(fname, "r") as f:
        data = f.read().split("\n")
    size = 0
    while data[size][0]==" ":
        size+=1
    size = int(size/2)
    mapA = []
    mapB = []
    mapC = []
    mapD = []
    mapE = []
    mapF = []
    for i in range(size):
        new = data.pop(0)
        mapA.append(new[size:size*2])
        mapB.append(new[size*2:size*3])
    for i in range(size):
        new = data.pop(0)
        mapC.append(new[size:size*2])
    for i in range(size):
        new = data.pop(0)
        mapD.append(new[:size])
        mapE.append(new[size:size*2])
    for i in range(size):
        new = data.pop(0)
        mapF.append(new[:size])
    return [
        mapA,
        mapB,
        mapC,
        mapD,
        mapE,
        mapF,
        fix(data[1]),
        size
    ]
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
def fixCords(position, direction, doFlipRelevent, doFlipIrrelevent, max):
    maxadj = max-1
    if direction==0 or direction==2:
        relevent = position[0]
        irrelevent = position[1]
    else:
        relevent = position[1]
        irrelevent = position[0]
    if doFlipRelevent:
        relevent = maxadj-relevent
    if doFlipIrrelevent:
        if irrelevent==-1:
            irrelevent = maxadj
        else:
            irrelevent = 0
    else:
        if irrelevent==-1:
            irrelevent = 0
        else:
            irrelevent = maxadj
    if direction==0 or direction==2:
        return [relevent,irrelevent]
    else:
        return [irrelevent,relevent]
def fixLocation(direction, position, frame, max):
    positionInstructions = sides[frame][direction]
    if positionInstructions[2]:
        updatedPos = fixCords(position, direction, positionInstructions[3], positionInstructions[4], max)
        return [updatedPos[1],updatedPos[0]], positionInstructions[1], positionInstructions[0]
    else:
        updatedPos = fixCords(position, direction, positionInstructions[3], positionInstructions[4], max)
        return updatedPos, positionInstructions[1], positionInstructions[0]

rslt = parse("input.txt")
sideLength = len(rslt[0])
direction = 0
frame = 0
framePos = [0,0]
size = rslt[7]
previous = []
for instruction in rslt[6]:
    if instruction=="L":
        direction = (direction-1)%4
    elif instruction=="R":
        direction = (direction+1)%4
    else:
        for i in range(instruction):
            newPos = framePos.copy()
            newPos[0]+=directionMap[direction][0]
            newPos[1]+=directionMap[direction][1]
            newFrame = frame
            newDirection = direction
            if newPos[0]<0 or newPos[1]<0 or newPos[0]==size or newPos[1]==size:
                newPos, newFrame, newDirection = fixLocation(direction, newPos, newFrame, size)
                print("old-{}".format((frame,framePos,direction)))
                print("new-{}".format((newFrame, newPos, newDirection)))
                print("")
            if rslt[newFrame][newPos[0]][newPos[1]]!="#":
                previous.append((frame,framePos,direction))
                frame = newFrame
                framePos = newPos
                direction = newDirection
            else:
                break
# Program prints final frame, framePos and direction after
# Math must be done manually (making sure to account that the row number starts at 1 and that framepos is relative to the current frame)
print(frame)
print(framePos)
print(direction)