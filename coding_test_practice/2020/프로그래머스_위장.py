def solution(lis):

    answer = 1
    dic = {}

    for i in lis:
        if i[1] in dic:
            dic[i[1]].append(i[0])

        else:
            dic[i[1]] = [i[0]]

    for k, v in dic.items():
        answer *= len(v)+1

    return answer - 1
