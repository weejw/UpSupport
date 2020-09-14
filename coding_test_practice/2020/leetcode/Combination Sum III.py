from itertools import combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = range(1,10)
        permute =combinations(nums,k)
        res = []
        for i in permute:
            if sum(i) == n:
                res.append(i)
        

        return res
