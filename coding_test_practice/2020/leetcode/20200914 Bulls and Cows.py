from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = sum((Counter(secret) & Counter(guess)).values())
        B = 0
        for idx in range(len(secret)):
            if secret[idx] == guess[idx]:
                B+=1
                A-=1
        return "{}A{}B".format(B,A)
