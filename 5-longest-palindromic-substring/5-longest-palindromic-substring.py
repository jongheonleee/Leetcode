class Solution:
    def longestPalindrome(self, s: str) -> str:
        # exception case
        if len(s) < 2 and s == s[::-1]:
            return s
        
        # for saving longest palindrome substring
        ans : str = ''
        
        def expand(left: int, right: int) -> str:
            # extract palindromic substring
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return s[left+1:right]
                
        
        for i in range(0, len(s)-1):
            ans = max(ans,
                     expand(i, i+1),
                     expand(i, i+2),
                     key=len)
            
        return ans
            
        