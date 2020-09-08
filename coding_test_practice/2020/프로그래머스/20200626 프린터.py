import queue

def solution(priorities, location):
    q_1 = queue.Queue()  

    max_value_list = []
    result_list = []

    for i in range(len(priorities)):
        q_1.put((priorities[i], i))
        max_value_list.append(priorities[i])

    cnt = 0
    while max_value_list:
        max_value = max(max_value_list)
        currentPaper = q_1.get()
        if currentPaper[0] < max_value:
            q_1.put(currentPaper)
        elif currentPaper[0] == max_value:
            cnt += 1
            if currentPaper[1] == location:
                return cnt
            max_value_list.remove(max_value)
            result_list.append(currentPaper)
