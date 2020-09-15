class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        print(dp)
        listLen = len(nums)
        if listLen == 0:
            return 0
        if listLen == 1:
            return nums[0]
        if listLen == 2:
            return max(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, listLen):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        return dp[-1]
