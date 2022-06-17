class Solution:
# 트라이를 객체형식으로 표현한 것이 아닌
# 딕셔너리 형태로 키-값 (매칭)형태로 구현함
    def findWords(self, board, words):
        #make trie
        count = Counter()
        for l in board:
            # 해당 행에 있는 글자들 갯수 저장
            count += Counter(l)
        
        trie={}
        for w in words:
            # 특정 단어 글자와 개수 딕셔너리 
            wc = Counter(w)
            for c in wc:
                # c는 키값
				# 단어 내의 글자가 보드 내의 글자보 많을 경우는 스킵(최적화)
                if wc[c] > count[c]:
                    continue
                    
            t=trie
            for c in w:
                if c not in t:
                    # 트라이에 새로운 글자 들어올시 새로운 딕셔너리 할당
                    t[c]={}
                # c값 업데이트
                t=t[c]
                
            # 마지막 노드
            # #는 w단어가 트라이로 구현됐다는 의미
            t['#']='#'
            
        self.res=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board,i,j,trie,[])
        return self.res
    
    def find(self,board,i,j,trie,pre):
        # pre는 탐색하면서 만들어지는 단어라고 생각하면됨
        if '#' in trie:
			# 중복되는 경우를 피하기 위해, 삭제해주기
            del trie["#"]
            self.res.append(''.join(pre))
            
        # 좌표 i, j가 board범위를 넘었을 경우    
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return
        
        # 구현한 트라이(찾아야하는 단어들)에 symbol (board[i][y])가 존재하는 경우
        if board[i][j] in trie:
            # 임시값 활용
            tmp = board[i][j]
            # 마크해주기
            board[i][j] = '$'
            # 탐색하면서 여태껏 탐색한 글자들을 저장하는 리스트
            pre.append(tmp)
            # board 4가지 방면으로 이동
            self.find(board,i+1,j,trie[tmp],pre)
            self.find(board,i,j+1,trie[tmp],pre)
            self.find(board,i-1,j,trie[tmp],pre)
            self.find(board,i,j-1,trie[tmp],pre)
            
            # 초기화
            board[i][j] = tmp
            pre.pop()
            
            if not trie[board[i][j]]:
				# 구현한 트라이에 board[i][j]의 글자가 없는 경우,
                # 해당 글자는 저장하지 않아도됨
                del trie[board[i][j]]        

    

