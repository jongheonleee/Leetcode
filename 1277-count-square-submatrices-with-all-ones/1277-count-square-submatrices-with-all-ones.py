class Solution:
    def countSquares_1(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        
        def dp(r, c):
            # Top Down DP
            # Time Limit Exceeded
            if matrix[r][c] == 1:
                if r > 0 and c > 0:
                    return min(dp(r-1, c), dp(r, c-1), dp(r-1, c-1)) + 1
                else:
                    return 1
                
            else:
                return 0
            
        return sum(dp(r, c) for r in range(row) for c in range(col))
    
    def countSquares_2(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * (col+1) for _ in range(row+1)]
        ans = 0
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c]:
                    dp[r+1][c+1] = min(dp[r][c+1], dp[r+1][c], dp[r][c]) + 1
                    ans += dp[r+1][c+1]
                    
        return ans
    
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [0] * (col+1)
        ans = 0
        
        dp_r_c = 0
        
        for r in range(row):
            for c in range(col):
                dp_r_c_nxt = dp[c+1]
                
                if matrix[r][c]:
                    # dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                    dp[c+1] = min(dp[c+1], dp[c], dp_r_c) + 1
                    ans += dp[c+1]
                    
                else:
                    dp[c+1] = 0
                    
                dp_r_c = dp_r_c_nxt
                
        return ans

        