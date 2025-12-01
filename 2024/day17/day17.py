from math import pow
def parse(input='input.txt'):
    with open(input,"r") as f:
        dataraw = f.read().split('\n')
    a = int(dataraw[0][12:])
    b = int(dataraw[1][12:])
    c = int(dataraw[2][12:])
    program = []
    for part in dataraw[4][9:].split(','):
        print(part)
        program.append(int(part))
    return (a,b,c), program
class Computer:
    def __init__(self,regs,program):
        self.a, self.b, self.c = regs
        self.p = program
        self.pc = 0
        self.out = []
    def execute(self):
        if self.pc >= len(self.p):
            return False
        inst = self.p[self.pc]
        op = self.p[self.pc+1]
        cop = self.findOp(op)
        if inst == 0:
            self.a = int(self.a / pow(2,cop))
        elif inst == 1:
            self.b = self.b ^ op
        elif inst == 2:
            self.b = cop % 8
        elif inst == 3:
            if self.a != 0:
                self.pc = op
                return True
        elif inst == 4:
            self.b = self.b ^ self.c 
        elif inst == 5:
            self.out.append(cop % 8)
        elif inst == 6:
            self.b = int(self.a / pow(2,cop))
        elif inst == 7:
            self.c = int(self.a / pow(2,cop))
        self.pc += 2
        return True
    def findOp(self,op):
        if op == 4:
            return self.a 
        elif op == 5:
            return self.b
        elif op == 6:
            return self.c
        elif op == 7:
            print(f"OP ERROR {op}")
        else:
            return op
regs, program = parse(input='test2.txt')
cpu = Computer(regs,program)
while cpu.execute():
    print('exec')
print(str(cpu.out)[1:-1].replace(' ',''))