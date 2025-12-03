def parse():
    with open('input.txt','r') as f:
        return f.read().split('\n')

# inp = parse()
summ = 0
for line in parse():
    maxL = 0
    maxI = 0
    for i, c in enumerate(line[:-1]):
        num = int(c)
        if num > maxL:
            maxL = num
            maxI = i
    nmax = 0
    maxI += 1
    while maxI < len(line):
        num = int(line[maxI])
        if nmax < num:
            nmax = num
        maxI += 1
    maxvol = maxL*10 + nmax
    print(f"{line}-{maxvol}")
    summ += maxL*10 + nmax
print(summ)