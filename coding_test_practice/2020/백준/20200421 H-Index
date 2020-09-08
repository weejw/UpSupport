def solution(citations):
    citations.sort(reverse=True)
    ciL = len(citations)
    
    for i in range(ciL):
        if citations[i] <= i: #지금까지 카운트한 논문 개수(index)와 arr[index]값을 비교
            return i
    return ciL # index에 비해 arr[index]값이 큰 경우 위 if문에 부적합하므로 그냥 arr길이 출력하면 됨
