class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        hash_table = collections.defaultdict(int)
        cnt = 0
        
        for num in nums:
            hash_table[num] = 1
            
        for num in nums:
            if num - diff in hash_table and num - 2*diff in hash_table:
                cnt += 1
                
                
        return cnt
            
        
        