import math
from collections import Counter

def solution(progresses, speeds):
    day = [0 for _ in range(len(progresses))]

    for i in range(len(progresses)):
        progress = progresses[i]
        day[i] = math.ceil((100 - progress)/speeds[i])

    for i in range(len(day)-1,-1,-1):
        progresses[i] = max(day[:i+1])

    answer = dict(Counter(progresses))

    return list(answer.values())
