class Solution:
    def isPalindrome(self, s: str) -> bool:
        # processing given string s
        proc_s = ''
        for char in s:
            if char.isalnum():
                proc_s += char.lower()
                
        # check if processing string s is palindrome or not
        left, right = 0, len(proc_s)-1
        while left <= right:
            if proc_s[left] != proc_s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
            
        