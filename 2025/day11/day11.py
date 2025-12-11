def parse():
    mappings = {}
    with open('input.txt','r') as f:
        for line in f.read().split('\n')[:-1]:
            left, right = line.split(": ")
            mappings[left] = tuple(right.split(" "))
    return mappings
def count_paths(current, previous):
    newprev = set(previous)
    newprev.add(current)
    newprev_tup = tuple(newprev)
    total_paths = 0
    for path in mappings[current]:
        if path == 'out':
            total_paths += 1
        elif path not in newprev:
            total_paths += count_paths(path, newprev_tup)
    return total_paths
mappings = parse()
result = count_paths('you',tuple([]))
print(result)