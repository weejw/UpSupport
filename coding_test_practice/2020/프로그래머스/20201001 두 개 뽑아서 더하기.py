from itertools import combinations

def solution(numbers):
    
    answer = set(sum(i) for i in list(combinations(numbers,2)))
    
    return sorted(list(answer))
