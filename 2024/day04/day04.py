with open("input.txt","r") as f:
    data = f.read().split("\n")
class scanner():
    def __init__(self, word):
        self.search = word
        self.cdx = 0
        self.cnt = 0
        self.cbuff = []
        self.clog = []
    def scan(self,c,cords=None):
        if self.search[self.cdx] == c:
            self.cdx += 1
            if cords:
                self.cbuff.append(cords)
        else:
            self.cdx = 0
            self.cbuff = []
            if self.search[self.cdx] == c:
                self.cdx += 1
                if cords:
                    self.cbuff.append(cords)
        if self.cdx == len(self.search):
            self.cnt+=1
            self.clog = self.clog + self.cbuff
            self.cbuff = []
            self.cdx = 0
    def reset(self):
        self.cdx = 0
        self.cbuff = []
search = scanner('XMAS')
logged_points = []
cdx = 0
cnt = 0
# search horizontal
for (i,line) in enumerate(data):
    for (ii,c) in enumerate(line):
        search.scan(c,(i,ii))
    search.reset()
    for (ii,c) in reversed(list(enumerate(line))):
        search.scan(c,(i,ii))
    search.reset()
# search vertical
for ii in range(len(data[0])):
    for i in range(len(data)):
        c = data[i][ii]
        search.scan(c,(i,ii))
    search.reset()
    for i in reversed(range(len(data))):
        c = data[i][ii]
        search.scan(c,(i,ii))
    search.reset()
# search horizontal
for i in range(len(data)):
    for ii in range(len(data)-i):
        c = data[i+ii][ii]
        search.scan(c,(i+ii,ii))
    search.reset()
    for ii in reversed(range(len(data)-i)):
        c = data[i+ii][ii]
        search.scan(c,(i+ii,ii))
    search.reset()
for i in range(1,len(data)):
    for ii in range(len(data)-i):
        c = data[ii][i+ii]
        search.scan(c,(ii,i+ii))
    search.reset()
    for ii in reversed(range(len(data)-i)):
        c = data[ii][i+ii]
        search.scan(c,(ii,i+ii))
    search.reset()
# horizontal other direction
for i in range(len(data)):
    for ii in range(len(data)-i):
        c = data[len(data)-i-ii-1][ii]
        search.scan(c,(len(data)-i-ii-1,ii))
    search.reset()
    for ii in reversed(range(len(data)-i)):
        c = data[len(data)-i-ii-1][ii]
        search.scan(c,(len(data)-i-ii-1,ii))
    search.reset()
for i in range(1,len(data)):
    for ii in range(len(data)-i):
        c = data[len(data)-ii-1][i+ii]
        search.scan(c,(len(data)-ii-1,i+ii))
    search.reset()
    for ii in reversed(range(len(data)-i)):
        c = data[len(data)-ii-1][i+ii]
        search.scan(c,(len(data)-ii-1,i+ii))
    search.reset()
print(search.cnt)
print(search.clog)
logged_points = search.clog
for (i,line) in enumerate(data):
    for (ii,c) in enumerate(line):
        if (i,ii) in logged_points:
            print(c,end="")
        else:
            print('.',end="")
    print("")