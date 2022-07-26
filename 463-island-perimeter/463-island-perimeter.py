class Solution:
    def islandPerimeter_(self, grid: List[List[int]]) -> int:
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
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r, c, q = len(grid), len(grid[0]), deque()
        
        for y in range(r):
            for x in range(c):
                if grid[y][x] == 1:
                    q.append((y, x))
                    return self.bfs(grid, r, c, q)
                
    def bfs(self, grid, r, c, q):
        vis = set()
        perimeter = 0
        
        while q:
            y, x = q.popleft()
            
            if (y, x) in vis:
                continue
                
            vis.add((y, x))
            
            for ny, nx in [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]:
                if 0<=ny<r and 0<=nx<c:
                    if grid[ny][nx] == 0:
                        perimeter += 1
                        
                    if grid[ny][nx] == 1:
                        q.append((ny, nx))
                        
                else:
                    perimeter += 1
                    
        return perimeter

        
       
        
                
                
        