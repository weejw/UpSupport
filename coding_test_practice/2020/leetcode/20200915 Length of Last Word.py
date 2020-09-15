import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "":
            return 0
        for alp in s.split(" ")[::-1]:
            if alp != "":
                return len(alp)
        return 0
