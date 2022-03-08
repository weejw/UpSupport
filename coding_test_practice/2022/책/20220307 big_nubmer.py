# 내 답안 책에서 아니나다를까,, 해당 코드는 값이 커지면 시간초과 판정을 받는 코드라고했다. 두둥
n, limit, k = map(int, input().split())
nums = sorted(map(int, input().split()), reverse=True)

answer, cnt, idx = 0, 1, 0
while cnt <= limit:
    if cnt % (k + 1) == 0:
        answer += nums[idx + 1]
    else:
        answer += nums[idx]
    cnt += 1

print(answer)
# 책에 의하면 이렇게 while문 돌 필요없이 아래처럼 큰 수가 몇 번 더해질지 먼저 계산한 뒤 더해주면 됐다.....
# 수열이 반복되는 횟수를 찾는ㄱㅔ 키포인트같았다.
# int(limit/(k+1)) * k + limit %(k+1)



