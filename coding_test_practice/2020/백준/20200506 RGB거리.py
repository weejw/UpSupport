n = int(input())

testN = []

for _ in range(n):
    testN.append(list(map(int, input().split())))

cost = [[0, 0, 0] for i in range(n)]

cost[0] = testN[0]

for i in range(len(testN)):
    cost[i][0]=min(cost[i-1][1], cost[i-1][2]) + testN[i][0] // r로 했을 때,
    cost[i][1]=min(cost[i-1][0], cost[i-1][2]) + testN[i][1] // g로 했을 때,
    cost[i][2]=min(cost[i-1][0], cost[i-1][1]) + testN[i][2] // b로 했을 때,

n -= 1

print(min(cost[n][0],cost[n][1],cost[n][2])) // 그 중에 제일 작은걸 고르기
