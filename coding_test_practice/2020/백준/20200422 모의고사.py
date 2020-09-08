def check(answers, student):
    answersN = len(answers)
    studentN = len(student)
    
    cnt  = 0
    n = 0
    
    for i in range(answersN):
        if answers[i] == student[n]:
            cnt += 1
            
        n += 1
        if n == studentN:
            n = 0
            
    return cnt
    

def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    resultArr = [-1]
    resultArr.append(check(answers, student1))
    resultArr.append(check(answers, student2))
    resultArr.append(check(answers, student3))
    
    maxV = max(resultArr)
    
    idx = [ i for i in range(len(resultArr)) if resultArr[i] == maxV]
    
    return idx
