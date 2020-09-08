num = int(input())
    
lis =[0 for i in range(num+1)]

for i in range(2,num+1):
    lis[i]=lis[i-1]+1
    if i%2 ==0 : lis[i]=min(lis[i],lis[int(i/2)]+1)
    if i%3 ==0 : lis[i]=min(lis[i],lis[int(i/3)]+1)
    
print(lis[num])
