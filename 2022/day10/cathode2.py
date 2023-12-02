def parse():
    with open("input.txt","r") as f:
        data = f.read().split("\n")
    return data
class clock:
    def __init__(self):
        self.clock = 0
        self.reg = 2
    def cycle(self):
        self.clock+=1
        if(abs(self.clock%40-self.reg)<2):
            print("█",end="")
        else:
            print(" ",end="")
        if(self.clock%40==0):
            print("")
data = parse()
reg = 1
clk = clock()
for inst in data:
    split = inst.split(" ")
    if(split[0]=="noop"):
        clk.cycle()
    elif(split[0]=="addx"):
        clk.cycle()
        clk.cycle()
        clk.reg+=int(split[1])