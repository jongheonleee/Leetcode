class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # [20,100,10,12,5,13]
        # 100 이후로 뒤에 숫자를 stack에 올릴 수 없음
        stack = []
        
        for n in nums:
            if len(stack) == 0:
                stack.append(n)
                
            elif stack[-1] < n:
                stack.append(n)
                
            
            if len(stack) == 3:
                return True
            
        return False
                    
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = math.inf
        
        for n in nums:
            if n <= first:
                first = n
                
            elif n <= second:
                second = n
                
            else:
                return True
            
        return False
            
        