def parse(filename='input.txt'):
    with open(filename,'r') as f:
        return f.read().split('\n')[:-1]
def findAllOrderings(string):
    if len(string) == 0:
        return ['']
    if len(string) == 1:
        return [string]
    newList = set()
    for i in range(len(string)):
        removedString = string[:i] + string[i+1:]
        for item in findAllOrderings(removedString):
            newList.add(string[i] + item)
    return list(newList)
def validateMoves(p,moves,pos=(3,0)):
    validMoves = []
    for move in moves:
        np = list(p)
        for action in move:
            if action == '>':
                np[1] += 1
            elif action == '<':
                np[1] -= 1
            elif action == '^':
                np[0] -= 1
            elif action == 'v':
                np[0] += 1
            if np[0] == pos[0] and np[1] == pos[1]:
                break
        else:
            validMoves.append(move)
    return validMoves
def findMinLengthdpad(code, depth=2):
    if depth == 0:
        return len(code)
    grid = {'^': (0,1), 'A': (0,2), '<': (1,0), 'v': (1,1), '>': (1,2)}
    p = (0,2)
    minCost = 0
    for c in code:
        np = grid[c]
        delta = [np[0]-p[0],np[1]-p[1]]
        requiredMoves = ''
        while delta[1] > 0:
            delta[1] -= 1
            requiredMoves += '>'
        while delta[1] < 0:
            delta[1] += 1
            requiredMoves += '<'
        while delta[0] < 0:
            delta[0] += 1
            requiredMoves += '^'
        while delta[0] > 0:
            delta[0] -= 1
            requiredMoves += 'v'
        potentialMoves = findAllOrderings(requiredMoves)
        validMoves = validateMoves(p,potentialMoves,pos=(0,0))
        if len(validMoves) == 0:
            import ipdb; ipdb.set_trace()
        cheapestMove = 10000000000000000000000000000000000000000
        for validMove in validMoves:
            current = findMinLengthdpad(validMove + "A",depth=depth-1)
            if current < cheapestMove:
                cheapestMove = current
        minCost += cheapestMove
        p = np
    return minCost
def findMinLength(code):
    grid = {'7': (0,0), '8': (0,1), '9': (0,2), '4': (1,0), '5': (1,1), '6': (1,2), '1': (2,0), '2': (2,1), '3': (2,2), '0': (3,1), 'A':(3,2)}
    p = (3,2)
    minCost = 0
    for c in code:
        np = grid[c]
        delta = [np[0]-p[0],np[1]-p[1]]
        requiredMoves = ''
        while delta[1] > 0:
            delta[1] -= 1
            requiredMoves += '>'
        while delta[1] < 0:
            delta[1] += 1
            requiredMoves += '<'
        while delta[0] < 0:
            delta[0] += 1
            requiredMoves += '^'
        while delta[0] > 0:
            delta[0] -= 1
            requiredMoves += 'v'
        potentialMoves = findAllOrderings(requiredMoves)
        validMoves = validateMoves(p,potentialMoves)
        cheapestMove = 10000000000000000000000000000000000000000000000000000000000000000000000000000
        for validMove in validMoves:
            current = findMinLengthdpad(validMove + 'A')
            if current < cheapestMove:
                cheapestMove = current
        minCost += cheapestMove
        p = np
    return minCost
toFind = parse(filename='input.txt')
sum = 0
for code in toFind:
    minLen = findMinLength(code)
    sum += minLen * int(code[:-1])
print(sum)
# result = findAllOrderings('')
# print(result)