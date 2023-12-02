import math
def parse(fname):
    data = []
    with open(fname,"r") as file:
        data = file.read().split("\n")
    nout = []
    for i in data:
        if(len(i)!=0):
            splitdd = i.split(" ")
            nout.append((splitdd[0],int(splitdd[1])))
    return nout
def inRange(head, tail):
    return (abs(head[0]-tail[0])<2) and (abs(head[1]-tail[1])<2)
def moveDir(head,tail, dur, amnt):
    prevhead = tuple(head)
    head[dur]+=amnt
    if(abs(head[dur-1]-tail[dur-1])>1 or abs(head[dur]-tail[dur]))>1:
        tail[0] = prevhead[0]
        tail[1] = prevhead[1]
# def printRecords(recs, tail=None, head=None):
#     for ii in range(0,5):
#         for i in range(0,5):
#             if tail!=None and tail[0]==i and tail[1]==ii:
#                 print("t",end="")
#             elif head!=None and head[0]==i and head[1]==ii:
#                 print("h",end="")
#             elif i==0 and ii==0:
#                 print("s",end="")
#             elif (i,ii) in recs:
#                 print("#",end="")
#             else:
#                 print(".",end="")
#         print("")
#     print("")
def printRecords(rope, hist, ran):
    for i in range(ran,-ran,-1):
        for ii in range(-ran,ran):
            cnt = 0
            printed = False
            for ro in rope:
                if ro[0]==i and ro[1]==ii:
                    print(cnt,end="")
                    printed = True
                    break
                cnt+=1
            if not printed:
                print(".",end="")
        print("")
    print("")
def fix(num):
    if num==0:
        return num
    return int(num/abs(num))
def updateLocation(head, tail):
    dx = tail[0]-head[0]
    dy = tail[1]-head[1]
    # print(dx)
    # print(dy)
    if abs(dx)==2 and abs(dy)==0:
        tail[0]-=fix(dx)
    elif abs(dx)==0 and abs(dy)==2:
        tail[1]-=fix(dy)
    elif (abs(dx)==2 and abs(dy)==1) or (abs(dx)==1 and abs(dy)==2) or (abs(dx)==2 and abs(dy)==2):
        tail[0]-=fix(dx)
        tail[1]-=fix(dy)
rslt = parse("input.txt")
print(rslt)
rope = []
for i in range(10):
    rope.append([0,0])
tailRecord = []
moves = {
    "U":(1,0),
    "D":(-1,0),
    "L":(0,-1),
    "R":(0,1)
}
# printRecords(rope, tailRecord, 5)
for inst in rslt:
    for i in range(inst[1]):
        rope[0][0]+=moves[inst[0]][0]
        rope[0][1]+=moves[inst[0]][1]
        for ii in range(len(rope)-1):
            updateLocation(rope[ii],rope[ii+1])
        # printRecords(rope, tailRecord, 5)
        if not tuple(rope[9]) in tailRecord:
            tailRecord.append(tuple(rope[9]))
    # print(rope)
    # printRecords(rope, tailRecord, 5)
print(len(tailRecord))