class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_num = collections.Counter(nums)
        return [key for key, val in cnt_num.most_common(k)]
            
            
            
        
       

    
