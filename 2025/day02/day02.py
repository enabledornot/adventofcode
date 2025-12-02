def parse():
    output = []
    with open("input.txt","r") as f:
        for rng in f.read().split(','):
            l, u = rng.split('-')
            output.append(tuple([int(l),int(u)]))
            # output.append(tuple[l,u])
    return output
def dupeNum(n):
    return int(str(n)+str(n))
def generate_special(rng):
    try:
        fhalf = int(str(rng[0])[:int((len(str(rng[0])))/2)])
        print(f"{rng}-{fhalf}")
    except:
        fhalf = int(str(rng[0])[:int(((len(str(rng[0])))/2)+1)])
    while dupeNum(fhalf) < rng[0]:
        fhalf += 1
    dupeset = set()
    while dupeNum(fhalf) <= rng[1]:
        dupeset.add(dupeNum(fhalf))
        fhalf += 1
    return dupeset
data = parse()

duplicate = set()
print(data)
for rng in data:
    newset = generate_special(rng)
    print(newset)
    duplicate = duplicate | newset
sum = 0
for item in duplicate:
    sum += item
print(sum)