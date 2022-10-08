class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word] += [word]
            
            
        return list(anagrams.values())
            
        
            

                
        
        