class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        n = len(edges)
        cnt = collections.defaultdict(int)
        
        for v1, v2 in edges:
            cnt[v1] += 1
            cnt[v2] += 1
            
            if cnt[v1] == n:
                return v1
            
            if cnt[v2] == n:
                return v2
            
        return 0
            
            
        