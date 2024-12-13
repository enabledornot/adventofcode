from tqdm import tqdm
def parse():
    with open('test.txt',"r") as f:
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
def gcd_euclid(a,b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = gcd_euclid(b, a % b)
    return gcd, y1, x1 - (a // b) * y1
def modInv(a,n):
    g, x, y = gcd_euclid(n % a, a)
    if g == 1:
        return x
def find_as(a,b,n):
    g = gcd_euclid(b,n)[0]
    if a % g != 0:
        return
    balt = b // g
    aalt = a // g
    nalt = n // g
    invb = modInv(balt, nalt)
    if invb is None:
        return
    x0 = (invb * aalt) % nalt
    for i in range(g):
        yield x0 + i * nalt
def atob(a,pdp):
    # return (pdp['ya']*a) + (pdp['yb']*((pdp['xp']-(pdp['xa']*a))/pdp['xb']))
    return ((pdp['xp']-(pdp['xa']*a))/pdp['xb'])
def btoa(b,pdp):
    # return (pdp['ya']*a) + (pdp['yb']*((pdp['xp']-(pdp['xa']*a))/pdp['xb']))
    return ((pdp['xp']-(pdp['xb']*b))/pdp['xa'])
def testCrane(a,b,pdp):
    xf = a*pdp['xa'] + b*pdp['xb']
    yf = a*pdp['ya'] + b*pdp['yb']
    return (
        xf == pdp['xp'] and yf == pdp['yp'],
        pdp['xp'],
        pdp['yp'],
        xf,
        yf,
        (3*a) + b
    )
def checkValids(oc,validAys,pdp,return_ab=False):
    a_b = []
    tc = 0
    while len(a_b) == 0:
        for a in validAys:
            a = a + (pdp['xb']*oc)
            b = atob(a,pdp)
            tc = testCrane(a,b,pdp)
            if tc[0]:
                a_b.append((a,int(b),(3*a)+b))
    if return_ab:
        return a_b
    return tc[4]
def solveInst(pdp):
    start = 0
    a = 0
    b = 0
    a_b = []
    validAys = []
    pdp_mod = pdp.copy()
    pdp_mod['xp'] = pdp_mod['xp'] % pdp['xb']
    pdp_mod['yp'] = pdp_mod['yp'] % pdp['yb']
    for a in range(pdp['xb']):
        b = atob(a,pdp)
        # print(testCrane(a,b,pdp_mod))
        if b - int(b) == 0:
            validAys.append(a)
    if len(validAys) == 0:
        return 0
    # validAys = list(find_as(pdp['xp'],pdp['xa'],pdp['xb']))
    print(validAys)
    oc = 1
    yp = 1000000000000000000000000000000000000
    while yp > pdp['yp']:
        yp = checkValids(oc,validAys,pdp)
        oc *= 2
    lower_oc = oc // 2
    upper_oc = oc
    while upper_oc - lower_oc > 1:
        middle_oc = (lower_oc+upper_oc) // 2
        if checkValids(middle_oc,validAys,pdp) <= pdp['yp']:
            lower_oc = middle_oc
        else:
            upper_oc = middle_oc
    rslt = []
    while len(rslt) == 0:
        rslt = checkValids(lower_oc,validAys,pdp,return_ab=True)
        lower_oc += 1
    a_b = []
    for a in rslt:
        b = atob(a,pdp)
        if b - int(b) == 0 and testCrane(a,b,pdp)[0]:
            a_b.append((a,int(b),(3*a)+b))
            # print(a_b[-1])
    if len(a_b) == 0:
        return 0
    else:
        return min([t[2] for t in a_b])
    # while a >= 0 or b >= 0:
    #     a = btoa(start,pdp)
    #     b = atob(start,pdp)
    #     if a - int(a) == 0 and testCrane(a,start,pdp)[0]:
    #         a_b.append(int(a),start,(3*a)+start)
    #     if b - int(b) == 0 and testCrane(start,b,pdp)[0]:
    #         a_b.append((start,int(b),(3*start)+b))
    #     start += 1
    if len(a_b) == 0:
        return 0
    else:
        return min([t[2] for t in a_b])
def solveInstRetro(pdp):
    a = 0
    b = 1
    a_b = []
    while b >= 0:
        
        b = atob(a,pdp)
        if b - int(b) == 0 and testCrane(a,b,pdp)[0]:
            a_b.append((a,int(b),(3*a)+b))
            # print(a_b[-1])
        a = a + 1
        # break
    # print(a_b)
    if len(a_b) == 0:
        return 0
    else:
        return min([t[2] for t in a_b])
def solveInstMod(pdpo):
    mod = (pdpo['xa'] * pdpo['xb']) + (pdpo['ya'] * pdpo['yb'])
    pdp = pdpo.copy()
    pdp['xp'] = pdp['xp'] % mod
    pdp['yp'] = pdp['yp'] % mod
    solve_mod = solveInstRetro(pdp)
    print(pdp)
    print(solve_mod)
    pdp = pdpo.copy()
    pdp['xp'] = mod
    pdp['yp'] = mod
    solve_mult = solveInstRetro(pdp)
    print(pdp)
    print(solve_mult)
    return (solve_mult * int((pdpo['xp']*pdpo['yp'])/mod)) + solve_mod
pd = parse()
tot = 0
# solveInst(pd[0])
for pdp in tqdm(pd):
    tot+=solveInstMod(pdp)
    # print(tot)
print(int(tot))