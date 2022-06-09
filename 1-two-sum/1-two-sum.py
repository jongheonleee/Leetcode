class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Base Step
        original_nums = nums[:]
        nums.sort()
        left, right = 0, len(nums)-1
        
        # Excutions Step
        
        while left < right:
            if nums[left] + nums[right] == target:
                if nums[left] == nums[right]:
                
                    i = original_nums.index(nums[left])
                    j = i + 1 + original_nums[i+1:].index(nums[right])
                    
                    return i, j
                
                return original_nums.index(nums[left]), original_nums.index(nums[right])
            
            elif nums[left] + nums[right] > target:
                right -= 1
                
            else:
                left += 1
                
        return None

            
                
        