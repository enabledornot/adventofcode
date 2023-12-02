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
parsed = parse("input.txt")
print(findMonkeyScore(parsed, "root"))