class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return abs(stones[0]-stones[1])
        
        while len(stones) >1:
            stones = sorted(stones, reverse = True)
            stones = [stones[0] - stones[1]] + stones[2:]
        
        return stones[0]
