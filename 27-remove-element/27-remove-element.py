class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for v in nums:
            if v == val:
                cnt += 1
                
        while cnt > 0:
            nums.remove(val)
            cnt -= 1
            
        return len(nums)
#         nums.sort()
        
#         left, right = 0, len(nums)-1
#         cnt = 0
        
#         while left <= right:
#             mid = left + (right - left)//2
            
#             if nums[mid] < val:
#                 left += 1
                
#             elif nums[mid] > val:
#                 right -= 1
                
#             elif nums[mid] == val:
#                 for i in range(mid, len(nums)):
#                     if nums[i] == val:
#                         cnt += 1
                
#                 break
                
#         while cnt > 0:
#             nums.remove(val)
#             cnt -= 1
            
        
                
#         return len(nums)
                
        