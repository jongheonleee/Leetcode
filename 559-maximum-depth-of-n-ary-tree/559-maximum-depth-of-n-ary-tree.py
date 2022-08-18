"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        level = 0
        queue = collections.deque([root])
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                for child in node.children:
                    queue.append(child)
                    
            level += 1
            
        return level
        
        