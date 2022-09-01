class Solution:
    def sortString(self, s: str) -> str:
        '''        
        char_cnt = collections.Counter(s)
        
        cnt = 0
        for k, v in char_cnt.items():
            cnt += 1
            
        tmp_cnt = cnt
        t = 0
        st = []
        
        for k, v in char_cnt.items():
            if st and t % 2 == 0:
                if ord(st[-1]) > ord(v):
                    st += [v, st.pop()]
                    
                else:
                    st += [v]
                    
                    
            elif st and t % 2:
                if ord(st[-1]) > ord(v):
                    st += [v]
                    
                else:
                    st += [v, st.pop()]
                    
            else:
                st += [v]
                
        return ''.join(st[::-1])
        '''
        # today, i has learned that hash_table can be used sort()
        # and del cnt[char]
        # also i can use for loop with condition!!
        # ans hash_table is iterative
        cnt, ans, asc = collections.Counter(s), [], 1
        
        while cnt:
            for char in sorted(cnt) if asc else reversed(sorted(cnt)):
                ans += [char]
                cnt[char] -= 1
                
                if cnt[char] == 0:
                    del cnt[char]
                    
            asc = not asc
            
        return ''.join(ans)
            