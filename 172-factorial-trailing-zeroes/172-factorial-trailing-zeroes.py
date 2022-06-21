class Solution:
    def trailingZeroes(self, n: int) -> int:
        # first my thought
        # but not satisfied what the problem ask 
        '''
        ans = 1
        while n<0:
            ans *= n
            n -= 1
            
        str_ans = str(ans)
        
        res = 0
        for c in str_ans:
            if c == '0':
                res += 1
                
        return res'''
        
        # other way to handle this problem
        '''
        1. The ZERO comes from 10.
        2. The 10 comes from 2 x 5
        3. And we need to account for all the products of 5 and 2. likes 4×5 = 20 ...
        4. So, if we take all the numbers with 5 as a factor, we'll have way more than enough even numbers to pair with them to get factors of 10
        '''
        
        r = 0
        while n > 0:
            n //= 5
            r += n
            
        return r