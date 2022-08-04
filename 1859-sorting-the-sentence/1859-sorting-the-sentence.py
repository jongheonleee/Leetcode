class Solution:
    def sortSentence(self, s: str) -> str:
        letters = s.split(' ')
        lst = ['' for _ in range(len(letters))]
        
        for c in letters:
            lst[int(c[-1])-1] = c[:-1] + ' '
            
        lst[-1] = lst[-1][:-1]
            
        return ''.join(lst)
    
        