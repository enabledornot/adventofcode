from tqdm import tqdm
import pulp

def parse():
    machines = []
    with open("input.txt",'r') as f:
        for line in f.read().split('\n')[:-1]:
            machines.append(Machine(line))
    return machines
class Machine:
    def __init__(self, line):
        splitLine = line.split(' ')
        self.indicatorGoal = []
        for c in splitLine[0][1:-1]:
            self.indicatorGoal.append(c == '#')
        self.buttons = []
        for button in splitLine[1:-1]:
            self.buttons.append(set(int(a) for a in button[1:-1].split(',')))
        self.joltages = tuple(int(a) for a in splitLine[-1][1:-1].split(','))
    def __str__(self):
        return f"{self.indicatorGoal}    {self.buttons}     {self.joltages}"
    def apply_button(self, lights, butID):
        # print(self)
        # print(butID)
        for flip in self.buttons[butID]:
            lights[flip] = not lights[flip]
        for a, b in zip(lights,self.indicatorGoal):
            if a != b:
                return False
        return True
    def solve(self):
        prob = pulp.LpProblem('myproblem',pulp.LpMinimize)
        variables = []
        for i, button in enumerate(self.buttons):
            variables.append(pulp.LpVariable(f"b{i}", lowBound=0, cat='Integer'))
        prob += sum(variables)
        for i, joltage in enumerate(self.joltages):
            joltSum = 0
            for j, button in enumerate(self.buttons):
                if i in button:
                    joltSum += variables[j]
            prob += joltSum == joltage
        prob.solve(pulp.PULP_CBC_CMD(msg=False))
        return int(pulp.value(prob.objective))

machines = parse()
tot = 0
for machine in tqdm(machines):
    res = machine.solve()
    # print(res)
    tot += res
print(tot)