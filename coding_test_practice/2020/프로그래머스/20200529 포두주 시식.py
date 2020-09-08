n = int(input())

testK = [0]
for i in range(n):
    testK.append(int(input()))

if len(testK) == 2:
    print(testK[0])
else:
    res = [0 for i in range(n+1)]
    res[1] = testK[1]#init
    res[2] = testK[1]+testK[2]

    for i in range(3, len(testK)):
        num1 = res[i-1]
        num2 = testK[i] + testK[i-1]+res[i-3]
        num3 = testK[i] + res[i-2]
        res[i] = max(num1, num2, num3)

    print(max(res))
