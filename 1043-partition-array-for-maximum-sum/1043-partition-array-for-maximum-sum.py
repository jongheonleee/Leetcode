class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        # dp is memorizing sum of sub array which have at most k length
        # we assume that can only look back for dividing groups!
        dp = [0] * n
        
        for i in range(k):
            dp[i] = max(arr[:i+1]) * (i+1)
            
        for j in range(k, n):
            curr = []
            
            for m in range(k):
                curr.append(dp[j-m-1] + max(arr[j-m:j+1]) * (m+1))
                
            dp[j] = max(curr)
            
        return dp[-1]
            
        
                