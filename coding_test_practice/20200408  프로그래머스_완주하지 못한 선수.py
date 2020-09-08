def solution(participant, completion): 
    sum = participant + completion 
    a = collections.Counter(sum) 
    res = '' 
    for k in a: 
        if a[k] % 2 != 0: 
            res = k 
            
    return res
