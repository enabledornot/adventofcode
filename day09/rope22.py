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
