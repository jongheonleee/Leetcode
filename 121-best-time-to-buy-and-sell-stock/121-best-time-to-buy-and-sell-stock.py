class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack, max_p = [], 0
        
        for p in prices:
            if not stack:
                stack.append(p)

                
            elif len(stack) == 1:
                if stack[-1] > p:
                    stack.pop()
                    
                stack.append(p)
                
            elif len(stack) == 2:
                if stack[-1] < p:
                    stack.pop()
                    stack.append(p)
                    
                elif stack[0] > p:
                    max_p = max(max_p, stack.pop() - stack.pop())
                    stack.append(p)
                    
        if len(stack) == 2:
            max_p = max(max_p, stack.pop() - stack.pop())
            
        return max_p
                
            


                    
        

            
                
   



        
                

        
        
                
                
            
            
            