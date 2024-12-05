import math
with open("input.txt") as f:
    data = f.read().split("\n")
doneReading = False
pairs = []
updates = []
for line in data:
    if line == "":
        doneReading = True
    elif doneReading:
        updates.append(line.split(","))
    else:
        pairs.append(tuple(line.split("|")))
def check_pairs(update,pairs):
    stillGood = True
    for p in pairs:
        try:
            l1 = update.index(p[0])
        except:
            continue
        try:
            l2 = update.index(p[1])
        except:
            continue
        if l2 < l1:
            return False
    return True
sum = 0
for update in updates:
    if check_pairs(update, pairs):
        sum += int(update[math.floor(len(update)/2)])
print(sum)