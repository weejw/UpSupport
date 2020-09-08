testC = int(input())

testN = []

for _ in range(testC):
    testN.append(int(input()))

lis = [(0,0) for i in range(41)]
lis[0]=(1,0)
lis[1]=(0,1)

for n in testN:
    for i in range(2,n+1):
        lis[i]=(lis[i-1][0]+lis[i-2][0], lis[i-1][1]+lis[i-2][1])

for i in testN:
    print(lis[i][0], lis[i][1])
