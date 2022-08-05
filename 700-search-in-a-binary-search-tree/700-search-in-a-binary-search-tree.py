# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(root): 
            if root.val == val:
                return root
            
            elif root.val > val and root.left:
                return dfs(root.left)
                
            elif root.val < val and root.right:
                return dfs(root.right)
                
        return dfs(root) if root else None
        