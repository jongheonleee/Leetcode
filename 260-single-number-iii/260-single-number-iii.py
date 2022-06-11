class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnt_map = collections.Counter(nums)
        res = []
        
        for k, v in cnt_map.items():
            if v == 1:
                res.append(k)
                
        return res
        