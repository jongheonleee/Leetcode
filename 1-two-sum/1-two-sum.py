class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_match = collections.defaultdict(list)
        
        for i, num in enumerate(nums):
            nums_match[num] += [i]
            
        for i, num in enumerate(nums):
            t = target - num
            
            if t in nums_match:
                for j in nums_match[t]:
                    if i != j:
                        return [i, j]
                    
                    
                
            
        
                

            
            
            
        

            
                
        