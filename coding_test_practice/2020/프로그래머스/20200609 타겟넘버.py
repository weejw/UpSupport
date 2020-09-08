cnt = 0
def solution(numbers, target):
    n = len(numbers)
    calRes = [i for i in numbers]

    def cal(resArr, idx):
        if idx < len(resArr):
            resArr[idx] *= 1
            cal(resArr, idx + 1) #계속 탐색하게 하고,,
            
            resArr[idx] *= -1
            cal(resArr, idx + 1)
            
        else: #하나의 탐색이 끝났을 땐 count를 올려주고,,
            if sum(resArr) == target:
                global cnt #cnt를 solution 함수 안에서 선언 했으면 nonlocal로 ㄱㄱ
                cnt += 1

    cal(calRes, 0)
    return cnt
