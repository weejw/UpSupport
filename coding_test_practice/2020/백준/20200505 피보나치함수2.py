# 1번째 시도: 시간초과 , 아마 파이썬이 느려서..?
n = int(input())

def fibo(n):
    return fibo(n-1)+fibo(n-2) if n>=2 else n

print(fibo(n))


# dp로 풀이

n = int(input())
num = list(range(1,101))
num[1] = 1

if n>=2:
    for i in range(2,n):
        num[i] = num[i-1] + num[i-2]
    n-=1
print(num[n])
