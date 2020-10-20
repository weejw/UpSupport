#공부용

def quad(idx, jdx, size, arr, ans):
    one = True
    zero = True
    
    for i in arr[idx:idx+size]:
        for j in i[jdx:jdx+size]:
            if j == 1:
                zero = False
            if j == 0:
                one =  False
        if zero == False and one ==False:
            break
    
    if one == True:
        ans[1]+=1
    elif zero == True:
        ans[0]+=1
    else:
        quad(idx,jdx,size//2,arr,ans)
        quad(idx,jdx+size//2,size//2,arr,ans)
        quad(idx+size//2,jdx,size//2,arr,ans)
        quad(idx+size//2,jdx+size//2,size//2,arr,ans)

def solution(arr):
    answer = [0,0]
    quad(0, 0, len(arr), arr, answer)
    return answer
