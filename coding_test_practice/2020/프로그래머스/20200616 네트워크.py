def dfs(computers, n):
    if not computers[n][n]:
        return False
    computers[n][n] = 0

    for i in range(len(computers)):
        if computers[n][i]:
            dfs(computers, i)
    return True

def solution(n, computers):
    answer = 0

    for i in range(n):
        if computers[i][i] and dfs(computers, i):
            answer += 1

    return answer
