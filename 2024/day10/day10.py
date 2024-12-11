with open("test.txt","r") as f:
    datao = f.read().split('\n')[:-1]
data = []
mask = []
for line in datao:
    data.append([])
    mask.append([])
    for c in line:
        try:
            data[-1].append(int(c))
        except:
            data[-1].append(-3)
        mask[-1].append(None)
def findNewPoints(data,cpoint):
    newp = []
    for offset in [[-1,0],[1,0],[0,1],[0,-1]]:
        potential = cpoint.copy()
        potential[0] += offset[0]
        potential[1] += offset[1]
        if potential[0] >= 0 and potential[0] < len(data) and potential[1] >= 0 and potential[1] < len(data[0]):
            newp.append(potential)
    return newp
def explore(data,mask,cpoint):
    # print(cpoint)
    global total_cnt
    global overkil_set
    if mask[cpoint[0]][cpoint[1]]:
        return mask[cpoint[0]][cpoint[1]]
    if data[cpoint[0]][cpoint[1]] == 9:
        # data[cpoint[0]][cpoint[1]] = -1
        return set([tuple(cpoint)])
    cnt = 0
    numcnt = 0
    nines = set()
    overfilcnt = 0
    otherdir_cnt = 0
    for newp in findNewPoints(data,cpoint):

        if data[newp[0]][newp[1]] == data[cpoint[0]][cpoint[1]] + 1:
            oldlen = len(nines)
            nines = nines | explore(data,mask,newp)
            # print(nines)
            if len(nines) > oldlen:
                overfilcnt += 1
            numcnt += 1
        if data[newp[0]][newp[1]] + 1 == data[cpoint[0]][cpoint[1]] and mask[newp[0]][newp[1]]:
            otherdir_cnt += 1
    if overfilcnt > 1 or otherdir_cnt > 1:
        # print(f"found_overfil {overfilcnt} {len(nines)}")
        # data[cpoint[0]][cpoint[1]] = -2
        overkil_set.add(tuple(cpoint))
        total_cnt += len(nines)
    mask[cpoint[0]][cpoint[1]] = nines
    return nines
    
global total_cnt
global overkil_set
overkil_set = set()
for line in data:
    print(line)
total_cnt = 0
for i in range(len(data)):
    for ii in range(len(data[i])):
        if data[i][ii] == 0:
            last = total_cnt
            explore(data,mask,[i,ii])
            print(total_cnt-last)
# explore(data,[0,2])
print(total_cnt)

for i, line in enumerate(data):
    for ii, c in enumerate(line):
        if c == -3:
            print(".",end="")
        elif c == -2 or (i,ii) in overkil_set:
            print("#",end="")
        else:
            print(c,end="")
    print("")