class Solution:
    def mostWordsFound_mine(self, sentences: List[str]) -> int:
        max_cnt = float('-inf')
        
        for s in sentences:
            cnt = 0 
            for char in s.split(' '):
                cnt += 1
                
            max_cnt = max(max_cnt, cnt)
                
                
            
        return max_cnt
    
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(s.count(' ') for s in sentences) + 1