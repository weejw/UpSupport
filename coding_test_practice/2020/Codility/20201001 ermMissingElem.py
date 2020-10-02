# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = sorted(A)
    if A:
        for idx, ele in enumerate(A):
            if idx+1 != ele:
                return idx+1
        return A[-1]+1
    return 1
