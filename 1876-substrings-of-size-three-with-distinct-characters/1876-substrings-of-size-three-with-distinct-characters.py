class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = 0
    
        for i in range(0, len(s)-2):
            seen = {}
            for j in range(i, i+3):
                if s[j] not in seen:
                    seen[s[j]] = 1
                    
                else:
                    break
                    
            if len(seen) == 3:
                cnt += 1
                
        return cnt
                
            
        