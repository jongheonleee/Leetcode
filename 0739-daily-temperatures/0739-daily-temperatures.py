class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, ans = [], [0 for _ in range(len(T))]
        
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                j = stack.pop()
                ans[j] = i-j
                
            stack.append(i)
                
        return ans
        
        