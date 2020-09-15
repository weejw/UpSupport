def solution(people, limit):
    people = sorted(people,reverse = True)
    answer = 0
    
    frontIdx = 0
    backIdx = len(people)-1
    
    while frontIdx <= backIdx:
        if people[backIdx]+people[frontIdx] <= limit:
            frontIdx += 1
            backIdx -= 1
        else:
            frontIdx +=1
        answer+=1
            
    return answer
