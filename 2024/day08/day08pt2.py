import itertools
with open("input.txt") as f:
    data = f.read().split("\n")[:-1]

antennas = {}
for i,line in enumerate(data):
    for ii,c in enumerate(line):
        if c != '.':
            if c not in antennas:
                antennas[c] = []
            antennas[c].append((i,ii))
def isValid(an,data):
    return an[0] >= 0 and an[1] >= 0 and an[0] < len(data) and an[1] < len(data[0])
def find_antinodes2(antenna0,antenna1,data):
    andes = []
    # current_node = [antenna0[0]-antenna1[0]+antenna0[0],antenna0[1]-antenna1[1]+antenna0[1]]
    current_node = list(antenna0)
    while isValid(current_node,data):
        andes.append(tuple(current_node))
        current_node[0]+=-antenna1[0]+antenna0[0]
        current_node[1]+=-antenna1[1]+antenna0[1]
    
    # antinode0 = (antenna0[0]-antenna1[0]+antenna0[0],antenna0[1]-antenna1[1]+antenna0[1])
    # current_node = [antenna1[0]-antenna0[0]+antenna1[0],antenna1[1]-antenna0[1]+antenna1[1]]
    current_node = list(antenna1)
    while isValid(current_node,data):
        andes.append(tuple(current_node))
        current_node[0]+=-antenna0[0]+antenna1[0]
        current_node[1]+=-antenna0[1]+antenna1[1]
    return andes
def find_antinodes(antennas,data):
    antinodes = []
    for i,a0 in enumerate(antennas):
        for a1 in antennas[i+1:]:
            print(f"{a0}-{a1}")
            # if a0 == a1:
            #     continue
            antinodes += find_antinodes2(a0,a1,data)
    new_antinodes = []
    for an in antinodes:
        new_antinodes.append(an)
    return new_antinodes
antinode_set = set()
for frequency in antennas:
    # print(frequency)
    # print(len(antennas[frequency]))
    for an in find_antinodes(antennas[frequency],data):
        if an not in antinode_set:
            antinode_set.add(an)
    # break
# print(len(antinode_set))
for i,line in enumerate(data):
    for ii,c in enumerate(line):
        if (i,ii) in antinode_set:
            print("#",end="")
        else:
            print(c,end="")
    print("")
print(len(antinode_set))