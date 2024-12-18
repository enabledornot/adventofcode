def parse(filename="input.txt"):
    with open(filename,"r") as f:
        map, moves = f.read().split('\n\n')
    m = moves.replace('\n','')
    newmap = []
    posA = []
    for i,line in enumerate(map.split('\n')):
        newmap.append(list(line))
        if '@' in newmap[-1]:
            posA = [i,newmap[-1].index('@')]
            newmap[-1][newmap[-1].index('@')] = '.'
    return newmap, m, posA
def moveBoulder(map, direction, position):
    cp = position.copy()
    while 0 <= cp[0] and cp[0] < len(map) and 0 <= cp[1] and cp[1] < len(map[0]):
        cp[0] += direction[0]
        cp[1] += direction[1]
        if map[cp[0]][cp[1]] == '.':
            map[cp[0]][cp[1]] = 'O'
            map[position[0]][position[1]] = '.'
            return True
        elif map[cp[0]][cp[1]] == '#':
            return False
    return False
def applyMove(map,pos,move):
    if move == 'v':
        direction = [1,0]
    elif move == '>':
        direction = [0,1]
    elif move == '^':
        direction = [-1,0]
    elif move == '<':
        direction = [0,-1]
    else:
        print("invalid move")
    newPos = [pos[0]+direction[0],pos[1]+direction[1]]
    if 0 <= newPos[0] and newPos[0] < len(map) and 0 <= newPos[1] and newPos[1] < len(map[0]):
        blocker = map[newPos[0]][newPos[1]]
        if blocker == '.':
            return newPos
        elif blocker == '#':
            return pos
        elif blocker == 'O':
            if moveBoulder(map,direction,newPos):
                return newPos
            else:
                return pos
    else:
        return pos
def calculateGPS(map):
    count = 0
    for i,line in enumerate(map):
        for ii,c in enumerate(line):
            if map[i][ii] == 'O':
                count += (i * 100)
                count += ii
    return count
def printMap(map,pos):
    for i,line in enumerate(map):
        for ii,c in enumerate(line):
            if (i,ii) == tuple(pos):
                print('@',end="")
            else:
                print(c,end="")
        print("")
    print("")
map, moves, startP = parse()
cp = startP.copy()
printMap(map,cp)
for move in moves:
    # print(move)
    cp = applyMove(map,cp,move)
    # printMap(map,cp)
printMap(map,cp)
print(calculateGPS(map))