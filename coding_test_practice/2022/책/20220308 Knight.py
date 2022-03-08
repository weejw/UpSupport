alpha_lis = list("abcdefgh")

initial_position = list(input())
initial_position[0] = alpha_lis.index(initial_position[0])
initial_position[1] = int(initial_position[1])

mvs = [(2, 1), (-2, 1), (-1, 2), (1, -2), (1, 2), (-2, -1), (-1, 2), (-1, -2)]
answer = 0
for mv in mvs:
    dx = mv[0]
    dy = mv[1]
    mv_dx = initial_position[0] + dx
    mv_dy = initial_position[1] + dy

    if 0 < mv_dx < 8 and 0 < mv_dy < 8:
        answer += 1

print(answer)
