import json
def jsonise(list):
    nlist = []
    for i in list:
        nlist.append(json.loads(i))
    return tuple(nlist)
def parse(fname):
    with open(fname, "r") as f:
        data = f.read().split("\n\n")
    # print(data)
    ndata = []
    for compare in data:
        ndata.append(jsonise(compare.split("\n")))
    return ndata
def inOrder(left, right):
    # print(left)
    # print(right)
    # print("")
    if isinstance(left,int) and isinstance(right,int):
        if left==right:
            return 0
        if left<right:
            return 1
        return -1
    if isinstance(left,int):
        left = [left]#*len(right)
    if isinstance(right,int):
        right = [right]#*len(right)
    count = 0
    while(True):
        if len(left) == count and len(right) == count:
            return 0
        if len(right) == count:
            return -1
        if len(left) == count:
            return 1
        rslt = inOrder(left[count],right[count])
        if rslt!=0:
            return rslt
        count+=1
    return 0
    

parsed = parse("input.txt")
index = 1
sum = 0
for compare in parsed:
    if inOrder(compare[0],compare[1])==1:
        print(index)
        sum+=index
    index+=1
print(sum)