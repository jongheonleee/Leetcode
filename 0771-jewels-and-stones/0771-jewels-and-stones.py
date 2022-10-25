class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt_j = collections.defaultdict(int)
        for s in stones:
            cnt_j[s] += 1
            
        ans = 0
        
        for j in jewels:
            ans += cnt_j[j]
            
        return ans