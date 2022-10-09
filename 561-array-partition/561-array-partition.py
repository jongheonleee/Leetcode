class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # using greedy
        # sort given list
        # and then sum of values which have 2*n as index
        nums.sort()
        ans:int = 0
        
        for i in range(0, len(nums), 2):
            ans += nums[i]
            
        return ans
        
        
        
        

            
                
        
            
        