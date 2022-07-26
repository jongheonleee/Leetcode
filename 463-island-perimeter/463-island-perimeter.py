class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n, P = len(grid), len(grid[0]), 0
        
        for i in range(m):
            for j in range(n):
                P += 4*grid[i][j]
                
                if i > 0:
                    P -= grid[i][j]*grid[i-1][j]
                
                if i < m-1:
                    P -= grid[i][j]*grid[i+1][j]
                    
                if j > 0:
                    P -= grid[i][j]*grid[i][j-1]
                    
                if j < n-1:
                    P -= grid[i][j]*grid[i][j+1]
                    
        return P

        
       
        
                
                
        