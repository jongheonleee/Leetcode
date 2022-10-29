class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0]*(len(triangle[i])) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][0]
                    
                elif j == len(triangle[i])-1:
                    dp[i][j] = triangle[i][j] + dp[i-1][-1]
                    
                else:
                    # 0 < j < len(triangle[i])
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
                    
        return min(dp[-1])
                    
        
        
        
                
                
        