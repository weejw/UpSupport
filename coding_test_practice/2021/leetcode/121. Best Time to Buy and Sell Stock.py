class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        revenue = 0
        min_price = 100000
        for price in prices:
            min_price = min(price, min_price)
            revenue = max(revenue, price-min_price)
        
        return revenue
        
