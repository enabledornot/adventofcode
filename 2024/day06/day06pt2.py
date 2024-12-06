from tqdm import tqdm
import copy
with open("input.txt","r") as f:
    datao = f.read().split('\n')
data = []
for line in datao:
    data.append([])
    for c in line:
        data[-1].append(c)
for i,line in enumerate(data):
    try:
        ind0 = i
        ind1 = line.index('^')
        break
    except:
        pass
def getOriginalVisited(ind0,ind1,data):
    movement = [(-1,0),(0,1),(1,0),(0,-1)]
    cmov = 0
    visited = [(ind0,ind1)]
    print(visited)
    keep_going = True
    while keep_going:
        n_ind0 = ind0 + movement[cmov % 4][0]
        n_ind1 = ind1 + movement[cmov % 4][1]
        try:
            if n_ind0 < 0 or n_ind1 < 0:
                break
            elif data[n_ind0][n_ind1] == '#':
                cmov += 1
                # if cmov == 10:
                #     break
            else:
                new_pos = (n_ind0,n_ind1)
                if new_pos not in visited:
                    visited.append(new_pos)
                ind0 = n_ind0
                ind1 = n_ind1
        except:
            print(len(visited))
            break
    print(len(visited))
    return visited
def checkData(ind0,ind1,data):
    movement = [(-1,0),(0,1),(1,0),(0,-1)]
    # print(visited)
    cmov = 0
    visited = {(ind0,ind1,0)}
    keep_going = True
    loop = False
    while keep_going:
        # print(len(visited))
        n_ind0 = ind0 + movement[cmov % 4][0]
        n_ind1 = ind1 + movement[cmov % 4][1]
        new_pos = (n_ind0,n_ind1,cmov%4)
        # print(new_pos)
        if n_ind0 < 0 or n_ind1 < 0 or n_ind0 >= len(data) or n_ind1 >= len(data[0]):
            break
        elif new_pos in visited:
            loop = True
            break
        elif data[n_ind0][n_ind1] == '#':
            cmov += 1
            # if cmov == 10:
            #     break
        else:
            visited.add(new_pos)
            ind0 = n_ind0
            ind1 = n_ind1
    return loop
looper = 0
visited = getOriginalVisited(ind0,ind1,data)
print(len(visited))
for i in tqdm(range(len(data))):
    for ii in range(len(data[i])):
        if data[i][ii] == '.' and (i,ii) in visited:
            dataC = copy.deepcopy(data)
            dataC[i][ii] = '#'
            # print(str(i) + " " + str(ii))
            if checkData(ind0,ind1,dataC):
                looper += 1

print(looper)