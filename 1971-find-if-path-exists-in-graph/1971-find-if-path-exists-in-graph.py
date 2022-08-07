class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        connections = collections.defaultdict(list)
        
        for v1, v2 in edges:
            connections[v1].append(v2)
            connections[v2].append(v1)
            
        queue = collections.deque([start])
        vis = set([start])
 
        
        while queue:
            vtx = queue.popleft()
            
            if vtx == end:
                return True
            
            for next_vtx in connections[vtx]:
                if next_vtx not in vis:
                    vis.add(next_vtx)
                    queue.append(next_vtx)
                
        return False
    
            
        