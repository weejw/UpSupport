n = int(input())

travel = input().split()

initial_space = [1, 1]
for i in range(len(travel)):
    if travel[i] == "R":
        if initial_space[1] + 1 > 5:
            continue
        initial_space[1] += 1

    elif travel[i] == "L":
        if initial_space[1] - 1 < 1:
            continue
        initial_space[1] -= 1

    elif travel[i] == "U":
        if initial_space[0] - 1 < 1:
            continue
        initial_space[0] -= 1

    elif travel[i] == "D":
        if initial_space[0] + 1 > 5:
            continue
        initial_space[0] += 1

print(*initial_space)

#책에서는 이동좌표를 미리 변수로 선언하고 진행했다. 훨씬 까끔하긴하다.