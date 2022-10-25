class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        ans:int = 0
        
        for i, c1 in enumerate(s):
            check, tmp = {c1:1}, c1

            for j, c2 in enumerate(s[i+1:]):
                if c2 in check:
                    break

                else:
                    check[c2] = 1
                    tmp += c2
                    
            ans = max(ans, len(tmp))
                    
        return ans
        
        
                    
                
                
                
            
            
            
            
            
        