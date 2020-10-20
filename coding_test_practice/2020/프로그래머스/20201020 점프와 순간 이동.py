def solution(n):
    res = 0
    for i in format(n,"b"):
        res += int(i)
    return res
