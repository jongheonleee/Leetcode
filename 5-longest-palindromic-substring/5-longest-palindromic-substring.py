class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_window(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return s[left+1:right]
        
        if len(s) < 2 and s == s[::-1]:
            return s
        
        ans = ""
        for i in range(0, len(s)):
            ans = max(ans,
                     expand_window(i, i+1),
                     expand_window(i, i+2), 
                     key = len)
        
        return ans