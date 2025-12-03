def parse():
    with open('input.txt','r') as f:
        return f.read().split('\n')

def find_max(ary):
    maxI = 0
    maxV = -1
    for i, c in enumerate(ary):
        num = int(c)
        if num > maxV:
            maxI = i
            maxV = num
    return maxI

def find_max_power(ary):
    currentPos = 0
    tot = 0
    for rem in reversed(range(12)):
        if rem != 0:
            currentPos += find_max(ary[currentPos:-rem])
        else:
            currentPos += find_max(ary[currentPos:])
        tot += int(ary[currentPos]) * 10**rem
        currentPos += 1
    return tot

# inp = parse()
summ = 0
for line in parse():
    if len(line) == 0:
        continue
    maxvol = find_max_power(line)
    print(f"{line}-{maxvol}")
    summ += maxvol
print(summ)