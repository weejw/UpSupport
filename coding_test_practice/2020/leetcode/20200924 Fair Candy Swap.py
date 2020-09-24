class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B) - sum(A))/2
        for candy in A:
            if candy + diff in B:
                return [candy, candy + diff] 
                
                #한명이 이렇게 푸니까 다 이렇게 푼다..
