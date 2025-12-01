def parse():
    with open('input.txt',"r") as f:
        return f.read().split("\n")

pos = 50
cnt = 0
for line in parse():
    if len(line) < 1:
        continue
    if int(line[1:]) == 0:
        continue
    if line[0] == "R":
        npos = int(line[1:])
    elif line[0] == "L":
        npos = - int(line[1:])
    else:
        print('err')
    cnt += abs(npos) // 100
    if npos < 0:
        npos = (-1*npos) % 100
        npos = -1*npos
    else:
        npos = npos % 100
    opos = pos
    pos = pos + npos
    if pos < 0:
        pos += 100
        if opos != 0:
            cnt += 1
    elif pos >= 100:
        pos -= 100
        cnt += 1
    elif pos == 0:
        cnt += 1
print(cnt)