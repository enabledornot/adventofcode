def parse(filename='input.txt'):
    with open(filename,'r') as f:
        return f.read().split('\n')[:-1]
# def computeAllDeltas
def findMovesKeypad(code):
    grid = {'7': (0,0), '8': (0,1), '9': (0,2), '4': (1,0), '5': (1,1), '6': (1,2), '1': (2,0), '2': (2,1), '3': (2,2), '0': (3,1), 'A':(3,2)}
    grido = {'^': (0,1), 'A': (0,2), '<': (1,0), 'v': (1,1), '>': (1,2)}
    p = (3,2)
    output = []
    for c in code:
        np = grid[c]
        delta = [np[0]-p[0],np[1]-p[1]]
        output.append("")
        # output.append([])
        sidePrio = False
        if delta[0] + p[0] == 3:
            sidePrio = True
        p = np
        if sidePrio:
            while delta[1] > 0:
                delta[1] -= 1
                output[-1] += '>'
                # output[-1].append(grido['>'])
            while delta[1] < 0:
                delta[1] += 1
                output[-1] += '<'
                # output[-1].append(grido['<'])
        while delta[0] < 0:
            delta[0] += 1
            output[-1] += '^'
            # output[-1].append(grido['^'])
        while delta[0] > 0:
            delta[0] -= 1
            output[-1] += 'v'
        if not sidePrio:
            while delta[1] > 0:
                delta[1] -= 1
                output[-1] += '>'
                # output[-1].append(grido['>'])
            while delta[1] < 0:
                delta[1] += 1
                output[-1] += '<'
                # output[-1].append(grido['<'])
            # output[-1].append(grido['v'])
        # output[-1].append(grido['A'])
        output[-1] += 'A'
    # return "".join(output)
    return output
def allPerms(code):
    if len(code) == 1:
        return [code[0]]
    code = list(code)
    possibles = []
    for i in range(len(code)):
        newcode = code.copy()
        c = newcode.pop(i)
        for item in allPerms(newcode):
            possibles.append(c + "".join(item))
    return possibles
def findBestMovesMovepad(code):
    if len(code) <= 2:
        return findMovesMovepad(code)
    print(code)
    possibles = allPerms(code[:-1])
    print(possibles)
    minLen = 100000000000000000000000000000000
    minLenv = ""
    for poss in possibles:
        potentalMin = findMovesMovepad(poss + "A")
        if len(potentalMin) < minLen:
            minLen = len(potentalMin)
            minLenv = potentalMin
    return minLenv
def findMovesMovepad(code):
    # print(code)
    grid = {'^': (0,1), 'A': (0,2), '<': (1,0), 'v': (1,1), '>': (1,2)}
    p = (0,2)
    output = []
    for c in code:
        np = grid[c]
        # np = c
        delta = [np[0]-p[0],np[1]-p[1]]
        # output.append([])
        output.append("")
        sidePrio = True
        # if p[0] + delta[0] == 0:
        #     sidePrio = True
        p = np
        if sidePrio:
            while delta[1] > 0:
                delta[1] -= 1
                # output[-1].append(grid['>'])
                output[-1] += '>'
            while delta[1] < 0:
                delta[1] += 1
                # output[-1].append(grid['<'])
                output[-1] += '<'
        while delta[0] < 0:
            delta[0] += 1
            # output[-1].append(grid['^'])
            output[-1] += '^'
        while delta[0] > 0:
            delta[0] -= 1
            # output[-1].append(grid['v'])
            output[-1] += 'v'
        if not sidePrio:
            while delta[1] > 0:
                delta[1] -= 1
                # output[-1].append(grid['>'])
                output[-1] += '>'
            while delta[1] < 0:
                delta[1] += 1
                # output[-1].append(grid['<'])
                output[-1] += '<'
        # output.append(delta)
        output[-1] += 'A'
        # output[-1].append(grid['A'])
    # return "".join(output)
    return output
def applyFindMoves(moves):
    newmoves = []
    for move in moves:
        if isinstance(move,list):
            newmoves.append(applyFindMoves(move))
        else:
            newmoves.append(findMovesMovepad(move))
    return newmoves
def unlist(moves):
    newmoves = ""
    for move in moves:
        if isinstance(move,list):
            newmoves += unlist(move)
        else:
            newmoves += move
    return newmoves
codes = parse(filename='test.txt')
sum = 0
# print(codes[0])
for code in codes:
    print(code)
    moves = findMovesKeypad(code)
    # moves = findMovesMovepad(moves)
    # print(moves)
    for _ in range(2):
        unlisted = unlist(moves)
        print(moves)
        print(f"{len(unlisted)}-{unlisted}")
        # print(moves)
        moves = applyFindMoves(moves)
    # for move in moves:
    #     print(f"{len(move)}-{move}")
    # print(len(moves[-1]))
    # print(int(code[:-1]))
    # print("")
    unlisted = unlist(moves)
    sum += len(unlisted) * int(code[:-1])
    print(moves)
    print(f"{len(unlisted)}-{unlisted}")
    # print(moves)
    print("")
print(sum)