import heapq

def solution(scoville, K):
    if min(scoville) >= K:
        return 0

    heap = []

    for i in scoville:
        heapq.heappush(heap, i)

    cnt = 0
    while True:
        if heap[0] < K:
            if len(heap) ==1:
                return -1
            cnt += 1
            heapq.heappush(heap, heapq.heappop(heap)+heapq.heappop(heap)*2)
  
        else:
            break

    return cnt
