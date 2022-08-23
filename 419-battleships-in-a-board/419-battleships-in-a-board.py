class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0
        m, n = len(board), len(board[0])
        vis = set()
        
        def dfs_r(y, x):
            if y < 0 or y >= m or x < 0 or x >= n or board[y][x] != 'X':
                return 
            
            if (y, x) in vis:
                return 
            
            vis.add((y, x))
            dfs_r(y+1, x)
            
        
        
        def dfs_c(y, x):
            if y < 0 or y >= m or x < 0 or x >= n or board[y][x] != 'X':
                return 
            
            if (y, x) in vis:
                return
            
            vis.add((y, x))
            dfs_c(y, x+1)
            
            
        
        for y in range(m):
            for x in range(n):
                if (y, x) not in vis and board[y][x] == 'X':
                    vis.add((y, x))
                    dfs_r(y+1, x)
                    dfs_c(y, x+1)
                    
                    cnt += 1
                    
                        
        return cnt
                        
                    
                    
                    