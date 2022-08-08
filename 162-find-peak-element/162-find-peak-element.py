class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        beg, end = 0, len(nums)-1
        
        while beg < end:
            mid = beg + (end-beg)//2
            
            if nums[mid] < nums[mid+1]:
                beg = mid + 1
                
            else:
                end = mid 
                
        return end
        