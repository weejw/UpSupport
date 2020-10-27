def solution(arr):
    res = [arr[0]]
    for idx in range(1, len(arr)):
        if arr[idx] == res[-1]:
            continue
        res.append(arr[idx])
    
    return res
