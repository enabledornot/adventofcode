def parse():
    output = []
    with open("input.txt","r") as f:
        for rng in f.read().split(','):
            l, u = rng.split('-')
            output.append(tuple([int(l),int(u)]))
            # output.append(tuple[l,u])
    return output
def dupeNum(n,divAmnt):
    out = ""
    for _ in range(divAmnt):
        out += str(n)
    return int(out)
def generate_special(rng,divAmnt):
    fhalf = 1
    while dupeNum(fhalf,divAmnt) < rng[0]:
        fhalf += 1
    dupeset = set()
    while dupeNum(fhalf,divAmnt) <= rng[1]:
        dupeset.add(dupeNum(fhalf,divAmnt))
        fhalf += 1
    return dupeset
data = parse()

duplicate = set()
print(data)
for rng in data:
    for divAmnt in range(2,100):
        newset = generate_special(rng,divAmnt)
        print(newset)
        duplicate = duplicate | newset        
print(duplicate)
sum = 0
for item in duplicate:
    sum += item
print(sum)