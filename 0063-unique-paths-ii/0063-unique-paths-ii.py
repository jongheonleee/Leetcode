class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        if (m == n and m == 1 and grid[m-1][n-1] == 1) or grid[0][0] == 1:
            return 0
        
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[1][1] = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                    
                if i+1 == 1 and j+1 == 1: 
                    continue
                    
                else: # grid[i][j] == 0
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
                    
        return dp[-1][-1]
        
                    
                
                
            
        
        
        
        