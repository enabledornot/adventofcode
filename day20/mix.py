import math
def parse(fname):
    with open(fname, "r") as f:
        data = f.read().split("\n")
    ndata = []
    cnt = 0
    for line in data:
        ndata.append((cnt,int(line)))
        cnt+=1
    return ndata
def mix(mixnum,mixlist):
    oldindex = mixlist.index(mixnum)
    newIndex = oldindex + mixnum[1]
    newIndex = newIndex%(len(mixlist)-1)
    mixlist.pop(oldindex)
    mixlist.insert(newIndex, mixnum)
def slowMix(mixnum,mixlist):
    starting = mixlist.index(mixnum)
    if mixnum < 0:
        for i in range(mixnum*-1):
            p1 = (starting - i)%len(mixlist)
            p2 = (starting - 1 - i)%len(mixlist)
            tmp = mixlist[p2]
            mixlist[p2] = mixlist[p1]
            mixlist[p1] = tmp
    else:
        for i in range(mixnum):
            p1 = (i + starting)%len(mixlist)
            p2 = (i + 1 + starting)%len(mixlist)
            tmp = mixlist[p2]
            mixlist[p2] = mixlist[p1]
            mixlist[p1] = tmp
def calculateGrove(mixlist):
    for i in range(len(mixlist)):
        if mixlist[i][1]==0:
            cords = i
            break
    ans = 0
    for i in range(3):
        cords = (cords+1000)%len(mixlist)
        ans+=mixlist[cords][1]
    return ans
parsed = parse("input.txt")
print(parsed)
parsedCopy = parsed.copy()
for line in parsedCopy:
    # print(line)
    mix(line,parsed)
    # print(parsed)
print(calculateGrove(parsed))