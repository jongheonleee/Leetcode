class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def find_target(sub_nums: List[int], target: int) -> None:
            left, right = 0, len(sub_nums)-1
            
            while left < right:
                if target == sub_nums[left] + sub_nums[right]:
                    res.append([-target, sub_nums[left], sub_nums[right]])
                    
                    while left < right and sub_nums[left] == sub_nums[left+1]:
                        left += 1
                        
                    while left < right and sub_nums[right] == sub_nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif target > sub_nums[left] + sub_nums[right]:
                    left += 1
                    
                else:
                    right -= 1
                    
            
            
        for i, target in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            find_target(nums[i+1:], -target)
            
        return res
                
            
                    
                
                
        
                    
            

                        
                
    
                    
                        
                    
                    
        