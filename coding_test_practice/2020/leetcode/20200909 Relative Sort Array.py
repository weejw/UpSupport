from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        arrC = Counter(arr1)
        for i in arr2:
            res.extend([i] * arrC[i])
        
        return res + sorted([i for i in arr1 if i not in res])
