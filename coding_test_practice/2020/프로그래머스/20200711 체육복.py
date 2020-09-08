def solution(n, lost, reserve):
    answer = 0
    
    reserveS = list(set(reserve)-set(lost))
    lostS = list(set(lost)-set(reserve))
    answer += n - len(lostS)

    for student in lostS:
        if student-1 in reserveS:
            reserveS.remove(student-1)
            answer+=1
        elif student+1 in reserveS:
            reserveS.remove(student+1)
            answer += 1
    return answer
