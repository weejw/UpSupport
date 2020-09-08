def solution(prices):
    n = len(prices)
    for i in range(n-1):
        for j in range(i+1, n):
            if prices[i] > prices[j]:
                prices[i] = j-i
                break
            if j == n-1:
                prices[i] = j-i

    prices[-1] = 0

    return prices
