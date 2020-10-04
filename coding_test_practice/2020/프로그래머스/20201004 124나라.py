def solution(n):
    res = ""
    while n > 0:
        n-=1
        res = '124'[n%3]+res
        n//=3
    return res
