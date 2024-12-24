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
init_val, all_gates = parse(filename='input.txt')
c = Circut(init_val,all_gates)
current = 0
cnt = 0
binary = []
for cnt in range(10000):
    current = c.find(f'z{cnt:02d}')
    if current == None:
        break
    binary.append(current)
print(binary)
b10 = 0
for b in reversed(binary):
    b10 = b10 * 2
    b10 += b
print(b10)