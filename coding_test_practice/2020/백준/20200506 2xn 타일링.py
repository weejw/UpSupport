n = int(input())

lis = [0 for i in range(1000)]
lis[0] = 1
lis[1] = 2

for i in range(2,n):
    lis[i] = lis[i-1]+lis[i-2]
    
print(lis[n-1]%10007)
