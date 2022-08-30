class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # first of all, i have to know N
        n = len(nums) // 2
        
        # make hash_table which key:num - val:number of num
        hash_table = collections.defaultdict(int)
        for key in nums:
            if hash_table.get(key):
                hash_table[key] += 1
                
            else:
                hash_table[key] = 1
                
            
        print(hash_table)
            
        for key in nums:
            if hash_table[key] == n:
                return key
            
        