def solution(A, K):     
  length = len(A)     
  for _ in range(K):         
    A = A[-1:]+A[:length-1]     
    return A
