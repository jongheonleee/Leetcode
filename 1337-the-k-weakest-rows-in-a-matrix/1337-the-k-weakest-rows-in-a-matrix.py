class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        heap = []
        
        for i, n in enumerate(mat):
            heapq.heappush(heap, (n, i))
            
            
        for _ in range(k):
            _, i = heapq.heappop(heap)
            res.append(i)
            
        return res
        
        