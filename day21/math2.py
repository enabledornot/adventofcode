def parse(fname):
    with open(fname, "r") as f:
        data = f.read().split("\n")
    ndata = {}
    for line in data:
        split = line.split(" ")
        mname = split[0][:-1]
        if len(split)==2:
            ndata[mname] = int(split[1])
        else:
            ndata[mname] = (split[1],split[2],split[3])
    return ndata
def findMonkeyScore(mm,name):
    if name=="humn":
        print("foundU")
    monkey = mm[name]
    if isinstance(monkey,int):
        return monkey
    else:
        if monkey[1]=="+":
            return findMonkeyScore(mm,monkey[0]) + findMonkeyScore(mm,monkey[2])
        elif monkey[1]=="-":
            return findMonkeyScore(mm,monkey[0]) - findMonkeyScore(mm,monkey[2])
        elif monkey[1]=="*":
            return findMonkeyScore(mm,monkey[0]) * findMonkeyScore(mm,monkey[2])
        elif monkey[1]=="/":
            return findMonkeyScore(mm,monkey[0]) / findMonkeyScore(mm,monkey[2])
def canFindScore(mm, name):
    if name=="humn":
        return False
    monkey = mm[name]
    if isinstance(monkey,int):
        return True
    else:
        if monkey[1]=="+":
            return canFindScore(mm,monkey[0]) and canFindScore(mm,monkey[2])
        elif monkey[1]=="-":
            return canFindScore(mm,monkey[0]) and canFindScore(mm,monkey[2])
        elif monkey[1]=="*":
            return canFindScore(mm,monkey[0]) and canFindScore(mm,monkey[2])
        elif monkey[1]=="/":
            return canFindScore(mm,monkey[0]) and canFindScore(mm,monkey[2])
def getRequiredScore(mm, name, required):
    if name=="humn":
        return required
    monkey = mm[name]
    if isinstance(monkey,int):
        print("ERROR")
        return -1

    if monkey[1]=="+":
        if canFindScore(mm,monkey[0]):
            newRequired = required - findMonkeyScore(mm,monkey[0])
            return getRequiredScore(mm, monkey[2], newRequired)
        elif canFindScore(mm,monkey[2]):
            newRequired = required - findMonkeyScore(mm,monkey[2])
            return getRequiredScore(mm, monkey[0], newRequired)
        else:
            print("ERROR")
    elif monkey[1]=="-":
        if canFindScore(mm,monkey[0]):
            newRequired = findMonkeyScore(mm,monkey[0]) - required
            return getRequiredScore(mm, monkey[2], newRequired)
        elif canFindScore(mm,monkey[2]):
            newRequired = findMonkeyScore(mm,monkey[2]) + required
            return getRequiredScore(mm, monkey[0], newRequired)
        else:
            print("ERROR")
    elif monkey[1]=="*":
        if canFindScore(mm,monkey[0]):
            newRequired = required / findMonkeyScore(mm,monkey[0])
            return getRequiredScore(mm, monkey[2], newRequired)
        elif canFindScore(mm,monkey[2]):
            newRequired = required / findMonkeyScore(mm,monkey[2])
            return getRequiredScore(mm, monkey[0], newRequired)
        else:
            print("ERROR")
    elif monkey[1]=="/":
        if canFindScore(mm,monkey[0]):
            newRequired = findMonkeyScore(mm,monkey[0]) / required
            return getRequiredScore(mm, monkey[2], newRequired)
        elif canFindScore(mm,monkey[2]):
            newRequired= required * findMonkeyScore(mm,monkey[2])
            return getRequiredScore(mm, monkey[0], newRequired)
        else:
            print("ERROR")
parsed = parse("input.txt")
if canFindScore(parsed, parsed["root"][0]):
    recscore = getRequiredScore(parsed, parsed["root"][2], findMonkeyScore(parsed, parsed["root"][0]))
else:
    recscore = getRequiredScore(parsed, parsed["root"][0], findMonkeyScore(parsed, parsed["root"][2]))
print(recscore)
