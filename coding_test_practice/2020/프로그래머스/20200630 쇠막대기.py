def solution(arrangement):
    arrangement = arrangement.replace("()", "l")

    laser = 0
    stack = []
    for ele in arrangement:
        if ele == "(":
            stack.append("(")
            print("stack 추가:", stack)
        elif ele == ")":
            stack.pop()
            laser += 1
            print("stack에서 빼고 더이상 잘리지 않음 :", laser)
        else:
            laser += len(stack)
            print("레이저로 자름:", laser)

    return laser
