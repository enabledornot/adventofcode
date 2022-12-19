import json
from functools import cmp_to_key
def jsonise(list):
    return json.loads(list)
def parse(fname):
    with open(fname, "r") as f:
        data = f.read().split("\n")
    ndata = []
    for compare in data:
        if compare!="":
            ndata.append(jsonise(compare))
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
def compare(item1, item2):
    return inOrder(item2, item1)

parsed = parse("input.txt")
parsed.append([[2]])
parsed.append([[6]])
parsed.sort(key=cmp_to_key(compare))
count = 1
value = 1
for line in parsed:
    if line==[[2]] or line==[[6]]:
        value*=count
    count+=1
print(value)