import numpy as np
from functools import lru_cache
import heapq
from tqdm import tqdm

def process_shape(shape_str):
    coords = []
    for i,line in enumerate(shape_str.split('\n')[1:]):
        for j,c in enumerate(line):
            if c == '#':
                coords.append((i-1,j-1))
    shape_orientals = []
    for i in range(8):
        shape_orientals.append(set())
    for coord in coords:
        x, y = coord
        shape_orientals[0].add((x,y))
        shape_orientals[1].add((-y,x))
        shape_orientals[2].add((-x,-y))
        shape_orientals[3].add((y,-x))
        shape_orientals[4].add((x,-y))
        shape_orientals[5].add((-x,y))
        shape_orientals[6].add((y,x))
        shape_orientals[7].add((-y,-x))
    all_shape = set()
    for so in shape_orientals:
        all_shape.add(frozenset(so))
    return all_shape
def parse_space(space_str):
    dim, counts = space_str.split(": ")
    
def parse():
    shapes = []
    with open('test.txt','r') as f:
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
    return Presents(shapes), present_spaces

class Space:
    def __init__(self, space_str):
        dim, counts = space_str.split(': ')
        sdim = dim.split('x')
        self.dim = (int(sdim[0]),int(sdim[1]))
        self.counts = [int(x) for x in counts.split(" ")]

class Presents:
    def __init__(self, shapes):
        self.id_to_present = [-1]
        self.id_to_shape_points = [set()]
        for i, so in enumerate(shapes):
            for j, shpe in enumerate(so):
                self.id_to_present.append(i)
                self.id_to_shape_points.append(shpe)
        self.size = len(self.id_to_present)
    def present_from_id(self,id):
        return self.id_to_present[id]
    def shape_from_id(self,id):
        return self.id_to_shape_points[id]
class Counter:
    def __init__(self, lowr_IJ, uppr_IJ):
        self.lowr_IJ = lowr_IJ
        self.uppr_IJ = uppr_IJ
        self.i = lowr_IJ[0]
        self.j = lowr_IJ[1]
        self.ij = (self.i,self.j)
    def inc(self):
        if self.i == self.uppr_IJ[0]-1:
            if self.j == self.uppr_IJ[1]-1:
                return False
            self.j += 1
            self.i = self.lowr_IJ[0]
        else:
            self.i += 1
        self.ij = (self.i, self.j)
        return True
    def dec(self):
        if self.i == self.lowr_IJ[0]:
            if self.j == self.lowr_IJ[1]:
                return False
            self.j -= 1
            self.i = self.uppr_IJ[0]-1
        else:
            self.i -= 1
        self.ij = (self.i, self.j)
        return True

# @lru_cache(maxsize=None)
# def is_valid_grid(grid_bytes):
#     grid = np.frombuffer(grid_bytes, np.int32).reshape((5,5))
#     if len(grid) != 5:
#         print('error')
#     otherPoints = set()
#     for i in range(5):
#         for j in range(5):
#             if (i,j) != (2,2):
#                 if grid[i,j] > 0:
#                     for p in presents.shape_from_id(grid[i,j]):
#                         otherPoints.add((p[0]+i-2,p[1]+j-2))
#     if otherPoints.intersection(presents.shape_from_id(grid[2,2])):
#         return False
#     else:
#         return True
def applyOffset(shapeID, i ,j ):
    setPoints = set()
    for p in presents.shape_from_id(shapeID):
        setPoints.add((p[0]+i,p[1]+j))
    return setPoints

@lru_cache(maxsize=None)
def is_valid_space_rec(vertEdge, vOffset, remaining, width):
    # print(vertEdge)
    # print(vOffset)
    # print(remaining)
    # print(width)
    # print("")
    if all(x == 0 for x in remaining):
        return True
    collision_map = set()
    for i in range(len(vertEdge)):
        if vertEdge[i] != 0:
            collision_map = collision_map.union(applyOffset(vertEdge[i],i,vOffset[i]))
    print(collision_map)
    for offset in range(1,4):
        for i in range(len(vertEdge)):
            for shapeID in range(presents.size):
                if remaining[presents.present_from_id(shapeID)] > 0 and vOffset[i]+offset < width and (not collision_map.intersection(applyOffset(shapeID,i,vOffset[i]+offset))):
                    newVertEdge = list(vertEdge)
                    newVOffset = list(vOffset)
                    newRemaining = list(remaining)
                    newVertEdge[i] = shapeID
                    newVOffset[i] = vOffset[i]+offset
                    newRemaining[presents.present_from_id(shapeID)] -= 1
                    if is_valid_space_rec(tuple(newVertEdge),tuple(newVOffset),tuple(newRemaining),width):
                        return True
    return False

def is_valid_space(space):
    space.dim
    return is_valid_space_rec(tuple([0]*(space.dim[0]-2)),tuple([0]*(space.dim[0]-2)),tuple(space.counts),space.dim[1]-1)

presents, present_spaces = parse()
# # print(presents.id_to_present)
# # print(presents.id_to_shape_points)
# cnt = 0
for present_space in tqdm(present_spaces):
    if is_valid_space(present_space):
        print('yoy')
        cnt += 1
    else:
        print('nay')
    # break
# print(cnt)

print(is_valid_space(Space("5x5: 1 0 1 0 5 2")))