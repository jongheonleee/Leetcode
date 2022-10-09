class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1 for _ in range(len(nums))]
        
        # multiple left side
        acc_l = 1
        for i in range(len(nums)):
            arr[i] *= acc_l
            acc_l *= nums[i]
            
        acc_r = 1
        for j in range(len(nums)-1, -1, -1):
            arr[j] *= acc_r
            acc_r *= nums[j]
            
        return arr
        
                    
                    
                

            
            