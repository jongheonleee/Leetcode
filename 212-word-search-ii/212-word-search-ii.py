'''
what are benefit when i use Trie

-1. it's effective way to store some of words

ex) compare when i try to store words = ['hi', 'hello'. 'height'] in any DS

among them(DS), the best way to store in it is Trie

> 1.save memory(the more duplication letters, the more effective)
> 2.quickly search pattern of string
'''

# Trie
# what im gonna do
# - for each word in our words insert it in our Trie
# - starting with each symbol in our board, start dfs(backtracking) which are looking for words in our Tire
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        root = self.root
        for symbol in word:
            # setdefault;
            root = root.children.setdefault(symbol, TrieNode())
            
        root.end_node = 1
        

# Variables:
# 1. self.num_words : total_number of words we still need to find

class Solution1:
    def findWords_mine(self, matrix: List[List[str]], words: List[str]) -> List[str]:
        res = []
        def dfs(y: int, x: int, word: str, tmp_word: str, idx:int) -> None:
            if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix) or matrix[y][x] == '#':
                return
            
            if word[idx] != matrix[y][x]:
                return 
            
            matrix[y][x] = '#'
            tmp_word += matrix[y][x]
            idx += 1
            
            if tmp_word == word:
                res.append(word)
                tmp_word = ''
                idx = 0
                return
            
            dfs(y-1, x)
            dfs(y+1, x)
            dfs(y, x-1)
            dfs(y, x+1)
            
            matrix[y][x] = tmp_word[y][x]
            
        for word in words:
            for y in range(len(matrix)):
                for x in range(len(matrix[0])):
                    if word[0] == matrix[y][x]:
                        matrix[y][x] = '#'
                        dfs(y, x, word, word[0], 1)
                        
                        
        return res
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # using dfs & Trie
        self.num_words = len(words)
        res, trie = [], Trie()
        
        for word in words:
            trie.insert(word)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, '', res)
                
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if self.num_words == 0:
            return
        
        if node.end_node:
            res.append(path)
            node.end_node = False
            self.num_words -= 1
            
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        tmp = board[i][j]
        
        if tmp not in node.children:
            return 
        
        board[i][j] = '#'
        
        for x, y in [[0,-1], [0, 1], [1, 0], [-1, 0]]:
            self.dfs(board, node.children[tmp], i+x, j+y, path+tmp, res)
            
        board[i][j] = tmp
'''
what are benefit when i use Trie

-1. it's effective way to store some of words

ex) compare when i try to store words = ['hi', 'hello'. 'height'] in any DS

among them(DS), the best way to store in it is Trie

> 1.save memory(the more duplication letters, the more effective)
> 2.quickly search pattern of string
'''

# Trie
# what im gonna do
# - for each word in our words insert it in our Trie
# - starting with each symbol in our board, start dfs(backtracking) which are looking for words in our Tire
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        root = self.root
        for symbol in word:
            # setdefault;
            root = root.children.setdefault(symbol, TrieNode())
            
        root.end_node = 1
        

# Variables:
# 1. self.num_words : total_number of words we still need to find

class Solution1:    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # using dfs & Trie
        self.num_words = len(words)
        res, trie = [], Trie()
        
        for word in words:
            trie.insert(word)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, '', res)
                
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if self.num_words == 0:
            return
        
        if node.end_node:
            res.append(path)
            node.end_node = False
            self.num_words -= 1
            
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        tmp = board[i][j]
        
        if tmp not in node.children:
            return 
        
        board[i][j] = '#'
        
        for x, y in [[0,-1], [0, 1], [1, 0], [-1, 0]]:
            self.dfs(board, node.children[tmp], i+x, j+y, path+tmp, res)
            
        board[i][j] = tmp
        
class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        #make trie
        count = Counter()
        for l in board:
            count += Counter(l)
        trie={}
        for w in words:
            wc = Counter(w)
            for c in wc:
				# optimization, ignore word if there isn't enough c in board
                if wc[c] > count[c]:
                    continue
            t=trie
            for c in w:
                if c not in t:
                    t[c]={}
                t=t[c]
            t['#']='#'
        self.res=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board,i,j,trie,[])
        return self.res
    
    def find(self,board,i,j,trie,pre):
        if '#' in trie:
			# optimization, delete for avoiding duplicated matches
            del trie["#"]
            self.res.append(''.join(pre))
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return
        if board[i][j] in trie:
            tmp = board[i][j]
            board[i][j] = '$'
            pre.append(tmp)
            self.find(board,i+1,j,trie[tmp],pre)
            self.find(board,i,j+1,trie[tmp],pre)
            self.find(board,i-1,j,trie[tmp],pre)
            self.find(board,i,j-1,trie[tmp],pre)
            board[i][j] = tmp
            pre.pop()
            if not trie[board[i][j]]:
				# nothing in trie[board[i][j]] because of matched before, delete node for optimization
                del trie[board[i][j]]        

    

