def parse(filename='input.txt'):
    with open(filename,'r') as f:
        data = f.read().split('\n')[:-1]
    t = None
    keys = []
    locks = []
    for line in data:
        if line != '':
            if t == None:
                if line[0] == '#':
                    t = 'lock'
                    locks.append([-1,-1,-1,-1,-1])
                else:
                    t = 'key'
                    keys.append([-1,-1,-1,-1,-1])
            if t == 'lock':
                liste = locks
            else:
                liste = keys
            for i,c in enumerate(line):
                if c == '#':
                    liste[-1][i] += 1
        else:
            t = None
    return keys, locks
def check(k,l):
    for i,ii in zip(k,l):
        if i+ii > 5:
            return False
    return True
keys, locks = parse(filename='input.txt')
print(keys)
print(locks)
cnt = 0
for k in keys:
    for l in locks:
        if check(k,l):
            cnt += 1
print(cnt)