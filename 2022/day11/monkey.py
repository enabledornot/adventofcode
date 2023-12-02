import math
enableWorryLoss = True
class monkey:
    def __init__(self, items, oplist, testd, tcase, fcase, num):
        self.it = items
        self.opl = oplist
        self.test = testd
        self.ontrue = tcase
        self.onfalse = fcase
        self.mnum = num
        self.inspcnt = 0
    def throw(self, modnum):
        rslt = []
        for item in self.it:
            newitem = self.updateWorry(item,modnum)
            self.inspcnt+=1
            if(newitem%self.test==0):
                rslt.append((self.ontrue,newitem))
            else:
                rslt.append((self.onfalse,newitem))
        self.it = []
        return rslt
    def updateWorry(self,item,modnum):
        if(self.opl[0]=="old"):
            a=item
        else:
            a=int(self.opl[0])
        if(self.opl[2]=="old"):
            b=item
        else:
            b=int(self.opl[2])
        if(self.opl[1]=="+"):
            new = a+b
        else:
            new = a*b
        if(enableWorryLoss):
            new = math.floor(new/3)
        new = new%modnum
        return new
    def __str__(self):
        out = "Monkey " + str(self.mnum)+": "
        for item in self.it[:-1]:
            out+=str(item)+","
        if(len(self.it)!=0):
            out+=str(self.it[-1])
        out+=" - " + str(self.inspcnt)
        return out

class monkeys:
    def __init__(self, monkeyList, modnum):
        self.ml = monkeyList
        self.mn = modnum
    def cycle(self):
        for mon in self.ml:
            thrown = mon.throw(self.mn)
            for throw in thrown:
                self.ml[throw[0]].it.append(throw[1])
    def printAll(self):
        for mon in self.ml:
            print(mon)
    def getMonkeyBis(self):
        first = 0
        secnd = 0
        for mon in self.ml:
            if(mon.inspcnt>first):
                secnd = first
                first = mon.inspcnt
                continue
            if(mon.inspcnt>secnd):
                secnd = mon.inspcnt
        return first * secnd
def parse():
    with open("input.txt","r") as f:
        data = f.read().split("\n\n")
    ml = []
    cnt = 0
    modnum = 3
    for i in data:
        split = i.split("\n")
        itemls = []
        for char in split[1].split(" ")[4:]:
            try:
                itemls.append(int(char))
            except:
                itemls.append(int(char[:-1]))
        oplys = split[2].split(" ")[5:]
        test = int(split[3].split(" ")[5])
        modnum*=test
        tc = int(split[4].split(" ")[9])
        fc = int(split[5].split(" ")[9])
        ml.append(monkey(itemls,oplys,test,tc,fc,cnt))
        cnt+=1
    return monkeys(ml, modnum)
monkeyss = parse()
for i in range(20):
    monkeyss.cycle()
print("Answer part 1: {}".format(monkeyss.getMonkeyBis()))
enableWorryLoss = False
monkeyss = parse()
for i in range(10000):
    monkeyss.cycle()
print("Answer part 2: {}".format(monkeyss.getMonkeyBis()))

