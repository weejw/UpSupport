def solution(board, moves):
    ln = len(board)
    stack = []
    answer = 0

    for step in moves:
        flag = False
        for i in range(ln):
            block = board[i][step-1]
            if block is not 0:
                stack.append(block)
                board[i][step-1] = 0
                flag = True
                break
        if flag and len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer +=2
    return answer
