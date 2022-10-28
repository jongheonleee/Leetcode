"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        if root:
            queue : Deque = collections.deque([root])
                
        while queue:
            m = len(queue)
            n = m
            for _ in range(m):
                node = queue.popleft()
                n -= 1
                
                if n >= 1:
                    node.next = queue[0]
                    
                elif n == 0:
                    node.next = None
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
        return root
                
                
                
                
                    
                    
                
            
        