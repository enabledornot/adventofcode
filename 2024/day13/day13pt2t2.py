import math
def parse():
    with open('input.txt',"r") as f:
        data = f.read().split('\n\n')
    parsed_data = []
    for part in data:
        splitdata = part.split('\n')
        splita = splitdata[0].split("+")
        xa = int(splita[1].split(",")[0])
        ya = int(splita[2])
        splitb = splitdata[1].split("+")
        xb = int(splitb[1].split(",")[0])
        yb = int(splitb[2])
        splitp = splitdata[2].split("=")
        xp = int(splitp[1].split(",")[0])
        yp = int(splitp[2])
        parsed_data.append({
            "xa": xa,
            "ya": ya,
            "xb": xb,
            "yb": yb,
            "xp": xp + 10000000000000,
            "yp": yp + 10000000000000
        })
    return parsed_data
def check(n):
    return math.isclose(n, round(n,6))
def findB(p):
    # print(p)
    # top = p['yp'] - ((p['ya']*p['xp'])/p['xa'])
    # mtop = (p['ya']*p['xp']) % p['xa']
    # bottom = p['yb'] - ((p['ya']*p['xb'])/p['xa'])
    # mbottom = (p['ya']*p['xb']) % p['xa']
    # result = top/bottom
    # if mbottom != 0 and mtop % mbottom != 0:
    #     return
    top = (p['yp']*p['xa']) - (p['ya']*p['xp'])
    bottom = (p['yb']*p['xa']) - (p['ya'] * p['xb'])
    if top % bottom != 0:
        return
    return top / bottom
def btoa(b,pdp):
    if (pdp['xp']-(pdp['xb']*b)) % pdp['xa'] != 0:
        return
    return ((pdp['xp']-(pdp['xb']*b))/pdp['xa'])
pd = parse()
cnt = 0
for p in pd:
    b = findB(p)
    print(b)
    if b:
        a = btoa(b,p)
        print(a)
        if b >= 0 and a and a >= 0:
            print(round(3*a + b))
            cnt += round(3*a + b)
    print("")
print(cnt)