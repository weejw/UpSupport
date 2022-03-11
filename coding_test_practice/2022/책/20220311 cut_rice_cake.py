n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start, end = 0, max(array)

res = 0

while start <= end:
    total = 0

    mid = (start+end) // 2
    for x in array:
        if x > mid:

            total += x - mid

    if total < m:
        end = mid - 1

    else:
        res = mid
        start = mid + 1

print(res)