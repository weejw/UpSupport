n, m = map(int, input().split())

_map = []
for _ in range(n):
    _map.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y >= m or y <= -1:
        return False
    if _map[x][y] == 0:
        _map[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1

print(answer)
