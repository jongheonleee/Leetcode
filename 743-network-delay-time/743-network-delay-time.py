class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in times:
            graph[u].append([v, w])
            
        heap = [(0, k)]
        dist = collections.defaultdict(int)
        
        while heap:
            time, node = heapq.heappop(heap)
            
            if node not in dist:
                dist[node] = time
                
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(heap, (alt, v))
                
        return max(dist.values()) if len(dist) == n else -1

    
    
        