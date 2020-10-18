def solution(n):
    lis = [[0 for _ in range(n)] for _ in range(n)]
    y, x = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i%3 == 0:
                y +=1
            elif i%3 == 1:
                x +=1
            elif i%3 == 2:
                y-=1
                x-=1
            lis[y][x] = num
            num+=1
    res = []
    for i in lis:
        for j in i:
            if j !=0:
                res.append(j)
    return res
   
   
   
#후에 알게된 방법
from itertools import chain
[i for i in chain(*lis) if i !=0]
