class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == '(':
                stack.append(')')
                
            elif c == '{':
                stack.append('}')
                
            elif c == '[':
                stack.append(']')
                
            else:
                if stack and stack[-1] == c:
                    stack.pop()
                    
                else:
                    return False
                
        return len(stack) == 0
            
            
    
                
            
        