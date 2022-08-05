class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(y, x):
            if y < 0 or x < 0 or y >= M or x >= N or board[y][x] != 'O':
                return
            
            board[y][x] = 'T'
            
            dir_ = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
            for ny, nx in dir_:
                dfs(ny, nx)
                
        
        if board is None:
            return
        
        M, N = len(board), len(board[0])
        
        
        for y in range(M):
            dfs(y, 0)
            dfs(y, N-1)
            
        for x in range(N):
            dfs(0, x)
            dfs(M-1, x)
            
        for y, x in product(range(M), range(N)):
            board[y][x] = 'X' if board[y][x] != 'T' else 'O'
            
        
        
                    
                    