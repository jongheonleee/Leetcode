class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            
        res = set()
        vis = [False] * n
        
        def dfs(v):
            vis[v] = True
            
            for adj in graph[v]:
                if not vis[adj]:
                    dfs(adj)
                    
                elif adj in res:
                    res.remove(adj)
                    
        for v in range(n):
            if not vis[v]:
                dfs(v)
                res.add(v)
                
        return res
        
        

                            
                        
                        