class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cnt_word = collections.defaultdict(int)
        
        def find_word(left, right) -> int:
            while right < len(paragraph) and paragraph[right].isalpha():
                right += 1
            
            if paragraph[left:right].lower() not in banned:
                cnt_word[paragraph[left:right].lower()] += 1
                
            return right 
        
        idx = 0
        while idx < len(paragraph):
            if paragraph[idx].isalpha():
                next_i = find_word(idx, idx)
                idx = next_i
                
            else:
                idx += 1

                
        return max(cnt_word, key=cnt_word.get)
                
        
            
        

                

        