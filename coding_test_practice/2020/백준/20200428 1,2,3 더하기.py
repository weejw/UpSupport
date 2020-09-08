n = int(input())

inlis=[]
for _ in range(n):
    inlis.append(int(input()))
    
lis = [1 for i in range(10)]
lis[1] = 2
lis[2] = 4

for num in inlis:
    for i in range(3,num):
        lis[i] = lis[i-1]+lis[i-2]+lis[i-3]
    
for r in inlis:
    print(lis[r-1])
