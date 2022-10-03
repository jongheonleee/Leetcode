class Solution:
    def longestPalindrome(self, s: str) -> str:
        # exception case
        if s == s[::-1] or len(s) < 2:
            return s
        
        # expand two pointers if s[left:right] is palindrome
        def expand_two_pointers(left:int, right:int) -> str:
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
                    expand_two_pointers(i, i+1),
                    expand_two_pointers(i, i+2),
                    key=len)
            
        return ans