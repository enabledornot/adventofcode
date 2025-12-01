class Counter:
    def __init__(self):
        self.cnt_dict = {}
    def check_and_add(self,id):
        if id not in self.cnt_dict:
            self.cnt_dict[id] = {
                "fence": 0,
                "plants": 0
            }
    def inc_fence(self,id):
        self.check_and_add(id)
        self.cnt_dict[id]['fence'] += 1
    def inc_plants(self,id):
        self.check_and_add(id)
        self.cnt_dict[id]['plants'] += 1
    def calculate_score(self):
        score = 0
        for p in self.cnt_dict:
            if p == 1:
                continue
            score += self.cnt_dict[p]['fence'] * self.cnt_dict[p]['plants'] 
        return score
def pad_data(data):
    newdata = []
    newdata.append("."*(len(data[0]) + 2))
    for line in data:
        newdata.append("." + line + ".")
    newdata.append("."*(len(data[0]) + 2))
    return newdata
def countFence(data):
    counts = Counter()
    for l1, l2 in zip(data[:-1],data[1:]):
        # print(l1)
        # print(l2)
        # print("")
        for c1, c2 in zip(l1,l2):
            if c1 != c2:
                counts.inc_fence(c1)
                counts.inc_fence(c2)
            counts.inc_plants(c1)
    for i in range(len(data[0])-1):
        for ii in range(len(data)):
            c1 = data[ii][i]
            c2 = data[ii][i+1]
            # print(c1,end="")
            # print(c2,end="")
            # print(" ",end="")
            if c1 != c2:
                counts.inc_fence(c1)
                counts.inc_fence(c2)
        # print("")
    print(counts.cnt_dict)
    return counts.calculate_score()
def findNewPoints(data,cpoint):
    newp = []
    for offset in [[-1,0],[1,0],[0,1],[0,-1]]:
        potential = cpoint.copy()
        potential[0] += offset[0]
        potential[1] += offset[1]
        if potential[0] >= 0 and potential[0] < len(data) and potential[1] >= 0 and potential[1] < len(data[0]):
            newp.append(potential)
    return newp
def rec_explore(data, e_value,n_value, p):
    if data[p[0]][p[1]] != e_value:
        return
    data[p[0]][p[1]] = n_value
    for newPoint in findNewPoints(data,p):
        rec_explore(data, e_value, n_value, newPoint)
def numberize_data(data):
    indx_cnt = 1
    for i in range(len(data)):
        for ii in range(len(data[i])):
            currentPoint = [i,ii]
            currentValue = data[i][ii]
            if isinstance(currentValue,str):
                rec_explore(data,currentValue,indx_cnt,currentPoint)
                indx_cnt += 1
with open("input.txt","r") as f:
    data0 = f.read().split("\n")[:-1]
data = []
for line in pad_data(data0):
    data.append([])
    for c in line:
        data[-1].append(c)
numberize_data(data)
for line in data:
    print(line)
rslt = countFence(data)
print(rslt)