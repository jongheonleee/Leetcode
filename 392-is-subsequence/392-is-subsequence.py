class Solution:
    def isSubsequence_(self, s, t):
        # using dp
        s, t = ' '+s, ' '+t
        m, n = len(s), len(t)
        
        dp = [[0] * m for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 1
            
        for i, j in product(range(1, n), range(1, m)):
            if s[j] == t[i]:
                dp[i][j] = dp[i-1][j-1]
                
            else:
                dp[i][j] = dp[i-1][j]
                
        return dp[-1][-1]
    
    def isSubsequence(self, s, t):
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1

            j += 1
                
        return i == len(s) 
            
        


        
        