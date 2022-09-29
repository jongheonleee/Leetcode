class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                
            return s[l+1:r]
        
        if len(s) < 2 and s == s[::-1]:
            return s
        
        ans = ''
        for i in range(len(s)-1):
            ans = max(ans, 
                     expand(i, i+1),
                     expand(i, i+2),
                     key=len)
            
        return ans
        