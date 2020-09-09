class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)
        for idx in range(len(A)-2):
            if A[idx] < A[idx+1]+A[idx+2]:
                return A[idx] + A[idx+1] + A[idx+2]
        return 0
