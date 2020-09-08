def solution(brown, red):
    w=0
    h=0
    for w in range(1,red+1):
        h = red/w #w값을 계속 증가시키면서 가능한한 h값을 계속 변경

        res = 2*w+2*h+4 #위, 아래, 모서리
        if  res == brown: #가 brown이랑 같을때까지 반복(for문이니까)
            answer=[max(h,w)+2,min(h,w)+2] 
            # 제한 사항 : 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
            return answer
