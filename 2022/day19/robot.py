import sys
import math
import tqdm
import multiprocessing
import time
def parse(fname):
    with open(fname, "r") as f:
        data = f.read().split("\n")
    ndata = []
    for line in data:
        split = line.split(" ")
        ndata.append([0,0,0,0])
        ndata[-1][0] = (int(split[6]),0,0)
        ndata[-1][1] = (int(split[12]),0,0)
        ndata[-1][2] = (int(split[18]),int(split[21]),0)
        ndata[-1][3] = (int(split[27]),0,int(split[30]))
    return ndata
class maxGeodesCached:
    def __init__(self, cost):
        self.costs = cost
        self.cache = []
        while len(self.cache)<=24:
            self.cache.append({})
        self.best = 0
        self.hit = 0
        self.miss = 0
    def possibleMax(self, max):
        if self.best < max:
            self.best = max
            # print(max)
    def maxGeodesU(self, resourceCount, robotCount, timeLeft):
        if timeLeft==0:
            return 0
        updatedResource = resourceCount.copy()
        for i in range(3):
            updatedResource[i]+=robotCount[i]
        max = []
        if self.costs[3][0] <= resourceCount[0] and self.costs[3][2] <= resourceCount[2]:
            possible = self.maxGeodes([updatedResource[0]-self.costs[3][0],updatedResource[1],updatedResource[2]-self.costs[3][2]],[robotCount[0],robotCount[1],robotCount[2],robotCount[3]+1],timeLeft-1)
            self.possibleMax(possible+robotCount[3])
            return possible + robotCount[3]
        if self.costs[0][0] <= resourceCount[0]:
            possible = self.maxGeodes([updatedResource[0]-self.costs[0][0],updatedResource[1],updatedResource[2]],[robotCount[0]+1,robotCount[1],robotCount[2],robotCount[3]],timeLeft-1)
            max.append(possible)
        if self.costs[1][0] <= resourceCount[0]:
            possible = self.maxGeodes([updatedResource[0]-self.costs[1][0],updatedResource[1],updatedResource[2]],[robotCount[0],robotCount[1]+1,robotCount[2],robotCount[3]],timeLeft-1)
            max.append(possible)
        if self.costs[2][0] <= resourceCount[0] and self.costs[2][1] <= resourceCount[1]:
            possible = self.maxGeodes([updatedResource[0]-self.costs[2][0],updatedResource[1]-self.costs[2][1],updatedResource[2]],[robotCount[0],robotCount[1],robotCount[2]+1,robotCount[3]],timeLeft-1)
            max.append(possible)
        if len(max)!=3:
            newMax = self.maxGeodes(updatedResource, robotCount, timeLeft-1)
            max.append(newMax)
        max.sort(reverse=True)
        self.possibleMax(max[0]+robotCount[3])
        return max[0] + robotCount[3]
    def maxGeodes(self, resourceCount, robotCount, timeLeft):
        key = str([resourceCount, robotCount])
        if not (key in self.cache[timeLeft]):
            self.cache[timeLeft][key] = self.maxGeodesU(resourceCount, robotCount, timeLeft)
        return self.cache[timeLeft][key]
def getAnswer(costs):
    mgc = maxGeodesCached(costs)
    return mgc.maxGeodes([0,0,0], [1,0,0,0], 24)
def threadHandle(costs, answers,lock):
    # print("Thread Start")
    while True:
        current = 0
        lock.acquire()
        while current<len(answers) and answers[current]!=-2:
            current+=1
        # print(current)
        if current==len(answers):
            lock.release()
            break
        answers[current] = -1
        lock.release()
        answers[current] = getAnswer(costs[current])
    print("thread exiting")
if __name__=="__main__":
    sys.setrecursionlimit(50000000)
    costs = parse("input.txt")
    threads = []
    answers = multiprocessing.Array('i',len(costs))
    for i in range(len(costs)):
        answers[i] = -2
    lock = multiprocessing.Lock()
    for i in range(5):
        threads.append(multiprocessing.Process(target=threadHandle, args=(costs,answers,lock)))
    for thread in threads:
        thread.start()
    print("starting processes")
    done = 0
    for i in tqdm.tqdm(range(len(answers))):
        while done<=i:
            done = 0
            for ans in answers:
                if ans>=0:
                    done+=1
            # print(answers)
            time.sleep(1)
    # for thread in threads:
    #     thread.join()
    cnt = 1
    score = 0
    for answer in answers:
        score+= answer*cnt
        cnt+=1
    print("SCORE")
    print(score)