class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        start, end = 0, 10
        candidate = {}
        while end <= len(s):
            seq = s[start:end]
            if seq in candidate:
                candidate[seq] +=1
            else:
                candidate[seq] = 1
            start +=1
            end +=1
        
        return [k for k,v in candidate.items() if v >=2]
            
