def parse():
    with open('input.txt',"r") as f:
        ranges, ids = f.read().split('\n\n')
    newRanges = []
    ids = ids.split('\n')[:-1]
    for rng in ranges.split('\n'):
        # print(rng)
        rangeA, rangeB = rng.split('-')
        newRanges.append(tuple([int(rangeA),int(rangeB)]))
    for i in range(len(ids)):
        ids[i] = int(ids[i])
    return newRanges, ids

def isFresh(ranges, id):
    for rang in ranges:
        if rang[0] <= id and id <= rang[1]:
            return True
    return False

ranges, ids = parse()
srng = sorted(ranges)
# print(srng)

i = 0
while i+1 < len(srng):
    if srng[i][1] >= srng[i+1][0]:
        if srng[i][1] <= srng[i+1][1]:
            newRng = (srng[i][0],srng[i+1][1])
            a = srng.pop(i)
            b = srng.pop(i)
            srng.insert(i,newRng)
        else:
            srng.pop(i+1)
    else:
        i += 1
# print(srng)
tot = 0
for rng in srng:
    delta = 1+rng[1]-rng[0]
    # print(delta)
    tot += delta
print(tot)