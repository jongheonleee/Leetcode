class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        
        for s in operations:
            if '-' in s:
                val -= 1
                
            else:
                val += 1
                
        return val
        