from math import pow
def parse(input='input.txt'):
    with open(input,"r") as f:
        dataraw = f.read().split('\n')
    a = int(dataraw[0][12:])
    b = int(dataraw[1][12:])
    c = int(dataraw[2][12:])
    program = []
    for part in dataraw[4][9:].split(','):
        # print(part)
        program.append(int(part))
    return (a,b,c), program
def p2i(n):
    return 1 << n
    # return int(pow(2,n))
def compute(a,prog):
    b = a % 8
    b = b ^ prog[3]
    c = a >> b
    b = b ^ c
    b = b ^ prog[9]
    return b
regs, program = parse()
valids = []
for a in range(int(pow(2,10))):
    if compute(a,program) % 8 == program[0]:
        valids.append(a)
for i,_ in enumerate(program[1:]):
    step = p2i(10 + (3*i))
    for aadj in range(0,step*8,step):
        print(aadj)

for i,val in enumerate(program[1:]):
    print(i)
    print(val)
    newvalids = []
    for valid in valids:
        step = p2i(10 + (3*i))
        for aadj in range(0,step*8,step):
            newa = aadj + valid
            newadiv = newa >> 3*(i+1)
            if compute(newadiv,program) % 8 == val:
                newvalids.append(newa)
    valids = newvalids
    # break
    print(valids)
    print("")
print(min(valids))