class Solution:
    def tribonacci_1(self, n: int) -> int:
        if n <= 1:
            return n
        
        
        return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1) if n >= 3 else self.tribonacci(n-2) + self.tribonacci(n-1) 
    

    def tribonacci_2(self, n: int) -> int:
        a, b, c = 1, 0, 0
        
        for _ in range(n):
            a, b, c = b, c, a+b+c
            
        return c
    
    def tribonacci(self, n: int) -> int:
        DP = [0, 1, 1]
        
        for i in range(3, n+1):
            DP[i%3] = sum(DP)
            
        return DP[n%3]