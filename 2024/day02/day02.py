def loadMulti(filename="input.txt"):
    with open(filename, "r") as f:
        data = f.read().split("\n")[:-1]
    newData = []
    for line in data:
        newLine = []
        for char in line.split(" "):
            # newLine.append(char)
            newLine.append(int(char))
            # newLine.append(float(char))
        newData.append(newLine)
    return newData

input = loadMulti(filename="input.txt")
cnt = 0
for line in input:
    last = line[0]
    allInc = True
    allDec = True
    rangeCorrect = True
    for i in line[1:]:
        diff = last - i
        if diff > 0:
            allDec = False
        if diff < 0:
            allInc = False
        if abs(diff) < 1 or abs(diff) > 3:
            rangeCorrect = False
        last = i
    if (allInc or allDec) and rangeCorrect:
        cnt += 1
print(cnt)