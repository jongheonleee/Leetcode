class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # processing given string -> push word in list 
        cnt_word = collections.Counter()
        lst = []
        word = ''
        
        for char in paragraph:
            if char.isalpha():
                word += char.lower()
                
            elif word != '':
                if word not in banned:
                    lst.append(word)
                
                word = ''
                
        if word != '':
            lst.append(word)
        
        cnt_word = collections.Counter(lst)
        return cnt_word.most_common()[0][0]
        
        

                
        
            
        

                

        