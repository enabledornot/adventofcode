from tqdm import tqdm
def parse(filename='input.txt'):
    with open(filename,"r") as f:
        data = f.read().split('\n')[:-1]
    newdata = []
    for i in data:
        newdata.append(int(i))
    return newdata
def generateNextNumber(number):
    number = ((number * 64) ^ number) % 16777216
    number = (int(number/32) ^ number) % 16777216
    number = ((number * 2048) ^ number) % 16777216
    return number
def generateSequences():
    sequences = []
    for a in range(-9,10):
        for b in range(-9,10):
            for c in range(-9,10):
                for d in range(-9,10):
                    sequences.append((a,b,c,d))
    return sequences
def computeDifferences(number):
    numbers = [number % 10]
    differences = []
    for _ in range(2000):
        number = generateNextNumber(number)
        numbers.append(number % 10)
        differences.append(numbers[-1] - numbers[-2])
    return numbers, differences
def computeFirstSeqGrid(number):
    n, d = computeDifferences(number)
    firstSeqValue = {}
    for i in range(4,len(n)):
        seq = tuple(d[i-4:i])
        if seq not in firstSeqValue:
            firstSeqValue[seq] = n[i]
    return firstSeqValue
startingNumbers = parse(filename='input.txt')
fsvsum = {}
for number in tqdm(startingNumbers):
    fsv = computeFirstSeqGrid(number)
    for p in fsv:
        if p not in fsvsum:
            fsvsum[p] = fsv[p]
        else:
            fsvsum[p] += fsv[p]
m = 0
mkey = ""
for p in fsvsum:
    if fsvsum[p] > m:
        m = fsvsum[p]
        mkey = p
print(mkey)
print(m)