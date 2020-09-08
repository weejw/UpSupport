def solution(x, n):
    answer = []
    if x == 0:
        return [0 for _ in range(n)]
    for i in range(x, x*n, x):
        answer.append(i)
    answer.append(x*n)
    
    return answer
