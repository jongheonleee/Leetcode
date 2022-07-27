class Solution_mine:
    # i only try to traverse graph by dfs but failed
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        res = float('-inf')
        dir_ = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def dfs(y, x, cnt):
            nonlocal res
            if y <= 0 or y > len(matrix) or x <= 0 or x > len(matrix[0]):
                return
            
            
            for dy, dx in dir_:
                ny, nx = y + dy, x + dx
                
                if 0 <= ny < len(matrix) and 0 <= nx < len(matrix[0]):
                    if matrix[y][x] < matrix[ny][nx]:
                        dfs(ny, nx, cnt + 1)
                    
                    else:
                        res = max(res, cnt)
                
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, 1)

        return res
        
# calculate the depth of graph, and return it   
class Solution_DAG:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        
        cols = len(matrix[0])
        # space for implementing graph
        indegree = [[0 for x in range(cols)] for y in range(rows)] 
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        for x in range(rows):
            for y in range(cols):
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] < matrix[x][y]:
                            indegree[x][y] += 1
        
        # append leaf vertices on queue
        queue = []
        for x in range(rows):
            for y in range(cols):
                if indegree[x][y] == 0:
                    queue.append((x, y))
    
        path_len = 0
        while queue:
            # first pop leaves and calculate the depth of graph
            sz = len(queue)
            for i in range(sz):
                x, y = queue.pop(0)
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] > matrix[x][y]:
                            indegree[nx][ny] -= 1
                            if indegree[nx][ny] == 0:
                                queue.append((nx, ny))
            path_len += 1
        return path_len 
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # find longest decreasing path, result will be same
        
        # use dp for recording previous results and choose the max dp value of smaller neighbors
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i-1, j) if i and val > matrix[i-1][j] else 0,
                    dfs(i+1, j) if i < r-1 and val > matrix[i+1][j] else 0,
                    dfs(i, j-1) if j and val > matrix[i][j-1] else 0,
                    dfs(i, j+1) if j < c-1 and val > matrix[i][j+1] else 0)
                
            return dp[i][j]
        
        if not matrix or not matrix[0]:
            return 0
        
        r, c = len(matrix), len(matrix[0])
        dp = [[0] * c for _ in range(r)]
        
        
        
        return max(dfs(y, x) for y in range(r) for x in range(c))
                
                
