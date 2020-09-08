n = int(input())
times = [int(x) for x in input().strip().split()]
times = sorted(times)
for i in range(n-1):
    times[i+1] = times[i]+times[i+1]
print(sum(times))
