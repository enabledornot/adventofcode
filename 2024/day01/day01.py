

def loadSingle(filename="input.txt"):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    # newData = []
    # for line in data:
    #     newData.append(int(line))
    #     newData.append(float(line))
    # data = newData
    return data

def loadMulti(filename="input.txt"):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    newData = []
    for line in data:
        newLine = []
        for char in line.split(" "):
            newLine.append(char)
            # newLine.append(int(char))
            # newLine.append(float(char))
        newData.append(newLine)
    return newData

def load(filename="input.txt"):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    left, right = [], []
    for line in data:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))
    return left, right
# loaded = loadSingle()
left, right = load()
left.sort()
right.sort()
part1 = 0
for i in range(len(left)):
    part1 += abs(left[i] - right[i])
print(part1)
part2 = 0
for l in left:
    part2 += l * right.count(l)
print(part2)