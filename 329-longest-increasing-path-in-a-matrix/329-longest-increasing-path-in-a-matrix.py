'''class Solution:
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
        '''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        
        cols = len(matrix[0])
        indegree = [[0 for x in range(cols)] for y in range(rows)] 
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        for x in range(rows):
            for y in range(cols):
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] < matrix[x][y]:
                            indegree[x][y] += 1
                            
        queue = []
        for x in range(rows):
            for y in range(cols):
                if indegree[x][y] == 0:
                    queue.append((x, y))
    
        path_len = 0
        while queue:
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