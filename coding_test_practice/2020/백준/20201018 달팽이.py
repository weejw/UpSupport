num = int(input())
findNum = int(input())
data = [[0]* num for i in range(num)]

n = num**2 + 1
s = 1
i = -1
j = 0
k = num

while True:
    for p in range(1, k+1):
        n -= 1
        i += s
        data[i][j] = n
    k -= 1

    if k <= 0:
        break
    for p in range(1, k+1):
        n -= 1
        j += s
        data[i][j] = n
    s*= -1
    
res = [0,0]
for i in range(len(data)):
    for j in range(len(data[0])):
        print(data[i][j], end=' ')
        if data[i][j] == findNum:
            res[0], res[1] = i+1, j+1
    print()
print(res[0],res[1])
