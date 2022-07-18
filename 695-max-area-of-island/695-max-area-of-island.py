class Solution:
    def maxAreaOfIsland_(self, grid: List[List[int]]) -> int:
        def dfs(i:int, j:int):
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
                return
            
            if grid[i][j] != 1:
                return
            
            grid[i][j] = "#"
            
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)
            
        if grid is None:
            return 0
        
        row, col = len(grid), len(grid[0])
        
        cnt = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    cnt += 1
                    dfs(i, j)
                    
        return cnt
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 1. approach: dfs
        m, n = len(grid), len(grid[0])
        
        DIR = [0, 1, 0, -1, 0]
        
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0:
                return 0
            
            ans = 1
            grid[r][c] = 0
            
            for i in range(4):
                ans += dfs(r+DIR[i], c+DIR[i+1])
                
            return ans
        
        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))
                
        return ans
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 2. approach: bfs
        m, n = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]
        
        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0
            ans = 0
            
            while q:
                r, c = q.popleft()
                ans += 1
                
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == 0:
                        continue
                        
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    
            return ans
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, bfs(r, c))
                    
                    
        return ans
    