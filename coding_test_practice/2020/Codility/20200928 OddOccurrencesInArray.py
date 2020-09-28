from collections import Counter

def solution(A):
    # write your code in Python 3.6
    c = Counter(A)
    for k, v in c.items():
        if v%2 != 0:
            return k
