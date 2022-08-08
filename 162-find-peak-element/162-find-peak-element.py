class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        ans = (-1, -math.inf)
        
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] >= nums[j]:
                if ans[1] <= nums[i]:
                    ans = (i, nums[i])
                    
                    
            elif nums[i] < nums[j]:
                if ans[1] <= nums[j]:
                    ans = (j, nums[j])
                    
            i += 1
            j -= 1
            
        return ans[0]
        