class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        row, col = len(s), len(t)
        
        def test(r, c):
            res = pre = cur = 0
            
            for k in range(min(row-r, col-c)):
                cur += 1
                if s[r+k] != t[c+k]:
                    pre, cur = cur, 0
                    
                
                res += pre
                
            return res
        
        return sum(test(r, 0) for r in range(row))+ sum(test(0, c) for c in range(1, col))
        