with open("input.txt","r") as f:
    data = f.read().split('\n')
for i,line in enumerate(data):
    try:
        ind0 = i
        ind1 = line.index('^')
        break
    except:
        pass
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