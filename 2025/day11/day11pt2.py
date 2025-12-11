from functools import lru_cache

def parse():
    mappings = {}
    with open('input.txt','r') as f:
        for line in f.read().split('\n')[:-1]:
            left, right = line.split(": ")
            mappings[left] = tuple(right.split(" "))
    return mappings
@lru_cache(maxsize=None)
def count_paths_rec(current, depth, dest, banned):
    if depth > 18:
        return []
    # newprev = set(previous)
    # newprev.add(current)
    # newprev_tup = tuple(newprev)
    valid_paths = []
    for path in mappings[current]:
        if path == dest:
            # print('end')
            valid_paths.append(tuple([dest]))
        elif path not in banned:
            for mapp in count_paths_rec(path, depth+1, dest, banned):
                mapset = set(mapp)
                if path not in mapset:
                    mapset.add(path)
                    valid_paths.append(tuple(mapset))
    return valid_paths
def count_paths(src, dest, banned=tuple('out')):
    # return count_paths_rec(src,tuple([src, 'out']), dest, 0)
    return len(count_paths_rec(src, 0, dest, banned))
def find_max_depth():
    foundSet = set(['svr'])
    current = ['svr']
    depth = 0
    while len(current) != 0:
        newcurrent = []
        for cur in current:
            if cur == 'out':
                continue
            for path in mappings[cur]:
                if path not in foundSet:
                    foundSet.add(path)
                    newcurrent.append(path)
        depth += 1
        current = newcurrent
    return depth
mappings = parse()
print(find_max_depth())
# asdf
svr_fft = count_paths('svr','fft', banned=tuple(['out','fft','dac']))
print(svr_fft)
svr_dac = count_paths('svr','dac', banned=tuple(['out','fft','dac']))
print(svr_dac)
fft_dac = count_paths('fft','dac', banned=tuple(['out','fft','dac']))
print(fft_dac)
fft_out = count_paths('fft','out', banned=tuple(['out','fft','dac']))
print(fft_out)
dac_out = count_paths('dac','out', banned=tuple(['out','fft','dac']))
print(dac_out)

print("")
print(svr_fft*fft_dac*dac_out)