def parse():
    with open('input.txt','r') as f:
        return f.read().split('\n')[:-1]

grid = parse()
beams = set()
beams.add(grid[0].index('S'))
# beams = [grid[0].index('S')]
# print(beams)
split = 0
for line in grid:
    newbeams = set()
    for beam in beams:
        if line[beam] == '^':
            split += 1
            if beam > 0 and beam+1 < len(grid[0]):
                newbeams.add(beam-1)
                newbeams.add(beam+1)
        else:
            newbeams.add(beam)
    beams = newbeams
# print(len(beams))
print(split)