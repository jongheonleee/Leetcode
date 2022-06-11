class Solution:
    def singleNumber(self, nums):
        s = reduce(xor, nums)
        nz = s & (s-1) ^ s
        num1 = reduce(xor, filter(lambda n: n & nz, nums))
        return(num1, s ^ num1)

    def singleNumber_mine(self, nums: List[int]) -> List[int]:
        # wrong ans: cuz i use O(n) in space complexity
        cnt_map = collections.Counter(nums)
        res = []
        
        for k, v in cnt_map.items():
            if v == 1:
                res.append(k)
                
        return res
        
