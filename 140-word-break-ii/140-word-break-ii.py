class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        '''        
        # i will uses sliding window for checking are there words in s
        # make a hash_table for storing cnt(key=word, val=cnt)
        # make [new sentences] if sum(hash_table) == 0 otherwise return []
        
                
        i, j = 0, 0
        lst = []
        
        tmp_word = ''
        while i<j and j<len(s):
            tmp_word += s[j]
            
            if tmp_word in wordDict:
                lst.append(tmp_word)
                i = j+1
                
            j += 1
            
        cnt_word = collections.Counter(wordDict)
        print(cnt_word)
        '''
        
        word_set = set(wordDict)
        n = len(s)
        
        dp_sol = [[] for _ in range(n)] + [[""]]
        dp = [0] * n + [1]
        
        for k in range(n):
            for j in range(k, -1, -1):
                if s[j:k+1] in word_set:
                    dp[k] = max(dp[k], dp[j-1])
                    
        if dp[-2] == 0:
            return []
        
        for k in range(n):
            for j in range(k, -1, -1):
                if s[j:k+1] in word_set:
                    for sol in dp_sol[j-1]:
                        dp_sol[k].append(sol + " " + s[j:k+1])
                        
                        
        return [s[1:] for s in dp_sol[-2]]