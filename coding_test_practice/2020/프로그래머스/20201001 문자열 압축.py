def solution(s):
    #for를 돌면서 interval을 변화시킨다.
    if len(s) == 1: #런타임 에러떴다. range 1부터였는데 idx 1은 없으므로 .. 
        return 1
    candidate = []
    length = len(s)
    
    for inter in range(1, length//2+1):
        currentParts = s[:inter] #현재 parts
        cnt = 0
        res = ""
        for parts in range(0, length, inter): #inter만큼씩 증가시킨다
            tmpParts = s[parts:parts+inter]
            if currentParts == tmpParts:
                cnt += 1
            else:
                if cnt == 1: #1인경우는 생략하라 하였으므로
                    res += str(currentParts)
                else:
                    res += str(cnt)+str(currentParts)
                currentParts = tmpParts
                cnt = 1
        
        #aabbaccc 마지막 ccc를 캐치를 못하므로 마지막 체크를 해줘야한다.
        if cnt == 1:
             res += str(currentParts)
        else:
             res += str(cnt)+str(currentParts)
                
        candidate.append(len(res))
    return min(candidate)
