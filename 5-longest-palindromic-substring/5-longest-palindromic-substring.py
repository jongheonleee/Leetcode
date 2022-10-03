class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dealing with exception case
        if s == s[::-1] or len(s) < 2:
            return s
        
        # expand window if window is palindrome
        def expand_window(left:int, right:int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            # palindrom substring
            return s[left+1:right]
        
        # store longest palindrome
        ans : str = ''
        
        
        for i in range(0, len(s)-1):
            ans = max(
                    ans,
                    expand_window(i, i+1),
                    expand_window(i, i+2),
                    key=len)
            
        return ans