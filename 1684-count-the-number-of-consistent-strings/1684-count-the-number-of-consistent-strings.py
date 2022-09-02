class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        neg = 0
        char_set = set(allowed)
        
        for word in words:
            for char in word:
                if char not in char_set:
                    neg += 1
                    break
                    
                
        return len(words) - neg