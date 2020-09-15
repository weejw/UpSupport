def solution(numbers): 
    if set(numbers) == {0}:
        return "0" 
    numbers = sorted([(str(i)*3, i) for i in numbers], reverse = True) 
    res = "" 
    for num in numbers: 
        res += str(num[1]) 
    return res
