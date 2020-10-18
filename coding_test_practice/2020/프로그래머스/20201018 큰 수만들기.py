def solution(number, k):
    res = []
    for num in number:
        while res and res[-1] < num and k>0:
            res.pop() # pop 말고 slice했을 때는 시간 초과가 났다. 
            k -=1
        res.append(num)
        
    while k > 0:
        res.pop()
        k-=1
            
    return ''.join(res)
        
