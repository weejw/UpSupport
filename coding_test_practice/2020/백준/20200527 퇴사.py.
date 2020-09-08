n = int(input())

testK = []
maxArr = [0 for i in range(n+1)]


for i in range(n):
    d, p = map(int, input().split())
    testK.append([d, p])

testK.append([0, 0])

for i in range(n-1, -1, -1):
    day = int(testK[i][0])
    pay = int(testK[i][1])

    if day == 1:
        maxArr[i] = maxArr[i+1] + pay

    elif (i + day) - 1 > n-1:
        maxArr[i] = maxArr[i+1]

    else:
        firstVal = pay + maxArr[i+day]
        secondVal = maxArr[i+1]

        if secondVal > firstVal:
            maxArr[i] = secondVal
        else:
            maxArr[i] = firstVal

print(maxArr[0])
