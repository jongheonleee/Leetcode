# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root.left and not root.right:
                return True if root.val == 1 else False
            
            left_sub_tree = dfs(root.left)
            right_sub_tree = dfs(root.right)
            
            if root.val == 2:
                return left_sub_tree or right_sub_tree
            
            if root.val == 3:
                return left_sub_tree and right_sub_tree
            
        return dfs(root)
            
            
            
        