from tqdm import tqdm
def parse():
    output = []
    with open('input.txt','r') as f:
        for line in f.read().split('\n')[:-1]:
            x, y = line.split(',')
            output.append((int(x),int(y)))
    return sorted(output)

coordinates = parse()
# print(coordinates)
# print(len(coordinates))
maxArea = 0
for coordA in tqdm(coordinates):
    for coordB in coordinates:
        deltaX, deltaY = abs(coordA[0]-coordB[0]), abs(coordA[1]-coordB[1])
        newArea = (deltaX+1) * (deltaY+1)
        if newArea > maxArea:
            maxArea = newArea
print(maxArea)