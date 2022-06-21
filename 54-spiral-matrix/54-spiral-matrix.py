class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # first my thought but failed
        # i have to analysis later
        '''
        res = []
        M = matrix
        def dfs(i:int, j:int) -> None:
            if i < 0 or i >= len(M) or j < 0 or j >= len(M[0]) or M[i][j] == '#':
                return
            
            if len(M) * len(M[0]) == len(res):
                return
            
            tmp = M[i][j]
            res.append(tmp)
            M[i][j] = '#'
            
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i-1, j)
            
        
        dfs(0, 0)
        return res'''
        
        # make where i have to go next clearn
        # by using some variables
        M = matrix
        
        height = len(M)
        width = len(M[0])
        
        top, bottom, left, right = 0, height -1, 0, width -1
        
        ans = []
        while top < bottom and left < right:
            for c in range(left, right):
                ans.append(M[top][c])
                
            for r in range(top, bottom):
                ans.append(M[r][right])
                
            for c in range(right, left, -1):
                ans.append(M[bottom][c])
                
            for r in range(bottom, top, -1):
                ans.append(M[r][left])
                
            top += 1
            bottom -= 1
            left += 1
            right -= 1
           
        # if a matrix remain inside it is either a 1*n or a m*1
        # a linear scan will return the same order as spiral for these
        if len(ans) < height ** width:
            for r in range(top, bottom+1):
                for c in range(left, right+1):
                    ans.append(M[r][c])
                    
        return ans