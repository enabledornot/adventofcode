from tqdm import tqdm
with open("input.txt") as f:
    data = f.read().split("\n")[:-1]
def generatePoss(n):
    if n == 1:
        return [[]]
    result = generatePoss(n-1)
    new_result = []
    for line in result:
        new_result.append(line+['*'])
        new_result.append(line+['+'])
        new_result.append(line+['||'])
    return new_result
def checkIfPossible(values,result):
    # print(values)
    poss = generatePoss(len(values))
    # print(poss)
    for p in poss:
        current = values[0]
        for value, op in zip(values[1:],p):
            if op == '+':
                current += value
            elif op == '*':
                current *= value
            elif op == '||':
                current = int(str(current) + str(value))
        # print(current)
        if current == int(result):
            # print("stopping")
            return True
    return False
parsed = {}
for line in data:
    first, second = line.split(": ")
    if first in parsed:
        print("dupe")
    parsed[first] = []
    for c in second.split(" "):
        parsed[first].append(int(c))
total = 0
for result in tqdm(parsed):
    if checkIfPossible(parsed[result],result):
        total += int(result)
print(total)
