# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        return 을 못받음
        
        '''
        
        def dfs(node, t):
            
            if not node:
                return False
            
            t += node.val
            
            if not node.left and not node.right:
                return t == targetSum
            
            return dfs(node.left, t) or dfs(node.right, t)
        
        return dfs(root, 0)

            
        