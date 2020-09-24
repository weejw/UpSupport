class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B) - sum(A))/2
        for candy in A:
            if candy + diff in B:
                return [candy, candy + diff] 
       
#set을 이용해 체크할 숫자의 개수를 줄임

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B) - sum(A))/2
        B = set(B)
        for candy in A:
            if candy + diff in B:
                return [candy, candy + diff] 
