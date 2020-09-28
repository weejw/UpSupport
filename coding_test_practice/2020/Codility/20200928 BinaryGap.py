import re
def solution(N):
    # write your code in Python 3.6
    openFlag, closeFlag, zeroFlag = False, False, False
    
    #1001001 로 예를 들면
    #가장 먼저 1이 있는지 체크
    if N <3:
        return 0
    binaryN = format(N,'b')
    
    checkOne = False
    checkZero = False #사이에 zero가 있었나?
    cntZero = 0
    longestZero = 0
    for n in binaryN:
        if n == '0':
            checkZero = True
            cntZero +=1
        #1을 만나면 1 체크 
        if n == '1':
            if checkOne and checkZero :#이미 직전에 1을 만난적이 있고 사이에 0이 있었는지 체크함
                if longestZero < cntZero :
                    longestZero = cntZero #1001과 같은 경우이므로 이전에 더 큰 0이 있었는지 확인한 후 체인지함
                cntZero = 0
            
            else:
                checkOne = True #1을 처음만났음
    
    return longestZero
