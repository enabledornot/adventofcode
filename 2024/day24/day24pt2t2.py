import json
from tqdm import tqdm
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
class CircutVirtual:
    def __init__(self,gates):
        self.g = gates
        self.v = {}
        self.c = set()
        self.cm = set()
    def find(self,v,incDest=False):
        if v[0] in ['x','y']:
            return v
        # if v[0] == 'z':
        #     self.c = self.c.union(self.cm)
        if v in self.c:
            return v
        if v not in self.g:
            return None
        self.cm.add(v)
        # if v in self.v:
        #     result = self.v[v]
        # else:
        oa, op, ob = self.g[v]
        result = (self.find(oa,incDest=incDest),op,self.find(ob,incDest=incDest))
        if incDest:
            return (result,v)
        else:
            return result
    def reset(self):
        self.c = self.c.union(self.cm)
    def search(self,q):
        for gate in self.g:
            cg = self.g[gate]
            if cg[0] == q[0] and cg[1] == q[1] and cg[2] == q[2]:
                return gate
            if cg[2] == q[0] and cg[1] == q[1] and cg[0] == q[2]:
                return gate
        return None
    def evaluate2(self,bound=None):
        wrong = 0
        for i in range(500):
            c = self.find(f'z{i:02d}')
            # print(c)
            if c == None:
                break
            sc = sortTuple(c)
            # print(sc)
            if i == 0:
                r0,r1 = compTUP(sc,('x00','XOR','y00'))
                if r0 != None:
                    return 99999
                    print('error')
                    break
            elif i == 1:
                r0,r1 = compTUP(sc,(('x00','AND','y00'),'XOR',('x01','XOR','y01')))
                v0 = self.search(sc[0])
                v1 = self.search(sc[2])
                if r0 != None:
                    return 9999
                    print('error')
                    break
            elif i == 44:
                break
            elif i > 1:
                r0,r1 = compTUP(sc,((f'x{i:02d}', 'XOR', f'y{i:02d}'), 'XOR', ((f'{v0}', 'AND', f'{v1}'), 'OR', (f'x{(i-1):02d}', 'AND', f'y{(i-1):02d}'))))
                if r0 != None and r0 != ((f'{v0}', 'AND', f'{v1}')):
                    r0,r1 = compTUP(sc,((f'x{i:02d}', 'XOR', f'y{i:02d}'), 'XOR', ((f'{v1}', 'AND', f'{v0}'), 'OR', (f'x{(i-1):02d}', 'AND', f'y{(i-1):02d}'))))
                v0 = self.search((f'x{i:02d}', 'XOR', f'y{i:02d}'))
                cadd = self.find(f'z{i:02d}',incDest=True)
                try:
                    if cadd[0][2][0][1] == 'OR':
                        v1 = cadd[0][2][1]
                except:
                    self.reset()
                    continue
                try:
                    if cadd[0][0][0][1] == 'OR':
                        v1 = cadd[0][0][1]
                except:
                    self.reset()
                    continue
                if r0 != None:
                    # print(r0)
                    # print(r1)
                    # print(sc)
                    # print('--')
                    wrong += 1
                    if bound != None:
                        if wrong == bound:
                            return bound
                    # if self.find(r0) != None:
                    #     wrong.append(self.find(r0))
                    # else:
                    #     wrong.append(r0)
            self.reset()
        # print(wrong)
        return wrong
                # r = compTUP(sc,)
            # elif i > 0:
            #     compare

    # def evaluate(self):
    #     wrong = []
    #     for i in range(500):
    #         c = self.find(f'z{i:02d}')
    #         if c == None:
    #             break
    #         print(wrong)
    #         print(c)
    #         if i == 0:
    #             if c != (('x00','XOR','y00'),'z00'):
    #                 wrong.append(c[1])
    #         elif i == 1:
    #             if c[0][1] != 'XOR':
    #                 wrong.append(c[1])
    #             xorLeft = compare((f'x{i:02d}','XOR',f'y{i:02d}'),c[0][0][0])
    #             xorRight = compare((f'x{i:02d}','XOR',f'y{i:02d}'),c[0][2][0])
    #             andLeft = compare((f'x{(i-1):02d}','AND',f'y{(i-1):02d}'),c[0][0][0])
    #             andRight = compare((f'x{(i-1):02d}','AND',f'y{(i-1):02d}'),c[0][2][0])
    #             if (xorLeft and xorRight) or (andLeft and andRight):
    #                 print('something went wrong')
    #                 break
    #             if xorLeft:
    #                 xorv = c[0][0][1]
    #             if xorRight:
    #                 xorv = c[0][2][1]
    #             if andLeft:
    #                 orv = c[0][0][1]
    #             if andRight:
    #                 orv = c[0][2][1]
    #         # elif i >= 10:
    #         #     break
    #         elif i >= 2:
    #             # print(xorv)
    #             # print(orv)
    #             # print(c)
    #             xorLeft = compare((f'x{i:02d}','XOR',f'y{i:02d}'),c[0][0][0])
    #             xorRight = compare((f'x{i:02d}','XOR',f'y{i:02d}'),c[0][2][0])
    #             # print(c[0][0])
    #             # print(c[0][2])
    #             # asdf
    #             # print(xorLeft)
    #             # print(xorRight)
    #             orLeft = False
    #             orRight = False
    #             orLeft = checkOr(self,c[0][0],i,xorv,orv)
    #             # else:
    #             #     print(checkOr(c[0][0],i,xorv,orv))
    #             orRight = checkOr(self,c[0][2],i,xorv,orv)
    #             print((xorLeft,xorRight,orLeft,orRight))
    #             # print((orLeft,orRight))
    #             # else:
    #             #     print(checkOr(c[0][2],i,xorv,orv))
    #             # asdf
    #             # if xorLeft and not orRight:
    #             #     wrong.append(c[0][2][1])
    #             #     # print(c[0][2][1])
    #             if xorLeft ^ xorRight:
    #                 if xorLeft:
    #                     xorv = c[0][0][1]
    #                 if xorRight:
    #                     xorv = c[0][2][1]
    #             else:
    #                 xorv = None
    #             if (orLeft == None) ^ (orRight == None):
    #                 if orLeft == None:
    #                     orv = c[0][0][1]
    #                 if orRight == None:
    #                     orv = c[0][2][1]
    #             else:
    #                 orv = None
    #             if (orLeft == None) and (orRight == None):
    #                 wrong.append(orLeft)
    #                 wrong.append(orRight)
    #             if xorRight and xorLeft:
    #                 wrong.append(c[0][2][1])
    #                 wrong.append(c[0][0][1])
    #             if xorRight and (orLeft != None):
    #                 wrong.append(orLeft)
    #             if xorLeft and (orRight != None):
    #                 wrong.append(orRight)
    #             if (orLeft == None) and not xorRight:
    #                 wrong.append(c[0][2][1])
    #             if (orRight == None) and not xorLeft:
    #                 wrong.append(c[0][0][1])
    #             print((orv,xorv))
    #             # print(wrong)
    #         else:
    #             break
    #             print('undefined')
    #         print('')
    #     print(wrong)
# def checkOr(c,sor,i,xorv,orv):
#     if isinstance(sor,str):
#         return sor
#     if isinstance(sor[0][0],str):
#         return sor[1]
#     if sor[0][1] != 'OR':
#         return sor[1]

#     xyaLeft = compare((f'x{(i-1):02d}','AND',f'y{(i-1):02d}'),sor[0][0][0])
#     xyaRight = compare((f'x{(i-1):02d}','AND',f'y{(i-1):02d}'),sor[0][2][0])
#     # rLeft = False
#     # rRight = False
#     # if sor[0][0][0][0][0] not in ['x','y']:
#     #     rLeft = True
#     # if sor[0][2][0][0][0] not in ['x','y']:
#     #     rRight = True
#     # print(sor[0][0][0][0][0])
#     # print(sor[0][0][0][2][0])
#     if xorv != None and orv != None:
#         rLeft = compare((f'{xorv}','AND',f'{orv}'),sor[0][0][0])
#         rRight = compare((f'{xorv}','AND',f'{orv}'),sor[0][2][0])
#     else:
#         rLeft = False
#         rRight = False
#         if sor[0][0][0][0][0] not in ['x','y']:
#             rLeft = True
#         if sor[0][2][0][0][0] not in ['x','y']:
#             rRight = True
#     # print((rLeft,rRight))
#     # print((xyaLeft,xyaRight))
#     if (xyaLeft and rRight) or (xyaRight and rLeft):
#         print('or success')
#         return None
#     if xyaLeft and xyaRight:
#         if rLeft:
#             return 
    # # rRight error
    # if xyaLeft and not rRight:
    #     return sor[0][2][1]
    # # rLeft error
    # if xyaRight and not rLeft:
    #     return sor[0][0][1]
    # # xyaRight error
    # if rLeft and not xyaRight:
    #     return sor[0][2][1]
    # # xyaLeft errror
    # if rRight and not xyaLeft:
    #     return sor[0][0][1]
    # return 5
def tstr(t):
    return json.dumps(t)
def tuplize(t):
    if isinstance(t, list):
        return tuple(tuplize(item) for item in t)
    return t
def fstr(t):
    return tuplize(json.loads(t))
def sortTuple(t):
    if isinstance(t,tuple):
        l = sorted([tstr(sortTuple(t[0])),tstr(sortTuple(t[2]))])
        return (fstr(l[0]),t[1],fstr(l[1]))
    else:
        return t
def compTUP(t0,t1):
    # print((t0,t1))
    if isinstance(t0,str) and isinstance(t1,str):
        if t0 == t1:
            return None,None
        else:
            return t0,t1
    if isinstance(t0,tuple) and isinstance(t1,tuple):
        comp0 = compTUP(t0[0],t1[0])
        if comp0[0] != None:
            return comp0
        if t0[1] != t1[1]:
            return t0,t1
        comp1 = compTUP(t0[2],t1[2])
        if comp1[0] != None:
            return comp1
        return None, None
        # return t0[1] == t1[1] and compTUP(t0[0],t1[0]) and compTUP(t0[2],t1[2])
    return t0,t1
def compare(expected,to):
    expectedFlipped = (expected[2],expected[1],expected[0])
    if to == expected or to == expectedFlipped:
        return True
    return False
def swapAndCheck(a,swaps,bound=None):
    agate = a.copy()
    for ab in swaps:
        a,b = ab
        tmp = agate[a]
        agate[a] = agate[b]
        agate[b] = tmp
    c = CircutVirtual(agate)
    try:
        return c.evaluate2(bound=bound)
    except:
        return 9999
    
ival, agate = parse()
minR = swapAndCheck(agate,[])
print(minR)
potentialSwaps = set()
allA = set()
for a in tqdm(agate):
    for b in agate:
        swapSet = set([(a,b)])
        r = swapAndCheck(agate,swapSet,bound=minR)
        if r < minR:
            potentialSwaps.add((tuple(swapSet),r))
            # print((a,b,r))
buffSwaps = set()
newSwaps = potentialSwaps
while True:
    potentialSwaps = potentialSwaps.union(buffSwaps)
    buffSwaps = set()
    for a in tqdm(potentialSwaps):
        for b in newSwaps:
            target = min(a[1],b[1])
            swapSet = set(a[0]).union(set(b[0]))
            r = swapAndCheck(agate,swapSet,bound=target)
            if r == 0:
                print(swapSet)
            if r < target:
                buffSwaps.add((tuple(swapSet),r))
            # print([(a[0],a[1]),(b[0],b[1])])
            # print(r)
            # print('')
    newSwaps = buffSwaps
# print(potentialSwaps)
# for ab in [('wnf','vtj')]:
#     a,b = ab
#     tmp = agate[a]
#     agate[a] = agate[b]
#     agate[b] = tmp
# c = CircutVirtual(agate)
# buff = c.evaluate2()
# print("")
# for b in buff:
#     print(b)