# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        
        queue = collections.deque([root])
        
        while queue:
            size = len(queue)
            for i in range(1, size+1):
                node = queue.popleft()
                
                if i == size:
                    res.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
        return res
                

                
                    
            
        