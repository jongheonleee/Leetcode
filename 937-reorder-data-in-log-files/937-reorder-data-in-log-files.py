class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        
        for l in logs:
            if l[-1].isalpha():
                letters.append(l)
                
            else:
                digits.append(l)
                
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letters + digits
                    
