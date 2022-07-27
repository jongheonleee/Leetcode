class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        
        heap = []
        
        for s in stones:
            heapq.heappush(heap, -s)
            
        while len(heap) > 1:
            s1, s2 = heapq.heappop(heap), heapq.heappop(heap)
            new_s = s1 - s2
            heapq.heappush(heap, new_s)
            
        return -heap[0]