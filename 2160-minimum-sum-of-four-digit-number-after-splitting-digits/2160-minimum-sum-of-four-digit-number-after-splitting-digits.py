class Solution:
    def minimumSum(self, num: int) -> int:
        lst = []
        
        for n in str(num):
            lst.append(int(n))
            
        lst.sort()
        
        new1, new2 = lst[0]*10+lst[2], lst[1]*10+lst[3]
        
        return new1+new2
        
    
        