class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_table = collections.Counter(nums)
        cnt = 0
        
        for key, val in hash_table.items():
            tmp = 0
            if val >= 2:
                for v in range(1, val):
                    tmp += v
                    
            cnt += tmp
            
        return cnt
                    
                
                
        
        