class Solution:
    def isPalindrome(self, s: str) -> bool:
        # extract alphabet/number in s then push list
        lst = []
        
        for char in s:
            if char.isalnum():
                lst.append(char.lower())
                
        # check if lst is palindrome or not
        while len(lst) > 1:
            if lst.pop() != lst.pop(0):
                return False
            
        return True
        