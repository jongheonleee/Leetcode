class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        '''        
        d = collections.defaultdict(int)
        ans = 0
        
        # key: num, val: count number of num in nums
        for num in nums:
            # print(d.get(num, 0))
            d[num] = d.get(num, 0) + 1
            
        print(d)
        for key in d:
            if (key + k) in d:
                ans += d[key] * d[key + k]
        return ans
        '''

        d = collections.defaultdict(int)
        ans = 0
        
        for num in nums:
            d[num] = d.get(num, 0) + 1 
            
        for key in d:
            if (key+k) in d:
                ans += d[key] * d[key+k]
                
        return ans
        