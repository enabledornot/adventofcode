def parse():
    with open('input.txt','r') as f:
        return f.read().split('\n')[:-1]

grid = parse()
beams = set()
beams.add(grid[0].index('S'))
# beams = [grid[0].index('S')]
# print(beams)
split = 0
counts = {}
counts[str(grid[0].index('S'))] = 1
for line in grid:
    newbeams = set()
    newcounts = {}
    for beam in beams:
        if line[beam] == '^':
            split += 1
            if beam > 0 and beam+1 < len(grid[0]):
                if beam-1 in newbeams:
                    newcounts[str(beam-1)] += counts[str(beam)]
                else:
                    newbeams.add(beam-1)
                    newcounts[str(beam-1)] = counts[str(beam)]
                if beam+1 in newbeams:
                    newcounts[str(beam+1)] += counts[str(beam)]
                else:
                    newbeams.add(beam+1)
                    newcounts[str(beam+1)] = counts[str(beam)]
        else:
            if beam in newbeams:
                newcounts[str(beam)] += counts[str(beam)]
            else:
                newbeams.add(beam)
                newcounts[str(beam)] = counts[str(beam)]
    beams = newbeams
    counts = newcounts
# print(len(beams))
print(split)
print(counts)
tot = 0
for count in counts:
    tot += counts[count]
print(tot)