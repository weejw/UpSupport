
def solution(s):
    answer = ''
    c = s.split(" ")
        
    for e in c:
        answer += e.capitalize()+" "
    return answer[:-1]
