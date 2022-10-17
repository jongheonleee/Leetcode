class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack, res = [], [0] * len(t)
        
        for crnt_i, crnt_t in enumerate(t):
            while stack and crnt_t > t[stack[-1]]:
                last_i = stack.pop()
                res[last_i] = crnt_i - last_i
                
            stack.append(crnt_i)
            
        return res
        
        