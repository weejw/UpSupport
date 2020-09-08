import heapq
def solution(stock, dates, supplies, k):
    candidates = []
    cnt = 0
    dates_idx = 0

    while stock < k:
        #공급일 후보 찾기
        for i in range(dates_idx, len(dates)):
            if dates[i] <= stock:# 현재 가진 stock으로 버틸 수 있는 최대 날짜를 찾음
                supply = supplies[i]
                heapq.heappush(candidates, (-supply, supply))
                dates_idx = i+1
            else:
                break
                
        cnt += 1 #이전까지 공급받을 수 있던 후보들중 공급자를 찾는다.
        stock += heapq.heappop(candidates)[1]

    return cnt
