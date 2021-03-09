def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            str = 'A'
        elif s[i].islower():
            str = 'a'
        else:
            continue
            
        s[i] = chr((ord(s[i])-ord(str)+ n)%26+ord(str))
    
    return ''.join(s)
