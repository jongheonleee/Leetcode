class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # exception case
        # if not any(nums) or (len(nums) == 3 and sum(nums) == 0):
        #     return [nums[0:3]]

        # for using two-pointers
        nums.sort()
        # store answer
        ans:list = []
        
        def find(left: int, right: int, target: int) -> None:
            while left < right:
                if target > nums[left] + nums[right]:
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                        
                    left += 1
                    
                elif target < nums[left] + nums[right]:
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    right -= 1
                    
                else:
                    ans.append([-target, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left += 1
                    right -= 1
                
            return None
                    
            
            
        # select a number as target
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            find(i+1, len(nums)-1, -nums[i])

        return ans
            
                    
                
                
        
                    
            

                        
                
    
                    
                        
                    
                    
        