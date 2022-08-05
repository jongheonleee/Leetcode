class Solution:
    def solve_(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
     
        row, col = len(board), len(board[0])
        cp_board = copy.deepcopy(board[:])
        dir_ = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def bfs(y, x):
            X_cnt = 0
            for dy, dx in dir_:
                ny, nx = y + dy, y + dx
                
                if ny < 0 or ny > len(board)-1 or nx < 0 or nx > len(board[0])-1:
                    X_cnt += 1
                
                elif cp_board[ny][nx] == 'X':
                    X_cnt += 1
                    
            
            board[y][x] = 'O' if X_cnt == 4 else 'X'
                        
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    bfs(r, c)
                    
                    
                    
    def dfs(self, i, j):
        if i < 0 or j < 0 or i >= self.M or j >= self.N or self.board[i][j] != 'O':
            return
        
        self.board[i][j] = 'T'
        next_yx = [[i+1, j], [i-1, j], [i, j-1], [i, j+1]]
        
        for ny, nx in next_yx:
            self.dfs(ny, nx)
            
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 0
        
        self.board, self.M, self.N = board, len(board), len(board[0])
        
        for i in range(0, self.M):
            self.dfs(i, 0)
            self.dfs(i, self.N-1)
            
        for j in range(0, self.N):
            self.dfs(0, j)
            self.dfs(self.M-1, j)
            
        for i, j in product(range(self.M), range(self.N)):
            print(i, j)
            board[i][j] = 'X' if board[i][j] != 'T' else 'O'
                    
                    