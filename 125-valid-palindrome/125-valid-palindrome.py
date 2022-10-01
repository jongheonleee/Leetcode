class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(left, right) -> bool:
            while left <= right:
                if new_str[left] != new_str[right]:
                    return False
                
                left += 1
                right -= 1
                
            return True
        
        new_str = ''
        
        for char in s:
            if char.isalnum():
                new_str += char.lower()
                
        return check(0, len(new_str)-1)
        