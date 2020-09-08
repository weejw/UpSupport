import heapq
def solution(jobs):
    n = len(jobs)
    if n == 1:
        return jobs[0][1]

    cnt = 0
    time = 0
    heap = []
    answer = 0
    end = -1

    jobs = sorted(jobs)

    while cnt < n:
        for job in jobs:
            if end < job[0] <= time:  # 앞선 작업이 진행되는동안 들어오는 후보군을 찾음
                answer += (time - job[0])
                heapq.heappush(heap, job[1])

        if heap:# 대기 중인 job이 있음
            answer += len(heap) * heap[0]
            end = time
            time += heapq.heappop(heap)
            cnt += 1
        else: # 대기 중인 job은 없지만 앞으로 들어올 job은 남았음 (cnt가 모두 카운팅되지 않았으니까)
            time += 1

    return answer // n
