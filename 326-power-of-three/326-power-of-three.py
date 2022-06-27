class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        if n > 2:
            if n % 3 > 0 :
                return False
            n /= 3
            self.isPowerOfThree(n)
            
        return n == 1
        '''
        # above code is that i try to implemented this solution recursion bu fail
        
        if n == 1:
            return True
        
        if n == 0:
            return False
        
        return n % 3 == 0 and self.isPowerOfThree(n//3)
        '''
        when you implemente a function recursively
        - set of end condition for basic case
        - try to detail end condition!!
        '''
            
            
