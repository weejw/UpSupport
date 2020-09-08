class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        points = []
        maxNum = len(A)
        answer = sorted(A)

        while True:
            if A == answer:
                return points
            reversePoint = A.index(maxNum) # 가장 큰 값이 있는 곳을 찾고
            points.append(reversePoint + 1)
            A = A[reversePoint::-1]+A[reversePoint+1:] # 그 곳에서 뒤집고 안뒤집은건 뒤에 붙여놓고 일단
            A = A[maxNum-1::-1]+A[maxNum:] # 다시 그 큰 수를 맨뒤로 보내기 위해 뒤집음
            points.append(maxNum)
            maxNum -= 1
