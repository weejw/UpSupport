class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        small = 1
        nums = [ i for i in sorted(set(nums)) if i > 0]
        if not nums:
            return 1
        for idx,num in enumerate(nums,1):
            if idx != num:
                return idx
            
        return nums[-1]+1
