from itertools import permutations

def solution(numbers):
    answer = ''
    lis = []
    
    for i in numbers:
        oriValue = str(i)
        mulValue = (oriValue * 3)
        lis.append((oriValue, mulValue))
    
    sortRes = sorted(lis, key = lambda el:el[1], reverse = True)
    
    if sortRes[0][0] == '0':
        return "0"
    
    for val in sortRes:
        answer += val[0]
    
    return answer
