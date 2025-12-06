def fix(a):
    asplit = a.split()
    return asplit
def parse():
    with open('input.txt',"r") as f:
        # print(len(f.read().split('\n')))
        a, b, c, d, symbol = f.read().split('\n')[:-1]
        return fix(a), fix(b), fix(c), fix(d), fix(symbol)

a, b, c, d, symbol = parse()
# print(a.split(' ').remove(''))
tot = 0
for i in range(len(a)):
    if symbol[i] == '+':
        tot += int(a[i]) + int(b[i]) + int(c[i]) + int(d[i])
    else:
        tot += int(a[i]) * int(b[i]) * int(c[i]) * int(d[i])
print(tot)