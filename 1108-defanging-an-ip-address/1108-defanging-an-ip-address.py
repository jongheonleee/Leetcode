class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ''
        
        for char in address:
            if char == '.':
                res += '[.]'
                
            else:
                res += char

        return res