from functools import reduce
from collections import Counter

# 이중 for문으로 풀 수 있겠지만 O(n)으로 풀어야 함
class Solution:
    def multiply(self,arr):
        return reduce(lambda x, y: x * y, arr)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 0의 개수를 체크 
        counterForZero = Counter(nums)[0]
        
        # 0 이 1개라면 0이 선택되는 경우 빼고 다 0이고 0의 자리에만 product value
        if counterForZero == 1:
            res = [0]*len(nums)
            idx = nums.index(0)
            res[idx] = self.multiply(nums[:idx]+nums[idx+1:])
            return res
    
        #0이 1개 이상이면 언제든 0
        if counterForZero  > 1:
            return [0]*len(nums)
        
        #0이 하나도 없는 경우
        res = self.multiply(nums)
        for idx,num in enumerate(nums):
            nums[idx] = int(res/num)
        
        return nums 
