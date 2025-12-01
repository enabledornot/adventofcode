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
startingNumbers = parse()
sum = 0
for number in tqdm(startingNumbers):
    for _ in range(2000):
        number = generateNextNumber(number)
    sum += number
print(sum)