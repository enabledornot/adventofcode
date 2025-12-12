import numpy as np
from functools import lru_cache
import heapq
from tqdm import tqdm
# I may or may not have taken a peak online for this one
def process_shape(shape_str):
    coords = []
    for i,line in enumerate(shape_str.split('\n')[1:]):
        for j,c in enumerate(line):
            if c == '#':
                coords.append((i-1,j-1))
    shape_orientals = []
    return len(coords)
def parse_space(space_str):
    dim, counts = space_str.split(": ")
    
def parse():
    shapes = []
    with open('input.txt','r') as f:
        p0, p1, p2, p3, p4, p5, spaces = f.read().split('\n\n')
        shapes.append(process_shape(p0))
        shapes.append(process_shape(p1))
        shapes.append(process_shape(p2))
        shapes.append(process_shape(p3))
        shapes.append(process_shape(p4))
        shapes.append(process_shape(p5))
    present_spaces = []
    for space_str in spaces.split('\n')[:-1]:
        present_spaces.append(Space(space_str))
    return shapes, present_spaces

class Space:
    def __init__(self, space_str):
        dim, counts = space_str.split(': ')
        sdim = dim.split('x')
        self.dim = (int(sdim[0]),int(sdim[1]))
        self.counts = [int(x) for x in counts.split(" ")]

def applyOffset(shapeID, i ,j ):
    setPoints = set()
    for p in presents.shape_from_id(shapeID):
        setPoints.add((p[0]+i,p[1]+j))
    return setPoints

def is_valid_space(present):
    cell_count = present.dim[0]*present.dim[1]
    tot = 0
    for i, pc in enumerate(present.counts):
        tot += pc * shape_counts[i]
    return cell_count > tot

shape_counts, present_spaces = parse()
# # print(presents.id_to_present)
# # print(presents.id_to_shape_points)
cnt = 0
for present_space in tqdm(present_spaces):
    if is_valid_space(present_space):
        cnt += 1
    # break
print(cnt)

# print(is_valid_space(Space("5x5: 1 0 1 0 5 2")))