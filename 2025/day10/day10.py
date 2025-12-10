from tqdm import tqdm

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
            self.buttons.append(tuple(int(a) for a in button[1:-1].split(',')))
    def __str__(self):
        return f"{self.indicatorGoal}    {self.buttons}"
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
        cnt = 0
        lastToDo = set([(tuple([False]*len(self.indicatorGoal)),tuple(set(range(len(self.buttons)))))])
        while True:
            newToDo = []
            cnt += 1
            while lastToDo:
                currentLights, currentSet = lastToDo.pop()
                for button in currentSet:
                    newLights = list(currentLights)
                    newSet = set(currentSet)
                    newSet.remove(button)
                    if self.apply_button(newLights,button):
                        return cnt
                    newToDo.append((tuple(newLights), tuple(newSet)))
            lastToDo = newToDo


machines = parse()
tot = 0
for machine in tqdm(machines):
    res = machine.solve()
    # print(res)
    tot += res
print(tot)