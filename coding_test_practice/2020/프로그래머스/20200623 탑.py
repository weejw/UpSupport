def solution(heights):
    flag = True
    idx = len(heights) - 1

    while flag:
        checkTop = heights[idx]
        findFlag = False

        for i in range(idx-1, -1, -1):
            if heights[i] > checkTop:
                heights[idx] = i+1
                findFlag = True
                break
            if not findFlag:
                heights[idx] = 0
        idx -= 1
        if idx == 0:
            heights[0] = 0
            flag = False

    return heights
