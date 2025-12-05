def parse():
    with open('input.txt',"r") as f:
        ranges, ids = f.read().split('\n\n')
    newRanges = []
    ids = ids.split('\n')[:-1]
    for rng in ranges.split('\n'):
        print(rng)
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
# print(ranges)
# print(ids)
freshCnt = 0
for id in ids:
    if isFresh(ranges, id):
        freshCnt += 1
print(freshCnt)