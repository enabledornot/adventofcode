from tqdm import tqdm
from functools import cache
with open("input.txt","r") as f:
    data = f.read().split('\n')[0]
stones = []
for s in data.split(' '):
    stones.append(int(s))
@cache
def getStoneCount(stone,todo=75):
    if todo == 0:
        return 1
    count = 0
    if stone == 0:
        count += getStoneCount(1,todo=todo-1)
    elif len(str(stone)) % 2 == 0:
        count += getStoneCount(int(str(stone)[:int(len(str(stone))/2)]),todo=todo-1)
        count += getStoneCount(int(str(stone)[int(len(str(stone))/2):]),todo=todo-1)
    else:
        count += getStoneCount(2024*stone,todo=todo-1)
    return count
def applyStones(startingStones):
    newStones = []
    for stone in startingStones:
        if stone == 0:
            newStones.append(1)
        elif len(str(stone)) % 2 == 0:
            newStones.append(int(str(stone)[:int(len(str(stone))/2)]))
            newStones.append(int(str(stone)[int(len(str(stone))/2):]))
        else:
            newStones.append(2024*stone)
    return newStones
total = 0
for stone in tqdm(stones):
    total += getStoneCount(stone)
print(total)