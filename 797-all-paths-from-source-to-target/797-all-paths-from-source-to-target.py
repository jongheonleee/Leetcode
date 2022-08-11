class Solution:
    def allPathsSourceTarget_(self, graph: List[List[int]]) -> List[List[int]]:
        res, n = [], len(graph)
        
        def dfs(formed):
            if formed[-1] == n-1:
                res.append(formed)
                return
            
            for child in graph[formed[-1]]:
                dfs(formed + [child])
                

        dfs([0])
        return res
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def dfs(v, path):
            if v == len(graph)-1:
                res.append(path)
                return
                
            for nv in graph[v]:
                dfs(nv, path + [nv])
                
        dfs(0, [0])
        return res
        
        
                    
                
                    
                
            
        
        