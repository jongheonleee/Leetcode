class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res, n = [], len(graph)
        
        def dfs(formed):
            if formed[-1] == n-1:
                res.append(formed)
                return
            
            for child in graph[formed[-1]]:
                dfs(formed + [child])
                

        dfs([0])
        return res
        
                    
                
                    
                
            
        
        