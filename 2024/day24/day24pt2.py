def parse(filename='input.txt'):
    with open(filename,"r") as f:
        ivalues, gates = f.read().split('\n\n')
    init_val = {}
    for line in ivalues.split('\n'):
        name, number = line.split(': ')
        init_val[name] = int(number)
    all_gates = {}
    for line in gates.split('\n')[:-1]:
        left, right = line.split(' -> ')
        all_gates[right] = tuple(left.split(' '))
    return init_val, all_gates
class Circut:
    def __init__(self,values,gates):
        self.v = values
        self.g = gates
    def find(self,variable):
        if variable in self.v:
            return self.v[variable]
        if variable not in all_gates:
            return None
        oa, op, ob = all_gates[variable]
        if op == 'AND':
            result = self.find(oa) & self.find(ob)
        elif op == 'OR':
            result = self.find(oa) | self.find(ob)
        elif op == 'XOR':
            result = self.find(oa) ^ self.find(ob)
        self.v[variable] = result
        return result
class CircutVirtual:
    def __init__(self,values,gates):
        self.vd = values.copy()
        self.v = values
        self.g = gates
        self.seen = set()
        self.log = []
        self.r = {}
        self.w = set()
        self.suspect = set()
        self.pserch = set()
    def reset(self):
        self.log = []
        self.seen = set()
        self.v = self.vd.copy()
    def find(self,variable):
        if variable[0] in ['x','y']:
            if variable not in self.seen:
                self.seen.add(variable)
            return variable
        if variable in self.v:
            return variable
            return self.v[variable]
        if variable not in self.g:
            return None
        oa, op, ob = self.g[variable]
        if variable not in self.seen:
            self.seen.add(variable)
            self.log.append(((oa,op,ob),variable))
        result = (self.find(oa), op, self.find(ob))
        self.v[variable] = result
        return variable
    def evaluate(self):
        for cnt in range(500):
            current = self.find(f'z{cnt:02d}')
            if current == None:
                break
    def dump(self,filename='output.txt',doLabels=True):
        outfile = ""
        for line in self.log:
            operation, result = line
            oa, op, ob = operation
            if result[0] == 'z':
                outfile += '\n'
            if doLabels:
                outfile+= f"{self.r.get(oa,oa)} {op} {self.r.get(ob,ob)} -> {self.r.get(result,result)}\n"
            else:
                outfile+= f"{oa} {op} {ob} -> {result}\n"
        with open(filename,'w') as f:
            f.write(outfile)
    def renameVariables(self):
        self.reset()
        self.evaluate()
        cnt = -1
        cntother = 0
        alpha = ['a','b','c','d','e','f','g','h','i','j']
        rename = {}
        for line in self.log:
            operation, result = line
            if result[0] == 'z':
                cnt += 1
                cntother = 0
            else:
                if result[0] not in ['x','y'] and result not in rename:
                    rename[result] = f"{alpha[cntother]}{cnt:02d}"
                    cntother += 1
        # newgates = {}
        # for gate in self.g:
        #     cg = self.g[gate]
        #     newgates[rename.get(gate,gate)] = (rename.get(cg[0],cg[0]),cg[1],rename.get(cg[2],cg[2]))
        self.r = rename
        self.reset()
        # self.g = newgates
    def renameSearch(self, q):
        w0 = q[0] in self.w
        w2 = q[2] in self.w
        g = None
        for gate in self.g:
            cg = self.g[gate]
            if (q[0] == self.r.get(cg[0],cg[0]) or w0) and q[1] == cg[1] and (q[2] == self.r.get(cg[2],cg[2]) or w2):
                g = gate
                break
            if (q[2] == self.r.get(cg[0],cg[0]) or w2) and q[1] == cg[1] and (q[0] == self.r.get(cg[2],cg[2]) or w0):
                g = gate
                break
        if g:
            if g in self.pserch:
                print(f"double search {g}")
                self.suspect.add(g)
                return
            else:
                self.pserch.add(g)
                return g
    def checkLogs(self):
        self.renameVariables()
        self.evaluate()
        splitLog = []
        for line in self.log:
            operation, result = line
            if result[0] == 'z':
                splitLog.append([])
            splitLog[-1].append(line)
    def validate(self,term):
        result = self.renameSearch(term[0])
        if result == None:
            print("NO TERM FOUND ERROR")
            self.suspect.add(term[0][0])
            self.suspect.add(term[0][2])
            self.w.add(term[1])
            return False
        # if result[0] == 'z':
        #     if result != term[1]:
        #         self.suspect.add(result)
        #         # print(f"Z RESULT ERROR {result}")
        #         return False
        # if:
        # print(f"{result} -> {term[1]}")
        self.r[result] = term[1]
        return True
    def fetch(self,term):
        result = self.g[self.r.get(term,term)]
        return (self.r.get(result[0],result[0]),result[1],self.r.get(result[2],result[2]))
    def reverseLookupAll(self,suspect):
        # print(suspect)
        liste = []
        for real in self.r:
            label = self.r[real]
            if label in suspect:
                # print(f"{label}->{real}")
                suspect.remove(label)
                liste.append(real)
        for leftover in suspect:
            if leftover[0] == 'z':
                liste.append(leftover)
        return liste
    def check(self):
        opening = [
            (('x00','XOR','y00'),'zzz_00'),
            (('x01','XOR','y01'),'base_00'),
            (('x00','AND','y00'),'carry_00')
        ]
        for openi in opening:
            if not self.validate(openi):
                break
        # print(c.r)
        errorBlocks = []
        for n in range(0,45):
            nextBlock = [
                ((f'base_{n:02d}','XOR',f'carry_{n:02d}'),f'zzz_{(n+1):02d}'),
                ((f'x{(n+2):02d}','XOR',f'y{(n+2):02d}'),f'base_{(n+1):02d}'),
                ((f'x{(n+1):02d}','AND',f'y{(n+1):02d}'),f'b{(n+1):02d}'),
                ((f'base_{n:02d}','AND',f'carry_{n:02d}'),f'dcarry_{(n+1):02d}'),
                ((f'b{(n+1):02d}','OR',f'dcarry_{(n+1):02d}'),f'carry_{(n+1):02d}')
            ]
            if n == 43:
                nextBlock.pop(4)
                nextBlock.pop(1)
            if n == 44:
                nextBlock.pop(0)
                nextBlock.pop(0)
                nextBlock.pop(0)
                nextBlock.pop(0)
                print(nextBlock)
            for block in nextBlock:
                if not self.validate(block):
                    errorBlocks.append(block)
                    # print(block)
                    # print(c.fetch(block[1]))
                    # asdf
                    # print('error')
        return self.reverseLookupAll(self.suspect), errorBlocks
    def findBadGates(self):
        bg = []
        for gate in self.g:
            if gate not in self.pserch:
                bg.append(gate)
        return bg
init_val, all_gates = parse(filename='input.txt')
c = CircutVirtual(init_val,all_gates)

suspects, eb = c.check()
print(suspects)
print(eb)
c.evaluate()
c.dump('output2.txt')
c.dump('output3.txt',doLabels=False)
# print(c.findBadGates())
print(suspects)
print(c.findBadGates())
sus_gates = suspects + c.findBadGates()
print(sus_gates)
# while len(suspects) > 4:
#     minSus = suspects
#     min_ag = all_gates
#     minBg = badGates
#     for s0 in badGates:
#         for s1 in suspects:
#             if s0 != s1:
#                 # print((s0,s1))
#                 # print(all_gates)
#                 ag = all_gates.copy()
#                 tmp = ag[s0]
#                 ag[s0] = ag[s1]
#                 ag[s1] = ag[s0]
#                 nc = CircutVirtual(init_val,ag)
#                 sus, eb = nc.check()
#                 if len(sus) < len(minSus):
#                     minSus = sus
#                     min_ag = ag
#                     minBg = c.findBadGates()
#     print(minSus)
#     all_gates = min_ag
#     suspects = minSus

# r = c.renameSearch(('x00','XOR','y00'))
# opening = [
#     (('x00','XOR','y00'),'z00'),
#     (('x01','XOR','y01'),'a00'),
#     (('x00','AND','y00'),'d00')
# ]
# for openi in opening:
#     if not c.validate(openi):
#         break
# # print(c.r)
# errorBlocks = []
# for n in range(0,44):
#     nextBlock = [
#         ((f'a{n:02d}','XOR',f'd{n:02d}'),f'z{(n+1):02d}'),
#         ((f'x{(n+2):02d}','XOR',f'y{(n+2):02d}'),f'a{(n+1):02d}'),
#         ((f'x{(n+1):02d}','AND',f'y{(n+1):02d}'),f'b{(n+1):02d}'),
#         ((f'a{n:02d}','AND',f'd{n:02d}'),f'c{(n+1):02d}'),
#         ((f'b{(n+1):02d}','OR',f'c{(n+1):02d}'),f'd{(n+1):02d}')
#     ]
#     if n == 43:
#         nextBlock.pop(4)
#         nextBlock.pop(1)
#     for block in nextBlock:
#         if not c.validate(block):
#             errorBlocks.append(block)
#             # print(block)
#             # print(c.fetch(block[1]))
#             # asdf
#             print('error')
# # lastBlocks = [
# #     (())
# # ]
# print(c.w)
# print(len(c.w))
# print(errorBlocks)
# print(len(errorBlocks))
# c.evaluate()
# c.dump('output2.txt')
# print(c.suspect)
# print(r)
# c.renameVariables()
# c.evaluate()
# c.dump()