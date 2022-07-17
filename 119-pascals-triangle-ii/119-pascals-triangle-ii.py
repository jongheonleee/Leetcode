class Solution:
    def getRow_(self, rowIndex: int) -> List[int]:
        
        dp = [[1] * (n+1) for n in range(rowIndex+1)]
        
        for i in range(1, len(dp)):
            for j in range(len(dp[i])):
                if j <= 0 or j >= len(dp[i])-1:
                    dp[i][j] = 1
                
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                
        return dp[rowIndex]
    
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]

        return row