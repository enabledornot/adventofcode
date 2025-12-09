from functools import lru_cache

def parse():
    with open('input.txt','r') as f:
        data = f.read().split('\n')[:-1]
    output = []
    for line in data:
        a, b, c = line.split(',')
        output.append(tuple([int(a),int(b),int(c)]))
    return output

@lru_cache(maxsize=None)
def dist(p0,p1):
    return abs(p0[0]-p1[0])**2 + abs(p0[1]-p1[1])**2 + abs(p0[2]-p1[2])**2

class wrap:
    def __init__(self, v):
        self.v = v

def find_set_contains(sl, v):
    for i in range(len(sl)):
        # print(sl[i])
        if v in sl[i]:
            return i

boxes = parse()
distAdj = []
for i in range(len(boxes)):
    # distAdj.append([])
    for j in range(i):
        distAdj.append((dist(boxes[i],boxes[j]),i,j))
distAdj.sort()
# print(distAdj)
adjSets = []
for box in range(len(boxes)):
    adjSets.append(set([box]))
lastMerge = None
for i in range(10000):
    if len(adjSets) == 1:
        break
    findA = distAdj[i][1]
    findB = distAdj[i][2]
    lastMerge = (findA,findB)
    foundA = find_set_contains(adjSets, findA)
    foundB = find_set_contains(adjSets, findB)
    if foundA > foundB:
        adjSets.append( adjSets.pop(foundA) | adjSets.pop(foundB) )
    elif foundA < foundB:
        adjSets.append( adjSets.pop(foundB) | adjSets.pop(foundA) )
print(boxes[lastMerge[0]][0]*boxes[lastMerge[1]][0])
# print("")
# lenBoxes = []
# for box in adjSets:
#     lenBoxes.append(len(box))
#     print(box)
# lenBoxes.sort()
# lenBoxes = list(reversed(lenBoxes))
# print(lenBoxes)
# print(lenBoxes[0]*lenBoxes[1]*lenBoxes[2])