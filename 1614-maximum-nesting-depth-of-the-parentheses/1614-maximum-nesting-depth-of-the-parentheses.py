class Solution:
    def maxDepth(self, s: str) -> int:
        st, res = [], 0
        
        for char in s:
            if char == ')':
                st.append('(')
                
            if st and char == st[-1]:
                st.pop()
                
            res = max(res, len(st))
            
        return res
    
                
        

                
                
            
        