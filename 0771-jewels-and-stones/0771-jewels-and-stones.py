class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt_j = collections.Counter(stones)
            
        ans = 0
        
        for j in jewels:
            ans += cnt_j[j]
            
        return ans