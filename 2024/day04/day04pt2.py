with open("input.txt","r") as f:
    data = f.read().split("\n")
cnt = 0
for i in range(len(data)):
    for ii in range(len(data[i])):
        if data[i][ii] == 'A' and i != 0 and ii != 0 and i != len(data)-1 and ii != len(data)-1:
            d1 = [data[i-1][ii-1],data[i+1][ii+1]]
            d2 = [data[i-1][ii+1],data[i+1][ii-1]]
            if 'M' in d1 and 'S' in d1 and 'M' in d2 and 'S' in d2:
                cnt+=1
print(cnt)
