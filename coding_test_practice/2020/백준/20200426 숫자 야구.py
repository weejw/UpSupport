def check(number, allNum):
    qNum     = str(number[0])
    qStrike  = number[1]
    qBalls   = number[2]
    candiArr = []
    
    for n in allNum:
        strikes, balls = (0,0)
        for j in range(3):
            if qNum[j] == n[j]:
                strikes += 1
            elif qNum[j] in n:
                balls += 1
        if (strikes, balls) == (qStrike, qBalls):
            candiArr.append(n)
            
    return candiArr
    

    
def solution(baseball):
    rNum   = [str(x) for x in range(1,10)]
    canNum = [
        rNum[x]+rNum[y]+rNum[z]
        for x in range(9)
        for y in range(9)
        for z in range(9)
        if x!=y and y!=z and z!=x
    ]
    for qusition in baseball:
        canNum = check(qusition, canNum)
        
    answer = len(canNum)
    return answer
