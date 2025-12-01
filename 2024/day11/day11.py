from tqdm import tqdm
with open("input.txt","r") as f:
    data = f.read().split('\n')[0]
stones = []
for s in data.split(' '):
    stones.append(int(s))

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
for i in tqdm(range(25)):
    stones = applyStones(stones)
print(len(stones))