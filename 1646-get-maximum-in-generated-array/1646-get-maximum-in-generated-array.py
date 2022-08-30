class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        # base case
        nums = [0  for _ in range(n+1)]
        nums[1] = 1
                
        for i in range(2, n+1):
            a, b = divmod(i, 2)
            
            if b == 0:
                nums[i] = nums[a]
                
            else:
                nums[i] = nums[a] + nums[a+1]
            
        return max(nums)
            
            