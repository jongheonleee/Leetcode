class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = ""
        cnt_word = collections.defaultdict(int)
        for char in paragraph:
            if char.isalpha():
                word += char.lower()
            
            else:
                if word not in banned + [""]:
                    cnt_word[word] += 1
                    
                word = ""
                
        if word != "":
            cnt_word[word] += 1
                
        print(cnt_word)
        return max(cnt_word, key=cnt_word.get)
                

        