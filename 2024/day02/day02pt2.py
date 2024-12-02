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
def doCheck(line):
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
        return True
    return False
input = loadMulti(filename="input.txt")
cnt = 0
bad_check = []
for line in input:
    last = line[0]
    allInc = []
    allDec = []
    rangeCorrect = []
    for i, val in enumerate(line[1:]):
        diff = last - val
        if diff > 0:
            allDec.append(i+1)
        if diff < 0:
            allInc.append(i+1)
        if abs(diff) < 1 or abs(diff) > 3:
            rangeCorrect.append(i+1)
        last = val
    if (len(allInc) == 0 or len(allDec) == 0) and len(rangeCorrect) == 0:
        cnt += 1
    else:
        # toDo = allInc + allDec + rangeCorrect
        bad_check.append(line)
        # for do in toDo:
        #     newLine = line.copy()
        #     newLine.pop(do)
        #     bad_check[-1].append(newLine)
# print(bad_check)
for line in bad_check:
    for i in range(len(line)):
        newLine = line.copy()
        newLine.pop(i)
        if doCheck(newLine):
            cnt+=1
            break
    # for line in group:
    #     last = line[0]
    #     allInc = True
    #     allDec = True
    #     rangeCorrect = True
    #     for i in line[1:]:
    #         diff = last - i
    #         if diff > 0:
    #             allDec = False
    #         if diff < 0:
    #             allInc = False
    #         if abs(diff) < 1 or abs(diff) > 3:
    #             rangeCorrect = False
    #         last = i
    #     if (allInc or allDec) and rangeCorrect:
    #         cnt += 1
    #         break
print(cnt)