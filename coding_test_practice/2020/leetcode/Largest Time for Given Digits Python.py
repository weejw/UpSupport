from itertools import permutations
from collections import Counter

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A = [str(i) for i in A]
        candiate = sorted(
                    [i for i in list(
                     map(''.join, permutations(A, 2))
                     ) 
                     if int(i) < 60],reverse = True)
        
        hourCandi = sorted([i for i in candiate if int(i) < 24], reverse = True)
        
        check = Counter(A)
        for hour in hourCandi:
            for cand in candiate:
                if check == Counter(hour+cand):
                    return "{0}:{1}".format(hour,cand)
        return ""
