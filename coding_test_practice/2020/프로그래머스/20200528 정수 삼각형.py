n = int(input())

size = 2 * n - 1  # 단말 노드 크기
maxTri = [[0 for _ in range(size)] for _ in range(n)]

startPoint = int((2 * n - 1) / 2)  # 루트 노드 시작점
maxTri[0][startPoint] = list(map(int, input().split()))[0]

startPoint -= 1
for i in range(1, n):
    num = list(map(int, input().split()))
    nextPoint = startPoint
    numL = len(num)
    for j in range(numL):
        ele = num[j]
        if j == 0:
            maxTri[i][nextPoint] = ele + maxTri[i - 1][nextPoint + 1]

        elif j == numL - 1:
            maxTri[i][nextPoint] = ele + maxTri[i - 1][nextPoint - 1]

        else:
            parents_1 = maxTri[i - 1][nextPoint + 1]
            parents_2 = maxTri[i - 1][nextPoint - 1]

            maxTri[i][nextPoint] = max(ele + parents_1, ele + parents_2)

        nextPoint += 2

    startPoint = startPoint - 1

print(max(map(max, maxTri)))
