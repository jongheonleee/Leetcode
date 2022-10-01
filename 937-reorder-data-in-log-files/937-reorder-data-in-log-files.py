class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        
        for log in logs:
            if log[-1].isalpha():
                letters.append(log)
                
            else:
                digits.append(log)
                
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return letters + digits
