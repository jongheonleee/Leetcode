class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words = re.sub(r'[^A-Za-z]', " ", paragraph.lower()).split()
        processing_words = [ word for word in words if word not in banned]
        word_cnt = collections.Counter(processing_words)
        
        return word_cnt.most_common()[0][0] 
            
        
        
        

                
        
            
        

                

        