with open("input.txt","r") as f:
    raw_data = f.read().split("\n")[0]
def find_free(fsystem,new_block):
    last_seen = -2
    for i,current in enumerate(fsystem):
        if last_seen == current[0]:
            print(f"fragmentation {i}")
            print(f"fsystem[i-1] = {fsystem[i-1]}")
            print(f"fsystem[i] = {fsystem[i]}")
            print(f"fsystem[i+1] = {fsystem[i+1]}")
        if current[0] == -1 and current[1] >= new_block[1]:
            return i
        last_seen = current[0]
def display_system(fsystem):
    for block in fsystem:
        if block[0] == -1:
            c = '.'*block[1]
        else:
            c = str(block[0])*block[1]
        print(c,end="")
    print("")
def calculateCheckSum(fsystem):
    currentIndex = 0
    cnt = 0
    for p in fsystem:
        if p[0] != -1:
            cnt += sum(range(currentIndex,currentIndex+p[1]))*p[0]
        currentIndex += p[1]
    return cnt
def getRealSize(fsystem):
    realSize = 0
    for p in fsystem:
        realSize+=p[1]
    return realSize
def defrag(fsystem,i,only_pre=False):
    defrag_cnt = 0
    if fsystem[i][0] != -1:
        print(f"ERROR {fsystem[i][0]}")
    if i < len(fsystem)-1 and fsystem[i+1][0] == -1:
        if only_pre:
            defrag_cnt += 1
        old_block = fsystem.pop(i+1)
        fsystem[i][1] += old_block[1]
    if i > 0 and fsystem[i-1][0] == -1:
        defrag_cnt += 1
        old_block = fsystem.pop(i)
        fsystem[i-1][1] += old_block[1]
    return defrag_cnt
fsystem = []
for i,c in enumerate(raw_data):
    if int(c) == 0:
        continue
    if i % 2 == 0:
        fsystem.append([int(i/2),int(c)])
        # for itr in range(int(c)):
        #     fsystem.append(int(i / 2))
    else:
        fsystem.append([-1,int(c)])
        # defrag(fsystem,len(fsystem)-1)
        # for itr in range(int(c)):
        #     fsystem.append(-1)
last = -2
for i,c in enumerate(fsystem):
    if c == last:
        print(f"fragmentation earlier {i}")
        print(f"fsystem[i-2] = {fsystem[i-2]}")
        print(f"fsystem[i-1] = {fsystem[i-1]}")
        print(f"fsystem[i] = {fsystem[i]}")
        print(f"fsystem[i+1] = {fsystem[i+1]}")
    last = c
# print(fsystem)
i = len(fsystem) - 1
while i >= 0:
    # print(i)
    popped = fsystem[i]
    if popped[0] == -1:
        i = i - 1
        continue
    new_loc = find_free(fsystem[:i],popped)
    # print(new_loc)
    if new_loc:
        # print(getRealSize(fsystem))
        # display_system(fsystem)
        fsystem[i] = [-1,popped[1]]
        d_cnt = defrag(fsystem,i,only_pre=True)
        oldloc_size = fsystem[new_loc][1]
        fsystem.pop(new_loc)
        if oldloc_size != popped[1]:
            # defrag(fsystem,new_loc)
            fsystem.insert(new_loc,[-1,oldloc_size-popped[1]])
            d_cnt = defrag(fsystem,new_loc)
            i = i + 1
        fsystem.insert(new_loc,popped)
    i = i - 1
    # else:
    #     break

# total = 0
# for i,e in enumerate(fsystem):
#     if e != -1:
#         total += i * e
# print(fsystem)
# display_system(fsystem)
last = -2
for i,c in enumerate(fsystem):
    if c == last:
        print(f"fragmentation later {i}")
        print(f"fsystem[i-2] = {fsystem[i-2]}")
        print(f"fsystem[i-1] = {fsystem[i-1]}")
        print(f"fsystem[i] = {fsystem[i]}")
        print(f"fsystem[i+1] = {fsystem[i+1]}")
    last = c
print(calculateCheckSum(fsystem))