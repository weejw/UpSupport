class Solution:
        
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idxs = []
        for idx in range(len(gas)):
            if gas[idx] >= cost[idx]:
                idxs.append(idx)
        
        flag = False
        for i in idxs:
            newGas, newCost = gas[i:]+gas[:i], cost[i:]+cost[:i]
            gasSome, costSome = 0, 0
            
            for j in range(len(gas)):
                gasSome += newGas[j]
                costSome += newCost[j]
                if gasSome >= costSome:
                    flag = True
                    
                else:
                    flag = False
                    break 
                    
            if flag:
                return i
        return -1
                
