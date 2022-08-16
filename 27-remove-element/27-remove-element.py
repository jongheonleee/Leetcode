class Solution:
    def removeElement_(self, nums: List[int], val: int) -> int:
        cnt = 0
        for v in nums:
            if v == val:
                cnt += 1
                
        while cnt > 0:
            nums.remove(val)
            cnt -= 1
            
        return len(nums)
    
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        for n in nums:
            if n != val:
                nums[i] = n
                i += 1
                
        return i
        

        