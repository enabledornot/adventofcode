import numpy as np
from functools import lru_cache

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
        # print('inc')
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
        # print('dec')
        if self.i == self.lowr_IJ[0]:
            if self.j == self.lowr_IJ[1]:
                return False
            self.j -= 1
            self.i = self.uppr_IJ[0]-1
        else:
            self.i -= 1
        self.ij = (self.i, self.j)
        return True

@lru_cache(maxsize=None)
def is_valid_grid(grid_bytes):
    # print(presents)
    grid = np.frombuffer(grid_bytes, np.int32).reshape((5,5))
    # print(grid)
    if len(grid) != 5:
        print('error')
    otherPoints = set()
    for i in range(5):
        for j in range(5):
            if (i,j) != (2,2):
                if grid[i,j] > 0:
                    # print(presents.shape_from_id(grid[i,j]))
                    for p in presents.shape_from_id(grid[i,j]):
                        otherPoints.add((p[0]+i-2,p[1]+j-2))
    # if len(otherPoints) > 7:
    #     print('yo')
    if otherPoints.intersection(presents.shape_from_id(grid[2,2])):
        # print(otherPoints.intersection(presents.shape_from_id(grid[2,2])))
        return False
    else:
        # print(grid)
        # print('valid')
        return True
    return False
    # if res:
    #     pass
    #     # print(grid)
    #     # print(presents.shape_from_id(grid[2,2]))
    #     # print('true')
    # else:
    #     print(otherPoints)
    return res
def is_valid_space(S):
    req = S.counts.copy()
    # req = [1,0,1,0,2,2]
    # print(req)
    # print(presents.present_from_id(23))
    # return
    # req[-1] = 0
    # req[-2] = 0
    # req[0] = 2
    # print(f"dim={S.dim}")
    space = np.zeros((S.dim[0]+2,S.dim[1]+2), dtype=np.int32)
    C = Counter((2,2),(S.dim[0],S.dim[1]))
    space[C.i,C.j] = -1
    while C.inc():
        space[C.i, C.j] = -1
    C = Counter((2,2),(S.dim[0],S.dim[1]))
    while True:
        # print(space[2:-2,2:-2])
        # print(req)
        # if C.j == 2:
        #     print(space[2:-2,2:-2])
        if space[C.ij] > 0:
            req[presents.present_from_id(space[C.ij])] += 1
        space[C.ij] += 1
        # if space[-4,-3] == 0 and space[-3,-3] == 23:
        #     print(req)
        #     print(space[2:-2,2:-2])
        if space[C.ij] == presents.size:
            space[C.ij] = -1
            if not C.dec():
                # print(C.ij)
                return False
            # else:
            #     print(C.ij)
        else:
            if space[C.ij] == 0:
                C.inc()
            else:
                # print(space[2:-2,2:-2])
                req[presents.present_from_id(space[C.ij])] -= 1
                # print(presents.present_from_id(space[C.ij]))
                if req[presents.present_from_id(space[C.ij])] >= 0 and is_valid_grid(space[C.i-2:C.i+3,C.j-2:C.j+3].tobytes()):
                    # print(req)
                    if all(x == 0 for x in req):
                        print(space[2:-2,2:-2])
                        return True
                    C.inc()
                # print(space[2:-2,2:-2])
            # print("")
    # while True:
    #     # print(f"{C.ij}->{space[C.ij]}")
    #     # print('')
    #     # if space[C.ij] > 0:
    #     #     req[presents.present_from_id(space[C.ij])] += 1
    #     space[C.ij] += 1
    #     if space[C.ij] == presents.size:
    #         space[C.ij] = 0
    #         if not C.dec():
    #             return False
    #     else:
    #         print(space[2:-2,2:-2])
    #         # print(space)
    #         print(C.ij)
    #         print(req)
    #         if space[C.ij] == 0 or req[presents.present_from_id(space[C.ij])] > 0:
    #             if space[C.ij] != 0:
    #                 req[presents.present_from_id(space[C.ij])] -= 1
    #             # print(space[2:-2,2:-2])
    #             if is_valid_grid(space[C.i-2:C.i+3,C.j-2:C.j+3].tobytes()):
    #                 # print(space[2:-2,2:-2])
    #                 # print(f"{C.ij}")
    #                 if all(x == 0 for x in req):
    #                     return True
    #                 C.inc()
    #                 # if not C.inc():
    #                 #     req[presents.present_from_id(space[C.ij])] += 1
    #                 #     space[C.ij] = 0
    #                 #     C.dec()
    #                 # else:
    #                 #     print(req)
    #                 #     print(f"good {C.ij}")

presents, present_spaces = parse()
# # print(presents.id_to_present)
# # print(presents.id_to_shape_points)
cnt = 0
for present_space in present_spaces:
    if is_valid_space(present_space):
        cnt += 1
print(cnt)

# print(is_valid_space(Space("6x6: 3 0 0 0 0 0")))