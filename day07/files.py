class fsobj:
    def __init__(self,fname, fparent, isFile, fileSize):
        self.name = fname
        self.parent = fparent
        self.isFile = isFile
        self.fileSize = fileSize
        self.fileList = []
    def calculateSize(self):
        if(self.isFile):
            return self.fileSize
        sum = 0
        for i in self.fileList:
            sum+=i.calculateSize()
        return sum
    def searchFor(self, key):
        for i in self.fileList:
            if(i.name == key):
                return i
        return None
    def createSubfile(self, fname, isFile, fileSize):
        searchRslt = self.searchFor(fname)
        if(searchRslt==None):
            newfobj = fsobj(fname, self, isFile, fileSize)
            self.fileList.append(newfobj)
        else:
            newfobj = searchRslt
        return newfobj
    def __str__(self):
        return self.name
    def returnAllDirsofSize(self, maxSize):
        if(self.calculateSize()<=maxSize):
            liste = [self]
        else:
            liste = []
        for dir in self.fileList:
            if not dir.isFile:
                liste+=dir.returnAllDirsofSize(maxSize)
        return liste

file = open("input.txt","r")
data = file.read().split("\n")
root = fsobj("/",None,False,0)
current = root
for i in data:
    if(i.startswith("$ cd ")):
        dirName = i[5:]
        if(dirName==".."):
            current = current.parent
        elif(dirName!="/"):
            current = current.searchFor(dirName)
    elif(i.startswith("dir ")):
        fileName = i[4:]
        current.createSubfile(fileName, False, 0)
    elif(i.startswith("$ ls")):
        None
    else:
        cnt = int(i.split(" ")[0])
        fileName = i.split(" ")[1]
        # print("FILE")
        # print(cnt)
        # print(fileName)
        current.createSubfile(fileName, True, cnt)
# Part 1
offiles = root.returnAllDirsofSize(100000)
sum = 0
for i in offiles:
    # print(i)
    # print(i.calculateSize())
    sum+=i.calculateSize()
print(sum)
# Part 2
total = root.calculateSize()
minSize = 40000000-total
offiles = root.returnAllDirsofSize(100000000000000)
offiles.sort(key = lambda x: x.calculateSize())
answer = 0
for i in offiles:
    answer = i.calculateSize()
    if i.calculateSize()>(minSize*-1):
        break
print(answer)