def cal(n):
    door = [0 for i in range(n + 1)]
    for j in range(1, n + 1):
        bitDoor = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            if i % j == 0:
                bitDoor[i] = 1
        for k in range(1, n + 1):
            door[k] = door[k] ^ bitDoor[k]

    return sum(door)


testK = []
res = []

k = int(input())

for i in range(k):
    testK.append(int(input()))

for n in testK:
    print(cal(n))
