class Solution:
    def isPalindrome(self, s: str) -> bool:
        # extract alphabet/number in s then push deque
        # deque help my to run this algoritm more fast compare with when i use list 
        lst = collections.deque()
        
        for char in s:
            if char.isalnum():
                lst.append(char.lower())
                
        # check if lst is palindrome or not
        while len(lst) > 1:
            if lst.pop() != lst.popleft():
                return False
            
        return True
        