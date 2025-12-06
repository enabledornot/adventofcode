def fix(a):
    asplit = a.split()
    return asplit
def parse():
    with open('input.txt',"r") as f:
        # print(len(f.read().split('\n')))
        a, b, c, d, symbol = f.read().split('\n')[:-1]
        # d = ''*len(a)
        # return fix(a), fix(b), fix(c), fix(d), fix(symbol)
        return a, b, c, d, symbol
def evalSlices(a, b, c, d, op):
    # print('\''+a+'\'')
    nums = []
    cid = 0
    while cid < len(a):
        newNum = 0
        try:
            newNum += int(a[cid])
            newNum *= 10
        except:
            pass
        try:
            newNum += int(b[cid])
            newNum *= 10
        except:
            pass
        try:
            newNum += int(c[cid])
            newNum *= 10
        except:
            pass
        try:
            newNum += int(d[cid])
            newNum *= 10
        except:
            pass
        newNum /= 10
        newNum = int(newNum)
        if newNum == 0:
            break
        nums.append(newNum)
        cid += 1
    print('---------------------------------------------')
    print(f"\'{a}\'")
    print(f"\'{b}\'")
    print(f"\'{c}\'")
    print(f"\'{d}\'")
    print(op)
    print(nums)
    if op == '+':
        r = 0
        for num in nums:
            r += num
        return r
    else:
        r = 1
        for num in nums:
            r *= num
        return r
a, b, c, d, symbol = parse()
o = []
for i, cn in enumerate(symbol):
    if cn in ['*','+']:
        o.append(i)
tot = 0
print(c)
for i in range(len(o)-1):
    res = evalSlices(a[o[i]:o[i+1]-1],b[o[i]:o[i+1]-1],c[o[i]:o[i+1]-1],d[o[i]:o[i+1]-1],symbol[o[i]])
    print(res)
    tot += res
res = evalSlices(a[o[-1]:],b[o[-1]:],c[o[-1]:],d[o[-1]:],symbol[o[-1]])
print(res)
tot += res
print(tot)
# a, b, c, d, symbol = parse()
# print(a.split(' ').remove(''))
# tot = 0
# for i in range(len(a)):
#     if symbol[i] == '+':
#         tot += int(a[i]) + int(b[i]) + int(c[i]) + int(d[i])
#     else:
#         tot += int(a[i]) * int(b[i]) * int(c[i]) * int(d[i])
# print(tot)