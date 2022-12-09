def parse():
    data = []
    with open("input.txt","r") as file:
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
def printRecords(recs, tail=None, head=None):
    for ii in range(0,5):
        for i in range(0,5):
            if tail!=None and tail[0]==i and tail[1]==ii:
                print("t",end="")
            elif head!=None and head[0]==i and head[1]==ii:
                print("h",end="")
            elif i==0 and ii==0:
                print("s",end="")
            elif (i,ii) in recs:
                print("#",end="")
            else:
                print(".",end="")
        print("")
    print("")
rslt = parse()
head = [0,0]
tail = [0,0]
prev = (0,0)
tailRecord = []
for inst in rslt:
    for i in range(inst[1]):
        if(inst[0]=="U"):
            moveDir(head, tail, 1, 1)
        elif(inst[0]=="D"):
            moveDir(head, tail, 1, -1)
        elif(inst[0]=="L"):
            moveDir(head, tail, 0, -1)
        elif(inst[0]=="R"):
            moveDir(head, tail, 0, 1)
        if(abs(head[0]-tail[0])>1 and abs(head[1])-tail[1]>1):
            print("ERROR BREAKING")
            break
        if(not tuple(tail) in tailRecord):
            tailRecord.append(tuple(tail))
print(len(tailRecord))