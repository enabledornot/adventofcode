from tqdm import tqdm
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
            "xp": xp,
            "yp": yp
        })
    return parsed_data
def atob(a,pdp):
    # return (pdp['ya']*a) + (pdp['yb']*((pdp['xp']-(pdp['xa']*a))/pdp['xb']))
    return ((pdp['xp']-(pdp['xa']*a))/pdp['xb'])
def testCrane(a,b,pdp):
    xf = a*pdp['xa'] + b*pdp['xb']
    yf = a*pdp['ya'] + b*pdp['yb']
    return (
        xf == pdp['xp'] and yf == pdp['yp'],
        xf,
        yf,
        (3*a) + b
    )
def solveInst(pdp):
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
pd = parse()
tot = 0
# solveInst(pd[0])
for pdp in tqdm(pd):
    tot+=solveInst(pdp)
    # print(tot)
print(int(tot))