# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''        
        res = []
        
        def traversal(node, cnt):
            if node is None:
                return
            
            res.append([node.val])
            cnt += 1
            
            if cnt % 2:
                traversal(node.right, cnt)
                
                if node.left:
                    traversal(node.left, cnt)
                
            else:
                traversal(node.left, cnt)
                
                if node.right:
                    traversal(node.right, cnt)
            return

    
        traversal(root, 0)
        return res
        '''
        from collections import deque
        
        if not root:
            return []
        
        q = deque([root])
        result, direction = [], 1
        
        while q:
            level = []
            
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                    
            result.append(level[::direction])
            direction *= (-1)
            
        return result
            
            