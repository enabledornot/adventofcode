def parse():
    with open('input.txt',"r") as f:
        return f.read().split("\n")

pos = 50
cnt = 0
for line in parse():
    # print(pos)
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
    while npos < 0:
        pos = (pos - 1 ) % 100
        npos += 1
        if pos == 0:
            cnt += 1
    while npos > 0:
        pos = (pos + 1) % 100
        npos -= 1
        if pos == 0:
            cnt += 1
    
print(cnt)