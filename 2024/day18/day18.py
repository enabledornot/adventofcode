from queue import PriorityQueue
def parse(input='input.txt'):
    data = []
    with open(input,"r") as f:
        for line in f.read().split('\n')[:-1]:
            a, b = line.split(',')
            data.append(tuple([int(a),int(b)]))
    return data
def findNewPoints(cpoint,bound=70):
    newp = []
    for did, offset in enumerate([[0,1],[1,0],[0,-1],[-1,0]]):
        potential = cpoint.copy()
        potential[0] += offset[0]
        potential[1] += offset[1]
        if potential[0] >= 0 and potential[0] < bound and potential[1] >= 0 and potential[1] < bound:
            newp.append((did,potential))
    return newp
def findShortest(corrupted,dim):
    cset = set(corrupted)
    visited = set()
    toDo = PriorityQueue()
    toDo.put((0,[0,0]))
    while True:
        p, point = toDo.get(block=False)
        # print(p)
        # print(point)
        if tuple(point) not in visited:
            visited.add(tuple(point))
            if tuple(point) == (dim-1,dim-1):
                return p
            for _, ppoint in findNewPoints(point,dim):
                if tuple(ppoint) not in cset or tuple(ppoint) == (dim-1,dim-1):
                    toDo.put((p+1,ppoint))
corrupted = parse()
dim = 71
print(len(corrupted))
for i in range(dim):
    for ii in range(dim):
        if (i,ii) in corrupted[:1024]:
            print('O',end="")
        else:
            print('.',end="")
    print("")
print(findShortest(corrupted[:1024],dim))
# print(corrupted)