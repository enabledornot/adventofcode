def parse(input='input.txt'):
    with open(input,"r") as f:
        data = f.read()
    return data

data = parse()

cmd_start = 'mul('
cstr = 0
numA = 0
numB = 0
prod_all = 0
mul_en = True
do_inst = 'do()'
dont_inst = 'don\'t()'
dnt_cnt = 0
for c in data:
    if mul_en:
        if dont_inst[dnt_cnt] == c:
            dnt_cnt += 1
            if dnt_cnt == 7:
                dnt_cnt = 0
                mul_en = False
        else:
            dnt_cnt = 0
        if cstr == 4:
            numA = 0
            numB = 0
            cstr += 1
        if cstr == 5:
            if c == ',':
                cstr += 1
            else:
                try:
                    numA = (numA * 10) + int(c)
                except:
                    cstr = 0
        elif cstr == 6:
            if c == ')':
                cstr = 0
                prod_all += numA * numB
            else:
                try:
                    numB = (numB * 10) + int(c)
                except:
                    cstr = 0
        elif cmd_start[cstr] == c:
            cstr += 1
        else:
            cstr = 0
    else:
        if do_inst[dnt_cnt] == c:
            dnt_cnt += 1
            if dnt_cnt == 4:
                dnt_cnt = 0
                mul_en = True
        else:
            dnt_cnt = 0
print(prod_all)