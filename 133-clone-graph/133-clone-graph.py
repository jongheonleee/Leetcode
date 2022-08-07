"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        queue, clones = deque([node]), {node.val: Node(node.val, [])}
        
        while queue:
            crnt_node = queue.popleft()
            crnt_clone = clones[crnt_node.val]
            
            for neighbor in crnt_node.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                    
                    
                crnt_clone.neighbors.append(clones[neighbor.val])
            
        return clones[node.val]
                
            
            

                    
                    
                
            
            
            
                    
                
            
            
    
    
                
                
                
            
            
            