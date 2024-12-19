from tqdm import tqdm
from functools import cache
def parse(input='input.txt'):
    with open(input,"r") as f:
        data = f.read().split('\n')
    towels = data[0].split(', ')
    designs = data[2:-1]
    return towels, designs
@cache
def tryDesign(design, towels):
    if len(design) == 0:
        return True
    for towel in towels:
        if len(towel) <= len(design):
            if design[:len(towel)] == towel:
                if tryDesign(design[len(towel):], towels):
                    return True
    return False

towels, designs = parse()
cnt = 0
for design in tqdm(designs):
    if tryDesign(design,tuple(towels)):
        cnt+=1
print(cnt)
# print(towels)
# print(designs)