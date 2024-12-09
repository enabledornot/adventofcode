with open("input.txt","r") as f:
    raw_data = f.read().split("\n")[0]
fsystem = []
for i,c in enumerate(raw_data):
    if i % 2 == 0:
        for itr in range(int(c)):
            fsystem.append(int(i / 2))
    else:
        for itr in range(int(c)):
            fsystem.append(-1)
for i in reversed(range(len(fsystem))):
    if fsystem[i] >= 0:
        new_indx = fsystem.index(-1)
        if new_indx > i:
            break
        fsystem[new_indx] = fsystem[i]
        fsystem[i] = -1
total = 0
for i,e in enumerate(fsystem):
    if e != -1:
        total += i * e
# print(fsystem)
print(total)