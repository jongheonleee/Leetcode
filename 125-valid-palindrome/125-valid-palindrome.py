class Solution:
    def isPalindrome(self, s: str) -> bool:
        processing_s = ''
        
        for c in s:
            if c.isalnum():
                processing_s += c.lower()
                
        return processing_s == processing_s[::-1]
        
    
        