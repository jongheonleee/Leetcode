class Solution:
    def countSubstrings1(self, s: str) -> int:
        '''
        [optimize] center expansion
        
        - select candidates which could be center in possible palimdrom
            > 2N - 1:
                - center is the candidate itself
                - center is that candidate + right character
                
        - expand when the case is palindrome
        
        [naive] divide s into every sub string
        
        - divide s into every sub string
        - check whether it's palindrome or not
        
        '''
        
        
        N = len(s)
        cnt = 0
        
        for center in range(2*N-1):
            left = center // 2
            right = left + center % 2
            
            while left >= 0 and right < N and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
                
        return cnt
    
    def countSubstrings(self, s: str) -> int:
        cnt, n, i = 0, len(s), 0
        
        while i < n:
            j, k = i-1, i
            
            while k < n-1 and s[k] == s[k+1]:
                k += 1
                
            cnt += (k-j) * (k-j+1) // 2
            i, k = k+1, k+1
            
            while ~j and k < n and s[k] == s[j]:
                j, k, cnt = j-1, k+1, cnt+1
                
        return cnt


                
                
            
        
        