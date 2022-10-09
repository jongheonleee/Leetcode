class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_table 
        # key = num, value = idx
        nums_idx = collections.defaultdict(int)
        
        for i, n in enumerate(nums):
            t = target - n
            
            if t in nums_idx:
                return [nums_idx[t], i]
            
            nums_idx[n] = i
            
        return None
    

            
            

                    
                
            
        
                

            
            
            
        

            
                
        