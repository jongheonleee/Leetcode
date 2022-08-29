class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # using BFS
        ans = -1
        queue = collections.deque([])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        fresh_oranges = 0
        # finding rotten orange
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    # this orange is rotten
                    queue.append((i, j))
                    
                if grid[i][j] == 1:
                    fresh_oranges += 1

        if not queue and not fresh_oranges:
            return 0
                    
        while queue:
            for _ in range(len(queue)):
                y, x = queue.popleft()
                

                for dy, dx in directions:
                    ny, nx = y + dy, x + dx

                    if 0<=ny<=len(grid)-1 and 0<=nx<=len(grid[0])-1 and grid[ny][nx] == 1:
                        grid[ny][nx] = 2
                        queue.append((ny, nx))
                        
            
            ans += 1
            
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    return -1
                
                
        return ans
                    
            
            
        