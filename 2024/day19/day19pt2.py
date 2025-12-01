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
        return 1
    cnt = 0
    for towel in towels:
        if len(towel) <= len(design):
            if design[:len(towel)] == towel:
                cnt += tryDesign(design[len(towel):], towels)
    return cnt

towels, designs = parse()
cnt = 0
for design in tqdm(designs):
    cnt += tryDesign(design,tuple(towels))
print(cnt)
# print(towels)
# print(designs)