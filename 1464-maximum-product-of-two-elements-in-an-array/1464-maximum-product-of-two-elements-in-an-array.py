class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        
        for n in nums:
            heapq.heappush(heap, -n)
            
        cnt = 2
        ans = 1
        
        while cnt > 0:
            cnt -= 1
            num = -heapq.heappop(heap)
            
            ans *= (num - 1)
            
        return ans
            
        