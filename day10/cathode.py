def parse():
    with open("input.txt","r") as f:
        data = f.read().split("\n")
    return data
data = parse()
reg = 1
clock = 0
mult = 0
for inst in data:
    split = inst.split(" ")
    if(split[0]=="noop"):
        clock+=1
        if(clock in [20, 60, 100, 140, 180, 220]):
            print(reg)
            mult+=clock*reg
    elif(split[0]=="addx"):
        clock+=1
        if(clock in [20, 60, 100, 140, 180, 220]):
            print(reg)
            mult+=clock*reg
        clock+=1
        if(clock in [20, 60, 100, 140, 180, 220]):
            print(reg)
            mult+=clock*reg
        reg+=int(split[1])
print(mult)