import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        '''
        deep copy, shallow copy 정확하게 차이점 공부하기
        '''
        if board is None:
            return
        
        dir_ = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1),]
        
        # cp_board = board[:]
        cp_board = copy.deepcopy(board[:])
        queue = collections.deque()
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                queue.append((y, x))
                
    
        while queue:
            y, x = queue.popleft()
            cnt = 0
            
            for dy, dx in dir_:
                ny, nx = y+dy, x+dx
                
                if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and cp_board[ny][nx]:
                    cnt += 1

            if cp_board[y][x] == 1:
                if cnt > 3:
                    board[y][x] = 0
                    
                elif 2 <= cnt <= 3:
                    board[y][x] = 1
                    
                elif cnt < 2:
                    board[y][x] = 0
                    
            elif cp_board[y][x] == 0:
                if cnt == 3:
                    board[y][x] = 1
                    
        print(cp_board)
                    
        return
                        
                    
                    
            
            
                
        