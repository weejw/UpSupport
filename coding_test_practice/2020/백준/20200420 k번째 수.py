def solution(array, commands):
    answer = []
    
    for com in commands:
        i = com[0] - 1
        j = com[1]
        k = com[2] - 1
        
        trimA = array[i:j]
        trimA.sort()
        answer.append(trimA[k])
        
    return answer
