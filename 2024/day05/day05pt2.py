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
def check_pairs_fix(updateg,pairs):
    update = updateg.copy()
    swapped = True
    while swapped:
        swapped = False
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
                tmp = update[l2]
                update[l2] = update[l1]
                update[l1] = tmp
                swapped = True
    return update
sum = 0
for update in updates:
    if not check_pairs(update, pairs):
        newUpdate = check_pairs_fix(update, pairs)
        sum += int(newUpdate[math.floor(len(newUpdate)/2)])
        # sum += int(update[math.floor(len(update)/2)])
print(sum)