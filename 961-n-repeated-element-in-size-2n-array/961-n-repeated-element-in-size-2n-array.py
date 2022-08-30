class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # first of all, i have to know N
        n = len(nums) // 2
        
        # make hash_table which key:num - val:number of num
        hash_table = collections.defaultdict(int)
        for num in nums:
            hash_table[num] += 1
            
        for num in nums:
            if hash_table[num] == n:
                return num
            
        return -1
        