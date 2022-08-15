class Solution:
    def totalNQueens(self, n: int) -> int:
        d1 = set()
        d2 = set()
        used_cols = set()
        
        return self.helper(n, d1, d2, used_cols, 0)
    
    def helper(self, n, d1, d2, used_cols, row):
        if row == n:
            return 1
        
        sol = 0
        
        for col in range(n):
            if row + col in d1 or row - col in d2 or col in used_cols:
                continue
                
            d1.add(row+col)
            d2.add(row-col)
            used_cols.add(col)
            
            sol += self.helper(n, d1, d2, used_cols, row+1)
            
            d1.remove(row+col)
            d2.remove(row-col)
            used_cols.remove(col)
            
        return sol
    
    
            
                    
            
                    
                    
        