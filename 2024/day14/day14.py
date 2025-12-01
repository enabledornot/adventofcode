class Robot:
    def __init__(self,string):
        spt = string.split(" ")
        self.sp = spt[0][2:].split(",")
        self.sp[0] = int(self.sp[0])
        self.sp[1] = int(self.sp[1])
        self.cp = self.sp.copy()
        self.v = spt[1][2:].split(",")
        self.v[0] = int(self.v[0])
        self.v[1] = int(self.v[1])
    def __str__(self):
        pstr = f"{self.cp[0]},{self.cp[1]}"
        vstr = f"{self.v[0]},{self.v[1]}"
        return f"p={pstr} v={vstr}"
    def __repr__(self):
        return self.__str__()
    def move(self,amnt):
        self.cp[0] = (self.cp[0] + (self.v[0] * amnt)) % 101
        self.cp[1] = (self.cp[1] + (self.v[1] * amnt)) % 103
def parse(filename='input.txt'):
    with open(filename,"r") as f:
        splitt = f.read().split("\n")[:-1]
    robots = []
    for line in splitt:
        robots.append(Robot(line))
    return robots
def countRobots(robots):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for r in robots:
        if r.cp[0] < 50 and r.cp[1] < 51:
            q1 += 1
        if r.cp[0] > 50 and r.cp[1] < 51:
            q2 += 1
        if r.cp[0] > 50 and r.cp[1] > 51:
            q3 += 1
        if r.cp[0] < 50 and r.cp[1] > 51:
            q4 += 1
    return q1 * q2 * q3 * q4

robots = parse()
for robot in robots:
    robot.move(100)
count = countRobots(robots)
print(count)