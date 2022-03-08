n, m = map(int, input().split())
_max = 0

for _ in range(n):
    _max = max(_max, min(map(int, input().split())))

print(_max)
