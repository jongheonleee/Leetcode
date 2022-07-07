class Solution:
    def countSubstrings(self, s: str) -> int:
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


                
                
            
        
        