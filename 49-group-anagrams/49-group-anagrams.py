class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = collections.defaultdict(list)
        
        for s in strs:
            sorted_s = sorted(s)
            group_anagram[''.join(sorted_s)] += [s]
            
        return [val for val in group_anagram.values()]
            

                
        
        